#太极.py
import turtle as tt

def waikuo(z):
    tt.pd
    tt.tracer(False)
    tt.clear()
    tt.width(1)
    tt.left(z)
    tt.fillcolor(0,0,0)
    tt.begin_fill()
    tt.circle(-100,180)
    tt.circle(-200,-180)
    tt.circle(-100,-180)
    tt.end_fill()
    tt.pencolor(1,1,1)
    tt.fillcolor(1,1,1)
    tt.begin_fill()
    tt.circle(-100,180)
    tt.circle(-200,-180)
    tt.circle(-100,-180)
    tt.end_fill()
    #外轮廓
    tt.pu()
    tt.right(90)
    tt.pencolor(0,0,0)
    tt.fd(100)
    tt.width(30)
    tt.pd()
    tt.fd(0)
    tt.pu()
    tt.right(180)
    tt.fd(200)
    tt.pd()
    tt.pencolor(1,1,1)
    tt.fd(0)#两点
    tt.pu()
    tt.home()
    tt.tracer(True)
        
tt.setup(500,500,200,200)
tt.ht()
for n in range(5):
    for i in range(0,361,1):
        waikuo(i)


