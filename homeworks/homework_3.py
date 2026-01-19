class Person:
    def __init__(self, name, birth_date, higher_education, occupation):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education
    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        if self.__higher_education == False:
            return "нет"
        else:
            return "есть"

    def introduce(self):
        return f"Привет, меня зовут {self.name}"
class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, group_name,):
        super().__init__(name, birth_date, higher_education, occupation)
        self.group_name = group_name

    def introduce(self):
        print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Я учился с Айсулуу в группе {self.group_name}. "
              f"У меня {self.higher_education} высшее образование")

class Friend(Person):
    def __init__(self, name,  birth_date, occupation, higher_education, hobby, ):
        super().__init__(name, birth_date, higher_education, occupation)
        self.hobby = hobby

    def introduce(self):
        if self.higher_education == "есть":
            print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Мое хобби {self.hobby}. "
                  f"У меня {self.higher_education} высшее образование")
        else:
            print(f"Привет, меня зовут {self.name}. Моя профессия {self.occupation}. Мое хобби {self.hobby}. У меня {self.higher_education} высшего образования")


cl1 = Classmate("Иван", "20.02.2000", "студент", True, "11D")
cl1.introduce()
print("*" * 35)
fr1 = Friend("Айбек", "20.02.2000", "студент", True, "футбол")
fr1.introduce()
