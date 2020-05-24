from functools import reduce
nums = [3, 5, 6, 7 ,8, 10]
evens = list(filter(lambda n : n%2==0, nums))
doubles = list(map(lambda n : n*2, nums))

print(evens)
print(doubles)

sum = reduce(lambda a,b : a+b, doubles)
print(sum)
