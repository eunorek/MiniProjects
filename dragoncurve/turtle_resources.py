import random

#거북이가 스크린의 가장자리 너머로 도망가려 할 때 뒤로 150만큼 잡아당기는 기능을 합니다.
def setright(t,x,y):
    if x >= 300 or x <= -300 or y >= 250 or y <= -250: t.backward(150)

#거북이의 색을 랜덤한 값으로 정해줍니다
def rgb():
    r = random.uniform(0,1)
    g = random.uniform(0,1)
    b = random.uniform(0,1)
    return (r,g,b)

#거북이가 자기 턴에 움직입니다
def move(t):
    t.color(rgb())
    orient = random.choice([0, 1, 2])
    if orient == 1: t.right(90)
    elif orient == 2: t.left(90)
    t.forward(10)

#거북이들의 기본적인 각자의 속성을 설정합니다.
def shaping (t,size):
    t.speed(0)
    t.pensize(2)
    t.shape("turtle")
    t.shapesize(size, size, size)
    #t.hideturtle()                                  #거북이를 깔끔하게 숨겨줍니다
