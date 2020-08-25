import turtle as t
import random

# t.bgcolor("black")
# t.speed(0)

# for x in range(200):
# 	if x % 3 == 0:
# 		t.color("red")
# 	if x % 3 == 1:
# 		t.color("yellow")
# 	if x % 3 == 2:
# 		t.color("blue")
# 	t.toward(x * 2)
# 	t.left(119)

# t.exitonclick()

te = t.Turtle() 	#악당 거북이(빨간색)
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0,200)

ts = t.Turtle()	#먹이(초록색 동그라미)
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0,-200)

def turn_right():	#오른쪽으로 방향을 바꿉니다.
	t.setheading(0)

def turn_up():
	t.setheading(90)

def trun_left():
	t.setheading(180)

def turn_down():
	t.setheading(270)

def play():
	t.toward(10)
	ang = te.towards(t.pos())
	te.setheading(ang)
	te.forward(9)
	if t.distance(ts) < 12:
		start_x = random.randint(-230, 230)
		start_y = random.randint(-230, 230)
		ts.goto(start_x, start_y)
	if t.distance(te) >= 12:
		t.ontimer(play, 100)

t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.shape(0)
t.up()
t.color("white")
t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen()
play()

t.exitonclick()