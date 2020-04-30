"""Generate the modified cross-sections of the gliding snake."""

from matplotlib import pyplot
import numpy
import os
import pathlib
import urllib.request


class Point2D(object):
    """Structure to store the coordinates of a point in 2D."""

    def __init__(self, x, y):
        """Set coordinates of the point."""
        self.x, self.y = x, y

    def __repr__(self):
        """Return the representation of the object."""
        return f'Point2D({self.x}, {self.y})'

    def distance(self, point):
        """Compute the distance to another point."""
        return numpy.sqrt((point.x - self.x)**2 + (point.y - self.y)**2)


class Curve2D(object):
    """Structure to store the coordinates of a 2D curve."""

    def __init__(self, x, y):
        """Set coordinates of the curve."""
        self.x, self.y = x, y
        self.size = x.size
        self.start, self.end = Point2D(x[0], y[0]), Point2D(x[-1], y[-1])
        self.length = numpy.sum(numpy.sqrt((x[1:] - x[:-1])**2 +
                                           (y[1:] - y[:-1])**2))

    def __repr__(self):
        """Return the representation of the object."""
        return (f'Curve2D(start={self.start},\n' +
                f'        end={self.end},\n' +
                f'        size={self.size},\n' +
                f'        length={self.length})')

    def point(self, i):
        """Return the point of the curve with index i."""
        return Point2D(self.x[i], self.y[i])

    def find_index(self, point):
        """Find index of point in the curve."""
        for i, (xi, yi) in enumerate(zip(self.x, self.y)):
            if xi == point.x and yi == point.y:
                return i

    def apply_mask(self, mask):
        """Apply a mask to return a new 2D curve."""
        return Curve2D(self.x[mask], self.y[mask])

    def view(self, start=0, end=None, stride=1):
        """Return a sub part of the curve."""
        if end is None:
            end = self.size
        return Curve2D(self.x[start:end:stride],
                       self.y[start:end:stride])

    def append(self, curves):
        """Return a new extended curve."""
        if not hasattr(curves, '__iter__'):
            curves = [curves]
        return Curve2D(numpy.concatenate((self.x, *(c.x for c in curves))),
                       numpy.concatenate((self.y, *(c.y for c in curves))))

    def cumsum_lengths(self):
        """Return cumulated sum of distances along the curve."""
        lengths = numpy.sqrt((self.x[1:] - self.x[:-1])**2 +
                             (self.y[1:] - self.y[:-1])**2)
        return numpy.cumsum(numpy.insert(lengths, 0, 0.0))

    def rotate(self, center=Point2D(0.0, 0.0), theta=0.0):
        """Rotate the curve."""
        x = center.x + ((self.x - center.x) * numpy.cos(theta) -
                        (self.y - center.y) * numpy.sin(theta))
        y = center.y + ((self.x - center.x) * numpy.sin(theta) -
                        (self.y - center.y) * numpy.cos(theta))
        self.x = x
        self.y = y

    def reverse(self):
        """Reverse the curve."""
        self.x, self.y = self.x[::-1], self.y[::-1]
        self.start, self.end = Point2D(x[0], y[0]), Point2D(x[-1], y[-1])


class Circle2D(Curve2D):
    """Structure to store the coordinates of a 2D circle."""

    def __init__(self, center, R, num=50):
        """Create the circle."""
        self.center = center
        self.R = R
        theta = numpy.linspace(0.0, 2 * numpy.pi, num=num)[:-1]
        super().__init__(center.x + R * numpy.cos(theta),
                         center.y + R * numpy.sin(theta))

    def __repr__(self):
        """Return the representation of the object."""
        return (f'Circle2D(R={self.R},\n' +
                f'         center={self.center},\n' +
                f'         size={self.size})')


class Line2D(Curve2D):
    """Structure to store the coordinates of a 2D line."""

    def __init__(self, point1, point2, num=50):
        """Create the line between two given points."""
        super().__init__(numpy.linspace(point1.x, point2.x, num=num),
                         numpy.linspace(point1.y, point2.y, num=num))

    def __repr__(self):
        """Return the representation of the object."""
        return (f'Line2D(start={self.start},\n' +
                f'       end={self.end},\n' +
                f'       size={self.size},\n' +
                f'       length={self.length})')


