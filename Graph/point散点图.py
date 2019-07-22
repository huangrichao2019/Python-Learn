
##
##  main.c
##  test3
##
##  Created by 黄日超 on 2018/5/6.
##  Copyright © 2018年 黄日超 . All rights reserved.
##
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6,7,8,9]
y = [1,2,3,4,5,6,7,8,9]
plt.scatter(x,y,label='skit',color='k',marker = '*',s = 100)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('ok')
plt.show()
