import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

import sys
sys.path.append('../../')
from AutomatskiKomencoNative import *


# Load the Titanic dataset
filename = 'titanic.csv' # use a small dataset 'titanic_small.csv' for trial run instead of the full dataset 
data = pd.read_csv(filename)

# Select relevant features and target
features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']
data = data[features + ['Survived']]

# Handle missing values
data.fillna( {'Age':data['Age'].mean()}, inplace=True)
data.fillna( {'Embarked': data['Embarked'].mode()[0] }, inplace=True)

# Convert categorical variables into numeric
data['Sex'] = data['Sex'].map({'male': 0, 'female': 1})
data = pd.get_dummies(data, columns=['Embarked'], drop_first=True)

# Separate features and target
X = data.drop('Survived', axis=1).values
y = data['Survived'].values

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Convert data to PyTorch tensors
X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
y_train = torch.tensor(y_train, dtype=torch.long)
y_test = torch.tensor(y_test, dtype=torch.long)


# Run the Circuit using Automatski' Quantum Simulators and Quantum Computers
sampler = AutomatskiKomencoNative(host="103.212.120.18", port=80)

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
                self.circuit.rx(x[i, j].item(), j)
            
            
            
            self.circuit.measure_all()
           
            # Run the circuit and get results
            results = sampler.run(self.circuit, repetitions=1000, topK=20)

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

class HybridModel(nn.Module):
    def __init__(self):
        super(HybridModel, self).__init__()
        self.fc1 = nn.Linear(X_train.shape[1], 8)
        self.quantum_layer = QuantumLayer(num_qubits=8, num_layers=1)  # Example with 8 qubits
        self.fc2 = nn.Linear(8, 2)  # Binary classification
        
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.quantum_layer(x) # (x[:, :4])  # Example using the first 4 features
        x = torch.log_softmax(self.fc2(x), dim=1)
        return x



model = HybridModel()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

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


model.eval()
with torch.no_grad():
    outputs = model(X_test)
    _, predicted = torch.max(outputs.data, 1)
    accuracy = (predicted == y_test).sum().item() / y_test.size(0)

print(f'Accuracy on test set: {accuracy * 100:.2f}%')
