"""Write the YAML configuration file for the probes."""

from collections import OrderedDict
import numpy
import pathlib
import yaml

import petibmpy


# Set directories.
simudir = pathlib.Path(__file__).absolute().parents[1]
datadir = simudir / 'output'

probes = []  # will store info about the probes

# Set probe information for vertical profiles of velocity and pressure.
fields = ['u', 'v', 'p']
for field in fields:
    filepath = datadir / 'grid.h5'
    grid = petibmpy.read_grid_hdf5(filepath, field)
    xlocs = [0.5, 1.0, 2.0, 3.0, 4.0, 5.0]
    for i, xloc in enumerate(xlocs):
        probe = OrderedDict({})
        name = f'probe{i + 1}-{field}'
        box = ((xloc, xloc), (-3.0, 3.0))
        probe = petibmpy.ProbeVolume(name, field,
                                     box=box, adjust_box=True, grid=grid,
                                     n_sum=10000,
                                     path=f'{name}.h5')
        probes.append(probe)

# Set probe information for monitoring pressure in vicinity of body.
filepath = datadir / 'grid.h5'
grid = petibmpy.read_grid_hdf5(filepath, 'p')
box = ((-0.6, 0.6), (-0.6, 0.6))
name = 'probe-p'
probe = petibmpy.ProbeVolume(name, 'p',
                             box=box, adjust_box=True, grid=grid,
                             n_sum=10000,
                             path=f'{name}.h5')
probes.append(probe)

# Save the probe information to a YAML file.
filepath = simudir / 'probes.yaml'
petibmpy.probes_yaml_dump(probes, filepath)
