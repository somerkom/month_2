class Money:
    def __init__(self, amount):
        self.amount = amount

        def __str__(self):
            return f"Money object amount = {self.amount}"



money_igor = Money(100)
print(money_igor.amount)