# Практическое задание 1
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age


    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Гав гав")
class Cat(Animal):
    def make_sound(self):
        print("Мияу мияу")

cat = Cat("Алиса","2")
cat.make_sound()
cat.name = "Лиса"
cat.age = "2"
print(f"{cat.name}, {cat.age} года")
print("*" * 35)
dog = Dog("Пупи","3")
dog.make_sound()
dog.name = "Муся"
dog.age = "4"
print(f"{dog.name}, {dog.age} года")
