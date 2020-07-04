sentence = input(f"For my next trick I will make your sentence completely unreadable. Tell me a sentence you want me to just destroy: ")

word_list = sentence.split()
print(len(word_list), word_list)

print(len(sentence), list(sentence))