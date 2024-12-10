import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, RegularPolygon
from matplotlib.path import Path
from matplotlib.projections.polar import PolarAxes
from matplotlib.projections import register_projection
from matplotlib.spines import Spine
from matplotlib.transforms import Affine2D

def radar_factory(num_vars, frame='circle'):
    theta = np.linspace(0, 2 * np.pi, num_vars, endpoint=False)
    
    class RadarTransform(PolarAxes.PolarTransform):
        def transform_path_non_affine(self, path):
            if path._interpolation_steps > 1:
                path = path.interpolated(num_vars)
            return Path(self.transform(path.vertices), path.codes)

    class RadarAxes(PolarAxes):
        name = 'radar'
        PolarTransform = RadarTransform

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.set_theta_zero_location('N')
            self.set_ylim(0, 255)  # Set a predefined scale with a maximum of 255

        def fill(self, *args, closed=True, **kwargs):
            return super().fill(closed=closed, *args, **kwargs)

        def plot(self, *args, **kwargs):
            lines = super().plot(*args, **kwargs)
            for line in lines:
                self._close_line(line)

        def _close_line(self, line):
            x, y = line.get_data()
            if x[0] != x[-1]:
                x = np.concatenate((x, [x[0]]))
                y = np.concatenate((y, [y[0]]))
                line.set_data(x, y)

        def set_varlabels(self, labels):
            self.set_thetagrids(np.degrees(theta), labels)

        def _gen_axes_patch(self):
            if frame == 'circle':
                return Circle((0.5, 0.5), 0.5)
            elif frame == 'polygon':
                return RegularPolygon((0.5, 0.5), num_vars, radius=0.5, edgecolor="k")
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

        def draw(self, renderer):
            if frame == 'polygon':
                gridlines = self.yaxis.get_gridlines()
                for gl in gridlines:
                    gl.get_path()._interpolation_steps = num_vars
            super().draw(renderer)

        def _gen_axes_spines(self):
            if frame == 'circle':
                return super()._gen_axes_spines()
            elif frame == 'polygon':
                spine = Spine(axes=self, spine_type='circle', path=Path.unit_regular_polygon(num_vars))
                spine.set_transform(Affine2D().scale(.5).translate(.5, .5) + self.transAxes)
                return {'polar': spine}
            else:
                raise ValueError("unknown value for 'frame': %s" % frame)

    register_projection(RadarAxes)
    return theta

def getPokemonStats():
    pokedex = int(input("Inserisci il numero di pokedex: "))
    with open('data/csv/pokemon_not_complete.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for index, values in enumerate(csv_reader):
            if index == pokedex:
                # 8 hp, 5 attack, 6 difense, 7 sp attack, 4 sp difense, 9 speed 
                print(index, values[1], values[8], values[5], values[6], values[7], values[4], values[9])
                return values[1], [int(values[8]), int(values[5]), int(values[6]), int(values[7]), int(values[4]), int(values[9])]

data = []
data.append(getPokemonStats())
data.append(getPokemonStats())

spoke_labels = ['special defense', 'attack', 'defense', 'special attack', 'hp', 'speed']
N = len(spoke_labels)
theta = radar_factory(N, frame='polygon')

fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(projection='radar'))
fig.subplots_adjust(top=0.85, bottom=0.05)
ax.set_title(f"Statistiche linea evolutiva di {data[0][0].capitalize()}", position=(0.5, 1.1), ha='center')

for name, stats in data:
    ax.plot(theta, stats, label=name.capitalize())
    ax.fill(theta, stats, alpha=0.25)

ax.set_varlabels(spoke_labels)
ax.legend(loc='upper right', bbox_to_anchor=(1.1, 1.1))

plt.show()