def reshape_lip(curve, reverse=False):
    """Reshape a lip of the cross-section.

    We replace the lip with an circular arc followed by a straight section.

    Parameters
    ----------
    curve : Curve2D
        2D curve of the original lip.
    reverse : bool
        Set to True if the lip coordinates start from the upper surface
        of the snake cross-section to finish in the lower surface;
        default: False.

    Returns
    -------
    Curve2D
        2D curve of the modified lip.

    """
    s = -1 if reverse else 1
    curve = Curve2D(s * curve.x[::s], curve.y[::s])
    start, end = curve.point(1), curve.end
    prev = curve.start
    # Find the intersection between the line (`prev`, `start`)
    # and horizontal line passing by `end`.
    inters = Point2D(start.x +
                     (end.y - start.y) / (start.y - prev.y) *
                     (start.x - prev.x),
                     end.y)
    # Compute distance (`start`, `inters`).
    L = start.distance(inters)
    # Compute intermediate point at distance `L` of `inters`
    # on the horizontal line.
    interm = Point2D(inters.x + L, end.y)
    # Compute the center of the circle with radius R,
    # passing by `start` and `interm` points,
    # such that lines (`prev`, `start`) and (`interm`, `end`) are tangents
    # to the circle, and such that the center and the intermediate points
    # have the same x-coord. (Using Pythagorean theorem.)
    center = Point2D(interm.x,
                     ((start.x - interm.x)**2 + start.y**2 - interm.y**2) /
                     (2 * (start.y - interm.y)))
    # Create the circle.
    R = center.y - end.y
    circle = Circle2D(center, R)
    # Keep arc that will define the retracted lip.
    arc = circle.apply_mask((circle.x < center.x) & (circle.y < start.y))
    # Create horizontal line between intermediate and end points.
    num = 10
    hline = Curve2D(numpy.linspace(center.x, end.x, num=num),
                    numpy.full(num, end.y))
    # Concatenate curves to form the modified lip.
    start_line = Line2D(prev, start, num=2)
    end_line = Line2D(Point2D(center.x, end.y), end, num=2)
    lip = start_line.append([arc, end_line])
    return Curve2D(s * lip.x[::s], lip.y[::s])


def truncate_curve(curve0, start, target_length, reverse=False):
    """Return a truncated curve based on a target distance (along the curve).

    The last point for the new curve is interpolated.

    Parameters
    ----------
    curve0 : Curve2D
        2D curve to truncate.
    start : Point2D
        Starting point along the curve.
    target_length : float
        Target length of the new curve.
    reverse : bool
        If True, reverse the curve before truncating it; default: False.

    Returns
    -------
    Curve2D
        The truncated curve with given length.
    int
        Index of the last point that belongs the both curves
        (one before interpolation).

    """
    if reverse:
        curve0.reverse()
    idx = curve0.find_index(start)
    curve = Curve2D(curve0.x[idx:], curve0.y[idx:])
    # Compute cumulated distances.
    cumsum_lengths = curve.cumsum_lengths()
    # Find cutoff index
    index = numpy.where(cumsum_lengths < target_length)[0][-1]
    p1 = curve.point(index)
    p2 = curve.point(index + 1)
    # Get remaining distance to add.
    extra_length = target_length - cumsum_lengths[index]
    # Compute the first ignored distance.
    next_length = cumsum_lengths[index + 1] - cumsum_lengths[index]
    # Interpolation.
    pi = Point2D(p1.x + extra_length / next_length * (p2.x - p1.x),
                 p1.y + extra_length / next_length * (p2.y - p1.y))
    # Keep section of interest.
    curve = Curve2D(numpy.concatenate((curve.x[:index + 1], [pi.x])),
                    numpy.concatenate((curve.y[:index + 1], [pi.y])))
    assert(abs(curve.length - target_length) < 1e-12)
    if reverse:
        curve0.reverse()
        curve.reverse()
    return curve, curve0.find_index(p1)


