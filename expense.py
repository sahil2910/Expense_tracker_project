class Expense:
    def __init__(self, name , category , amount) -> None:
        self.name = name
        self.category = category
        self.amount = amount

    def __repr__(self) : # without using this we get output like this = <expense.Expense object at 0x00000277A4E3BE00> to make it more useful we use __repr__ so to get usefull output
        return f"<Expense: {self.name},{self.category}, RS {self.amount} >" 