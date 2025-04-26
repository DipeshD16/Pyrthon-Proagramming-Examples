fact = 1
for i in range(1, 1001):
    fact *=i
print(fact)
str_fact = str(fact)
my_list = [int(d) for d in str(str_fact)]

count = 0
for num in my_list[::-1]:
    if num  == 0:
        count +=1
    else:
        break
print(count)