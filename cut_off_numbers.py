#this program ask the user for the cut-off and and separates the number below the cutoff value and after the cutoff value
cutoff_value =int(input("Enter the number to be set as cut off value:"))

#create two empty list to store the number based on whether they are high or low:
less_than_cutoff =[]
high_than_cutoff =[]

#ask the user for the number as a input and prompt the user press enter to exit
while True:
    num = input("Enter the number (or press enter to finish: )")

#break the loop if user presses enter  
    if num =="":
        break

#convert the number into integer
    try:
        num = int(num)
       
#append the two list based on the input by the user:
        if num<cutoff_value:
            less_than_cutoff.append(num)
        elif num>cutoff_value:
            high_than_cutoff.append(num)
        else:
            pass

#raise an exception for the value error
    except ValueError:
        print("Plase enter a number.")

#print the numbers:
for num in less_than_cutoff:
    print(f"{num}")

print(f"{cutoff_value}")

for num in high_than_cutoff:
    print(f"{num}")