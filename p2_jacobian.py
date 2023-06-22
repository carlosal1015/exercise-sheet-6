#!/usr/bin/env python

"""Programa p2_jacobian.py"""

import sympy as sp

sp.init_printing()

x = sp.Symbol("x", real=True)
y = sp.Symbol("y", real=True)
# z_1 = sp.Symbol("z_1", real=True)
# z_2 = sp.Symbol("z_2", real=True)

f_1 = x**2 + x * y - 77
f_2 = x * y + y**2 - 44

F = sp.Matrix([f_1, f_2])
X = sp.Matrix([x, y])

DF = F.jacobian(X)
# DF_inversa = DF.inv()

x0 = sp.Matrix([1, 1])
A = DF.subs({x: x0[0], y: x0[1]})
b = -F.subs({x: x0[0], y: x0[1]})
print(f"{A}")
print(f"{b}")
h0 = sp.solve_linear_system(sp.Matrix.hstack(A, b), x, y)
h0 = sp.Matrix([h0[x], h0[y]])
print(f"{h0}")
x1 = x0 + h0
print(f"{x1}")
# x_ast_1 = [7, 4]
# print(f_1.subs({x: 7, y: 4}))
# print(f_2.subs({x: 7, y: 4}))

# cálculo del C
# print(sp.N(D_X_Y_inversa.subs({x: 7, y: 4}).norm()))

# print(DF)
# print(f_2.subs({x: 7, y: 4}))
