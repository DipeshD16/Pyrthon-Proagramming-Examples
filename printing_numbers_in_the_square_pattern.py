# to ask the user for the number of rows:
num = int(input("Enter the number of rows: "))

# to create a n X n list
n_list=[[0 for x in range(num)] for y in range(num)]

#to declare the variables to iterate over the list.
n = 1 #used to print
low = 0 #for indexing
high = num-1 #for indexing
count = int((num+1)/2) #for the number of times of the outer loop should run.

#main program body to create a matrix
for i in range(count):
    for j in range(low, high+1):  #this loops specifies range
        n_list[i][j]= n     # this specifies the index
        n=n+1
    for j in range(low+1, high+1):
        n_list[j][high] = n
        n=n+1
    for j in range(high-1, low-1, -1):
        n_list[high][j] = n
        n= n+1
    for j in range(high-1, low, -1):
        n_list[j][low] =n
        n=n+1
   
    low = low+1
    high = high-1
       
#to print the list for the desired output:
for i in range(num):
    for j in range(num):
        print(n_list[i][j], end="\t")
    print()
