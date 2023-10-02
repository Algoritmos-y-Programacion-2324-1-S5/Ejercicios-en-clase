dict_input = input("Please enter your dictionary in this format word:palabra,word:palabra,...:")
words= {}
comma_dict = dict_input.split(",")
for element in comma_dict:
    word_list = element.split(":")
    words[word_list[0].lower()] = word_list[1]

user_input = input("Please enter a phrase to translate: ")
user_words = user_input.split(" ")
result = ""
for word in user_words:
    result += words.get(word.lower(),word)
    result += " "
print(result)
