#this program ask for the input word or phrase and checkes whether its palindome or not
def palindrome_checker(string): #create a function called palindrome checked

#remove the spaces and convert it to lower case
    cleaned_string = ''.join(string.lower().split())

#reverse and compare the string.
    if cleaned_string == cleaned_string[::-1]:
        return True
    else:
        return False

#user input
word =input("Enter a word or phrase: ")

#to run the function.
if palindrome_checker(word):
    print("Its a palindrome")
else:
    print("Its not a palindrome.")
