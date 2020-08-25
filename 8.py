def average(n1, n2):
	result = (n1+n2)/2
	return result
print(average(4, 11))



def calculate_volume(n1, n2, n3):
	result = n1 * n2 * n3
	return result
Box_volume = calculate_volume(4,4,6)
print(Box_volume)



def f(n1):
	result = n1**2 + n1 + 1
	return result
print(f(6))



score = [90, 80, 100, 70]
def list_avg(score):
	result = 0
	avg = 0
	for i in score:
		result += i
	avg = result/len(score)
	return avg
print(list_avg(score))



def average(n1, n2):
	result = (n1+n2)/2
	print(result)
average(4,11)



def mul(n1, n2):
	print('result of mult of two numbers : ', n1 * n2)
mul(3,11)



def is_even_or_odd(n1):
	if n1%2 == 0:
		print(n1,"is even")
	else:
		print(n1,"is odd")
is_even_or_odd(3)
is_even_or_odd(4)



def list_add(num, numlist):
	if num in numlist:
		print("이미 있는 원소입니다.")
	else:
		numlist += [num]
		print("원소를 추가했습니다.")
list_add(3, [4,5,6])
list_add(3, [3,6,9])



def coin_food(coin):
	if coin == "앞":
		print("중국 요리로 결정되었습니다.")
	else:
		print("일본 요리로 결정되었습니다.")
coin_food("앞")
coin_food("뒤")



kor_score = int(input("국어 점수를 입력하세요 : "))
math_score = int(input("수학 점수를 입력하세요 : "))
eng_score = int(input("영어 점수를 입력하세요 : "))
if kor_score >= 90:
	kor_grade = "A"
elif kor_score >= 80:
	kor_grade = "B"
elif kor_score >= 70:
	kor_grade = "C"
elif kor_score >= 60:
	kor_grade = "D"
else:
	kor_grade = "F"
if math_score >= 90:
	math_grade = "A"
elif math_score >= 80:
	math_grade = "B"
elif math_score >= 70:
	math_grade = "C"
elif math_score >= 60:
	math_grade = "D"
else:
	math_grade = "F"
if eng_score >= 90:
	eng_grade = "A"
elif eng_score >= 80:
	eng_grade = "B"
elif eng_score >= 70:
	eng_grade = "C"
elif eng_score >= 60:
	eng_grade = "D"
else:
	eng_grade = "F"
print("국어 학점은 ", kor_grade, "입니다.")
print("수학 학점은 ", math_grade, "입니다.")
print("영어 학점은 ", eng_grade, "입니다.")



kor_score = int(input("국어 점수를 입력하세요 : "))
math_score = int(input("수학 점수를 입력하세요 : "))
eng_score = int(input("영어 점수를 입력하세요 : "))
def calgrad(score):
	if score >= 90:
		grade = "A"
	elif score >= 80:
		grade = "B"
	elif score >= 70:
		grade = "C"
	elif score >= 60:
		grade = "D"
	else:
		grade = "F"
	return grade
kor_grade = calgrad(kor_score)
math_grade = calgrad(math_score)
eng_grade = calgrad(eng_score)
print("국어 학점은 ", kor_grade, "입니다.")
print("수학 학점은 ", math_grade, "입니다.")
print("영어 학점은 ", eng_grade, "입니다.")



def calavg(list):
	sum=0
	avg=0
	for i in list:
		sum += i
	avg = sum/len(list)
	return avg
def passFail(numlist):
	avg = calavg(numlist)
	if avg >= 60:
		message = "Pass"
	else:
		message = "Fail"
	return message
passFail([60,70,90,60])
passFail([60,70,90,60,0])



def max_score(score_list):
	max_num = 0
	for score in score_list:
		if score > max_num:
			max_num = score
	return max_num
max_score([81, 91, 93, 88, 89, 94, 81, 90, 79, 76, 83, 89, 88, 96, 77, 89, 76, 79])
math_score = [81, 91, 93, 88, 89, 94, 81, 90, 79, 76, 83, 89, 88, 96, 77, 89, 76, 79]
print(max_score(math_score))



def add(n1, n2):
	result = n1+n2
	return result
def sub(n1, n2):
	if(n1 >= n2):
		result = n1-n2
	else:
		result = n2-n1
	return result
def mult(n1, n2):
	result = n1*n2
	return result
def div(n1, n2):
	if(n1 >= n2):
		result = n1/n2
	else:
		result = n2/n1
	return result
print("#### 계산기 ####")
num_result = 0
while(True):
	select = int(input("1.덧셈  2.뺄셈  3.곱셈  4.나눗셈  5.종료 :"))
	if select == 5:
		break;
	else : 
		print("정수 2개를 입력하세요")
		n1 = int(input("정수 1: "))
		n2 = int(input("정수 2: "))
		if select == 1:
			num_result = add(n1, n2)
		elif select == 2:
			num_result = sub(n1, n2)
		elif select == 3:
			num_result = mult(n1, n2)
		else:
			num_result = div(n1, n2)
	print("계산 결과 : ", num_result)



def channel(now_channel ,num):
	now_channel += num
	return now_channel
def volume(now_volume, num):
	now_volume += num
	return now_volume
now_channel = 5
now_volume = 4
while (True):
	select = int(input("1.채널	2.음량	3.종료 : "))
	if select == 3:
		break;
	elif select == 1:
		num = int(input("바꾸고 싶은 만큼 입력 :"))
		now_channel = channel(now_channel, num)
		print("현재 채널 : ", now_channel)
	elif select == 2:
		num = int(input("바꾸고 싶은 만큼 입력 :"))
		now_volume = volume(now_volume, num)
		print("현재 음량 : ", now_volume)
	else:
		print("잘못 입력했습니다. 다시 입력해주세요.")



##어려웠어##
import random
random_num = random.randint(1, 100)
def is_same(target, num):
	if target == num:
		result = "Win"
	elif target > num:
		result = "Low"
	elif target < num:
		result = "High"
	return result
print("안녕.\n 난 1부터 100중 숫자를 하나 골랐어요.")
guess = int(input("숫자를 입력하고 엔터 키를 누르세요. "))
high_or_low = is_same(random_num, guess)
while high_or_low != "Win":
	if high_or_low == "Low":
		guess = int(input("그것보다 높은 수입니다. 다시 생각해보세요. "))
	elif high_or_low == "High":
		guess = int(input("그것보다 작은 수입니다. 다시 생각해보세요. "))
	high_or_low = is_same(random_num, guess)
input("정답!\n정말 잘했어요.\n\n\n마치려면 엔터키를 누르세요.")



