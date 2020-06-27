# Question 4
height_prompt = f"So, you want to ride the roller coaster? How tall are you ...? "
height = int(input(height_prompt))

can_ride = height>=120

if can_ride:
     print("Hop on!")
else:
     print("Sorry, not today :(")