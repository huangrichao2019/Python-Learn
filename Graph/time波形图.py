
##
##  main.c
##  test3
##
##  Created by 黄日超 on 2018/5/6.
##  Copyright © 2018年 黄日超 . All rights reserved.
##

import numpy as np
import matplotlib.pyplot as pl
import matplotlib
import math
import random

myfont = matplotlib.font_manager.FontProperties(fname=r'/Users/huangmengyao/Library/Fonts/msyh.ttf')

pl.figure(figsize=(9,9))
row = 4
col = 4

N = 500
fs = 5
n = [2*math.pi*fs*t/N for t in range(N)]    # 生成了500个介于0.0-31.35之间的点
# print n
axis_x = np.linspace(0,3,num=N)

#频率为5Hz的正弦信号
x = [math.sin(i) for i in n]
pl.subplot(221)
pl.plot(axis_x,x)
pl.title(u'5Hz的正弦信号',FontProperties=myfont)




#频率为5Hz、幅值为3的正弦+噪声
x1 = [random.gauss(0,0.5) for i in range(N)]
xx = []
#有没有直接两个列表对应项相加的方式？？
for i in range(len(x)):
    xx.append(x[i]*3 + x1[i])

pl.subplot(222)
pl.plot(axis_x,xx)
pl.title(u'频率为5Hz、幅值为3的正弦+噪声',FontProperties=myfont)


#频谱绘制
xf = np.fft.fft(x)
xf_abs = np.fft.fftshift(abs(xf))
axis_xf = np.linspace(-N/2,N/2-1,num=N)
pl.subplot(223)
pl.title(u'频率为5Hz的正弦频谱图',FontProperties=myfont)
pl.plot(axis_xf,xf_abs)


#频谱绘制
xf = np.fft.fft(xx)
xf_abs = np.fft.fftshift(abs(xf))
pl.subplot(224)
pl.title(u'频率为5Hz的正弦频谱图',FontProperties=myfont)
pl.plot(axis_xf,xf_abs)

pl.axis('tight')
pl.show()
