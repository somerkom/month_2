# Практическое задание 1
class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    @property
    def age(self):
        return self.__age

    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Гав гав")
class Cat(Animal):
    def make_sound(self):
        print("Мияу мияу")

cat = Cat("Алиса","2 месяца")
cat.make_sound()
print("*" * 35)
dog = Dog("Пупи","3месяца")
dog.make_sound()


"""

"""