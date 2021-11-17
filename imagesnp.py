from PIL import Image
from time import perf_counter
import numpy as np
from numpy.core.fromnumeric import shape

print(perf_counter(), "Reading image...")

filename = "images/100.jpg"
image = Image.open(filename)

print(perf_counter(), "Resolution: ", image.width, image.height)
total_pixels = image.width * image.height
print(perf_counter(), "Total pixels: ", total_pixels)


print(perf_counter(), "Extracting pixels...")
array = np.array(image)

#print(array)
#print(array.shape)
# (x-ancho, y-alto, z-3 colores. las 3 dimensiones que tiene)
#print(array.dtype)
# muestra "uint8" unsigned(valorabsol) interger, 8 bit number (numero 8 bites longitud de: 0 y 1)

print(perf_counter(), "Procesing image...")
#average = array.mean(axis=2).astype("uint8")
#pixels = np.repeat(average, 3).reshape(image.height, image.width, 3)



print(perf_counter(), "Saving new image...")
new_image = Image.fromarray(average)
new_image.save("images/12_bw.jpg")
print(perf_counter(), "Saved.")


#Cambiar el sentido o disposición de la imagen (::-1  -> cambiar el sentido de los pixeles)
#print(perf_counter(), "Procesing image...")

#new_image = array[:, ::-1, :]

#print(perf_counter(), "Saving new image...")
#new_image = Image.fromarray(new_image)
#new_image.save("images/12_new.jpg")
#print(perf_counter(), "Saved.")
