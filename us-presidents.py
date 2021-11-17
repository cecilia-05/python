import csv
import numpy as np

with open("us-presidents.csv", "r") as file:
    reader = csv.reader(file)
    rows = list(reader)

print("Read",len(rows),"rows.")
print("Read", len(rows[0]), "columns.")
#Quitas la primera linea de us-presidents.cvs porque no lo necesitamos y no deja pasar los años y dias a días solo
rows.pop(0)


colours = set()
for row in rows:
    _, _, eye, hair, _ = row 

    colours.add(eye)
    colours.add(hair)

colours = list(colours)
print("Found", len(colours), "unique colours.")
print(colours)

names = np.array(rows)[:, 0]
#print(names)
# nombre mas largo, número de caracteres
#print(names.dtype)
converted_rows = []
for i in range(len(rows)):
    name, height, eye, hair, age =  rows[i]
    converted =[]

    years = int(age[:2])
    days = int(age[9:-4])
    total = years * 365 + days


    converted.append(int(height))
    #numero de tipos de colores de ojos
    converted.append(colours.index(eye))
    converted.append(colours.index(hair))
    converted.append(total)

    converted_rows.append(converted)

def years(days):
    return round(days/ 365, 1)

def days(years):
    return years* 365


#print(converted_rows)

data = np.array(converted_rows, dtype="uint16")

#print(data)
#print(data.shape)
#print(data.dtype)


ages = data[:, 3]
youngest = years(ages.min())
oldest = years(ages.max())
average = years(ages.mean())
print("youngest:", youngest)
print("Oldest:", oldest)
print("Average:", average)


#en que fila está el más joven
#index = np.where(data == ages.min())[0][0]
#youngest_president = names[index]

#print("Youngest at inauguration was", youngest_president, "at", youngest, "days old.", years, "years.")

#En versión + corta podemos meter la función older directamente dentro de [] y no crear otra variable
#older = data.T[3] > average
#older_presidents = data[older]
#print(np.where(data == older.T))

brown = data == colours.index("brown")
print(data[brown])

older = data[:, 3] > 19000
print(older)
print(names[older])
#te dice la edad de aquellos presidentes que fueron elegidos cnd eran mayores de 19000 días. 
# ([:, 0] -> nombre), ([:, 1] -> height) ([:, 2] -> eye)
print(data[:, 3][older])


youngest_a = ages == youngest
print(names[youngest_a])

#oldest pres. w/ blue eyes and brownn hair

blue = eye == colours.index("blue")

brown = hair == colours.index("brown")

print(eye[blue])
print(hair[brown])
