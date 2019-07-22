
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-04-18 19:19:57
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

myfont = matplotlib.font_manager.FontProperties(fname=r'/Users/huangrichao/Library/Fonts/msyh.ttf')

"""
使用最小二乘法可以解决的问题之
将一个方波分解为
asin(x)+bsin(2x)+...+csin(nx)+dcos(x)+ecos(2x)+...+fcos(nx)
"""
# 产生一个方波(x,y),使用sin函数产生的，sinx>0,y=-1,sinx<0,y=1
x = np.linspace(-10,10,300)
y=[]
for i in x:
    if np.sin(i)>-.79:#调用sin，cos要使用np.sin，np.cos
        y.append(-1)
    else:
        y.append(1)
y=np.array(y)#需要把list转化成array，方便进行矩阵的运算

"""
将一个方波分解为
asin(nx),bcon(nx)的线性组合，
如：
asin(x)+bsin(2x)+...+csin(nx)+dcos(x)+ecos(2x)+...+fcos(nx)
要求的是系数a，b...c,d...e,f组成的矩阵，输入量是方波（x，y）与n的值。
所以定义函数：
"""
#傅立叶函数，sin(nx),cos(nx),n是可以选择的
#所以输入这个函数的三个参数分别为x，n，y
def fourier(x,y,n):
    x1=[]
    for i in range(n):
        x1.append(np.sin(x*i+x))
        x1.append(np.cos(x*i+x))
    m=np.mat(x1).T
    print(m.shape)
    y.shape=(y.shape[0],1)
    p=m*np.linalg.inv(m.T*m)*m.T*y
    ym=np.array(p)
    ym.shape=(ym.shape[0],)
    return ym


#对比选择不同n值得分解结果：
#plt.plot(x,y,color="g",label=u'Square')
plt.plot(x,fourier(x,y,3)-.6,color='r',label='3')
plt.plot(x,fourier(x,y,8)-.6,color='b',label='8')
plt.plot(x,fourier(x,y,140),color='k',label='20ms/Sprint')
plt.title(u'PWM波占空比12.5%',fontProperties=myfont)

plt.legend()
plt.axis('equal')
plt.show()
