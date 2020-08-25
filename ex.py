import turtle as t 

x_min = -5
x_max = 5
y_min = -5
y_max = 5

space =0.1

func = ["y=abs(x)", "y=x*x", "y=0.5*x+1"]

t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.speed(5)
t.pensize(2)

t.up()
t.goto(x_min, 0)
t.down()
t.goto(x_max, 0)

t.up()
t.goto(0, y_min)
t.down()
t.goto(0, y_max)

#x좌표, y좌표가 만들어짐


for i in func:
	t.color("green")
	x = x_min
	exec(i)
	t.up()
	t.goto(x, y)
	t.down()
	while (x <= x_max):
		x = x + space
		exec(i)
		t.goto(x, y)