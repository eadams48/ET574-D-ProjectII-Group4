#Create two math functions not built into python
#1st Function - Compounding Annual Interest Rate
#2nd Fucntion - Volume of a pyramid

def Annual_Compd_Intrst(P, r, n, t):
    """
    Name: compound_interest
    Purpose: Calculates the final amount after compound interest
    Parameters:
        P(float): initial principal
        r(float): annual interest rate
        n(int): num of times compounded per year
        t(int): num of years
    Return:
        float: final amount after interest
    """

    if P < 0 or n <= 0 or t < 0:
        return "Invalid input"

    return P * (1 + r / n) ** (n * t)
def factorial(x):
    """
    Name: factorial
    Purpose: Calculates the factorial of a non-negative integer
    Parameters:
        x(int): a non-negative integer
    Return:
        int: factorial of x
    """

    if not isinstance(x, int) or x < 0:
        return "Invalid input"

    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result


def area_of_circle(r):
    """
    Name: area_of_circle
    Purpose: Calculates the area of a circle
    Parameters:
        r(int or float): radius of the circle
    Return:
        float: area of the circle
    """

    if r < 0:
        return "Invalid input"

    pi = 3.14159
    return pi * r * r
