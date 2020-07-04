foods = [
    "orange",
    "apple",
    "banana",
    "strawberry",
    "grape",
    "blueberry",
    ["carrot", "cauliflower", "pumpkin"],
    "passionfruit",
    "mango",
    "kiwifruit"
    ]

print("Question 1.1:",foods[0])
print("Question 1.2:",foods[2])
print("Question 1.3:",foods[-1])
print("Question 1.4:",foods[0:3])
print("Question 1.5:",foods[-3:])
print("Question 1.6:",foods[6][-1])

print()

mailing_list = [
    ["Roary", "roary@moth.catchers"],
    ["Remus", "remus@kapers.dog"],
    ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
    ["Biscuit", "biscuit@whippies.park"],
    ["Rory", "rory@whippies.park"],
    ]

print("Question 2:")
for x in mailing_list:
    print(x[0],": ",x[-1])