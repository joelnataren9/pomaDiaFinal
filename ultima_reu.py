###
###
### 
###
###
###
class Budget(object):
  def __init__(self, expense=0, income=0) -> None:
    self.expense = 0
    self.income = 0
    self.total_money = self.income - self.expense
    self.expense_types = {}
    self.income_types = {}
    self.payment_types = {
      "credit": [],
      "debit": []
    }

  def __str__(self):
    out_str = "Total Money so far {}\n\n Income: {}\n Expenses: {}".format(self.total_money, self.income, self.expense)
    return out_str
