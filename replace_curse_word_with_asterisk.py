curse_word_list = ['darn', 'dang', 'freakinm', 'shoot', 'heck']

my_string = input("Enter a sentence: ")
censored_words = []

my_string_list = my_string.split()
#print(my_string_list)
for word in my_string_list:
    if word in curse_word_list:
        censored_word = len(word)*"*"
        censored_words.append(word.replace(word, censored_word))
    else:
        censored_words.append(word)
   
#print(censored_words)

for word in censored_words:
    print(word, end = " ")