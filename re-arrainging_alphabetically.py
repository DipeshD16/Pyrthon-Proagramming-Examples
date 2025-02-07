#this programs accepts an alphabetic string re-arrange them alphabetically.

def sort_code(s):
    return "".join(sorted(s))

while True:
    try:
        user_input = input("Enter a string of unique alphabet characters: ")
        if user_input.isalpha():
            break
        else:
            print("an error occured. Please try again.")
    except ValueError:
        print("Its not a string.")
sorted_string = sort_code(user_input)

print("Sorted string:-", sorted_string)