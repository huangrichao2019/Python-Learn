
##
##  main.c
##  test3
##
##  Created by 黄日超 on 2018/5/6.
##  Copyright © 2018年 黄日超 . All rights reserved.
##
# coding=utf-8
'''
import numpy as np
import matplotlib.pyplot as plt



    极坐标分为：极径和角度
    

r = np.arange(2.5, 12.5, 1)

theta = [i*np.pi/10 for i in range(10)]


ax = plt.subplot(111,projection='polar')
#projection = 'polar' 指定为极坐标

ax.plot(theta, r, linewidth=3,color='red')
#第一个参数为角度，第二个参数为极径

ax.grid(True) #是否有网格

plt.show()
'''
# coding=utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib


myfont = matplotlib.font_manager.FontProperties(fname=r'/Users/huangrichao/Library/Fonts/msyh.ttf')

plt.figure(figsize=(9,6))
           
r = np.arange(2.5,12.5,0.1)
r1 = np.arange(3.5,10.5,0.07)
t = np.arange(0,1,0.01)
theta = np.pi*t

ax = plt.subplot(111,projection='polar')
bx = plt.subplot(111,projection='polar')
#projection = 'polar' 指定为极坐标

ax.plot(theta, r, linewidth=3,color='green',label="Ideality Case")
bx.plot(theta, r1, linewidth=3,color='black',label="Actually Case")
#第一个参数为角度，第二个参数为极径

x0 = 1
y0 = 2*x0 + 3.5
plt.plot([x0,x0,],[0,y0],'k--',linewidth=2.5)

plt.scatter([x0, ], [y0, ], s=50, color='r') #在这点加个蓝色的原点 原点大小50
plt.title(u'以PWM波的占空比为极距',fontproperties=myfont)
ax.grid(True) #是否有网格
plt.legend()
plt.savefig('/Users/huangrichao/Desktop/毕业设计/p2.png')
plt.show()

