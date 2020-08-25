import turtle as t
import random

score = 0
speed = 1
playing = False

te = t.Turtle() #악당
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
#왜 up을 하면 선이 안그어져?
te.goto(0, 200)

ts = t.Turtle() #먹이
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up() #아 좌표처럼 눌려있는 상태라서 화면으로 띄워준다는 의미
ts.goto(0, -200)

def turn_right():
    t.setheading(0)  #0도를 바라보라는 이야기
    # t.forward(10)

def turn_up():
    t.setheading(90)
    # t.forward(10)

def turn_left():
    t.setheading(180)
    # t.forward(10)

def turn_down():
    t.setheading(270)
    # t.forward(10)

# def black():
#     t.clear()

def play():
    global speed
    t.forward(10)
    ang = te.towards(t.pos()) #현재 흰색 거북이의 좌표값을 나타내라는 뜻
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

def start():
    global playing
    
    if playing == False:
        playing = True
        t.clear()
        play()

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