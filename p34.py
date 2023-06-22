#!/usr/bin/env python

"""Programa p34.py"""

import sympy as sp

sp.init_printing()

x_1 = sp.Symbol("x_1", real=True)
x_2 = sp.Symbol("x_2", real=True)
x_3 = sp.Symbol("x_3", real=True)

f_1 = 10 * x_1 - 2 * x_2**2 - 2 * x_3 - 5
f_2 = 8 * x_2**2 + 4 * x_3**2 - 9
f_3 = 8 * x_2 * x_3 + 4

X = sp.Matrix([f_1, f_2, f_3])
Y = sp.Matrix([x_1, x_2, x_3])

D_X_Y = X.jacobian(Y)

print(f"{D_X_Y.det().subs({x_1: 0, x_2: 0, x_3: 0})}")

# print(f"{D_X_Y}")
# print(f"{sp.N(D_X_Y.inv().norm().subs({x_1: 1, x_2: 1, x_3: 0}))}")
# print(f"{sp.simplify(D_X_Y * D_X_Y.inv())}")
# f_1_prime_x_1 = sp.diff(f_1, x_1)
# f_1_prime_x_2 = sp.diff(f_1, x_2)
# f_1_prime_x_3 = sp.diff(f_1, x_3)

# f_2_prime_x_1 = sp.diff(f_2, x_1)
# f_2_prime_x_2 = sp.diff(f_2, x_2)
# f_2_prime_x_3 = sp.diff(f_2, x_3)

# f_3_prime_x_1 = sp.diff(f_3, x_1)
# f_3_prime_x_2 = sp.diff(f_3, x_2)
# f_3_prime_x_3 = sp.diff(f_3, x_3)

# print(f"{f_1_prime_x_1}")
# print(f"{f_2_prime_x_1}")
# print(f"{f_3_prime_x_1}")

# print(f"{f_1_prime_x_2}")
# print(f"{f_2_prime_x_2}")
# print(f"{f_3_prime_x_2}")

# print(f"{f_1_prime_x_3}")
# print(f"{f_2_prime_x_3}")
# print(f"{f_3_prime_x_3}")
