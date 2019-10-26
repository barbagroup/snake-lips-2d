"""Get snake cross-section from FigShare and plot geometry."""

from matplotlib import pyplot
import numpy
import pathlib
import urllib.request

scriptdir = pathlib.Path(__file__).absolute().parent
rootdir = scriptdir.parent

# Get geometry from FigShare.
filename = pathlib.Path('snakeFigshare.txt')
url = 'https://ndownloader.figshare.com/files/3088811'
urllib.request.urlretrieve(url, str(filename))
with open(filename, 'r') as infile:
    coords = numpy.loadtxt(infile, dtype=numpy.float64, unpack=True)
filename.unlink()

# Plot the geometry.
pyplot.rc('font', family='serif', size=12)
fig, ax = pyplot.subplots(figsize=(6.0, 3.0))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(*coords, linewidth=2, linestyle='-')
ax.set_xlim(-15.0, 15.0)
ax.set_ylim(-4.0, 7.0)
ax.axis('scaled', adjustable='box')
fig.tight_layout()

pyplot.show()

# Save the figure as a PNG file.
figdir = rootdir / 'figures'
figdir.mkdir(parents=True, exist_ok=True)
filepath = figdir / 'snake_figshare.png'
fig.savefig(filepath, dpi=300, bbox_inches='tight')
