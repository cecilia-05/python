import matplotlib.pyplot as plt
import math 
import numpy as np

#Fondo de la gráfica
#plt.style.use("bmh")
    

x_coordinates = np.arange(-10, 10, 0.1)
#y_coordinates = np.sin(x_coordinates)
y_coordinates = x_coordinates ** 2
plt.plot(x_coordinates, y_coordinates, c="cyan")

# En la gráfica muestra cuantas medidas de x quieres, como tú quieras de largo
#plt.xlim(-50, 50)
plt.show()

