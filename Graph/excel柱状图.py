
##
##  main.c
##  test3
##
##  Created by 黄日超 on 2018/5/6.
##  Copyright © 2018年 黄日超 . All rights reserved.
##
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

myfont = matplotlib.font_manager.FontProperties(fname=r'/Users/huangmengyao/Library/Fonts/msyh.ttf')
plt.figure(figsize=(6,9))

X=[0,6,12]
Y=[4,6,6]
p1 = plt.bar(X,Y,0.3,color="green")
for a,b in zip(X,Y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=8)

X=[1,7,13]
Y=[7,9,33]
p2 =plt.bar(X,Y,0.3,color="blue")
for a,b in zip(X,Y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=8)

X=[2,8,14]
Y=[32,32,19]
p3 =plt.bar(X,Y,0.3,color="red")
for a,b in zip(X,Y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=8)

X=[3,9,15]
Y=[40,42,21]
p4 =plt.bar(X,Y,0.3,color="cyan")
for a,b in zip(X,Y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=8)

X=[4,10,16]
Y=[10,8,4]
p5 =plt.bar(X,Y,0.3,color="black")
for a,b in zip(X,Y):
    plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=8)

XX=[2,8,14]
YY=[32,32,32]
ZZ=['14级','15级','16级']
for a,b,c in zip(XX,YY,ZZ):
    plt.text(a,b+2,'%s' %c,ha='center', va= 'bottom',fontsize=15,fontproperties=myfont)

plt.legend([p1,p2,p3,p4,p5], [u'优秀', u'良好',u'中等',u'及格',u'不及格'], loc='upper right', scatterpoints=1,prop=myfont)

plt.xlabel(u'X-年级',fontproperties=myfont)
plt.ylabel(u'Y-人数',fontproperties=myfont)
plt.title(u'信息学院年级成绩分布柱状图',fontproperties=myfont)

fig = plt.figure()
plt.show()
plt.savefig("barChart.jpg")
