###
###
### 
###
###
###
class Budget(object):
  def __init__(self, expense=0, income=0, budget=0) -> None:
    self.budget =0.0
    self.expense = 0
    self.income = 0
    self.total_money = self.income - self.expense
    self.expense_types = {}
    self.income_types = {}
    self.payment_types = {
      "credit": [],
      "debit": []
    }
    
def main():
    budget = float(input("Enter new budget"))
    newBudget = Budget(0,0, budget)
    
if __name__ == '__main__':
  main()