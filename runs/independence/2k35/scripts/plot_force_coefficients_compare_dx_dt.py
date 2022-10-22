"""Plot the history of the force coefficients, comparing multiple solutions."""

import collections
from matplotlib import pyplot
import numpy
import pathlib

import petibmpy


Solution = collections.namedtuple('Solution', ['t', 'cd', 'cl'])


def get_force_coefficients(simudir):
    """Load forces from file and return force coefficients."""
    datadir = simudir / 'output'
    filepath = datadir / 'forces-0.txt'
    t, fx, fy = petibmpy.read_forces(filepath)
    cd, cl = petibmpy.get_force_coefficients(fx, fy, coeff=2.0)
    return Solution(t, cd, cl)


def get_force_coefficients_krishnan_et_al_2014(datadir):
    """Load forces from file and return force coefficients."""
    filepath = datadir / 'krishnan_et_al_2014_forces_2k35.txt'
    t, fx, fy = petibmpy.read_forces(filepath)
    cd, cl = petibmpy.get_force_coefficients(fx, fy, coeff=2.0)
    return Solution(t, cd, cl)


def get_time_averaged_stats(solution, limits):
    mask = numpy.where((solution.t >= limits[0]) & (solution.t <= limits[1]))
    return Solution(limits,
                    numpy.mean(solution.cd[mask]),
                    numpy.mean(solution.cl[mask]))


# Set parameters.
show_figure = True  # display Matplotlib figure
save_figure = True  # save Matplotlib figure as PNG
maindir = pathlib.Path(__file__).absolute().parents[1]

# Initialize data structures to store solutions and mean quantities.
solutions, means = dict(), dict()
# Initialize dict to store keyword arguments for pyplot.plot.
plot_kwargs = dict()

# Set time limits to compute statistics about force coefficients.
time_limits = (50.0, 80.0)

# Load solution obtained on nominal grid (dx=0.004, dt=0.0004).
label = 'Base case'
simudir = maindir / 'base'
solution = get_force_coefficients(simudir)
mean = get_time_averaged_stats(solution, time_limits)
solutions[label], means[label] = solution, mean
plot_kwargs[label] = dict(color='black', linestyle='-')

# Load solution obtained on nominal grid with smaller dt (dt=0.0002).
label = 'Finer in time'
simudir = maindir / 'finer_dt'
solution = get_force_coefficients(simudir)
mean = get_time_averaged_stats(solution, time_limits)
solutions[label], means[label] = solution, mean
plot_kwargs[label] = dict(color='C1', linestyle='--')

# Load solution obtained on finer grid (dx=0.002).
label = 'Finer in space'
simudir = maindir / 'finer_grid'
solution = get_force_coefficients(simudir)
mean = get_time_averaged_stats(solution, time_limits)
solutions[label], means[label] = solution, mean
plot_kwargs[label] = dict(color='C0', linestyle='-.')

# Load solution obtained on coarser grid (dx=0.008).
# label = 'Coarser in space'
# simudir = maindir / 'coarser_grid'
# solution = get_force_coefficients(simudir)
# mean = get_time_averaged_stats(solution, time_limits)
# solutions[label], means[label] = solution, mean
# plot_kwargs[label] = dict(color='red', linestyle='-')

# Load solution from Krishnan et al. (2014).
label = 'Krishnan et al. (2014)'
datadir = maindir / 'data'
solution = get_force_coefficients_krishnan_et_al_2014(datadir)
mean = get_time_averaged_stats(solution, time_limits)
solutions[label], means[label] = solution, mean
plot_kwargs[label] = dict(color='gray', linestyle='-', linewidth=0.75)

# Print mean quantities.
print('Case\tTime-limits\t<C_D>\t<C_L>')
print('----\t-----------\t-----\t-----')
for label, mean in means.items():
    print(f'{label}\t{mean.t}\t{mean.cd:.4f}\t{mean.cl:.4f}')

# Set default font family and size for Matplotlib figures.
pyplot.rc('font', family='serif', size=14)

# Plot the history of the force coefficients.
fig, (ax1, ax2) = pyplot.subplots(nrows=2, figsize=(8.0, 6.0), sharex=True)
# Drag coefficient.
ax1.set_ylabel('Drag coefficient')
for label, solution in solutions.items():
    ax1.plot(solution.t, solution.cd, label=label, **plot_kwargs[label])
ax1.legend(loc='upper right', ncol=2, frameon=False)
ax1.axis((20.0, 80.0, 0.5, 2.0))
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
# Lift coefficient.
ax2.set_xlabel('Non-dimensional time')
ax2.set_ylabel('Lift coefficient')
for label, solution in solutions.items():
    ax2.plot(solution.t, solution.cl, label=label, **plot_kwargs[label])
ax2.axis((20.0, 80.0, 0.5, 3.0))
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
fig.tight_layout()

if save_figure:
    # Save the figure as a PNG file.
    figdir = maindir / 'figures'
    figdir.mkdir(parents=True, exist_ok=True)
    filepath = figdir / 'force_coefficients_compare_dx_dt.png'
    fig.savefig(filepath, dpi=300, bbox_inches='tight')

if show_figure:
    # Display the figure.
    pyplot.show()
