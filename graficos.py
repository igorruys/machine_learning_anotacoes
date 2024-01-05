import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rand

rand.seed(1)
#Geracao dos dados D
dadosx = rand.normal(0,1,15)
dadosy = np.zeros_like(dadosx)


gaussian = lambda x,mu: 1/np.sqrt(2*np.pi) * np.exp(-(x-mu)**2/2)
list_mu = [-1,0,1]
list_gaussians = []
for mu in list_mu:
    gaussx = np.linspace(mu-4,mu+4,500)
    gaussy = gaussian(gaussx,mu)
    list_gaussians.append([gaussx,gaussy])

plt.figure(figsize=[12,2])
plt.plot(dadosx,dadosy,'o')

for gauss in list_gaussians:
    p = plt.plot(gauss[0],gauss[1])
    print(p[0].get_color())

plt.xlim([-5.5,5.5])
plt.show()
    