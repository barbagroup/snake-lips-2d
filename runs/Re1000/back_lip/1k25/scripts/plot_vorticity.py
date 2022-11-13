"""Plot the voriticity field at saved time steps."""

import pathlib

import numpy
import petibmpy
import yaml
from matplotlib import pyplot


maindir = pathlib.Path(__file__).absolute().parents[1]
datadir = maindir / 'postprocessing' / 'wz'
figdir = maindir / 'figures'
figdir.mkdir(parents=True, exist_ok=True)

filepath = maindir / 'config.yaml'
with open(filepath, 'r') as f:
    config = yaml.safe_load(f)['parameters']
start, end, nsave = config['startStep'], config['nt'], config['nsave']
dt = config['dt']
timesteps = numpy.arange(start, end + 1, step=nsave)
timesteps = [180000]

filepath = maindir / 'snake.body'
body = petibmpy.read_body(filepath, skiprows=1)

filepath = datadir / 'grid.h5'
grid = petibmpy.read_grid_hdf5(filepath, 'wz')

pyplot.rc('font', family='serif', size=12)
levels = numpy.linspace(-5.0, 5.0, num=50)

for timestep in timesteps:
    print(f'[time step {timestep}] Loading and plotting the vorticity field ...')
    filepath = datadir / f'{timestep:0>7}.h5'
    wz = petibmpy.read_field_hdf5(filepath, 'wz')

    fig, ax = pyplot.subplots(figsize=(5.0, 3.0))
    ax.text(-0.5, 1.0, f't = {timestep * dt:.1f}')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.contourf(*grid, wz, levels=levels, extend='both')
    ax.fill(*body, color='gray')
    ax.axis('scaled', adjustable='box')
    ax.set_xlim(-1.0, 4.0)
    ax.set_ylim(-1.5, 1.5)
    fig.tight_layout()

    filepath = figdir / f'vorticity_{timestep:0>7}.png'
    fig.savefig(filepath, dpi=300, bbox_inches='tight')

    pyplot.close(fig)
