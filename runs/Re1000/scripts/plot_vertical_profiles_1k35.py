"""Plot vertical profiles of the velocity components."""

import pathlib

import h5py
import numpy
from matplotlib import pyplot

import petibmpy


def get_time_values_hdf5(filepath, name):
    """Return time values of HDF5 datasets."""
    with h5py.File(filepath, 'r') as infile:
        times = [float(t_str) for t_str in list(infile[name].keys())[:-1]]
    return numpy.array(sorted(times))


def get_time_averaged_profile(filepath, name, xloc, time_limits):
    """Return the time-averaged vertical profile at given x-location."""
    # Get array of revelant time values.
    times = get_time_values_hdf5(filepath, name)
    mask = numpy.where((times >= time_limits[0]) &
                       (times <= time_limits[1]))[0]
    times = times[mask]
    # Load solution, interpolate at x-location, and time-average.
    probe = petibmpy.ProbeVolume(name, name)
    initialized = False
    for time in times:
        # Load solution from file.
        (x, y), vals_ = probe.read_hdf5(filepath, time)
        # Interpolate at x=xloc.
        vals_ = petibmpy.linear_interpolation(vals_.T, x, xloc)
        if not initialized:
            vals = vals_
            initialized = True
        else:
            vals += vals_
    vals /= times.size
    return dict(y=y, vals=vals)


def get_time_averaged_profiles(simudir, name, xlocs,
                               time_limits=(50.0, 80.0)):
    """Return time-averaged profiles at given x locations."""
    profiles = dict()
    datadir = simudir / 'output'
    for i, xloc in enumerate(xlocs):
        filepath = datadir / f'probe{i + 1}-{name}.h5'
        profile = get_time_averaged_profile(filepath, name, xloc, time_limits)
        profiles[xloc] = profile
    return profiles


# Set parameters.
maindir = pathlib.Path(__file__).absolute().parents[1]
xlocs = [0.5, 1.0, 2.0]
case = '1k35'

# Initialize data structures to store solution of profiles.
u_profiles, v_profiles, p_profiles = dict(), dict(), dict()
# Initialize dict to store keyword arguments for pyplot.plot.
plot_kwargs = dict()

# Get vertical profiles for section with both lips.
label = 'Both'
simudir = maindir / 'both_lips' / case
u_profiles[label] = get_time_averaged_profiles(simudir, 'u', xlocs)
v_profiles[label] = get_time_averaged_profiles(simudir, 'v', xlocs)
plot_kwargs[label] = dict(color='C0', linestyle='-')

# Get vertical profiles for section with front lip only.
label = 'Front'
simudir = maindir / 'front_lip' / case
u_profiles[label] = get_time_averaged_profiles(simudir, 'u', xlocs)
v_profiles[label] = get_time_averaged_profiles(simudir, 'v', xlocs)
plot_kwargs[label] = dict(color='C1', linestyle='-')

# Get vertical profiles for section with back lip only.
label = 'Back'
simudir = maindir / 'back_lip' / case
u_profiles[label] = get_time_averaged_profiles(simudir, 'u', xlocs)
v_profiles[label] = get_time_averaged_profiles(simudir, 'v', xlocs)
plot_kwargs[label] = dict(color='C2', linestyle='-')

# Get vertical profiles for section with no lips.
label = 'None'
simudir = maindir / 'no_lips' / case
u_profiles[label] = get_time_averaged_profiles(simudir, 'u', xlocs)
v_profiles[label] = get_time_averaged_profiles(simudir, 'v', xlocs)
plot_kwargs[label] = dict(color='C3', linestyle='-')

# Set default font family and size for Matplotlib figures.
pyplot.rc('font', family='serif', size=12)

# Plot vertical profiles of the velocity components.
for component in ('u', 'v'):
    fig, ax = pyplot.subplots(figsize=(6.0, 5.0))
    ax.set_xlabel('$x/c$')
    ax.set_ylabel('$y/c$')
    # Add guide lines.
    ax.vlines(xlocs, -2.0, 2.0, color='gray', linestyle=':')
    # Add vertical profiles at x locations.
    comp_profiles = eval(component + '_profiles')
    for label, profiles in comp_profiles.items():
        kwargs = plot_kwargs[label]
        for xloc, profile in profiles.items():
            if component == 'u':
                y, u = profile['y'], profile['vals']
                ax.plot(xloc + u - 1.0, y, label=label, **kwargs)
                text_content = '$<u> / U_\infty - 1$'
            else:  # v component
                y, v = profile['y'], profile['vals']
                ax.plot(xloc + v, y, label=label, **kwargs)
                text_content = '$<v> / U_\infty$'
            label = None
    ax.axis('scaled', adjustable='box')
    ax.axis((-2.0, 2.2, -2.0, 2.0))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.legend(frameon=False, loc='upper left', fontsize=12)
    ax.text(-1.8, -1.8, text_content, fontsize=14)
    fig.tight_layout()
    # Add immersed body to the plot.
    filepath = maindir / 'both_lips' / case / 'snake.body'
    body = petibmpy.read_body(filepath, skiprows=1)
    ax.fill(*body, color='black', alpha=0.5)
    # Save figure as PNG.
    figdir = maindir / 'figures'
    figdir.mkdir(parents=True, exist_ok=True)
    filepath = figdir / f'{component}_profiles_{case}.png'
    fig.savefig(filepath, dpi=300, bbox_inches='tight')

pyplot.show()
