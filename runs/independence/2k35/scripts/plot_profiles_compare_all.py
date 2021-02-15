"""Plot vertical profiles of the velocity components and pressure."""

import h5py
from matplotlib import pyplot
import numpy
import pathlib

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
xlocs = [0.5, 1.0, 2.0, 3.0, 4.0, 5.0]

# Initialize data structures to store solution of profiles.
u_profiles, v_profiles, p_profiles = dict(), dict(), dict()
# Initialize dict to store keyword arguments for pyplot.plot.
plot_kwargs = dict()

labels = ['base', 'coarser_grid', 'finer_grid', 'finer_dt', 'atol',
          'larger_domain', 'markers', 'uniform']
for i, label in enumerate(labels):
    simudir = maindir / label
    u_profiles[label] = get_time_averaged_profiles(simudir, 'u', xlocs)
    v_profiles[label] = get_time_averaged_profiles(simudir, 'v', xlocs)
    p_profiles[label] = get_time_averaged_profiles(simudir, 'p', xlocs)
    plot_kwargs[label] = dict(color=f'C{i}')

# Set default font family and size for Matplotlib figures.
pyplot.rc('font', family='serif', size=12)

# Plot vertical profiles of the velocity components and pressure.
for name, x_offset in zip(['u', 'v', 'p'], [-1.0, 0.0, 0.0]):
    fig, ax = pyplot.subplots(figsize=(6.0, 5.0))
    ax.set_xlabel('x/c')
    ax.set_ylabel('y/c')
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
            label=None
    ax.legend(frameon=False, loc='upper left', prop=dict(size=10))
    ax.axis('scaled', adjustable='box')
    ax.axis((-2.0, 6.0, -3.0, 3.0))
    fig.tight_layout()
    # Add immersed body to the plot.
    filepath = maindir / 'base' / 'snake.body'
    body = petibmpy.read_body(filepath, skiprows=1)
    ax.fill(*body, color='black', alpha=0.5)

pyplot.show()
