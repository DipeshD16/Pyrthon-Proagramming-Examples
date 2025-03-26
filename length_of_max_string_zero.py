from random import randint
num_list =[]
for i in range(100):
    num_list.append(randint(0, 1))
print(num_list)


frequencies =[]
count = 0
for i in range(len(num_list)):
    if num_list[i] == 0:
        count += 1
    else:
        if count > 0:
            frequencies.append(count)
        count = 0

if count> 0:

    frequencies.append(count)
print(max(frequencies))