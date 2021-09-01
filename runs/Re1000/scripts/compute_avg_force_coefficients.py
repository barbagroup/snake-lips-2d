"""Compute time-averaged force coefficients vs. angle of attack."""

import pathlib

import yaml

import petibmpy


maindir = pathlib.Path(__file__).absolute().parents[1]

sections = ['both_lips', 'front_lip', 'back_lip', 'no_lips']
angles = [15, 20, 25, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 45]
Re = 1000  # Reynolds number
limits = (50.0, 80.0)  # time-limits use for averaging force coefficients

# Load forces from files and compute time-averaged force coefficients.
cd_all, cl_all = dict(), dict()
for section in sections:
    label = section.replace('_', ' ')
    cd_section, cl_section = [], []
    for angle in angles:
        folder = f'{Re // 1000}k{angle}'
        print(f'[{label} - {folder}] Computing time-averaged values ...')
        simudir = maindir / section / folder
        datadir = simudir / 'output'
        filepath = datadir / 'forces-0.txt'
        t, fx, fy = petibmpy.read_forces(filepath)
        cd, cl = petibmpy.get_force_coefficients(fx, fy, coeff=2.0)
        cd, cl = petibmpy.get_time_averaged_values(t, cd, cl, limits=limits)
        cd_section.append(float(cd))
        cl_section.append(float(cl))
    cd_all[label], cl_all[label] = cd_section, cl_section

data = dict()
data['Re'] = Re
data['time limits'] = limits
data['AoA'] = angles
data['Cd'] = cd_all
data['Cl'] = cl_all

datadir = maindir / 'data'
datadir.mkdir(parents=True, exist_ok=True)
filepath = datadir / 'avg_force_coefficients.yaml'
with open(filepath, 'w') as f:
    yaml.safe_dump(data, f)
