import random


class Parrot:

    def __init__(self,name):
        self.name = name
        self.gladness =35
        self.hunger =50
        self.fatigue = 10
        self.alive = True

    def to_eat(self):
        print("Yes, I ate a minute ago but I want more")
        self.hunger += 8
        self.fatigue += 1
        self.gladness += 2

    def to_sleep(self):
        print("Time to think about life")
        self.hunger -= 2
        self.fatigue -= 2
        self.gladness += 1

    def to_chill(self):
        print("Time for great discoveries")
        self.hunger -= 2
        self.fatigue -= 2
        self.gladness += 1

    def to_go_to_the_toilet(self):
        print("Time to drop the bombs")
        self.hunger -= 2
        self.fatigue += 4
        self.gladness -= 3
    def is_alive(self):
        if self.hunger <= 0:
            print("Why was I so busy?")
            self.alive = False
        elif self.gladness <= -5:
            print("Depression...")
            self.alive =False
        elif self.fatigue > 90:
            print("I'm so tired. I can't eat...")
            self.alive = False
        elif self.fatigue < 50 & self.gladness > 35 & self.hunger > 40:
            print("How am I still alive?")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Hunger = {self.hunger}")
        print(f"Fatigue = {self.fatigue}")

    def live(self,day):
        day = "Day " + str(day) + ' of ' + self.name + ' life'
        print(f'{day:=^50}')
        live_cube = random.randint(1,4)
        if live_cube == 1:
            self.to_eat()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_go_to_the_toilet()
        self.end_of_day()
        self.is_alive()

nick = Parrot(name="Orange")

for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)