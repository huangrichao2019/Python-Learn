
##
##  main.c
##  test3
##
##  Created by 黄日超 on 2018/5/6.
##  Copyright © 2018年 黄日超 . All rights reserved.
##
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_colorspaces/py_colorspaces.html#converting-colorspaces
# -- coding: utf-8 --
#如若程序有中文注释，将上行代码加到代码的第一行或第二行
#识别摄像头图像中的指定颜色并显示
###########################################
####Import Module                      ####
import cv2
import numpy as np
###########################################
####Main Function                      ####
#print color space convert method
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
#BGR 转换成 HSV 的好处：HSV模型的三维表示从RGB立方体演化而来,可以更具体的知道颜色信息
#HSV概念具体参见https://baike.baidu.com/item/HSV/547122?fr=aladdin
#HSV值表参见http://blog.csdn.net/scythe666/article/details/45748187
#1.H参数表示色彩信息，即所处的光谱颜色的位置。该参数用角度量来表示，红色为0度，绿色为120度，蓝色为240度，红、绿、蓝分别相隔120度。互补色分别相差180度。
#2.S参数表示饱和度，该参数为一比例值，范围从0到1，它表示成所选颜色的纯度和该颜色最大的纯度之间的比率。S=0时，只有灰度。
#3.V参数表示色彩的明亮程度，范围从0到1。有一点要注意：它和光强度之间并没有直接的联系。
cap = cv2.VideoCapture(0)
while(1):
    
    # Take each frame
    ret, frame = cap.read()
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # define range of blue color in HSV
    #修改阈值上下限即是修改目标颜色
    #HSV值表参见http://blog.csdn.net/scythe666/article/details/45748187
    lower_blue = np.array([112,25,25])
    upper_blue = np.array([255,255,255])
    
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    #    cv2.imshow('frame',frame)
    #    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
