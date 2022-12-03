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
  def __init__(self, expense=0, income=0) -> None:
    self.expense = float(expense)
    self.income = float(income)
    self.total_money = self.income - self.expense
    self.expense_types = {}
    self.income_types = {}
    self.payment_types = {
      "credit": [],
      "debit": []
    }


  def substract_expense(self, expense):
      self.expense = self.expense - expense
      self.total_money = self.total_money - expense
      
  def addIncome(self, newBudget):
    income = int(input("Insert income: "))
    self.income += income
      
      
    
    
def main():
    budget = float(input("Enter new budget"))
    newBudget = Budget(0,budget)

    decision = str(input("Would you like to proceed? Yes(Y) or No(N)"))

    while decision == "Y":
      action = str(input("Would you like to add a new Income(I) or Expense(E)"))
    
      if(action == "I"):
        budget.addIncome(newBudget)
      ##elif(action == "E"):
        ##addExpense(newBudget)
        
      decision = str(input("Would you like to proceed? Yes(Y) or No(N)"))
    
    
if __name__ == '__main__':
  main()
