def team(lst):
    x=0
    y=0
    for i in lst:
        if len(i)>5:
            x+=1
        else:
            y+=1

    return x,y
lst1=[]
for i in range(10):
    lst.append(input("Enter the names of the team member"))
print(lst)
x, y = team(lst)

print("no of names > than 5 ch. {} and no of names < 5 ch {}". format(x,y))
