"""Compute the vorticity field."""

import pathlib

import numpy
import petibmpy
import yaml


maindir = pathlib.Path(__file__).absolute().parents[1]
datadir = maindir / 'output'
outdir = maindir / 'postprocessing' / 'wz'
outdir.mkdir(parents=True, exist_ok=True)

filepath = maindir / 'config.yaml'
with open(filepath, 'r') as f:
    config = yaml.safe_load(f)['parameters']
start, end, nsave = config['startStep'], config['nt'], config['nsave']
timesteps = numpy.arange(start, end + 1, step=nsave)
timesteps = [170000, 180000]

filepath = datadir / 'grid.h5'
grid_u = petibmpy.read_grid_hdf5(filepath, 'u')
grid_v = petibmpy.read_grid_hdf5(filepath, 'v')
saved_once = False
for timestep in timesteps:
    print(f'[time step {timestep}] Computing and saving vorticity field ...')
    filepath = datadir / f'{timestep:0>7}.h5'
    u = petibmpy.read_field_hdf5(filepath, 'u')
    v = petibmpy.read_field_hdf5(filepath, 'v')
    wz, grid_wz = petibmpy.compute_wz(u, v, grid_u, grid_v)

    if not saved_once:
        filepath = outdir / 'grid.h5'
        petibmpy.write_grid_hdf5(filepath, 'wz', *grid_wz)
        saved_once = True

    filepath = outdir / f'{timestep:0>7}.h5'
    petibmpy.write_field_hdf5(filepath, 'wz', wz)
