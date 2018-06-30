import turtle_resources as r
import turtle

turtles = list(map(lambda i:turtle.Turtle(), range(int(input('How many turtles do you want?'))))) #입력한 (유효한)수 만큼 거북이를 생성합니다
#=======입력한 수 만큼 거북이를 생성하는 대안적인 코드입니다=========
# tnum = range(int(input('How many turtles do you want?')))
# turtles = [turtle.Turtle() for t in tnum]
#====================================================================
turtle.bgcolor(0,0,0)       #배경을 검게 만들어줍니다
loop = 0
for t in turtles:
    r.shaping(t,0.5+0.1*loop)
    loop += 1

while True:
    for t in turtles:
        r.move(t)
        x = t.xcor()
        y = t.ycor()
        r.setright(t,x,y)

turtle.done()
