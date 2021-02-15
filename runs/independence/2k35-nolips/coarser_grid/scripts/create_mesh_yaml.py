"""Create a YAML file with info about the structured Cartesian mesh."""

import collections
from matplotlib import pyplot
import pathlib

import petibmpy


Box = collections.namedtuple('Box', ['xstart', 'xend', 'ystart', 'yend'])

domain = Box(-15.0, 25.0, -15.0, 15.0)
box, d = Box(-1.0, 7.0, -3.0, 3.0), 0.008
show_figure = True

config_x1 = dict(start=domain.xstart, end=box.xstart,
                 width=d, stretchRatio=1.1, max_width=10 * d, reverse=True)
config_x2 = dict(start=box.xstart, end=box.xend, width=d)
config_x3 = dict(start=box.xend, end=domain.xend,
                 width=d, stretchRatio=1.01, max_width=10 * d)

config_y1 = dict(start=domain.ystart, end=box.ystart,
                 width=d, stretchRatio=1.1, max_width=10 * d, reverse=True)
config_y2 = dict(start=box.ystart, end=box.yend, width=d)
config_y3 = dict(start=box.yend, end=domain.yend,
                 width=d, stretchRatio=1.1, max_width=10 * d)

config = [dict(direction='x', start=domain.xstart,
               subDomains=[config_x1, config_x2, config_x3]),
          dict(direction='y', start=domain.ystart,
               subDomains=[config_y1, config_y2, config_y3])]

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
