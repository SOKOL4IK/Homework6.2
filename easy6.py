
class Car:
	def __init__(self, car_speed, car_color, car_name,):
		self.speed = car_speed
		self.color = car_color
		self.name = car_name
	def Go(self, name, speed):
		print(name,"Поехал со скоростью ",speed/1.5)
	def Stop(self, name):
		print(name, "Остановился")
	def Turn(self, turn, name):
		print(name, "повернула на ", turn)	

class TownCar(Car):
	pass
class SportCar(Car):
	pass
class WorkCar(Car):
	pass
class PoliceCar(Car):
	def Flashing_lights(self):
		print("Включенны проблесковые маячки.")	

Police_Car = PoliceCar(120, "White and black", "Ford Victoria")
Work_Car = WorkCar(50, "White", "Mercedes-benz Sprinter")
Sport_car = SportCar(180, "Gray", "Mercedes-benz W204 E63 AMG")
Street_car = TownCar(60, "White", "Mercedes-benz W210 E320")
car = Car(90, "Black", "Mercedes-benz W140 S600")




		