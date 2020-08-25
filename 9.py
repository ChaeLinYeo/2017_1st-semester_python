A = {1,2,3,4}
B = {3,4,5,6}
print(A)
print(B)
print(1 in A)
print(6 in A)
print(len(A))
print(A|B)	#합집합
print(A&B)	#교집합
print(A-B)	#차집합 



C = {x for x in range(1, 11)}	#C = {x|x는 1이상 11미만의 정수}
D = {x for x in range(1, 11) if x%3==0}	#C = {x|x는 1이상 11미만의 3의 배수}
print(C)
print(D)
print(C<D)	#C는 D의 부분집합인가?
print(D<C)	#D는 C의 부분집합인가?



##어려워 
#소인수분해 프로그램 
#소인수분해 : 어떤 정수를 소수의 곱만으로 표현하는것.
num = int(input("소인수분해할 정수를 입력하세요 : "))
result = 2
while result<= num:
	if num % result == 0:
		print(result)
		num = num/result
	else:
		result = result+1



#기초 통계
#평균 : 여러 개의 자료값을 모두 더한 다음 자료의 개수로 나눈 값
#분산 : 편차 제곱의 평균값, 즉, 각 자료값에서 평균값을 뺀 값(편차)의 제곱을 모두 더해서 자료의 개수로 나눈 값
#표준편차 : 분산의 제곱 근
import math
d = [1,2,3,4,5]
print(d)
#평균 구하기
mean = sum(d)/len(d)
print(mean)
#분산 구하기
vsum = 0
for x in d:
	vsum = vsum + (x-mean)**2
var = vsum/len(d)
print(var)
#표준편차 구하기
std = math.sqrt(var)	#sqrt는 루트!
print(std)



import math
import sys
print("ax2 + bx + c = 0")
#계수 a,b,c를 입력받고, 입력받은 문자열을 소수로 바꿉니다.
a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))
D = b*b - 4*a*c #판별식
if a == 0:
	print("a=0 : 이차방정식이 아닙니다.")
	sys.exit()	#이차방정식이 아니면 프로그램 실행을 멈춥니다.
D = b*b - 4*a*c #판별식
if D > 0 :	#근이 두개일 때
	result1 = (-b - math.sqrt(D))/2*a
	result2 = (-b + math.sqrt(D))/2*a
	print("2개의 해 : ", result1, result2)
elif D == 0 : #근이 한 개일 때
	result = -(b/2*a)
	print("1개의 해 : ", result)
else:
	print("해가 없습니다.")



import turtle as t 
#그래프를 그릴 x 좌표 범위
x_min = -5
x_max = 5
#그래프를 그릴 y 좌표 범위
y_min = -5
y_max = 5
#그래프를 그릴 간격
space = 0.1
#그릴 함수의 리스트
func_list = ["y=x*x", "y=abs(x)", "y=0.5*x+1"]
#좌표 설정, 거북이 속도, 선 굵기
t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.speed(0)
t.pensize(2)
#x축 그리기
t.up()
t.goto(x_min, 0)
t.down()
t.goto(x_max, 0)
#y축 그리기
t.up()
t.goto(0, y_min)
t.down()
t.goto(0, y_max)
#그래프 그리기
t.color("green")
for func in func_list:	#func_list에 있는 함수를 하나씩 그립니다.
	x = x_min	#x_min부터 계산을 시작합니다.
	exec(func)	#수식을 계산합니다.
	t.up()
	t.goto(x,y)	#계산된 좌표로 이동합니다.
	t.down()
	while x <= x_max:	#x_max까지 그래프를 그립니다. 
		x = x+space	#space만큼 x를 증가시킨 후
		exec(func)	#수식을 계산합니다.
		t.goto(x,y)	#계산된 좌표로 이동합니다.



#계산맞추기
import random
def make_question():
	a = random.randint(1, 40)	#1~40 사이의 임의의 수를 a에 저장합니다.
	b = random.randint(1, 20)	#1~20 사이의 임의의 수를 b에 저장합니다.
	op = random.randint(1, 3)	#1~3 사이의 임의의 수를 op에 저장합니다.
	#문자열 변수 q에 문제를 만듭니다.
	#첫 번째 숫자를 q에 저장합니다.
	q = str(a)	#a값(정수)를 문자열로 바꾸어 저장합니다.
	#연산자를 추가합니다.
	if op == 1:
		q = q+"+"
	if op == 2:
		q = q+"-"
	if op == 3:
		q = q+"*"
	#두번째 숫자를 q에 저장합니다.
	q = q + str(b)
	#만들어진 문제를 돌려줍니다.
	return q
#정답/오답 횟수를 저장할 변수 sc1과 sc2를 0으로 초기화합니다.
sc1 = 0
sc2 = 0
for x in range(5):
	q = make_question()
	print(q)
	ans = input("=")
	r = int (ans)
	#컴퓨터가 계산한 결과인 eval(q)의 값과 사용자가 입력한 결과 (r)를 비교합니다.
	if eval(q) == r:	#eval(expression)은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아 문자열을 실행한 결과값을 리턴하는 함수이다
		print("정답")
		sc1 += 1
	else:
		print("오답")
		sc2 += 1
print("정답 : ", sc1, "오답 : ", sc2)
if sc1 == 5: #모든 문제(5개)를 맞추었을 때
	print("당신은 천재입니다.")



##어려워##
import random
import time
#단어 리스트 : 여기에 단어를 추가하면 문제에 나옵니다.
w = ["cat", "dog", "fox", "monkey", "생쥐", "개구리", "사자", "호랑이"]
n = 1 #문제번호
print("[타자게임] 준비되면 엔터를 누르세요.")
input() #사용자가 엔터를 누를때까지 기다립니다.
start = time.time() #시작 시간을 기록합니다.
q = random.choice(w)
while n <= 5: #문제를 5번 반복합니다.
	print("*문제", n)
	print(q)	#문제를 보여줍니다.
	x = input()	#사용자 입력을 받습니다.
	if q == x:
		print("통과!")
		n = n+1	#문제번호를 1 증가시킵니다.
		q = random.choice(w) #새 문제를 선택합니다.
	else:
		print("오타! 다시 도전!")
end = time.time()	#끝나는 시간을 기록합니다.
et = end-start	#실제로 걸린 시간을 계산합니다.
et = format(et, ".2f") #보기좋게 소수점 둘째 자리까지만 표기합니다.
print("타자시간 : ", et, "초")







