"""Run post-processing scripts."""

import os
import subprocess
from pathlib import Path

pwd = Path(__file__).absolute().parent
os.environ['MPLBACKEND'] = 'AGG'  # set non-GUI backend to skip showing figures

scripts = [
    'compute_stats_force_coefficients.py',
    'plot_force_coefficients_compare_dx_dt.py',
    'plot_profiles_compare_dx_dt.py',
    'plot_surface_pressure_compare_dx_dt.py'
]

for script in scripts:
    print(f'[INFO] Running script {script} ...')
    script = str(pwd / script)
    p = subprocess.Popen(
        f'python {script}', shell=True
    )
    p.communicate()
