from turtle import forward
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

x_data = [[1, 2], [2, 3], [3, 1], [4, 3], [5, 3], [6, 2]]
y_data = [[0], [0], [0], [1], [1], [1]]
x_train = torch.FloatTensor(x_data)
y_train = torch.FloatTensor(y_data)
W = torch.zeros((x_train.shape[1],y_train.shape[1]), requires_grad=True)
b = torch.zeros(y_train.shape[1], requires_grad=True)
optimizer = optim.SGD([W,b], lr = 1)
for epoch in range(1001):
    hypothesis = torch.sigmoid(x_train.matmul(W) + b)
    cost = F.binary_cross_entropy(hypothesis,y_train)
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()
print(hypothesis)
prediction = hypothesis >= torch.FloatTensor([0.5])
print(prediction)

#model separate

# model = nn.Sequential(
#     nn.Linear(2,1),
#     nn.Sigmoid()
# )
# class BinaryClassifier(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.linear = nn.Linear(2,1)
#         self.sigmoid = nn.Sigmoid()
#     def forward(self, x):
#         return self.sigmoid(self.linear(x))
