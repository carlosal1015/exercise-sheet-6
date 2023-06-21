import numpy as np


def f(x):
    ft = np.zeros((3, 1))
    ft[0] = 10 * x[0] - 2 * x[1] ** 2 - 2 * x[2] - 5
    ft[1] = 8 * x[1] ** 2 + 4 * x[2] ** 2 - 9
    ft[2] = 8 * x[1] * x[2] + 4
    return ft


def J(x):
    Jf = np.zeros((3, 3))
    Jf[:, 0] = np.transpose([10, 0, 0])
    Jf[:, 1] = np.transpose([-4 * x[1], 16 * x[1], 8 * x[2]])
    Jf[:, 2] = np.transpose([-2, 8 * x[2], 8 * x[1]])
    return Jf


def homotopia(f, J, x0, N=10):
    k = 1
    h = 1 / N
    a = f(x0)
    b = -1 * h * a
    while k <= N:
        A = J(x0)
        k1 = ((np.linalg.inv(A) @ b)).T
        C = x0 + (1 / 2 * k1)
        C = C.ravel().tolist()
        D = J(C)
        k2 = ((np.linalg.inv(D) @ b)).T
        E = x0 + (1 / 2 * k2)
        E = E.ravel().tolist()
        F = J(E)
        k3 = ((np.linalg.inv(F) @ b)).T
        G = x0 + k3
        G = G.ravel().tolist()
        I = J(G)
        k4 = ((np.linalg.inv(I) @ b)).T
        x = x0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        print("Iteracion", k, x[0])
        x0 = x.ravel().tolist()
        k = k + 1


x0 = [1.0, 1.0, 0.0]

if __name__ == "__main__":
    print(f"x0: {x0}")
    homotopia(f, J, x0)
