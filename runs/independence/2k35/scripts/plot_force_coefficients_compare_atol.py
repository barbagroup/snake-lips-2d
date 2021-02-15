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

# Load solution obtained on base grid.
label = 'Nominal ($atol = 10^{-6}$)'
simudir = maindir / 'base'
solution = get_force_coefficients(simudir)
mean = get_time_averaged_stats(solution, (50.0, 80.0))
solutions[label], means[label] = solution, mean
plot_kwargs[label] = dict(color='black', linestyle='-')

# Load solution obtained on coarser grid.
label = 'Tighter solvers ($atol = 10^{-9}$)'
simudir = maindir / 'atol'
solution = get_force_coefficients(simudir)
mean = get_time_averaged_stats(solution, (50.0, 80.0))
solutions[label], means[label] = solution, mean
plot_kwargs[label] = dict(color='C0', linestyle='--')

# Print mean quantities.
print('Case\tTime-limits\t<C_D>\t<C_L>')
print('----\t-----------\t-----\t-----')
for label, mean in means.items():
    print(f'{label}\t{mean.t}\t{mean.cd:.4f}\t{mean.cl:.4f}')

# Set default font family and size for Matplotlib figures.
pyplot.rc('font', family='serif', size=14)

# Plot the history of the force coefficients.
fig, ax = pyplot.subplots(figsize=(8.0, 4.0))
ax.set_xlabel('Non-dimensional time')
ax.set_ylabel('Force coefficients')
for label, solution in solutions.items():
    ax.plot(solution.t, solution.cd, label=label, **plot_kwargs[label])
    ax.plot(solution.t, solution.cl, **plot_kwargs[label])
ax.legend(loc='lower right', ncol=1, frameon=False)
ax.axis((0.0, 80.0, 0.0, 3.0))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.annotate('$C_D$', xy=(30.0, 0.90), xytext=(20.0, 0.25),
            arrowprops=dict(facecolor='black', arrowstyle='-|>',
                            shrinkA=0, shrinkB=0))
ax.annotate('$C_L$', xy=(50.0, 2.40), xytext=(40.0, 2.75),
            arrowprops=dict(facecolor='black', arrowstyle='-|>',
                            shrinkA=0, shrinkB=0))
fig.tight_layout()

if save_figure:
    # Save the figure as a PNG file.
    figdir = maindir / 'figures'
    figdir.mkdir(parents=True, exist_ok=True)
    filepath = figdir / 'force_coefficients_compare_atol.png'
    fig.savefig(filepath, dpi=300, bbox_inches='tight')

if show_figure:
    # Display the figure.
    pyplot.show()
