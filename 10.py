#자주색 정오각형 만들기
#오각형 변의 길이 = 50
#오각형 내각 = 360/5
import turtle as t
n=5	#오각형을 그립니다. 다른 값을 입력하면 다른 도형을 그립니다.
t.color("purple")	#객체 t의 색을 자주색으로 지정합니다.
t.begin_fill()	#색칠할 영역 시작 함수
t.speed(0)
for x in range(n):
	t.forward(50)	#for문을 사용하여 변의 길이 50으로 하고
	t.left(360/n)	#각도를 360을 5로 나눈값을 지정
t.end_fill()


#원반복
#반지름크기 80인녹색원 50개를 반복그리기
#반복그리기 각변화= 360/50
import turtle as t 
n = 50	#50개 원 그리기
t.bgcolor("black")	#바탕화면의 색을 검은색으로 지정
t.color("green")	#객체 t의 색을 녹색으로 지정
t.speed(0)
for x in range(n):	#for문을 사용하여 50번 반복
	t.circle(80)	#반지름 80인 원을 그리는 함수
	t.left(360/n)	#360/50만큼 왼쪽으로 방향 변경하는 함수


#선반복
#상황: 각도를 200번변경 하면서 200개의선을 그리기
#1부터 200까지 선의길이가 증가함
import turtle as t 
angle = 89
t.bgcolor("black")
t.color("yellow")
t.speed(0)
for x in range(200):	#for문을 사용하여
	t.forward(x)		#선의 길이를 0부터 199까지 증가시키면서 0부터 199까지 선을 긋는 것을 반복
	t.left(angle)		#각도 89만큼 왼쪽으로 방향 변경하는 함수


t.exitonclick()