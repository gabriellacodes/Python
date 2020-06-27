# Question 1
first_int = 3
second_int = 9

print("The output for 1a is",first_int + second_int)
print("The output for 1b is",-(first_int) + second_int)
print("The output for 1c is",float(first_int) + -(second_int))

print()
# Question 2
result = first_int * second_int
print("The output for 2a is",first_int,"*",second_int,"=",result)
result = -first_int * second_int
print("The output for 2b is",-first_int,"*",second_int,"=",result)
result = float(first_int) * -second_int
print("The output for 2c is",float(first_int),"*",-second_int,"=",result)

print()
# Question 3
third_int = 10
print("The output for 3a is",str(third_int)+"km","=",str(third_int*1000)+"m")
print(str(third_int)+"km","=",str(third_int*100000)+"cm")
fourth_float = 5.4
print("The output for 3b is",str(fourth_float)+"km","=",str(int(fourth_float*1000))+"m")
print(str(fourth_float)+"km","=",str(int(fourth_float*100000))+"cm")

print()
# Question 4
name = "William"
height = 192
print("The output for 4a is",name,"is",str(height)+"cms","tall")
name = "Roary"
height = 27
print("The output for 4b is",name,"is",str(height)+"cms","tall")