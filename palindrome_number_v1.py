
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def reverse_number(n):
    return int(str(n)[::-1])

# Store numbers that take >20 steps to become palindromes
hard_numbers = []

for num in range(10, 100):  # two-digit numbers only
    count = 0
    current = num
    while not is_palindrome(current) and count <= 1000:
        rev = reverse_number(current)
        current += rev
        count += 1
    if count > 20:
        hard_numbers.append(num)

print("Two-digit numbers that need more than 20 steps to reach a palindrome:")
print(hard_numbers)