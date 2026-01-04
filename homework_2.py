class Person:
    def __init__(self, name, birth_date, higher_education, profession = " "):
        self.name = name
        self.birth_date = birth_date
        self.higher_education = higher_education
        self.profession = profession
        if higher_education == "нет":
            self.higher_education = False
        if higher_education == "да":
            self.higher_education = True
    def introduce(self):
        if self.profession == " " and self.higher_education == True:
            return f"Меня зовут {self.name}, я родилась {self.birth_date}, по профессии {self.profession}, высшее образование есть"
        elif self.profession != " " and self.higher_education == True:
            return f"Меня зовут {self.name}, я родилась {self.birth_date}, по профессии {self.profession}, высшее образование есть"
        elif self.profession != " " and self.higher_education == False:
            return f"меня зовут {self.name}, я родилась {self.birth_date}, по профессии {self.profession}, высшего образования нет"
        else:
            return f"Меня зовут {self.name}, я родилась {self.birth_date}, профессии нет, высшего образования нет"
