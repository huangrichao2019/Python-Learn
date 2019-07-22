
##
##  main.c
##  test3
##
##  Created by 黄日超 on 2018/5/6.
##  Copyright © 2018年 黄日超 . All rights reserved.
##
import cv2
import numpy as np#添加模块和矩阵模块
cap=cv2.VideoCapture(0)
#打开摄像头，若打开本地视频，同opencv一样，只需将０换成("×××.avi")
while(1):    # get a frame
    ret, frame = cap.read()    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
#释放并销毁窗口

