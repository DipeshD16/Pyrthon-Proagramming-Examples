""" Here is an old puzzle you can solve using brute force by using a computer program to check all the possibilities: In the calculation 43 + 57 = 207, every digit is precisely one away from its true value. What is the correct calculation?
"""
def possible_digits(d):
    return [i for i in range(10)if abs(i-d) == 1]
   
def solve_puzzle():
    for a1 in possible_digits(4):
        for a2 in possible_digits(3):
            num1 = a1*10 + a2
            for b1 in possible_digits(5):
                for b2 in possible_digits(7):
                    num2 = b1*10 + b2
                    result = num1+ num2
                    if 100 <= result <=999:
                        r1, r2, r3 = int(str(result)[0]), int(str(result)[1]), int(str(result)[2])
                        if r1 in possible_digits(2) and r2 in possible_digits(0) and r3 in possible_digits(7):
                            print(f"Correct Calculation: {num1} + {num2} = {result}")
                            return
solve_puzzle()
    