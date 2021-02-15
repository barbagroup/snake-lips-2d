"""Generate a figure of the drag and lift force coefficients over time.

Save the figure in the sub-folder `figures` of the simulation directory.
"""

import sys
import pathlib
from matplotlib import pyplot

import petibmpy


# Set parameters.
show_figure = True  # display Matplotlib figure
save_figure = True  # save Matplotlib figure as PNG
simudir = pathlib.Path(__file__).absolute().parents[1]
datadir = simudir / 'output'

# Load forces from file and compute force coefficients.
filepath = datadir / 'forces-0.txt'
t, fx, fy = petibmpy.read_forces(filepath)
cd, cl = petibmpy.get_force_coefficients(fx, fy, coeff=2.0)

# Compute the time-averaged force coefficients.
time_limits = (50.0, 80.0)
cd_mean, cl_mean = petibmpy.get_time_averaged_values(t, cd, cl,
                                                     limits=time_limits)
print(f'Time limits: {time_limits}')
print(f'<CD> = {cd_mean}')
print(f'<CL> = {cl_mean}')

# Plot the history of the force coefficients.
pyplot.rc('font', family='serif', size=14)
fig, ax = pyplot.subplots(figsize=(8.0, 4.0))
ax.set_xlabel('Non-dimensional time')
ax.set_ylabel('Force coefficients')
ax.plot(t, cd, label='$C_D$')
ax.plot(t, cl, label='$C_L$')
ax.legend(loc='upper right', ncol=2, frameon=False)
ax.axis((t[0], t[-1], 0.0, 3.0))
fig.tight_layout()

if save_figure:
    # Save the figure as a PNG file.
    figdir = simudir / 'figures'
    figdir.mkdir(parents=True, exist_ok=True)
    filepath = figdir / 'force_coefficients.png'
    fig.savefig(filepath, dpi=300, bbox_inches='tight')

if show_figure:
    # Display the figure.
    pyplot.show()
