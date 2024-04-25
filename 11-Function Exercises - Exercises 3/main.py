target = 10000
sales = {
  'joao': 15000,
  'julia': 27000,
  'marcus': 9900,
  'maria': 10300,
  'ana': 7870,
}

def calculate_goal(target, sales):
    met_goal = []
    for seller in sales:
        if sales[seller] >= target:
            met_goal.append(seller)
    percentage_met_goal = len(met_goal) / len(sales)
    return percentage_met_goal, met_goal

print(calculate_goal(target, sales))