import random


class Person:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.hunger = 0
        self.mood = 50
        self.money = 0

    def eat(self, food):
        self.hunger = max(0, self.hunger - food.nutrition)
        self.energy = min(100, self.energy + 10)
        print(f"{self.name} поїв(ла) {food.name}.")

    def sleep(self):
        self.energy = 100
        self.mood += 5
        print(f"{self.name} поспав(ла) і відновив(ла) енергію.")

    def __str__(self):
        return f"{self.name} | 💰: {self.money}$ | ⚡: {self.energy} | 🍔: {self.hunger} | 🙂: {self.mood}"


class Food:
    def __init__(self, name, nutrition):
        self.name = name
        self.nutrition = nutrition


class Job:
    def __init__(self, title, min_salary, max_salary):
        self.title = title
        self.min_salary = min_salary
        self.max_salary = max_salary

    def work(self, person):
        if person.energy >= 30:
            person.energy -= 30
            person.mood += 10
            salary_today = random.randint(self.min_salary, self.max_salary)
            person.money += salary_today
            print(f"{person.name} працює як {self.title} і сьогодні заробляє {salary_today}$!")
        else:
            print(f"{person.name} занадто втомлений(а), щоб працювати!")


class House:
    def __init__(self, address):
        self.address = address

    def rest(self, person):
        person.sleep()
        print(f"{person.name} відпочив(ла) вдома на {self.address}.")

class Pet:
    def __init__(self, name):
        self.name = name

    def play(self, person):
        person.mood += 15
        print(f"{person.name} грається з {self.name} і стає щасливішим!")


class Game:
    def __init__(self, person):
        self.person = person
        self.day = 1

    def next_day(self):
        print(f"\n📅 День {self.day}")
        self.person.hunger += random.randint(5, 15)
        self.person.mood -= random.randint(5, 10)
        self.day += 1


alex = Person("Alex")
job = Job("Бариста", min_salary=80, max_salary=150)
food = Food("піца", 25)
house = House("вул. Сонячна 5")
pet = Pet("Мурчик")
game = Game(alex)

for _ in range(7):
    game.next_day()
    print(alex)

    if alex.hunger > 30:
        alex.eat(food)

    job.work(alex)

    if alex.mood < 40:
        pet.play(alex)

    house.rest(alex)

print(f"\n🏁 Тиждень завершено. {alex.name} має {alex.money}$ на рахунку.")

