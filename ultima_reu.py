###
###
### 
###
###
###
class Purchase(object):
  def __init__(self, amount=0, transaction_type="", date="", name_of_product=""):
    self.amount = float(amount)
    self.transaction_type = transaction_type
    self.date = date
    self.product_name = name_of_product

class Budget(object):
  def __init__(self, expense=0, income=0, budget=0) -> None:
    self.expense = float(expense)
    self.income = float(income)
    self.budget = float(budget)
    self.total_money = self.income - self.expense
    self.expense_types = {}
    self.income_types = {}
    self.payment_types = {
      "credit": [],
      "debit": []
    }

  def __str__(self):
    out_str = "Total Money so far ${:.2f}\n\n Income: ${:.2f}\n Expenses: ${:.2f}".format(self.total_money, self.income, self.expense)
    return out_str


p = Budget(10, 100)
print(p)

def main():
    budget = float(input("Enter new budget"))
    newBudget = Budget(0,0, budget)

if __name__ == '__main__':
  main()
