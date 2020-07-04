groceries = [ 
    ["Baby Spinach", 2.78], 
    ["Hot Chocolate", 3.70], 
    ["Crackers", 2.10], 
    ["Bacon", 9.00], 
    ["Carrots", 0.56], 
    ["Oranges", 3.08] 
]

for x in groceries:
    item_number = input(f'How many {x[0]} did you buy? ')
    [x][-1].append(float(item_number))

# print(groceries)

shopping_bill = 0
print(f"====Izzy's Food Emporium====")
for x in groceries:
    item_total = float(x[1] * x[2])
    shopping_bill = shopping_bill + item_total
    print(f"{x[0]:<17} ${item_total:.2f}")
print(f"============================")
print(f"{'':<18}${shopping_bill:.2f}")