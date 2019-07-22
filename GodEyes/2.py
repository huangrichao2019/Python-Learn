import godEye
import cv2
import numpy as np
from socket import *
import time

def hello():
    '''作者黄日超。初始化，取str型坐标，接收当前占空比i，追踪算法()'''

Window = "GodEye_0"
port = 13141
cap=cv2.VideoCapture(int(0))
cap.set(3,640) #设置分辨率
cap.set(4,480)
fps =cap.get(cv2.CAP_PROP_FPS)
success, frame = cap.read()
color = (255,200,0)
classfier=cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
host  = '192.168.43.246' # 这是客户端的电脑的ip
bufsize = 102400  #定义缓冲大小
addr = (host,port) # 元祖形式
udpClient = socket(AF_INET,SOCK_DGRAM)#创建客户端

count = 0 #初始化计时器
x_str = 0 #全局化str型坐标变量
face = 0 #全局化识别记录变量face
#创建识别文档字典
#data = {}
#flag = 0

while success:
    count +=1
    success, frame = cap.read()
    faceRects = godEye.Process(frame,cap,classfier)
    if(len(faceRects)>0):
        #flag+=1
        #data["Isrecognize"]=flag,'person','found at East of classroom'
        #data['Time'] = time.ctime()
        #TianYan.store(data)
        for faceRect in faceRects[:1]:
            x_str=godEye.Coordinate(faceRect,frame,color)
            x = x_str.encode(encoding="utf-8")
            print(x)
            udpClient.sendto(x,addr)
        data_f = godEye.PrintReceive(bufsize,udpClient)
        print('current Cuty:{0:.1f}'.format(data_f))
        face +=1
        count = 0

    elif(face>0):
        godEye.AutoTurn(count,x_str,addr,udpClient,bufsize)
                
    cv2.imshow(Window, frame)

    if godEye.QuitCheck():
        break
        
cap.release
cv2.destroyWindow(Window)
udpClient.close()
