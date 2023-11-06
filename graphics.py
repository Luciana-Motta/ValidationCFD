import pandas as pd
import numpy as np

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# Especifique a fonte diretamente nas configurações do Matplotlib
matplotlib.rcParams['font.family'] = 'Times New Roman'
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.preamble'] = r'\usepackage{newtxtext,newtxmath}'


# Ler o arquivo CSV com vírgulas como delimitadores
result = pd.read_csv('results/results.csv', delimiter=',')

# Extrair os dados de alpha, cd e cl e convertê-los em arrays NumPy
alpha = result['alpha'].to_numpy()
cd = result['cd'].to_numpy()
cl = result['cl'].to_numpy()


# Ler o arquivo cd60.txt
data = pd.read_csv('data/cd60.txt', sep='\s+', header=None, names=['cl', 'cd'])

# Extrair os dados de cl e cd do arquivo cd60.txt
data_cl = data['cl'].to_numpy()
data_cd = data['cd'].to_numpy()

# Ler o arquivo cd60.txt
data1 = pd.read_csv('data/cl60.txt', sep='\s+', header=None, names=['alpha', 'cl'])

# Extrair os dados de cl e cd do arquivo cd60.txt
data1_alpha = data1['alpha'].to_numpy()
data1_cl = data1['cl'].to_numpy()


# Criar gráfico de cd por alpha
plt.figure(figsize=(8, 6))
plt.plot(alpha, cd, marker='o', linestyle='-')
plt.title('cd por alpha')
plt.xlabel('alpha')
plt.ylabel('cd')
plt.grid()
plt.savefig('graphics/cd60.pdf', format='pdf', bbox_inches='tight')

# Criar gráfico de cl por alpha
plt.figure(figsize=(8, 6))
plt.plot(alpha, cl, linestyle='--', color = (.50, .0, .50))
plt.title('cl por alpha')
plt.xlabel('alpha')
plt.ylabel('cl')
plt.grid()
# Adicionar os dados de cl e cd do arquivo cd60.txt ao mesmo gráfico
plt.plot(data1_alpha, data1_cl, marker='o', linestyle='None', label='cd/cl por cl', color = (.0, .60, 0.70))
plt.legend()

plt.savefig('graphics/cl60..pdf', format='pdf', bbox_inches='tight')

# Criar gráfico de cd por alpha
plt.figure(figsize=(8, 6))
plt.grid(True)
plt.gca().set_axisbelow(True)  # 'gca' é abreviação de 'get current axis'
plt.plot(cl[0:12], cd[0:12], linestyle='--', color = (.50, .0, .50))
plt.title('cd-cl por cl')

plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

plt.xlabel('cl')
plt.ylabel('cd')
plt.grid()

# Adicionar os dados de cl e cd do arquivo cd60.txt ao mesmo gráfico
plt.plot(data_cl, data_cd, marker='o',  linestyle='None', label='cd/cl por cl', color = (.0, .60, 0.70))
plt.legend()

plt.savefig('graphics/cd-cl60.pdf', format='pdf', bbox_inches='tight')

# Mostrar o gráfico (opcional)
plt.show()