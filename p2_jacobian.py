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
A0 = DF.subs({x: x0[0], y: x0[1]})
b0 = -F.subs({x: x0[0], y: x0[1]})
print(f"A0:\n{A0}")
print(f"|A0|={A0.det()}")
print(f"b0:\n{b0}")
h0 = sp.solve_linear_system(sp.Matrix.hstack(A0, b0), x, y)
h0 = sp.Matrix([h0[x], h0[y]])
print(f"h0:\n{h0}")
x1 = x0 + h0
print(f"x1:\n{x1}")
print(f"{h0.norm(ord=sp.oo)}")

A1 = DF.subs({x: x1[0], y: x1[1]})
b1 = -F.subs({x: x1[0], y: x1[1]})
print(f"A1:\n{A1}")
print(f"|A1|={A1.det()}")
print(f"b1:\n{b1}")
h1 = sp.solve_linear_system(sp.Matrix.hstack(A1, b1), x, y)
h1 = sp.Matrix([h1[x], h1[y]])
print(f"h1:\n{h1}")
x2 = x1 + h1
print(f"x2:\n{x2}")
print(f"{h1.norm(ord=sp.oo)}")
# x_ast_1 = [7, 4]
# print(f_1.subs({x: 7, y: 4}))
# print(f_2.subs({x: 7, y: 4}))

# cálculo del C
# print(sp.N(D_X_Y_inversa.subs({x: 7, y: 4}).norm()))

# print(DF)
# print(f_2.subs({x: 7, y: 4}))
