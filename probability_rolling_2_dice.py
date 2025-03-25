list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [1, 2, 3, 4, 5, 6]
list_3 = []

for i in range(len(list_1)):
    for j in range(len(list_2)):
        list_3.append(list_1[i]+ list_2[j])
print(list_3)

frequnecies = []

for i in range(1, 12):
    frequnecies.append(list_3.count(i+1))

print(frequnecies)

percentage = []
for i in range(len(frequnecies)):
    percentage.append(frequnecies[i]*100/len(list_3))

for i in range(len(percentage)):
    print(f"probability of {i+2} is {percentage[i]:.0f}%")