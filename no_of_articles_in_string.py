my_string = input("Enter a string: ")
my_string_list = my_string.split()
print(my_string_list)

articles = ["a", "the", "an"]
count = 0
for word in my_string_list:
    if word.lower() in articles:
        count+=1

print(count)
