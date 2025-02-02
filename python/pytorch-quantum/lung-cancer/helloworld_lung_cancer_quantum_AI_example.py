import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import torch.nn as nn
import torch.optim as optim
import time

import sys
sys.path.append('../../')
from AutomatskiKomencoNative import *



# Load the dataset
df = pd.read_csv('survey-lung-cancer.csv')

# Preprocess the data
# Convert categorical data to numerical
df['GENDER'] = df['GENDER'].map({'M': 0, 'F': 1})
df['LUNG_CANCER'] = df['LUNG_CANCER'].map({'NO': -1, 'YES': 1})

# Extract features and labels
X = df.drop('LUNG_CANCER', axis=1).values
y = df['LUNG_CANCER'].values

# Standardize the features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert to PyTorch tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.float32).unsqueeze(1)
y_test = torch.tensor(y_test, dtype=torch.float32).unsqueeze(1)

# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
sampler = AutomatskiKomencoNative(host="103.212.120.18", port=80) # 

class QuantumLayer(nn.Module):
    def __init__(self, num_qubits, num_layers):
        super(QuantumLayer, self).__init__()
        self.num_qubits = num_qubits
        self.num_layers = num_layers
        
        
    def forward(self, x):
        # Quantum part (Placeholder comments, omitted due to lack of details)
        # x should be of shape (batch_size, num_qubits)
        batch_size = x.size(0)
        output = []
        
        
        for i in range(batch_size):
            # Example of applying quantum operations
            #self.circuit.h(0)  # Apply Hadamard gate
            #self.circuit.cx(0, 1)  # Apply CNOT gate
            
            self.circuit = QuantumCircuit(self.num_qubits)
            
            # Convert input to angles for rotation gates
            for j in range(self.num_qubits):
                self.circuit.ry(x[i, j].item(), j)
                       
            self.circuit.measure_all()
           
            # Run the circuit and get results
            results = sampler.run(self.circuit, repetitions=1000, topK=20)
            #time.sleep(0.1) # connection bug fix 
            
            # Extract and count the measurement results
            measurements = results['result']
            #print(measurements)
            
            # Find the key with the highest value (count)
            state_with_highest_probability = max(measurements, key=measurements.get)
            
            #print(state_with_highest_probability)
            numerical_state_array = [1 if char == '1' else -1 for char in state_with_highest_probability[::-1]]  #reverse the state_with_highest_probability string
            
            output.append(numerical_state_array)
        
        #print(output)
        
        return torch.tensor(output, dtype=torch.float32)
        
        
# Define the neural network model
class HybridModel(nn.Module):
    def __init__(self):
        super(HybridModel, self).__init__()
        self.fc1 = nn.Linear(X_train.shape[1], 15)
        self.quantum_layer1 = QuantumLayer(num_qubits=15, num_layers=1)  # Example with 8 qubits
        self.fc2 = nn.Linear(15, 1)
        
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.quantum_layer1(x) 
        x = torch.sigmoid(self.fc2(x))
        #x = self.fc4(x)
        return x

model = HybridModel()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.0001)

n_epochs = 10

for epoch in range(n_epochs):
    model.train()
    optimizer.zero_grad()
    
    # Forward pass
    outputs = model(X_train)
    loss = criterion(outputs, y_train)
    
    # Backward pass and optimization
    loss.backward()
    optimizer.step()
    
    print(f'Epoch [{epoch + 1}/{n_epochs}], Loss: {loss.item():.4f}')


# Evaluate the model
model.eval()
with torch.no_grad():
    test_outputs = model(X_test)
    test_loss = criterion(test_outputs, y_test)
    print(f'Test Loss: {test_loss.item():.4f}')

    # Convert outputs to binary predictions
    predicted = (test_outputs >= 0.0).float()
    accuracy = (predicted == y_test).sum() / y_test.size(0)

print(f'Accuracy on test set: {accuracy * 100:.2f}%')
