"""Run post-processing scripts."""

import os
import subprocess
from pathlib import Path

pwd = Path(__file__).absolute().parent
os.environ['MPLBACKEND'] = 'AGG'  # set non-GUI backend to skip showing figures

scripts = [
    'create_body.py',
    'compute_vorticity.py',
    'plot_vorticity.py'
]

for script in scripts:
    print(f'[INFO] Running script {script} ...')
    script = str(pwd / script)
    p = subprocess.Popen(
        f'python {script}', shell=True
    )
    p.communicate()
