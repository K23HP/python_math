from my_math.algebra import Algebra
from my_math.algebra import calc_square_root

algebra = Algebra(a=2, b=7, c=-15, d=13)
print(algebra.first_degree_x())
print(algebra.quadratic_x())

print(calc_square_root(-10))