import geopandas
import matplotlib.pyplot as plt

world_file = geopandas.datasets.get_path("naturalearth_lowres")
world = geopandas.read_file(world_file)
cities_file = geopandas.datasets.get_path("naturalearth_cities")
cities = geopandas.read_file(cities_file)
base = world.plot(color="green")
cities.plot(ax=base, color="blue", markersize=3)
plt.show()
