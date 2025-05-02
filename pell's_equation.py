#this program finds integer solutions to the Pell's equation x^2 - 2y^2 = 1
#using brute force search
def solve_pells_equation(limit=100):
    print("Solutions to x^2 - 2y^2 = 1 where 1 ≤ x, y ≤ 100:\n")
    for x in range(1, limit + 1):
        for y in range(1, limit + 1):
            if x**2 - 2 * y**2 == 1:
                print(f"x = {x}, y = {y}")

solve_pells_equation()