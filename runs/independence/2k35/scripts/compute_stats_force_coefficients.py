"""Compute statistics about the force coefficients."""

import pathlib

import petibmpy


class Table:

    def __init__(self, header):
        self.table = ['| ' + ' | '.join(header) + ' |',
                      '|:-|' + ':-:|' * (len(header) - 1)]

    def __repr__(self):
        return '\n'.join(self.table)

    def add_row(self, data, compare_to=None):
        row = f'| {data[0]} |'
        for i, val in enumerate(data[1:], start=1):
            row += f' {val:.3f} '
            if compare_to is not None:
                rel = (val - compare_to[i]) / compare_to[i] * 100.0
                if abs(rel) >= 0.005:
                    sign = '+' if rel >= 0 else '-'
                    row += f'({sign}{abs(rel):.2f} %) '
            row += '|'
        self.table.append(row)


maindir = pathlib.Path(__file__).absolute().parents[1]
metadata = {'Base': 'base',
            'Coarser in Space': 'coarser_grid',
            'Finer in Space': 'finer_grid',
            'Finer in Time': 'finer_dt',
            'Larger Domain': 'larger_domain',
            'Larger Uniform Area': 'uniform',
            'Shifted Markers': 'markers',
            'Tighter Iterative Solvers ($atol = 10^{-9}$)': 'atol'}
time_limits = (50.0, 80.0)
print(f'Time limits: {time_limits}')

table = Table(['Case', '<C_D>', 'rms(C_D)', '<C_L>', 'rms(C_L)'])

compare_to = None
for name, folder in metadata.items():
    simudir = maindir / folder
    filepath = simudir / 'output' / 'forces-0.txt'
    t, fx, fy = petibmpy.read_forces(filepath)
    cd, cl = petibmpy.get_force_coefficients(fx, fy, coeff=2.0)
    cd_mean, cl_mean = petibmpy.get_time_averaged_values(t, cd, cl,
                                                         limits=time_limits)
    cd_rms, cl_rms = petibmpy.get_rms_values(t, cd, cl, limits=time_limits)
    data = [name, cd_mean, cd_rms, cl_mean, cl_rms]
    table.add_row(data, compare_to=compare_to)
    if name == 'Base':
        compare_to = data

print(table)
