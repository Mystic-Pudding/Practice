import pandas as pd 
import numpy as np 
x = []
data_sample = []
y = []
for i in range(1,1000,1):
    if(i%4==0):
        y.append([i])
        x.append(np.array(data_sample))
        data_sample = []
    else:
        data_sample.append(int(i))

import torch.nn as nn 
import torch.nn.functional as F
import torch

x_train  =  torch.FloatTensor(x)  
y_train  =  torch.FloatTensor(y)

# 모델 초기화
W = torch.zeros((3, 1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)
# optimizer 설정
optimizer = torch.optim.SGD([W, b], lr=1e-5)

nb_epochs = 20
for epoch in range(nb_epochs + 1):

    # H(x) 계산
    # 편향 b는 브로드 캐스팅되어 각 샘플에 더해집니다.
    hypothesis = x_train.matmul(W) + b

    # cost 계산
    cost = torch.mean((hypothesis - y_train) ** 2)

    # cost로 H(x) 개선
    optimizer.zero_grad()
    cost.backward()
    optimizer.step()

print(W,b)