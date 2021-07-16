import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv('data/data10.csv')
lista_generation = tabela['generation']
lista_life_time = tabela['average life time']

tabela2 = pd.read_csv('data/data11.csv')
lista_generation2 = tabela2['generation']
lista_life_time2 = tabela2['average life time']

plt.plot(lista_generation, lista_life_time, label='Algoritmo genético')
plt.plot(lista_generation2, lista_life_time2, label='Algoritmo aleatório')
plt.grid(True)
plt.legend()
plt.xlabel('Generation')
plt.ylabel('Average life time')
plt.show()