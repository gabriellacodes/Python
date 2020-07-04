sentence_list = []

sentence_prompt = f"For my next trick I will make your sentence completely unreadable. Tell me a sentence you want me to just destroy: "
sentence_list = input(sentence_prompt)

# print(f"Here: ",sentence_list)

word_list = sentence_list.split()
print(len(word_list))

for x in word_list:
    char_list = x.list()

print(word_list)