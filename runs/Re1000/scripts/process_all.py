"""Run post-processing scripts."""

import os
import subprocess
from pathlib import Path

pwd = Path(__file__).absolute().parent
os.environ['MPLBACKEND'] = 'AGG'  # set non-GUI backend to skip showing figures

scripts = [
    'compute_avg_force_coefficients.py',
    'plot_avg_force_coefficients.py',
    'plot_force_coefficients_1k35.py',
    'plot_surface_pressure_1k35.py',
    'plot_vertical_profiles_1k35.py'
]

for script in scripts:
    print(f'[INFO] Running script {script} ...')
    script = str(pwd / script)
    p = subprocess.Popen(
        f'python {script}', shell=True
    )
    p.communicate()
