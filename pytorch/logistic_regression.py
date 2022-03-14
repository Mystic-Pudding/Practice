import torch
class BinaryClassfier(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8,1)
        self.sigmoid = torch.nn.Sigmoid()
    def forward(self, x):
        return self.sigmoid(self.linear(x))
model = BinaryClassfier()
optimizer = torch.optim.SGD(model.parameters(), lr=1)

for epoch in range(100):
    hypothesis = model(x_train)
    cost =torch.nn.BCELoss(hypothesis,y_train)

    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

    