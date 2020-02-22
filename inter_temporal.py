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

var_diurna08 = base_efec08['valor'] - pd.Series.mean(base_efec08['valor'])
var_diurna09 = base_efec09['valor'] - pd.Series.mean(base_efec09['valor'])
var_diurna11 = base_efec11['valor'] - pd.Series.mean(base_efec11['valor'])
var_diurna12 = base_efec12['valor'] - pd.Series.mean(base_efec12['valor'])

seg_magBase08 = hora_a_seg(base_efec08['hhmmss'])
seg_magBase09 = hora_a_seg(base_efec09['hhmmss'])
seg_magBase11 = hora_a_seg(base_efec11['hhmmss'])
seg_magBase12 = hora_a_seg(base_efec12['hhmmss'])

seg_mag08 = hora_a_seg(mag08['time'])
seg_mag09 = hora_a_seg(mag09['time'])
seg_mag11 = hora_a_seg(mag11['time'])
seg_mag12 = hora_a_seg(mag12['time'])

int_diurna08 = np.poly1d(np.polyfit(seg_magBase08, var_diurna08, 5))
int_diurna09 = np.poly1d(np.polyfit(seg_magBase09, var_diurna09, 5))
int_diurna11 = np.poly1d(np.polyfit(seg_magBase11, var_diurna11, 5))
int_diurna12 = np.poly1d(np.polyfit(seg_magBase12, var_diurna12, 5))

#### FIGURAS ####

# fig1 = plt.figure(1)
# ax1 = fig1.add_subplot(111)
# ax1.plot(magBase08['medicion'], basecont(magBase08['medicion'], int_temp08))
# ax1.plot(magBase08['medicion'], magBase08['valor'])
#
# fig2 = plt.figure(2)
# ax2 = fig2.add_subplot(111)
# ax2.plot(hora_a_seg(mag08['time']), mag08['nT'])
# ax2.plot(hora_a_seg(base_efec08['hhmmss']), base_efec08['valor']/10)
#
# fig3 = plt.figure(3)
# ax3 = fig3.add_subplot(111)
# ax3.plot(hora_a_seg(mag09['time']), mag09['nT'])
# ax3.plot(hora_a_seg(base_efec09['hhmmss']), base_efec09['valor']/10)
#
# fig4 = plt.figure(4)
# ax4 = fig4.add_subplot(111)
# ax4.plot(hora_a_seg(mag11['time']), mag11['nT'])
# ax4.plot(hora_a_seg(base_efec11['hhmmss']), base_efec11['valor']/10)
#
# fig5 = plt.figure(5)
# ax5 = fig5.add_subplot(111)
# ax5.plot(hora_a_seg(mag12['time']), mag12['nT'])
# ax5.plot(hora_a_seg(base_efec12['hhmmss']), base_efec12['valor']/10)

mag08_corr = []
mag09_corr = []
mag11_corr = []
mag12_corr = []

for i in range(len(mag08)):
    mag08_corr = np.append(mag08_corr, mag08['nT'][i] - int_diurna08(seg_mag08[i]))

for i in range(len(mag09)):
    mag09_corr = np.append(mag09_corr, mag09['nT'][i] - int_diurna09(seg_mag09[i]))

for i in range(len(mag11)):
    mag11_corr = np.append(mag11_corr, mag11['nT'][i] - int_diurna11(seg_mag11[i]))

for i in range(len(mag12)):
    mag12_corr = np.append(mag12_corr, mag12['nT'][i] - int_diurna12(seg_mag12[i]))

fig6 = plt.figure(6)
ax6 = fig6.add_subplot(111)
ax6.plot(seg_magBase08, basecont(seg_magBase08, int_diurna08) + pd.Series.mean(base_efec08['valor']) / 10)
ax6.plot(seg_mag08, mag08['nT'])

fig7 = plt.figure(7)
ax7 = fig7.add_subplot(111)
ax7.plot(seg_mag08, mag08_corr)