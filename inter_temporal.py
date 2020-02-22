from practica_import import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def hora_a_seg(time):
    output = (time // 10000) * 3600 + ((time % 10000) // 100) * 60 + time % 100
    return output


def basecont(x, coef):
    output = coef[0] + x * coef[1] + x**2 * coef[2] + x**3 * coef[3] + x**4 * coef[4] + x**5 * coef[5]
    return output

int_temp08 = np.poly1d(np.polyfit(magBase08['medicion'], magBase08['valor'], 5))
int_temp08 = np.poly1d(np.polyfit(magBase08['medicion'], magBase08['valor'], 5))

var_diurna08 = base_efec08['valor'] - pd.Series.mean(base_efec08['valor'])
var_diurna09 = base_efec09['valor'] - pd.Series.mean(base_efec09['valor'])
var_diurna11 = base_efec11['valor'] - pd.Series.mean(base_efec11['valor'])
var_diurna12 = base_efec12['valor'] - pd.Series.mean(base_efec12['valor'])

int_diurna08 = np.poly1d(np.polyfit(base_efec08['medicion'], var_diurna08, 5))
int_diurna09 = np.poly1d(np.polyfit(base_efec09['medicion'], var_diurna09, 5))
int_diurna11 = np.poly1d(np.polyfit(base_efec11['medicion'], var_diurna11, 5))
int_diurna12 = np.poly1d(np.polyfit(base_efec12['medicion'], var_diurna12, 5))

#### FIGURAS ####

fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111)
ax1.plot(magBase08['medicion'], basecont(magBase08['medicion'], int_temp08))
ax1.plot(magBase08['medicion'], magBase08['valor'])

fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111)
ax2.plot(hora_a_seg(mag08['time']), mag08['nT'])
ax2.plot(hora_a_seg(base_efec08['hhmmss']), base_efec08['valor']/10)

fig3 = plt.figure(3)
ax3 = fig3.add_subplot(111)
ax3.plot(hora_a_seg(mag09['time']), mag09['nT'])
ax3.plot(hora_a_seg(base_efec09['hhmmss']), base_efec09['valor']/10)

fig4 = plt.figure(4)
ax4 = fig4.add_subplot(111)
ax4.plot(hora_a_seg(mag11['time']), mag11['nT'])
ax4.plot(hora_a_seg(base_efec11['hhmmss']), base_efec11['valor']/10)

fig5 = plt.figure(5)
ax5 = fig5.add_subplot(111)
ax5.plot(hora_a_seg(mag12['time']), mag12['nT'])
ax5.plot(hora_a_seg(base_efec12['hhmmss']), base_efec12['valor']/10)

fig6 = plt.figure(6)
ax6 = fig6.add_subplot(111)
#x_08 = np.arange(1499, 1609, 0.5)
ax6.plot(base_efec08['medicion'], var_diurna08 + pd.Series.mean(base_efec08['valor']) / 10, '.')
ax6.plot(base_efec08['medicion'], basecont(base_efec08['medicion'], int_diurna08) + pd.Series.mean(base_efec08['valor']) / 10)
x_06 = np.linspace(1499, 1609, len(mag08['nT']))
ax6.plot(x_06, mag08['nT'])
