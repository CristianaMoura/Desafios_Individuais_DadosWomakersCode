# import statsmodels.api as sm
# import matplotlib.pyplot as plt

# dados = [500, 510, 490, 520]  
# sm.qqplot(dados, line='s')  
# plt.show() 
# 


import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np  # <--- importe o numpy

dados = [500, 510, 490, 520]
dados = np.array(dados)  # <--- converte a lista em array numpy

sm.qqplot(dados, line='s')
plt.show()