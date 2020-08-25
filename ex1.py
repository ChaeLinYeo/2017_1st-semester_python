import turtle as t
import random

#아무 곳에서나 생성되는 초록색 먹이를 먹으면서
#빨간 색 거북이를 피해 돌아다니는 게임

score = 0
speed = 1#흰색 거북이가 초록색 먹이를 먹을 때마다 빨간색 거북이 속도가 2씩 증가한다.

te = t.Turtle() # 악당 거북이
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0,200)
 
ts= t.Turtle() # 먹이
ts.shape('circle')
ts.color('green')
ts.speed(0)
ts.up()
ts.goto(0, -200)

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)
 
def turn_left():
    t.setheading(180)
    
def turn_down():
    t.setheading(270)

def play():
    global speed
    te.forward(10)
    ang = te.toward(t.pos())
    te.setheading(ang)
    te.forward(speed)
    if t.distance(ts) < 12: #간격이 12미만이면 먹은걸로 간주
        global score
        score = score + 1
        speed = speed + 2
        t.write(score)
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y)#random으로 이동이 됨

    if t.distance(ts) >= 12:
    	t.ontimer(play, 100)#빨간 거북이와 접촉하면 게임 끝남 

    t.ontimer(play,100) #0.1초 후에 play실행 1000분의 1초가 단위

t.setup(500,500) #창의 크기
t.bgcolor('orange') # 창의 배경색 오렌지색
t.shape('turtle')
t.color('white')
t.speed(0)
t.up()

t.onkeypress(turn_right,"Right")
t.onkeypress(turn_left,"Left")
t.onkeypress(turn_up,"Up")
t.onkeypress(turn_down,"Down")
t.listen()
play()
t.exitonclick()