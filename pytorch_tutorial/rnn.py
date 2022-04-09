import torch
import torch.nn as nn
input_size = 5 # 입력의 크기
hidden_size = 8 # 은닉 상태의 크기
inputs = torch.Tensor(1, 10, 5)
cell = nn.RNN(input_size,hidden_size,batch_first=True,num_layers=2)
ouputs,_status = cell(inputs)
print(ouputs.shape)
print(_status.shape)

#LSTM  = nn.RNN -> nn.LSTM