import matplotlib.pyplot as plt
import matplotlib



####
## @author 黄日超
## @data 2018.06.11
## @description SG90电机旋转度数与输入的PWM
####


matplotlib.rcParams["font.sans-serif"] = ["Microsoft YaHei"]
matplotlib.rcParams['axes.unicode_minus'] = False

myfont = matplotlib.font_manager.FontProperties(fname=r'/Users/huangrichao/Library/Fonts/msyh.ttf')

x = ['2.5%','4%','6%','7.5%','9%','11%','12.5%']
y1 = [-45,30,60,90,120,150,180]
y2 = [-45,39,52,102,112,152,177]
y3 = [-45,20,65,79,125,142,183]
plt.plot(x,y1,marker="o",mec='r',mfc='w',label='First')
plt.plot(x,y2,marker="*",ms='10',label='Second')
plt.plot(x,y3,marker=".",c='red',ms='10',label='Third')
plt.title("同一型号不同舵机的脉冲响应差异",fontproperties=myfont)
plt.xlabel("PWM")
plt.ylabel("Angle")

plt.legend()
plt.savefig('/Users/huangrichao/Desktop/毕业设计/p3.png')
plt.show()
