import turtle #导入海归库
hg=turtle #设置海龟的名字
hg.fillcolor("red") #填充颜色
hg.speed(1)#速度
'''
以下是画正方形
'''
for i in range(0,4):
    hg.fd(200)
    hg.rt(90)
#画正方形结束
hg.seth(0)#面向逆时针0°
hg.up()#抬笔
hg.goto(100,-200)#传送
hg.down()#落笔
'''
以下是菱形
'''
hg.begin_fill()#准备填充
hg.circle(100,360,4)#菱形框架
hg.end_fill()#填充
#画菱形结束
'''
hg.up()
hg.goto(-100,-300)
hg.down()
hg.write("this is my work",True,font=("Harlow Solid Italic",50,"normal"))
'''
hg.hideturtle()#隐藏箭头
hg.done()#停笔