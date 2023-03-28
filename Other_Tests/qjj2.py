# coding=gbk
import torch
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-3,3,30)
f=x**2

f_noise=f+np.random.randn(x.__len__()) #��ӵ��ǻ��ڸ�˹�ֲ��������




#������Ϻ���
def f_prob(x,a,b,c):
    return a*(x**2)+b*x+c

x_tensor=torch.from_numpy(x)
f_tensor=torch.from_numpy(f_noise)
#��ƫ��
def gradient(x,y,a,b,c):
    x_len=len(x)
    tmp_value=f_prob(x,a,b,c)-y
    ja=2/x_len*(tmp_value*x.pow(2)).sum()
    jb=2/x_len*(tmp_value*x.pow(1)).sum()
    jc=2/x_len*(tmp_value*x.pow(0)).sum()
    return torch.Tensor([ja,jb,jc])

#����a��b��c��n���������
coeff_value=torch.Tensor([1,1,1])
lr=0.05
iterations=30
loss_return_list=[]
re_ix=[]
for ix in range(iterations):
    # coeff_value-lr*gradient(x_tensor,f_tensor,coeff_value[0],coeff_value[1],coeff_value[2])
    coeff_value=coeff_value-lr*gradient(x_tensor,f_tensor,*coeff_value)
    loss_value=(f_prob(x_tensor,*coeff_value)-f_tensor).pow(2).sum().numpy()
    loss_return_list.append(round(float(loss_value),2))
    print("��������:{0},ϵ����:{1},��ʧ����:{2:.2f}".format(ix+1,coeff_value,loss_value))
    re_ix.append(ix+1)



#��ͼ
fig=plt.figure(figsize=(7,5))
plt.plot(x,f,'r-',label='original')
plt.scatter(x,f_noise)
plt.plot(x,f_prob(x_tensor,*coeff_value).numpy(),'g-',label='fitting')
plt.legend()
plt.xlabel('$x$')
plt.ylabel('$x$')
plt.show()


fig2=plt.figure(figsize=(7,5))
plt.plot(re_ix,loss_return_list,'x')
plt.plot(re_ix,loss_return_list,'r-',label='fitting')
plt.xlabel('$x$')
plt.ylabel('$x$')
plt.show()
