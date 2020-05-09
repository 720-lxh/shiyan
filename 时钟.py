import turtle as tt
import time

def drawLine(draw):#七段数码管一段
    if draw :
        for i in range(10):
            tt.pd()
            tt.fd(0)
            tt.pu()
            tt.fd(4)
        tt.pd()
        tt.fd(0)
    else :
        tt.pu()
        tt.fd(40)
    tt.right(90)

def draw(d):#七段数码管一个数字
    drawLine(True) if d in[2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in[0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in[0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if d in[0,2,6,8] else drawLine(False)
    tt.left(90)
    drawLine(True) if d in[0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if d in[0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if d in[0,1,2,3,4,7,8,9] else drawLine(False)
    
def shi():#提出当前小时（1~12）
    m = str(time.strftime("%I",time.localtime(time.time())))
    if m[0]=='0':
        i = eval(m[-1])
    else:
        i = eval(m)
    return i

def fen():#提出当前分钟
    m = str(time.strftime("%M",time.localtime(time.time())))
    if m[0]=='0':
        i = eval(m[-1])
    else:
        i = eval(m)
    return i

def miao():#提出当前秒
    m = str(time.strftime("%S",time.localtime(time.time())))
    if m[0]=='0':
        i = eval(m[-1])
    else:
        i = eval(m)
    return i

def zhen1(h,c,j):
    tt.pu()
    tt.home()
    tt.fd(20)#时钟中心
    tt.pd()
    tt.width(h)#针宽度
    tt.seth(j+90)#针摆角
    tt.fd(c)#针长度

def zhen2():#清除针
    tt.pu()
    tt.home()
    tt.fd(20)
    tt.seth(-90)
    tt.fd(140)
    tt.seth(0)
    tt.pd()
    tt.pencolor(1,1,1)
    tt.fillcolor(1,1,1)
    tt.begin_fill()
    tt.circle(142)
    tt.end_fill()
    tt.pencolor(0,0,0)
    
def zhen3():#画出三个针
    tt.tracer(False)
    zhen2()
    tt.pu()
    tt.home()
    tt.fd(20)
    tt.width(10)
    tt.pd()
    tt.fd(0)#画中点
    zhen1(6,90,shi()*(-30))
    zhen1(4,120,fen()*(-6))
    zhen1(3,140,miao()*(-6))
    tt.tracer(True)

tt.setup(800,800)
tt.width(4)
tt.speed(1000)
for i in range(1,10):
    tt.pu()
    tt.home()
    tt.seth(i*(-30)+90)
    tt.fd(200)
    tt.seth(0)
    if(i==1):
        tt.fd(-20)
    draw(i)
for i in range(10,13):
    tt.pu()
    tt.home()
    tt.seth(i*(-30)+90)
    tt.fd(200)
    tt.seth(0)
    tt.fd(-40)
    draw(1)
    tt.pu()
    tt.seth(0)
    tt.fd(10)
    draw(i-10)
while miao()<=59:#转两圈（并没有）
    zhen3()
    if miao()==59:
        break
while miao()<59:
    zhen3()
    if miao()==58:
        break
