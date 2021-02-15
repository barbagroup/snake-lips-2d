"""Plot the time-averaged force coefficients versus the angle of attack."""

from matplotlib import pyplot
import pathlib

import petibmpy


maindir = pathlib.Path(__file__).absolute().parents[1]

sections = ['both_lips', 'front_lip', 'back_lip', 'no_lips']
angles = [15, 20, 25, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
Re = 2000  # Reynolds number
limits = (50.0, 80.0)  # time-limits use for averaging force coefficients
save_figures = True  # save Matplotlib figures as PNG files
show_figures = True  # display Matplotlib figures

# Set default font family and size for Matplotlib figures.
pyplot.rc('font', family='serif', size=12)

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
        cd_section.append(cd)
        cl_section.append(cl)
    cd_all[label], cl_all[label] = cd_section, cl_section

# Plot time-averaged drag coefficient versus angle of attack.
print('[INFO] Plotting drag coefficient vs. angle ...')
fig, ax = pyplot.subplots(figsize=(5.0, 5.0))
ax.set_xlabel('Angle of attack ($^o$)')
ax.set_ylabel('Drag coefficient')
for label, values in cd_all.items():
    ax.plot(angles, values, label=label, marker='o')
ax.legend(loc='upper left', frameon=False)
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
ax.set_xlabel('Angle of attack ($^o$)')
ax.set_ylabel('Lift coefficient')
for label, values in cl_all.items():
    ax.plot(angles, values, label=label, marker='o')
ax.legend(loc='upper left', frameon=False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
fig.tight_layout()

if save_figures:
    # Save figure of drag coefficient versus angle of attack.
    filepath = figdir / 'avg_lift_coefficients_vs_aoa.png'
    fig.savefig(filepath, dpi=300, bbox_inches='tight')

if show_figures:
    pyplot.show()
