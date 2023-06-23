from my_math.algebra import Algebra

algebra = Algebra(a=2, b=7, c=-15, d=13)
print(f"x-value in first-degree algebra equation: {algebra.first_degree_x()}")
print(f"(x1, x2) in quadratic equation: {algebra.quadratic_x()}")