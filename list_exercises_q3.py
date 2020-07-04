import time
name_list = []

name_prompt = f"Hey! Immabout to do a magic trick and I need you to give me 3 names. What's the first name you got for me? "
name_list.append(input(name_prompt))

name_prompt = f"Sweet, what's the second name? "
name_list.append(input(name_prompt))

name_prompt = f"Aaaand the last one? "
name_list.append(input(name_prompt))

print(f"Sweet, give me a sec ...")

time.sleep(2)

print(name_list)

print(f"Tada! I made them into a list. Impressed? I thought so ...")