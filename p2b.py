import sympy as sp

sp.init_printing()

x = sp.Symbol("x", real=True)
y = sp.Symbol("y", real=True)
z_1 = sp.Symbol("z_1", real=True)
z_2 = sp.Symbol("z_2", real=True)

f_1 = x**2 + x * y - 77
f_2 = x * y + y**2 - 44

X = sp.Matrix([f_1, f_2])
Y = sp.Matrix([x, y])

D_X_Y = X.jacobian(Y)
D_X_Y_inversa = D_X_Y.inv()

# x_ast = [7, 4]
# print(f_1.subs({x: 7, y: 4}))
# print(f_2.subs({x: 7, y: 4}))

# cálculo del C
print(sp.N(D_X_Y_inversa.subs({x: 7, y: 4}).norm()))

print(D_X_Y)
# print(f_2.subs({x: 7, y: 4}))
