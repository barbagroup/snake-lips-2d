"""Create the coordinates of the immersed boundary."""

import pathlib

import petibmpy


# Set directories.
simudir = pathlib.Path(__file__).absolute().parents[1]
rootdir = simudir.parents[3]
datadir = rootdir / 'data'

# Load input coordinates from file.
filepath = datadir / 'snake_nobacklip.txt'
x, y = petibmpy.read_body(filepath, skiprows=1)

# Regularize and rotate geometry.
x, y = petibmpy.regularize2d(x, y, ds=0.004)
x, y = petibmpy.rotate2d(x, y, center=(0.0, 0.0), angle=-33.0)

# Save coordinates to file.
filepath = simudir / 'snake.body'
petibmpy.write_body(filepath, x, y)
