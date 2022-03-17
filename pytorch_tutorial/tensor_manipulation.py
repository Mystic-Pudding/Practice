import torch 
import numpy as np 
t = torch.FloatTensor([0,1,2,3,4,5])
# print(t) # t.dim(),t,shape,t.size(),t[:2]

m1 = torch.FloatTensor([[3,3]])
m2 = torch.FloatTensor([[2]])
#print(m1+m2)

t = np.array([0,1,2,3])
t = torch.FloatTensor(t)
#print(t.view(-1,2))
# print(t.squeeze()) #unsqueeze


#type casting
#t.float() t.long()

#concatenate
#torch.cat

