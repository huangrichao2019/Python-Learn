
##
##  main.c
##  test3
##
##  Created by 黄日超 on 2018/5/6.
##  Copyright © 2018年 黄日超 . All rights reserved.
##
"""
    树莓派ssh链接key
    ➜  ~ sudo ssh 10.20.20.205
    Password:
    The authenticity of host '10.20.20.205 (10.20.20.205)' can't be established.
    ECDSA key fingerprint is SHA256:9fuPVjZCddHb9oddMoyiBnl3aA4IkdhQayTth6KMefo.
    Are you sure you want to continue connecting (yes/no)? y
    Please type 'yes' or 'no': yes
    Warning: Permanently added '10.20.20.205' (ECDSA) to the list of known hosts.
    root@10.20.20.205's password:
"""
from socket import *
import time

'''
def load():
    with open('C:\\Users\\A\\Desktop\\Aliyun-godEyes\\linkdevelop-webapp-device\\control1.json')as json_file:
        data = json.load(json_file)
        return data
'''
port = 12141
host  = '192.168.43.246' # 这是客户端的电脑的ip
bufsize = 102400  #定义缓冲大小
addr = (host,port) # 元祖形式
udpClient = socket(AF_INET,SOCK_DGRAM)#创建客户端

#data,addr = udpClient.recvfrom(bufsize) #接收数据和返回地址
#data = data.decode(encoding = 'utf-8')
while True:
    send = str(input("请输入控制摄像头转动:"))
    print('发送指令：',send)
    send = send.encode(encoding = "utf-8")
    udpClient.sendto(send, addr)
    time.sleep(0.1)
#data,addr = udpClient.recvfrom(bufsize) #接收数据和返回地址
#data = data.decode(encoding = 'utf-8')




