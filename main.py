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
