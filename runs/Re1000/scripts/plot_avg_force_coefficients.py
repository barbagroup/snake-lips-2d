"""Plot time-averaged force coefficients vs. angle of attack."""

import pathlib

import yaml
from matplotlib import pyplot

import petibmpy


save_figures = True  # save Matplotlib figures as PNG files
show_figures = True  # display Matplotlib figures
# Set default font family and size for Matplotlib figures.
pyplot.rc('font', family='serif', size=12)

maindir = pathlib.Path(__file__).absolute().parents[1]
datadir = maindir / 'data'

with open(datadir / 'avg_force_coefficients.yaml', 'r') as f:
    data = yaml.safe_load(f)
Re = data['Re']
angles = data['AoA']
cd_all = data['Cd']
cl_all = data['Cl']

ratio_all = dict()
sections = ['both lips', 'front lip', 'back lip', 'no lips']
labels = ['both', 'front', 'back', 'none']
for section in sections:
    ratio_all[section] = [cl / cd
                          for cl, cd in zip(cl_all[section], cd_all[section])]

# Plot time-averaged drag coefficient versus angle of attack.
print('[INFO] Plotting drag coefficient vs. angle ...')
fig, ax = pyplot.subplots(figsize=(5.0, 5.0))
ax.grid(axis='x', color='gray', linewidth=0.5, linestyle=':')
ax.set_xlabel('Angle of attack ($^o$)')
ax.set_ylabel('Drag coefficient')
for section, label in zip(sections, labels):
    ax.plot(angles, cd_all[section], label=label, marker='o')
ax.set_ylim(0.2, 2.1)
ax.legend(loc='upper left', frameon=True,
          framealpha=1.0, edgecolor='white', borderaxespad=0.1)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
fig.tight_layout()

if save_figures:
    # Save figure of drag coefficient versus angle of attack.
    figdir = maindir / 'figures'
    figdir.mkdir(parents=True, exist_ok=True)
    filepath = figdir / 'avg_drag_coefficients_vs_aoa.png'
    fig.savefig(filepath, dpi=300, bbox_inches='tight')

# Plot time-averaged lift coefficient versus angle of attack.
print('[INFO] Plotting lift coefficient vs. angle ...')
fig, ax = pyplot.subplots(figsize=(5.0, 5.0))
ax.grid(axis='x', color='gray', linewidth=0.5, linestyle=':')
ax.set_xlabel('Angle of attack ($^o$)')
ax.set_ylabel('Lift coefficient')
for section, label in zip(sections, labels):
    ax.plot(angles, cl_all[section], label=label, marker='o')
ax.set_ylim(0.2, 2.1)
ax.legend(loc='upper left', frameon=True,
          framealpha=1.0, edgecolor='white', borderaxespad=0.1)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
fig.tight_layout()

if save_figures:
    # Save figure of drag coefficient versus angle of attack.
    filepath = figdir / 'avg_lift_coefficients_vs_aoa.png'
    fig.savefig(filepath, dpi=300, bbox_inches='tight')

# Plot time-averaged lift/drag ratio versus angle of attack.
print('[INFO] Plotting lift/drag ratio vs. angle ...')
fig, ax = pyplot.subplots(figsize=(5.0, 5.0))
ax.grid(axis='x', color='gray', linewidth=0.5, linestyle=':')
ax.set_xlabel('Angle of attack ($^o$)')
ax.set_ylabel('Lift/Drag ratio')
for section, label in zip(sections, labels):
    ax.plot(angles, ratio_all[section], label=label, marker='o')
ax.set_ylim(0.5, 1.9)
ax.legend(loc='lower center', frameon=True,
          framealpha=1.0, edgecolor='white', borderaxespad=0.1)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
fig.tight_layout()

if save_figures:
    # Save figure of drag coefficient versus angle of attack.
    filepath = figdir / 'avg_lift_drag_ratio_vs_aoa.png'
    fig.savefig(filepath, dpi=300, bbox_inches='tight')

if show_figures:
    pyplot.show()
