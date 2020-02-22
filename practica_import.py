####Importacion de Datos usando la librería Pandas de Python para leer archivos txt####

import numpy as np
import pandas as pd
import datetime

mag07 = pd.read_csv('DatMagPractica/mag_07_12_19', header=8)
mag09 = pd.read_csv('DatMagPractica/mag_08_12_19', header=8)
mag08 = pd.read_csv('DatMagPractica/mag_09_12_19', header=8)
mag11 = pd.read_csv('DatMagPractica/mag_11_12_19', header=8)
mag12 = pd.read_csv('DatMagPractica/mag_12_12_19', header=8)
magBase = pd.read_csv('DatMagPractica/MagBaseDic2019.stn', header=0)

lat08 = mag08['/lat'][1:].astype(float)
lon08 = mag08['lon'][1:].astype(float)
val08 = mag08['nT'][1:].astype(float)

lat09 = mag09['lat'][1:].astype(float)
lon09 = mag09['lon'][1:].astype(float)
val09 = mag09['nT'][1:].astype(float)

lat11 = mag11['/lat'][1:].astype(float)
lon11 = mag11['lon'][1:].astype(float)
val11 = mag11['nT'][1:].astype(float)

lat12 = mag12['/lat'][1:].astype(float)
lon12 = mag12['lon'][1:].astype(float)
val12 = mag12['nT'][1:].astype(float)

# grilla_lon = lon08.append(lon09)
# grilla_lat = lat08.append(lat09)
# grilla_val = val08.append(val09)

magBase07 = magBase[1215:1340].astype(float)
magBase08 = magBase[1341:1662].astype(float)
magBase09 = magBase[1663:1959].astype(float)
magBase11 = magBase[1960:2195].astype(float)
magBase12 = magBase[2196:2373].astype(float)

base_efec08 = magBase[1499:1610].astype(float)
base_efec09 = magBase[1777:1904].astype(float)
base_efec11 = magBase[2001:2136].astype(float)
base_efec12 = magBase[2225:2290].astype(float)

