# class Car:
# 	color = ""
# 	speed = 0

# 	def __init__(self, name, speed):
# 		self.name = name
# 		self.speed = speed

# 	def getName(self):
# 		return self.name

# 	def getSpeed(self):
# 		return self.speed

# myCar1 = Car()
# myCar1.color = "빨강"
# myCar1.speed = 0

# myCar2 = Car()
# myCar2.color = "파랑"
# myCar2.speed = 0

# myCar1.upSpeed(30)
# print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다."%(myCar1.color, myCar1.speed))
# myCar2.upSpeed(60)
# print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다."%(myCar2.color, myCar2.speed))


# car1 = Car("빨강", 0)
# car2 = Car("파랑", 30)
# print("자동차1의 색상은 %s이며, 현재 속도는 %dkm입니다."%(car1.getName(), car1.getSpeed()))
# print("자동차2의 색상은 %s이며, 현재 속도는 %dkm입니다."%(car2.getName(), car2.getSpeed()))

class Car:
	speed = 0
	def upSpeed(self, value):
		self.speed += value
		print("현재 속도(슈퍼 클래스) : %d" %self.speed)

class Sedan(Car):
	pass

class Truck(Car):
	def upSpeed(self, value):
		self.speed += value

		if self.speed > 110:
			self.speed = 100
		print("현재 속도(서브 클래스) : %d" %self.speed)

sedan1 = Sedan()
truck1 = Truck()

print("==승용차==")
sedan1.upSpeed(200)
 
print("==트럭==")
truck1.upSpeed(200)