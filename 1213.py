#절차지향과 객체지향
#절차지향은 순서고려
#객체지향은 객체고려

# def car1(color, speed):
# 	print("자동차1의 색상은 %s 이고, 속도는 %d 입니다."%(color, speed))

# def car2(color, speed):
# 	print("자동차2의 색상은 %s 이고, 속도는 %d 입니다."%(color, speed))

# car1("빨강", 30)
# car2("파랑", 60)


class Car:#클래스
	speed = 0

	def upSpeed(self, value):
		self.speed = value

class Sedan:
	seatNum = 0

	def getSeatNum(self):
		return self.seatNum

class Truck:
	capacity = 0
	def upSpeed(self, value):
		self.speed = value

		if self.speed > 110:
			self.speed = 110

	def getCapaciy(self):
		return self.capacity

# sedan1 = Sedan()
# sedan1 = upSpeed(100)
# sedan1.seatNum = 5

truck1 = Truck()
truck1.upSpeed(200)
truck1.capacity = 0
print("승용차의 속도는 %d 이고, 좌석수는 %d 입니다."%(sedan1, speed, sedan1.getSeatNum()))

# myCar1 = Car()
# myCar1.color = "빨강"
# myCar1.upSpeed(30)
# print("자동차1의 색상은 %s 이고, 속도는 %d 입니다."%(myCar1.color, myCar1.speed()))

# myCar1 = Car()
# myCar1.color = "파랑"
# myCar1.upSpeed(60)
# print("자동차1의 색상은 %s 이고, 속도는 %d 입니다."%(myCar1.color, myCar1.speed()))