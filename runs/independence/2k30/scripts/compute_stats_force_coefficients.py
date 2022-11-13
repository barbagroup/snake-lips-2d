"""Compute statistics about the force coefficients."""

import pathlib

import pandas

import petibmpy


maindir = pathlib.Path(__file__).absolute().parents[1]
metadata = {'Base case': 'base',
            'Finer in time': 'finer_dt',
            'Finer in space': 'finer_grid',
            'Coarser in space': 'coarser_grid',
            'Extended domain': 'larger_domain',
            'Extended uniform region': 'uniform',
            'Displaced body': 'markers',
            'Tighter iterative solvers': 'atol'}
time_limits = (50.0, 80.0)
print(f'Time limits: {time_limits}')

df = pandas.DataFrame(
    columns=['Case', '<C_D>', 'rms(C_D)', '<C_L>', 'rms(C_L)']
)

for name, folder in metadata.items():
    simudir = maindir / folder
    filepath = simudir / 'output' / 'forces-0.txt'
    t, fx, fy = petibmpy.read_forces(filepath)
    cd, cl = petibmpy.get_force_coefficients(fx, fy, coeff=2.0)
    cd_mean, cl_mean = petibmpy.get_time_averaged_values(t, cd, cl,
                                                         limits=time_limits)
    cd_rms, cl_rms = petibmpy.get_rms_values(t, cd, cl, limits=time_limits)

    df.loc[len(df)] = [name, cd_mean, cd_rms, cl_mean, cl_rms]

df = df.set_index('Case').round(decimals=3)

print('\nForce coefficient statistics:')
print(df)

ref = df.loc['Base case']
rdiff_df = df.apply(lambda row: (row - ref) / ref * 100, axis=1)
rdiff_df = rdiff_df.round(decimals=1)

print('\nPercentage relative difference wrt Base case:')
print(rdiff_df)

merged = df.merge(rdiff_df, on='Case', suffixes=('', '_rdiff'))
ncols = len(df.columns)
ordered_cols = [
    c for t in zip(merged.columns[:ncols], merged.columns[ncols:]) for c in t
]
datadir = maindir / 'data'
datadir.mkdir(parents=True, exist_ok=True)
filepath = datadir / 'force_coefficients_stats.csv'
merged[ordered_cols].to_csv(filepath)
