import matplotlib.pyplot as plt
import numpy as np
from geopy.geocoders import Nominatim

from pykrige.uk import UniversalKriging

geolocator = Nominatim(user_agent="vogu_basyan_kriging")

data = np.empty((0, 3))

address = ''
while address != '.':
    address = input()
    addressGeoCode = geolocator.geocode(address)
    if addressGeoCode:
        # получение широны и долготы точки
        newDataElement = np.array([addressGeoCode.latitude, addressGeoCode.longitude, np.random.uniform(low=0.0, high=0.1)])
        data = np.vstack([data, newDataElement])


# шиорта - координата x, максимум 90
gridx = np.arange(0.0, 90.0, 1.5)
# долгота - координата y, максимум 189
gridy = np.arange(0.0, 180.0, 1.5)

UK = UniversalKriging(
    data[:, 0],
    data[:, 1],
    data[:, 2],
    variogram_model="linear",
    drift_terms=["regional_linear"],
)
z, ss = UK.execute("grid", gridx, gridy)
plt.imshow(z)
plt.show()
