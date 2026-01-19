class Distance:
    conversion_dict = {
        "cm": 0.01,
        "m": 1,
        "km": 1000
    }

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def to_meters(self):
        return self.value * self.conversion_dict[self.unit]

    def __add__(self, other):
        total_meters = self.to_meters() + other.to_meters()
        new_value = total_meters / self.conversion_dict[self.unit]
        return Distance(new_value, self.unit)

    def __sub__(self, other):
        total_meters = self.to_meters() - other.to_meters()
        new_value = total_meters / self.conversion_dict[self.unit]
        return Distance(new_value, self.unit)


a = Distance(10, "m")
b = Distance(2, "km")
c = Distance(100, "cm")

print(a)
print(b)
print(c)

print("*" * 35)
print("Сложение")
print(a + b)
print(b + a)
print(a + c)

print("*" * 35)
print("Вычитание")
print(b - a)
print(a - c)
