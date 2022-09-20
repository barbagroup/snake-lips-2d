"""Plot vertical profiles of the velocity components and pressure."""

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

# Initialize data structures to store solution of profiles.
u_profiles, v_profiles, p_profiles = dict(), dict(), dict()
# Initialize dict to store keyword arguments for pyplot.plot.
plot_kwargs = dict()

# Get vertical profiles for section with both lips.
label = 'Both'
simudir = maindir / 'both_lips' / '1k35'
u_profiles[label] = get_time_averaged_profiles(simudir, 'u', xlocs)
v_profiles[label] = get_time_averaged_profiles(simudir, 'v', xlocs)
p_profiles[label] = get_time_averaged_profiles(simudir, 'p', xlocs)
plot_kwargs[label] = dict(color='C0', linestyle='-')

# Get vertical profiles for section with front lip only.
label = 'Front'
simudir = maindir / 'front_lip' / '1k35'
u_profiles[label] = get_time_averaged_profiles(simudir, 'u', xlocs)
v_profiles[label] = get_time_averaged_profiles(simudir, 'v', xlocs)
p_profiles[label] = get_time_averaged_profiles(simudir, 'p', xlocs)
plot_kwargs[label] = dict(color='C1', linestyle='-')

# Get vertical profiles for section with back lip only.
label = 'Back'
simudir = maindir / 'back_lip' / '1k35'
u_profiles[label] = get_time_averaged_profiles(simudir, 'u', xlocs)
v_profiles[label] = get_time_averaged_profiles(simudir, 'v', xlocs)
p_profiles[label] = get_time_averaged_profiles(simudir, 'p', xlocs)
plot_kwargs[label] = dict(color='C2', linestyle='-')

# Get vertical profiles for section with no lips.
label = 'None'
simudir = maindir / 'no_lips' / '1k35'
u_profiles[label] = get_time_averaged_profiles(simudir, 'u', xlocs)
v_profiles[label] = get_time_averaged_profiles(simudir, 'v', xlocs)
p_profiles[label] = get_time_averaged_profiles(simudir, 'p', xlocs)
plot_kwargs[label] = dict(color='C3', linestyle='-')

# Set default font family and size for Matplotlib figures.
pyplot.rc('font', family='serif', size=12)

# Plot vertical profiles of the velocity components and pressure.
for name, x_offset in zip(['u', 'v', 'p'], [-1.0, 0.0, 0.0]):
    fig, ax = pyplot.subplots(figsize=(6.0, 5.0))
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    # Add guide lines.
    for xloc in xlocs:
        ax.axvline(xloc, color='gray', linestyle=':')
    # Add vertical profiles at x locations.
    var_profiles = eval(name + '_profiles')
    for i, (label, profiles) in enumerate(var_profiles.items()):
        kwargs = plot_kwargs[label]
        for xloc, profile in profiles.items():
            ax.plot(xloc + profile['vals'] + x_offset, profile['y'],
                    label=label, **kwargs)
            label = None
    ax.legend(frameon=False, loc='upper left', prop=dict(size=10))
    ax.axis('scaled', adjustable='box')
    ax.axis((-2.0, 2.1, -2.0, 2.0))
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    fig.tight_layout()
    # Add immersed body to the plot.
    filepath = maindir / 'both_lips' / '1k35' / 'snake.body'
    body = petibmpy.read_body(filepath, skiprows=1)
    ax.fill(*body, color='black', alpha=0.5)
    # Save figure as PNG.
    figdir = maindir / 'figures'
    figdir.mkdir(parents=True, exist_ok=True)
    filepath = figdir / f'{name}_profiles_1k35.png'
    fig.savefig(filepath, dpi=300, bbox_inches='tight')

pyplot.show()
