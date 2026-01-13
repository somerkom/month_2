class Animal:
    def move(self):
        print('двигается')


class Swimming(Animal):
    def move(self):
        print('плавает')


class Flying(Animal):
    def move(self):
        print('летает')


class Duck(Flying, Swimming):
    def move(self):
        print('летает и плавает')

# MRO = method resolution order
print(Duck.__mro__)
duck = Duck()
duck.move()