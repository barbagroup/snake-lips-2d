"""Plot the modified cross-sections side by side (with angle of attack)."""

from matplotlib import pyplot
import pathlib

import petibmpy


show_figure = True  # display the Matplotlib figure
save_figure = True  # save the figure as PDF
maindir = pathlib.Path(__file__).absolute().parents[1]

# Load coordinates of the sections from files.
aoa = 35.0  # angle of attack
data = {}
tags = ['bothlips', 'nobacklip', 'nofrontlip', 'nolips']
for tag in tags:
    filepath = maindir / f'snake_{tag}.txt'
    x, y = petibmpy.read_body(filepath)
    x, y = petibmpy.rotate2d(x, y, angle=-aoa)
    data[tag] = (x, y)

# Plot the modified and rotated cross-sections.
pyplot.rc('font', family='serif', size=16)
fig, ax = pyplot.subplots(figsize=(10.0, 4.0))
x_ref, y_ref = data['bothlips']
for i, coords in enumerate(data.values()):
    x, y = coords
    x += i
    x_ref_ = x_ref + i
    ax.plot(x_ref_, y_ref, color='black', linestyle='--')
    ax.plot(x, y, color='black', linewidth=2)
ax.axis('scaled')
ax.axis('off')
fig.tight_layout()

if show_figure:
    # Display the Matplotlib figure.
    pyplot.show()

if save_figure:
    # Save the figure as PDF.
    figdir = maindir / 'figures'
    figdir.mkdir(parents=True, exist_ok=True)
    filepath = figdir / f'modified_sections_aoa{round(aoa)}.pdf'
    fig.savefig(filepath, dpi=300, bbox_inches='tight')
    filepath = figdir / f'modified_sections_aoa{round(aoa)}.png'
    fig.savefig(filepath, dpi=300, bbox_inches='tight')
