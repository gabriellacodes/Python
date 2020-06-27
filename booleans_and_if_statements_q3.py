# Question 3
light_prompt = f"Look at me, I'm a traffic light! What colour am I? Please answer Red, Amber, or Green "
light_colour = input(light_prompt)

car_prompt = f"and is there a car nearby? Please answer True or False "
car_detected = input(car_prompt)

if light_colour == "Red" and car_detected == "True":
     print("Flash!")
else:
     print("Do nothing.")
