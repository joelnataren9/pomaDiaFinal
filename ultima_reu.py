###
###
### 
###
###
###
class Budget(object):
  def __init__(self, expense=0, income=0.0) -> None:
    self.expense = 0
    self.income = 0.0
    self.total_money = self.income - self.expense
    self.expense_types = {}
    self.income_types = {}
    self.payment_types = {
      "credit": [],
      "debit": []
    }
    def addIncome(self, newBudget = Budget()):
      income = int(input("Insert income: "))
      self.income += income
      
      
    
    
def main():
    budget = float(input("Enter new budget"))
    newBudget = Budget(0,budget)
    
    decision = str(input("Would you like to proceed? Yes(Y) or No(N)"))
                   
    while decision == "Y":
      action = str(input("Would you like to add a new Income(I) or Expense(E)"))
    
      if(action == "I"):
        addIncome(newBudget)
      ##elif(action == "E"):
        ##addExpense(newBudget)
        
      decision = str(input("Would you like to proceed? Yes(Y) or No(N)"))
    
    
if __name__ == '__main__':
  main()