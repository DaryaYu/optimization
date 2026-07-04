import numpy as np


GRID = 1000

x = np.linspace(0, 10, GRID)
y = np.linspace(0, 10, GRID)

X, Y = np.meshgrid(x, y)

POINTS = np.column_stack((X.ravel(), Y.ravel()))


def estimate_coverage(centers, radii):
    coords = centers.reshape(-1, 2)

    dx = POINTS[:, None, 0] - coords[None, :, 0]
    dy = POINTS[:, None, 1] - coords[None, :, 1]

    distances2 = dx**2 + dy**2
    covered = distances2 <= radii**2
    coverage = covered.any(axis=1).mean()

    return coverage


def estimate_objective(centers, radii):

    return float(-estimate_coverage(centers, radii))