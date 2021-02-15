"""Plot the spanwise vorticity in the computational domain."""

from matplotlib import pyplot
import numpy
import pathlib

import petibmpy


# Set directories.
simudir = pathlib.Path(__file__).absolute().parents[1]
datadir = simudir / 'output'
figdir = simudir / 'figures'
figdir.mkdir(parents=True, exist_ok=True)

# Load gridlines from file.
filepath = datadir / 'grid.h5'
grid = petibmpy.read_grid_hdf5(filepath, 'wz')

# Load body coordinates from file.
filepath = simudir / 'snake.body'
body = petibmpy.read_body(filepath, skiprows=1)

# Set default font family and size for Matplotlib figures.
pyplot.rc('font', family='serif', size=14)

# List of time-step indices to process.
timesteps = numpy.arange(0, 400000 + 1, 10000)

# Levels of the filled contours.
levels = numpy.linspace(-5.0, 5.0, num=20)

# Define limits of the axes.
axis_limits = (-5, 10, -5, 5)

for timestep in timesteps:
    print(f'[time step {timestep}] Plot and save contours of wz ...')

    # Load vorticity field from file.
    filepath = datadir / f'{timestep:0>7}.h5'
    wz = petibmpy.read_field_hdf5(filepath, 'wz')

    # Plot the filled contours of the field and the immersed body.
    fig, ax = pyplot.subplots(figsize=(8.0, 6.0))
    ax.set_xlabel('x/c')
    ax.set_ylabel('y/c')
    ax.contourf(*grid, wz, levels=levels, extend='both')
    ax.fill(*body, color='black', alpha=0.6)
    ax.axis('scaled', adjustable='box')
    ax.axis(axis_limits)
    fig.tight_layout()

    # Save Matplotlib figure as PNG.
    filepath = figdir / f'wz_{timestep:0>7}.png'
    fig.savefig(filepath, dpi=300, bbox_inches='tight')

    pyplot.close(fig)


