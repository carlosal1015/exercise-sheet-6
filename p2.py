#!/usr/bin/env python

"""Programa p2.py"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from scipy.optimize import fsolve

plt.rcParams["text.usetex"] = True
plt.rcParams["font.serif"] = ["Computer Modern"]
# plt.rcParams["figure.autolayout"] = True
# plt.rcParams["figure.figsize"] = [10, 10]


nx = 301
x = np.linspace(start=-20.0, stop=20.0, num=nx)
y = 24 - x

x_, y_ = np.meshgrid(x, x)
equation = x_**2 + y_**2 - 290


def func(x):
    return [x[0] ** 2 + x[1] ** 2 - 290, x[0] + x[1] - 24]


root = fsolve(func, [-12, 35])


if __name__ == "__main__":
    fig, ax = plt.subplots()
    ax.grid()
    ax.plot(x, y, "b", lw=0.5)
    # https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axis_equal_demo.html
    # https://stackoverflow.com/a/39500357/9302545
    ax.axis("equal")
    CS = ax.contour(x, y, equation, [0], linewidths=0.5)
    # h, _ = CS.legend_elements()
    # label=r"$x + y = 24$"
    black_patch = mpatches.Patch(
        color="black", label=r"$x^{2} + y^{2} = 290$", linewidth=0.2, linestyle="-"
    )
    red_patch = mpatches.Patch(
        color="blue", label=r"$x + y = 24$", linewidth=0.2, linestyle="-"
    )
    ax.legend(
        handles=[black_patch, red_patch], shadow=True, title="Leyenda", fancybox=True
    )
    fig.savefig("p2.pdf", transparent=True, bbox_inches="tight")
    print(f"Solución: {root}")
