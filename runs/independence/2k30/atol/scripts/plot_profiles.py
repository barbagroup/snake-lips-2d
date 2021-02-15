"""Plot vertical profiles of the velocity components and pressure."""

from matplotlib import pyplot
import numpy
import pathlib

import petibmpy


# Set directories.
simudir = pathlib.Path(__file__).absolute().parents[1]
datadir = simudir / 'output'
figdir = simudir / 'figures'
figdir.mkdir(parents=True, exist_ok=True)

xlocs = [0.5, 1.0, 2.0, 3.0, 4.0, 5.0]
ylim = (-3.0, 3.0)
times = numpy.arange(50.0, 80.0 + 1, 4.0)

names = ['u', 'v', 'p']
mean_vals = [1.0, 0.0, 0.0]

pyplot.rc('font', family='serif', size=14)
for name, mean_val in zip(names, mean_vals):
    fig, ax = pyplot.subplots(figsize=(6.0, 5.0))
    ax.set_xlabel('x/c')
    ax.set_ylabel('y/c')
    for i, xloc in enumerate(xlocs):
        filepath = datadir / f'probe{i + 1}-{name}.h5'
        probe = petibmpy.ProbeVolume(name, name)
        for j, time in enumerate(times):
            (x, y), d = probe.read_hdf5(filepath, time)
            d = petibmpy.linear_interpolation(d.T, x, xloc)
            if j == 0:
                data = d
            else:
                data += d
        data /= times.size
        ax.axvline(xloc, color='gray', linestyle=':')
        ax.plot(xloc + data - mean_val, y, color='C0')
    # Add immersed boundary to the plot.
    filepath = simudir / 'snake.body'
    body = petibmpy.read_body(filepath, skiprows=1)
    ax.fill(*body, color='black', alpha=0.6)
    ax.axis('scaled', adjustable='box')
    ax.axis((-2.0, 6.0, *ylim))
    fig.tight_layout()
    filepath = figdir / f'{name}_profiles.png'
    fig.savefig(filepath, dpi=300, bbox_inches='tight')

pyplot.show()
