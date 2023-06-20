import numpy as np
from skimage import measure
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

xl = np.linspace(-3, 3, 50)
X, Y, Z = np.meshgrid(xl, xl, xl)


def f_1(x_1, x_2, x_3):
    return 6 * x_1 - 2 * np.cos(x_2 * x_3) - 1


def f_2(x_1, x_2, x_3):
    return 9 * x_2 + np.sqrt(x_1**2 + np.sin(x_3) + 1.06) + 0.9


def f_3(x_1, x_2, x_3):
    return 60 * x_3 + 3 * np.exp(-x_1 * x_2) + 10 * np.pi - 3


F = f_1(X, Y, Z)

verts, faces, normals, values = measure.marching_cubes(
    F, 0, spacing=[np.diff(xl)[0]] * 3
)
verts -= 3

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_trisurf(verts[:, 0], verts[:, 1], faces, verts[:, 2], cmap="jet", lw=0)
plt.show()

# https://stackoverflow.com/a/63773167