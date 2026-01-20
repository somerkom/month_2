class Money:
    def __init__(self, amount):
        self.amount = amount

        def __str__(self):
            return f"Money object amount = {self.amount}"

        # eq это ==
        def __eq__(self, other):
            if self.amount != other.amount:
                return False
            else:
                return True
            # return self.amount == other.amount

        # gt = greateer than это ">"
        # lt = less than это "<"
        # gte = greater than or equal это "=>"
        # lte = less than or equal
        def __gt__(self, other):
            if self.amount > other.amount:
                return False
            else:
                return True

money_igor = Money(100)
money_danil = Money(200)
print(money_igor.amount)
print(money_igor.amount == money_danil.amount)
