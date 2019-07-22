
##
##  main.c
##  test3
##
##  Created by 黄日超 on 2018/5/6.
##  Copyright © 2018年 黄日超 . All rights reserved.
##
import matplotlib.pyplot as plt
import matplotlib

# 解决中文乱码问题
myfont = matplotlib.font_manager.FontProperties(fname=r'/Users/huangmengyao/Library/Fonts/msyh.ttf')
plt.rcParams['font.sans-serif']=['SimHei']

plt.figure(figsize=(6,9))
labels = [u'优秀',u'Hogs',u'Dogs',u'Logs']
sizes = [15,30,45,10]
explode = (0,0.1,0,0) #0.1表示将Hogs那一块凸显出来
patches,text1,text2 = plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90) #startangle表示饼图的起始角度
plt.title(u'信息学院15级学生成绩分布',fontProperties=myfont)
plt.axis('equal')
plt.legend()
plt.savefig('/Users/huangmengyao/Desktop/毕业设计/p1.png')
plt.show()

