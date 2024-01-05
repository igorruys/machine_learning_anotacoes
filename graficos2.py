import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rand

rand.seed(1)
#Geracao dos dados D
dadosx = rand.normal(0,1,15)
dadosy = np.zeros_like(dadosx)


gaussian = lambda x,mu: 1/np.sqrt(2*np.pi) * np.exp(-(x-mu)**2/2)
mu = 1
gaussx = np.linspace(mu-4,mu+4,5000)
gaussy = gaussian(gaussx,mu)

eqy = []
for dado in dadosx:
    indice_mais_proximo = 0
    mais_proximo = gaussx[0]
    for i in range(1,len(gaussx)):
        if abs(dado - gaussx[i]) < abs(dado - mais_proximo):
            mais_proximo = gaussx[i]
            indice_mais_proximo = i
    eqy.append(gaussy[indice_mais_proximo])

plt.figure(figsize=[12,2])
plt.stem(dadosx,eqy,basefmt=' ',linefmt='--')
plt.plot(gaussx,gaussy,'#d62728')
plt.xlim([-5.5,5.5])
plt.show()

#ff7f0e
#2ca02c
#d62728