from my_math.square_root import calc_square_root
"""A class used to calculate the values of x in first-degree 
and second-degree formula"""

class Algebra:
    """A simple attempt to find the values of x in first-degree and 
    quadratic (second-degree) formula."""
    def __init__(self, a, b, c, d=0, decimal=2):
        
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.decimal = decimal
        
    def first_degree_x(self) -> float:
        """This function calculates the value of x in first-degree general 
        formula ax + b = cx + d. a and c are the coefficients of x. 
        b and d are constants. If there is no x on one side of the equation, 
        its coefficient is zero. The general formula for calculating x is
        x = (d - b) / (a - c).

        Returns:
            float: The value of x in first degree algebra equation.
        """
        return round((self.d - self.b) / (self.a - self.c), self.decimal)
        
    def quadratic_x(self) -> tuple:
        """This function calculates the values of x1 and x2 in second-degree 
        general (quadratic) formula ax^2 + bx + c = 0. a and b are the coefficients 
        of x. c is the constant. The general formula for calculating x1 and x2 is 
        x1 = (-b + sqrt(b**2 - (4*a*c))) / (2*a), and 
        x2 = (-b - sqrt(b**2 - (4*a*c))) / (2*a).

        Returns:
            tuple: (x1, x2)
        """
        num = (self.b ** 2) - (4 * self.a * self.c)  # num = b^2 - 4ac
        square_root = calc_square_root(num)  # sqrt(num)
        x1 = (-self.b + square_root) / (2 * self.a)
        x2 = (-self.b - square_root) / (2 * self.a)
        
        return (round(x1, self.decimal), round(x2, self.decimal))
    
        
        
        