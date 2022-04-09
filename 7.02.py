import random

class Student:

    def __init__(self,name):
        self.name = name
        self.gladness =50
        self.money = 20
        self.progress =0
        self.alive = True

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -=5
        self.money -= 0.08

    def to_work(self):
        print("Time to earn money")
        self.gladness -=5
        self.money += 0.2

    def to_sleep(self):
        print("I will sleep")
        self.gladness +=3
        self.money -= 0.02

    def to_chill(self):
        print("I wonna relax")
        self.gladness +=5
        self.progress -= 0.1
        self.money -= 0.05

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive=False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive =False
        elif self.progress > 5:
            print("Passed externally")
            self.alive = False
        elif self.money <= 0:
            print("No money to live...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress,2)}")
        print(f"Money = {round(self.money,2)}")

    def live(self,day):
        day = "Day " + str(day) + ' of ' + self.name + ' life'
        print(f'{day:=^50}')
        if self.gladness < 10:
            ran1 = random.randint(1, 2)
            if ran1 == 1:
                self.to_chill()
            if ran1 == 2:
                self.to_sleep()
        elif self.money < 10:
            self.to_work()
        elif self.progress < 2:
            self.to_study()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Sanechka")

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)