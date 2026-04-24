#-------Annual_Compd_Intrst------
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


#------factorial------
def factorial(x):
    """
    Name: factorial
    Purpose: Calculates the factorial of a non-negative integer
    Parameters:
        x(int): a non-negative integer
    Return:
        int: factorial of x
    """

    if not isinstance(x, int):
        raise TypeError("Input must be a non-negative integer")
    if x < 0:
        raise ValueError("Input must be a non-negative integer")
    result = 1
    for i in range(1, x + 1):
        result = result * i
    return result

#-------area_of_circle------
def area_of_circle(r):
    """
    Name: area_of_circle
    Purpose: Calculates the area of a circle
    Parameters:
        r(int or float): radius of the circle
    Return:
        float: area of the circle
    """
    # Check if r is a valid type
    if not isinstance(r, (int, float)) or isinstance(r, bool):
        raise TypeError("Radius must be a number")
    
    # Check if r is negative
    if r < 0:
        raise ValueError("Radius cannot be negative")
    
    pi = 3.14159
    return pi * r * r
    
#--------pow--------
def pow(x, y):
    """
    Name: pow
    Purpose: Calculates x raised to the power y
    Parameters:
        x(float or int): base
        y(int): exponent
    Return:
        float or int: x ** y
    """
 
    try:
       if y == 0:
         return 1
    
       result = 1
       abs_y = abs(y)
       for z in range(abs_y):
         result *= x
    
       if y < 0:
         return 1 / result
       return result
    except ValueError:
        return "Invalid input"

