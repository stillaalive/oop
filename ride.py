# def ride(car):
#     car['distance']+=car['speed']
#     car['size']-=car['spend']

# def turbo(car):
#     car['distance']+=car['turbo']
#     car['size']-=car[speed]*2


# car_2={
#     'name':'Маруся',
#     'speed':5,
#     'size':30, # количество топлива 
#     'spend':7, # расход топлива 
#     'turbo':5,
#     'distance':0
# }

# car_2={
#     'name':'Ламба',
#     'speed':6,
#     'size':25,
#     'spend':8,
#     'turbo':9,
#     'distance':0
# }


class Car:
    def __init__(self,name,speed,size,spend,turbo,distance): #init - конструктор
        self.name=name
        self.speed=speed
        self.size=size
        self.spend=spend
        self.turbo=turbo
        self.distance=distance
    def ride(self):
        self.distance+=self.speed
        self.size-=self.spend
# у методов класса всегда должен быть хотя бы один параметр
    def turbo_make(self):
        self.distance+=self.turbo
        self.size-=self.spend*2

car_1=Car('BMW',30,100,20,20,0)
car_2=Car('Audi',40,120,10,30,0)
print(car_1.size)
print(car_2.size)
car_1.ride()
car_2.ride()
print()
print(car_1.size)
print(car_2.size)
car_1.turbo_make()
car_2.turbo_make()
print()
print(car_1.size)
print(car_2.size)