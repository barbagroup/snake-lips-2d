"""Run post-processing scripts."""

import os
import subprocess
from pathlib import Path

pwd = Path(__file__).absolute().parent
os.environ['MPLBACKEND'] = 'AGG'  # set non-GUI backend to skip showing figures

scripts = [
    'plot_modified_sections.py',
]

for script in scripts:
    print(f'[INFO] Running script {script} ...')
    script = str(pwd / script)
    p = subprocess.Popen(
        f'python {script} --no-compute --no-show', shell=True
    )
    p.communicate()
