import matplotlib.pyplot as plt
from practica_import import *
from mpl_toolkits.mplot3d import Axes3D

fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111, projection='3d')
plt.title('Mediciones 08/12')
ax1.plot(lon08, lat08, val08)

fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111, projection='3d')
plt.title('Mediciones 09/12')
ax2.plot(lon09, lat09, val09)

fig3 = plt.figure(3)
ax3 = fig3.add_subplot(111, projection='3d')
plt.title('Mediciones 11/12')
ax3.plot(lon11, lat11, val11)

fig4 = plt.figure(4)
ax4 = fig4.add_subplot(111, projection='3d')
plt.title('Mediciones 12/12')
ax4.plot(lon12, lat12, val12)

fig6 = plt.figure(6)
ax6 = fig6.add_subplot(111)
plt.title('Perfil NS 12/12')
ax6.plot(lat12, val12)

fig7 = plt.figure(7)
ax7 = fig7.add_subplot(111)
plt.title('Perfil EO 11/12')
ax7.plot(lon11, val11)

fig8 = plt.figure(8)
ax8 = fig8.add_subplot(111)
plt.title('Valores base 07/12')
ax8.plot(magBase07['medicion'], magBase07['valor'])

fig9 = plt.figure(9)
ax9 = fig9.add_subplot(111)
plt.title('Valores base 08/12')
ax9.plot(magBase08['medicion'], magBase08['valor'])

fig10 = plt.figure(10)
ax10 = fig10.add_subplot(111)
plt.title('Valores base 09/12')
ax10.plot(magBase09['medicion'], magBase09['valor'])

fig11 = plt.figure(11)
ax11 = fig11.add_subplot(111)
plt.title('Valores base 11/12')
ax11.plot(magBase11['medicion'], magBase11['valor'])

fig12 = plt.figure(12)
ax12 = fig12.add_subplot(111)
plt.title('Valores base 12/12')
ax12.plot(magBase12['medicion'], magBase12['valor'])

fig13 = plt.figure(13)
ax13 = fig13.add_subplot(111)
plt.title('Track base 08/12')
plt.grid(True)
plt.xlabel('longitude (°)')
plt.ylabel('latitude (°)')
ax13.plot(lon08, lat08)

fig14 = plt.figure(14)
ax14 = fig14.add_subplot(111)
plt.title('Track 09/12')
plt.grid(True)
plt.xlabel('longitude (°)')
plt.ylabel('latitude (°)')
ax14.plot(lon09, lat09)

fig15 = plt.figure(15)
ax15 = fig15.add_subplot(111)
plt.title('Track 11/12')
plt.grid(True)
ax15.axis('equal')
plt.xlabel('longitude (°)')
plt.ylabel('latitude (°)')
ax15.plot(lon11, lat11)

fig16 = plt.figure(16)
ax16 = fig16.add_subplot(111)
plt.title('Track 12/12')
plt.grid(True)
ax16.axis('equal')
plt.xlabel('longitude (°)')
plt.ylabel('latitude (°)')
ax16.plot(lon12, lat12)

