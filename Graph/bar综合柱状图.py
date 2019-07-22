
##
##  main.c
##  test3
##
##  Created by 黄日超 on 2018/5/6.
##  Copyright © 2018年 黄日超 . All rights reserved.
##
import matplotlib.pyplot as plt
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting\nChick it out')
x = [2,4,6,8,10]
y = [6,7,8,2,4]
x2 = [2,4,6,8,10]
y2 = [7,8,2,4,2]
plt.bar(x,y,label='bar1',color='r')
plt.bar(x2,y2,label='bar2',color='c')
plt.legend()
plt.show()
