# import torch
# import torch.nn as nn
# import torch.nn.functional as F
# import torch.optim as optim
# class SoftmaxClassifierModel(nn.Module):
#     def __init__(self) -> None:
#         super().__init__()
#         self.linear = nn.Linear(4,3)
#     def forward(self,x):
#         return self.linear(x)
# x_train = [[1, 2, 1, 1],
#            [2, 1, 3, 2],
#            [3, 1, 3, 4],
#            [4, 1, 5, 5],
#            [1, 7, 5, 5],
#            [1, 2, 5, 6],
#            [1, 6, 6, 6],
#            [1, 7, 7, 7]]
# y_train = [2, 2, 2, 1, 1, 1, 0, 0]
# x_train = torch.FloatTensor(x_train)
# y_train = torch.LongTensor(y_train)
# y_one_hot = torch.zeros(8,3)
# y_one_hot.scatter_(1,y_train.unsqueeze(1),1)
# print(y_one_hot.shape) #(low,class count)
# # W = torch.zeros((x_train.shape[1], y_one_hot.shape[1]), requires_grad=True)
# # b = torch.zeros(1,requires_grad=True)
# model = SoftmaxClassifierModel()
# optimizer = optim.SGD(model.parameters(), lr=0.1)
# for epoch in range(100):
#     hypothesis = model(x_train)
#     cost = F.cross_entropy(hypothesis,y_train)
#     optimizer.zero_grad()
#     cost.backward()
#     optimizer.step()
# print(cost)

import torch
import torchvision.datasets as dsets
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
import torch.nn as nn
import matplotlib.pyplot as plt
import random

USE_CUDA = torch.cuda.is_available()
device = torch.device("cuda" if USE_CUDA else "cpu")
training_epoch = 15
batch_size = 100
mnist_train = dsets.MNIST(root='MNIST_data/',
                          train=True,
                          transform=transforms.ToTensor(),
                          download=True)

mnist_test = dsets.MNIST(root='MNIST_data/',
                         train=False,
                         transform=transforms.ToTensor(),
                         download=True)
data_loader = DataLoader(dataset=mnist_train,batch_size=batch_size, shuffle=True,drop_last=True)
linear = nn.Linear(784, 10, bias=True).to(device)
criterion = nn.CrossEntropyLoss().to(device)
optimizer = torch.optim.SGD(linear.parameters(),lr=0.1)

for epoch in range(training_epoch): # 앞서 training_epochs의 값은 15로 지정함.
    avg_cost = 0
    total_batch = len(data_loader)

    for X, Y in data_loader:
        # 배치 크기가 100이므로 아래의 연산에서 X는 (100, 784)의 텐서가 된다.
        X = X.view(-1, 28 * 28).to(device)
        # 레이블은 원-핫 인코딩이 된 상태가 아니라 0 ~ 9의 정수.
        Y = Y.to(device)

        optimizer.zero_grad()
        hypothesis = linear(X)
        cost = criterion(hypothesis, Y)
        cost.backward()
        optimizer.step()

        avg_cost += cost / total_batch

    print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

print('Learning finished')
with torch.no_grad(): # torch.no_grad()를 하면 gradient 계산을 수행하지 않는다.
    X_test = mnist_test.test_data.view(-1, 28 * 28).float().to(device)
    Y_test = mnist_test.test_labels.to(device)

    prediction = linear(X_test)
    correct_prediction = torch.argmax(prediction, 1) == Y_test
    accuracy = correct_prediction.float().mean()
    print('Accuracy:', accuracy.item())

    # MNIST 테스트 데이터에서 무작위로 하나를 뽑아서 예측을 해본다
    r = random.randint(0, len(mnist_test) - 1)
    X_single_data = mnist_test.test_data[r:r + 1].view(-1, 28 * 28).float().to(device)
    Y_single_data = mnist_test.test_labels[r:r + 1].to(device)

    print('Label: ', Y_single_data.item())
    single_prediction = linear(X_single_data)
    print('Prediction: ', torch.argmax(single_prediction, 1).item())

    plt.imshow(mnist_test.test_data[r:r + 1].view(28, 28), cmap='Greys', interpolation='nearest')
    plt.show()