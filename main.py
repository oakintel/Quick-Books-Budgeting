class Category:
  def __init__(self, name):
    self.name = name
    self.total = 0.0
    self.ledger = []

  def __repr__(self):
    display = f"{self.name:*^30}\n"
    total = 0

    for each_ledger in self.ledger:
      display += f"{each_ledger['description']}{each_ledger['amount']:>{30-len(each_ledger['description'])}}\n"
      total += each_ledger["amount"]

    display += f"Total= {total}"
    return display

  def deposit(self, amount, *args):
    description = args[0] if args else ""
    
    self.total += amount
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, *args):
    description = args[0] if args else ""
    
    if self.check_funds(amount):
      self.total -= amount
      self.ledger.append({"amount": -amount, "description": description})
      
    return self.check_funds(amount) 
      
  def get_balance(self):
    return self.total

  def transfer(self, amount, instance):
    if self.check_funds(amount):
      self.withdraw(amount, f"Transfer to {instance.name}")
      instance.deposit(amount, f"Transfer from {self.name}")

    return self.check_funds(amount)

  def check_funds(self, amount):
    if amount > self.total:
      return False
    return True


 


def create_spend_chart(categories):
  display = "Percentage spent by category\n"

  total = 0
  cats = {}
  for cat in categories:
    cat_total = 0
    for item in cat.ledger:
      amount = item["amount"]
      if amount < 0:
        total += amount
        cat_total += amount

    cats[cat.name] = abs(cat_total)
  print(cats)

  total = abs(total)

  for key,val in cats.items():
    percent = (val/total)*100
    cats[key] = percent
    
  print(cats)
    
  for n in range(100,-1,-10):
    display += f"{str(n)+'|':>4}\n"
    for val in cats.values():
      if val >= n:
        display += " o"
    display += "\n"

  L = len(cats.values())
  display += f"    {(L*2) * '-'}\n"

  i = 0
  while True: 
    try: 
      temp_str = ""
      for key in cats.keys():
        temp_str += key[1]
      i += 1
      display += f"     {temp_str}\n"
    except:
      break

  # print(display)




food = Category("Food")
clothing = Category("Clothing")
food.deposit(100, "Jollof Rice")
food.transfer(20, clothing)
# print (food.ledger)
# print (clothing.ledger)
# print (food.get_balance())
# print (clothing.get_balance())
# print (clothing.check_funds(10))

print (food)

# create_spend_chart([food, clothing])