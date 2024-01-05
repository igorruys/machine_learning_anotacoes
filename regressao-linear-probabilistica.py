import numpy as np
import numpy.random as rand
import matplotlib.pyplot as plt

N_pontos = 500
x_ajuste = np.linspace(0,10,500)
x_pontos = np.linspace(0,10,N_pontos)

y_ajuste = x_ajuste * 1.5 + 1

perturbacao1 = rand.uniform(-2,2,N_pontos)
perturbacao2 = rand.normal(0,1.2,N_pontos)
y_pontos = x_pontos * 1.5 + 1 + perturbacao2 

plt.rc('axes', titlesize = 18)     # fontsize of the axes title
plt.rc('axes', labelsize = 12)    # fontsize of the x and y labels
plt.rc('xtick', labelsize = 12)    # fontsize of the tick labels
plt.rc('ytick', labelsize = 12)    # fontsize of the tick labels
plt.rc('legend', fontsize = 12)

plt.plot(x_pontos, y_pontos, 'o', markersize=2)
plt.plot(x_ajuste, y_ajuste, '-', linewidth=3)

plt.legend(['Dados', 'Ajuste'])
plt.grid()
plt.show()



