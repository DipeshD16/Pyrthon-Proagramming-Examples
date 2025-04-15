num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
if num2 < num1:
    num1, num2=num2, num1
print(num1, num2)
gcd_list =[]
while num1 != 0:
    remainder = num2%num1
    gcd_list.append(num1)
    num2, num1 = num1, remainder
print("List of remainders: ",gcd_list)
print("GCD: ",num2)