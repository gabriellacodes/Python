# Question 1 & 2
moths_prompt = f"Are there moths in the house for Roary to catch? Please answer True or False "
moths_in_house = input(moths_prompt)

mitch_prompt = f"and is Mitch home? Please answer True or False "
mitch_is_home = input(mitch_prompt)

if moths_in_house == "True" and mitch_is_home == "True":
     print("Hoooman! Help me get the moths!")

if moths_in_house == "False" and mitch_is_home == "False":
     print("No threats detected.")

if moths_in_house == "True" and mitch_is_home == "False":
     print("Meooooooooooooow! Hissssss!")

if moths_in_house == "False" and mitch_is_home == "True":
     print("Climb on Mitch.")
