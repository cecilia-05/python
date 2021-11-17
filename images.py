from PIL import Image
from time import perf_counter

print(perf_counter(), "Reading image...")

filename = "images/100.jpg"
#with open(filename, "rb") as file:
#    print(file.read())
image = Image.open(filename)
#print(image.width, image.height)

print(perf_counter(), "Resolution: ", image.width, image.height)
total_pixels = image.width * image.height
print(perf_counter(), "Total pixels: ", total_pixels)


print(perf_counter(), "Extracting pixels...")
pixels = list(image.getdata())

# solo un color
#print("Procesing image...")
#new_pixels = []
#for pixel in pixels:
#   r, g, b = pixel
#   red_pixel = (r, 0, 0)
#    new_pixels.append(red_pixel)

#blanco o negro, solo dos tonos
#print("Procesing image...")
#new_pixels = []
#for pixel in pixels:
#    r, g, b = pixel
#    if r > 100 or g > 100 or b > 100:
#        new_pixel = (255, 255, 255)
#    else: 
#        new_pixel = (0, 0, 0)
#    new_pixels.append(new_pixel)

# blancos y negros con tonos
print(perf_counter(), "Procesing image...")
new_pixels = []
for pixel in pixels:
    r, g, b = pixel
    average = sum(pixel) // 3
    new_pixel = (average, average, average)
    new_pixels.append(new_pixel)

print(perf_counter(), "Saving new image...")
new_image = Image.new(mode="RGB", size=image.size)
new_image.putdata(new_pixels)
new_image.save("images/100_bw.jpg")
print(perf_counter(), "Saved.")
