#!/usr/bin/env python

"""Programa p11.py
Faddeev-LeVerrier"""

import numpy as np

A = np.array(object=[[0.6, 0.2], [0.4, 0.8]], dtype=float)

B_1 = np.copy(a=A)
b_1 = -np.trace(a=B_1) / 1

B_2 = A @ (B_1 + b_1 * np.identity(2))
b_2 = -np.trace(a=B_2) / 2

if __name__ == "__main__":
    print(f"A:\n{A}")
    print(f"B_1:\n{B_1}")
    print(f"b_1:\n{b_1}")
    print(f"B_2:\n{B_2}")
    print(f"b_2:\n{b_2}")
    # Comprobación
    w, _ = np.linalg.eig(a=A)
    # assert sorted(w) == np.roots(p=[1, -1.4, 0.4])
