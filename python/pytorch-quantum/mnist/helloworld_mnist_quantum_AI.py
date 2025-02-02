import torch
import torch.nn as nn
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision.datasets as datasets
from torch.utils.data import DataLoader, Subset


import sys
sys.path.append('../../')
from AutomatskiKomencoNative import *

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers 
sampler = AutomatskiKomencoNative(host="103.212.120.18", port=80) # 

# Define the QuantumLayer and HybridModel classes
class QuantumLayer(nn.Module):
    def __init__(self, num_qubits, num_layers):
        super(QuantumLayer, self).__init__()
        self.num_qubits = num_qubits
        self.num_layers = num_layers

    def forward(self, x):
        # Quantum part (Placeholder comments, omitted due to lack of details)
        # x should be of shape (batch_size, num_patches, num_qubits)
        batch_size, num_patches, num_qubits = x.size()
        output = []

        for i in range(batch_size):
            patch_outputs = []
            for p in range(num_patches):
                self.circuit = QuantumCircuit(self.num_qubits)

                # Convert input to angles for rotation gates
                for j in range(self.num_qubits):
                    self.circuit.rx(x[i, p, j].item(), j)

                self.circuit.measure_all()

                # Run the circuit and get results
                results = sampler.run(self.circuit, repetitions=1000, topK=20)

                # Extract and count the measurement results
                measurements = results['result']

                # Find the key with the highest value (count)
                state_with_highest_probability = max(measurements, key=measurements.get)

                numerical_state_array = [1 if char == '1' else -1 for char in state_with_highest_probability[::-1]]

                patch_outputs.append(numerical_state_array)

            output.append(patch_outputs)

        return torch.tensor(output, dtype=torch.float32)

class HybridModel(nn.Module):
    def __init__(self, patch_size=18):
        super(HybridModel, self).__init__()
        self.patch_size = patch_size
        self.num_patches = (32 // patch_size) ** 2
        self.fc1 = nn.Linear(patch_size * patch_size, 16)
        self.quantum_layer = QuantumLayer(num_qubits=16, num_layers=1)  # Example with 16 qubits
        self.fc2 = nn.Linear(16 * self.num_patches, 10)  # 10 classes for MNIST

    def forward(self, x):
        batch_size = x.size(0)
        x = x.view(batch_size, 1, 32, 32)  # Ensure input is of shape (batch_size, 1, 32, 32)
        
        # Extract patches
        patches = x.unfold(2, self.patch_size, self.patch_size).unfold(3, self.patch_size, self.patch_size)
        patches = patches.contiguous().view(batch_size, -1, self.patch_size * self.patch_size)  # Shape: (batch_size, num_patches, patch_size*patch_size)
        
        # Process each patch with a fully connected layer
        patches = torch.relu(self.fc1(patches))
        
        # Process patches with the quantum layer
        patches = self.quantum_layer(patches)
        
        # Flatten the patches
        patches = patches.view(batch_size, -1)
        
        # Final fully connected layer
        x = torch.log_softmax(self.fc2(patches), dim=1)
        return x

# Load the MNIST dataset
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,))
])

train_dataset = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

# Create subsets of 1000 odd images for training and testing
train_subset = Subset(train_dataset, range(1000))
test_subset = Subset(test_dataset, range(100))
# if you want to use the entire train_dataset and test_dataset then change the two lines below, to use them
train_loader = DataLoader(dataset=train_subset, batch_size=64, shuffle=True)
test_loader = DataLoader(dataset=test_subset, batch_size=1000, shuffle=False)


# Initialize the model, loss function, and optimizer
model = HybridModel()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
n_epochs = 10

for epoch in range(n_epochs):
    model.train()
    running_loss = 0.0
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        
        # Forward pass
        outputs = model(data)
        loss = criterion(outputs, target)
        
        # Backward pass and optimization
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
    
    print(f'Epoch [{epoch + 1}/{n_epochs}], Loss: {running_loss / len(train_loader):.4f}')

# Evaluation
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for data, target in test_loader:
        outputs = model(data)
        _, predicted = torch.max(outputs.data, 1)
        total += target.size(0)
        correct += (predicted == target).sum().item()

accuracy = correct / total
print(f'Accuracy on test set: {accuracy * 100:.2f}%')