scriptdir = pathlib.Path(__file__).absolute().parent
rootdir = scriptdir.parent

# Get geometry from FigShare.
filename = pathlib.Path('snakeFigshare.txt')
url = 'https://ndownloader.figshare.com/files/3088811'
urllib.request.urlretrieve(url, filename)
with open(filename, 'r') as infile:
    x, y = numpy.loadtxt(infile, dtype=numpy.float64, unpack=True)
filename.unlink()

snakes = {}

# Scale the cross-section to have a chord-length of 1.0.
chord = x.max() - x.min()
x /= chord
y /= chord
chord = x.max() - x.min()
# Center the geometry at point (0, 0).
x -= (x.max() + x.min()) / 2
y -= (y.max() + y.min()) / 2
snake = Curve2D(x, y)

# Find the tip of the front lip.
curve = snake.apply_mask(snake.x < 0.0)
tip = curve.point(numpy.argmin(curve.y))
tip_idx = snake.find_index(tip)
# Decision: lip starts at 15% of the chord length from the tip
# along the upper surface.
target_length = 0.25 * chord
curve1, index1 = truncate_curve(snake, tip, target_length, reverse=True)
# Decision: lip ends at 25% of the chord length from the tip
# along the lower surface.
target_length = 0.25 * chord
curve2, index2 = truncate_curve(snake, tip, target_length)
# Grab the front lip and reshape it.
front = curve1.append(curve2)
front_mod = reshape_lip(front)

# Generate cross-section with no front lip.
section1 = snake.view(end=index1)
after = snake.view(start=index2 + 1)
nofront = section1.append([front_mod, after])

# Find the tip of the back lip.
curve = snake.apply_mask(snake.x > 0.0)
tip = curve.point(numpy.argmin(curve.y))
tip_idx = snake.find_index(tip)
# Decision: lip starts at 25% of the chord length from the tip
# along the lower surface.
target_length = 0.25 * chord
curve3, index3 = truncate_curve(snake, tip, target_length, reverse=True)
# Decision: lip ends at 25% of the chord length from the tip
# along the upper surface.
target_length = 0.25 * chord
curve4, index4 = truncate_curve(snake, tip, target_length)
# Grab the back lip and reshape it.
back = curve3.append(curve4)
back_mod = reshape_lip(back, reverse=True)

# Generate cross-section with no front lip.
before = snake.view(end=index3)
section3 = snake.view(start=index4 + 1)
noback = before.append([back_mod, section3])

# Generate cross-section missing both lips.
before = snake.view(end=index1)
interm = snake.view(start=index2 + 1, end=index3)
after = snake.view(start=index4 + 1)
nolips = before.append([front_mod, interm, back_mod, after])

# Save coordinates of modified cross-sections into files
geometries = [snake, nofront, noback, nolips]
filenames = ['snake_bothlips.txt', 'snake_nofrontlip.txt',
             'snake_nobacklip.txt', 'snake_nolips.txt']
for filename, geometry in zip(filenames, geometries):
    filepath = rootdir / filename
    with open(filepath, 'wb') as outfile:
        numpy.savetxt(outfile, numpy.c_[geometry.x, geometry.y],
                      header='{} points'.format(geometry.size))

# Plot the geometries.
pyplot.rc('font', family='serif', size=12)
fig, ax = pyplot.subplots(figsize=(6.0, 6.0))
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.plot(snake.x, snake.y, label='both lips', color='black', linestyle='-')
ax.plot(nofront.x, nofront.y, label='no front lip', linestyle='-.')
ax.plot(noback.x, noback.y, label='no back lip', linestyle='--')
ax.plot(nolips.x, nolips.y, label='no lips', linestyle=':')
ax.legend(loc='best', frameon=False)
ax.axis('scaled', adjustable='box')
fig.tight_layout()
pyplot.show()
