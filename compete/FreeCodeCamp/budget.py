import itertools


class Category:

    def __init__(self, category_name):
        self.ledger = []
        self.category_name = category_name.capitalize()
        self.balance = 0

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(round(item['amount'], 2) for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, 'Transfer to ' + category.category_name)
            category.deposit(amount, 'Transfer from ' + self.category_name)
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def _format_ledger_item(self, item):
        return f"{item['description'][:23]:<23}{item['amount']:>7.2f}"

    def __repr__(self) -> str:
        category_title = self.category_name.center(30, '*')
        category_total = f"Total: {self.get_balance():.2f}"
        printable = [
            category_title, *[self._format_ledger_item(item) for item in self.ledger], category_total]
        return "\n".join(printable)


def create_spend_chart(categories):
    cat_withdrawls_percentage = []
    total_withdrawls = 0
    # getting sum of all withdrawls
    for cat in categories:
        total_cat_withdrawl = 0
        total_cat_withdrawl = sum(item['amount']
                                  for item in cat.ledger if item['amount'] < 0)
        total_withdrawls += total_cat_withdrawl
        cat_withdrawls_percentage.append(
            (cat.category_name, total_cat_withdrawl))

    # getting percentage of withdrawls
    cat_withdrawls_percentage = [
        (k, round(v/total_withdrawls*100)//10) for k, v in cat_withdrawls_percentage]
    # title
    res_str = 'Percentage spent by category'

    # bar chart
    for i in range(10, -1, -1):
        bar_graph = f'{i*10:>3}| '
        bar_graph += "".join(
            [f'{"o":3}' for item in cat_withdrawls_percentage if item[1] >= i])
        res_str += f'\n{bar_graph:10}'

    # list of categories
    categories_names = [cat[0] for cat in cat_withdrawls_percentage]

    # divider
    divider_str = f'{"-":>5}' + f"{'-'*(len(categories_names)*3)}"
    res_str += f'\n{divider_str}\n'

    # printing bill of amount
    res_str += "\n".join(["  ".join([f'{i[0]:>6}', *i[1:]])
                          for i in itertools.zip_longest(*categories_names, fillvalue='')])
    return res_str


food = Category('Food')
entertainment = Category('Entertainment')
business = Category('Business')

# Example-1
# food.deposit(900, "deposit")
# food.transfer(100, entertainment)
# entertainment.deposit(900, "deposit")
# business.deposit(900, "deposit")
# food.withdraw(105.55)
# entertainment.withdraw(33.40)
# business.withdraw(10.99)
# business.transfer(10.99, food)
# res = create_spend_chart([food, entertainment, business])

# print(res)
# print(len(res))

# Example-2
# food.deposit(1000.00, 'initial deposit')
# food.withdraw(10.15, 'groceries')
# food.withdraw(15.89, 'restaurant and more foo')
# food.transfer(50.00, entertainment)
# Total: 923.96

# print(food)

# Example-3
# sample = "*************Food*************\ndeposit                 900.00\nmilk, cereal, eggs, bac -45.67\nTransfer to Entertainme -20.00\nTotal: 834.33"


# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.transfer(20, entertainment)

# print(food)
# print(len(food.__repr__()))
# print(len(sample))

# Example-4
expected = "Percentage spent by category\n100|          \n 90|          \n 80|          \n 70|    o     \n 60|    o     \n 50|    o     \n 40|    o     \n 30|    o     \n 20|    o  o  \n 10|    o  o  \n  0| o  o  o  \n    ----------\n     B  F  E  \n     u  o  n  \n     s  o  t  \n     i  d  e  \n     n     r  \n     e     t  \n     s     a  \n     s     i  \n           n  \n           m  \n           e  \n           n  \n           t  "
print(expected)
print(len(expected))

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

actual = create_spend_chart([business, food, entertainment])
print(actual)
print(len(actual))
