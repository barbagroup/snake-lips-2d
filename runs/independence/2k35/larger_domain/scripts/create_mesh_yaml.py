"""Create a YAML file with info about the structured Cartesian mesh."""

import collections
from matplotlib import pyplot
import pathlib

import petibmpy


Box = collections.namedtuple('Box', ['xstart', 'xend', 'ystart', 'yend'])

domain = Box(-20.0, 35.0, -20.0, 20.0)
box1, d1 = Box(-0.6, 1.2, -0.6, 0.6), 0.004
box2, d2 = Box(-1.0, 7.0, -3.0, 3.0), 0.008
show_figure = True

config_x1 = dict(start=domain.xstart, end=box2.xstart,
                 width=d2, stretchRatio=1.1, max_width=10 * d2, reverse=True)
config_x2 = dict(start=box2.xstart, end=box1.xstart,
                 width=d1, stretchRatio=1.1, max_width=d2, reverse=True)
config_x3 = dict(start=box1.xstart, end=box1.xend, width=d1)
config_x4 = dict(start=box1.xend, end=box2.xend,
                 width=d1, stretchRatio=1.01, max_width=d2)
config_x5 = dict(start=box2.xend, end=domain.xend,
                 width=d2, stretchRatio=1.01, max_width=10 * d2)

config_y1 = dict(start=domain.ystart, end=box2.ystart,
                 width=d2, stretchRatio=1.1, max_width=10 * d2, reverse=True)
config_y2 = dict(start=box2.ystart, end=box1.ystart,
                 width=d1, stretchRatio=1.1, max_width=d2, reverse=True)
config_y3 = dict(start=box1.ystart, end=box1.yend, width=d1)
config_y4 = dict(start=box1.yend, end=box2.yend,
                 width=d1, stretchRatio=1.1, max_width=d2)
config_y5 = dict(start=box2.yend, end=domain.yend,
                 width=d2, stretchRatio=1.1, max_width=10 * d2)

config = [dict(direction='x', start=domain.xstart,
               subDomains=[config_x1, config_x2,
                           config_x3,
                           config_x4, config_x5]),
          dict(direction='y', start=domain.ystart,
               subDomains=[config_y1, config_y2,
                           config_y3,
                           config_y4, config_y5])]

grid = petibmpy.CartesianGrid(config)
print(grid)
simudir = pathlib.Path(__file__).absolute().parents[1]
filepath = simudir / 'mesh.yaml'
grid.write_yaml(filepath, ndigits=10)
grid.print_info()

if show_figure:
    fig, ax = grid.plot_gridlines_2d()
    # Plot body coordinates.
    filepath = simudir / 'snake.body'
    xb, yb = petibmpy.read_body(filepath, skiprows=1)
    ax.plot(xb, yb, color='C3', marker='x')
    pyplot.show()
