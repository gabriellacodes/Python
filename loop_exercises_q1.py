sum_numbers = 0
number = input("Give me a number: ")

while len(number) > 0:
    sum_numbers = sum_numbers + int(number)
    number = input("Give me another number: ")

print(sum_numbers)
