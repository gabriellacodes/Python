name_list = []
counter = 0

while counter < 3:
    name = input("Give me a name: ")
    name_list.append(name)
    counter = counter + 1

print(f'The names you gave me were: ')
for x in name_list:
    print(x)
