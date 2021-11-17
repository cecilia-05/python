# CET,Max TemperatureC,Mean TemperatureC,Min TemperatureC,Dew PointC,MeanDew PointC,Min DewpointC,Max Humidity, Mean Humidity, Min Humidity, Max Sea Level PressurehPa, Mean Sea Level PressurehPa, Min Sea Level PressurehPa, Max VisibilityKm, Mean VisibilityKm, Min VisibilitykM, Max Wind SpeedKm/h, Mean Wind SpeedKm/h, Max Gust SpeedKm/h,Precipitationmm, CloudCover, Events,WindDirDegrees
# 2005-2-1,13,4,-5,1,-4,-8,86,59,33,1029,1027,1025,,,,27,6,,0.00,,,359

import csv
import numpy as np
import matplotlib.pyplot as plt
import datetime

@np.vectorize
def convert_value(value):
    if value.replace("-", "").isdigit():
        return int(value)
    elif "." in value:
        return int(float(value) * 100)
    elif value == "":
        return 999999
    else:
        raise ValueError(value)

@np.vectorize
def convert_date(date):
    format = "%Y-%m-%d" 
    return datetime.datetime.strptime(date, format).strftime(format)

filename = "weather/data_weather.csv"
with open(filename, "r") as file:
    reader = list(csv.reader(file))

print("Read {} rows, {} columns".format(
    (len(reader)), len(reader[0]))
)
#print(reader[:5])

columns, *data = reader
# print nombres columnas y luego cntas lineas de data quedan (tdos días del año)
#print(columns)
#print(len(data))

counts = dict.fromkeys(columns, 0)
for column in columns:
    index = columns.index(column)
    for row in data:
        value = row[index]
        if value == "":
            counts[column] += 1

for column, count in counts.items():
    if count > 10:
        print(f"{column}: {count}")

data = list(np.array(data).T)
for column in reversed(columns):
    count = counts[column]
    if count > 10:
        print(f"Removing {column}: {count}")
        del data[columns.index(column)]

print(len(data), "columns remaining.")

dates = data[0]
values = datvalues = np.array(data[1:])
values = convert_value(values)

#print(dates)
#print(np.array(values, dtype=int))
# for column, count in counts.items():
#     print(f"{column}: {count}")


values[0][values[0] == 999999] = 24
values[1][:1300][values[1][:1300] == 999999] = 24
values[1][1300:][values[1][1300:] == 999999] = 20
values[2][values[2] == 999999] = 18


#gráfica con lineas
#plt.style.use("ggplot")
#plt.plot(dates, values[0], marker=".", linewidth=0, c="r")
#plt.plot(dates, values[1], marker=".", linewidth=0, c="g")
#plt.plot(dates, values[2], marker=".", linewidth=0, c="b")
#plt.show()

#con lineas
#plt.style.use("ggplot")
#plt.plot(dates, values[0], linewidth=1, c="r")
#plt.plot(dates, values[1], linewidth=1, c="g")
#plt.plot(dates, values[2], linewidth=1, c="b")
#plt.show()
#plt.plot(dates, values[0])
#plt.plot(dates, values[0])
#plt.show()
#print(np.array(convert_date(dates), dtype="datetime64").dtype)

values[7][values[7] == 999999] = 33

dates = np.array(convert_date(dates), dtype="datetime64")
#print(dates.dtype)

plt.style.use("ggplot")
def plot_all_temperatures():

    # plt.scatter(dates, values[0], marker=".", linewidth=1, c="r")
    # plt.plot(dates, values[1], linewidth=1, c="g")
    # plt.plot(dates, values[2], linewidth=1, c="b")

    plt.plot(dates, values[0], linewidth=0, marker=".")
    plt.plot(dates, values[7], linewidth=0, marker=".")

    end_date = datetime.datetime.fromisoformat("2004-12-31")
    plt.xlim((start_date, end_date))
    plt.show()

#Calculate average yearly temperatures

#print(values.shape)

yearly_averages = np.zeros((3, 19), dtype=float)
for i in range(19):
    year = 1997 + i
    year_rows = dates.astype("datetime64[Y]") == np.datetime64(str(year))
    year_data = values[:3, year_rows]
    print(year_data.shape)
    averages = year_data.mean(axis=1)
    print(averages)
    print(averages.shape)

    yearly_averages[:, i] = averages

x_axis = range(1997, 2016)
plt.plot(x_axis, yearly_averages[0])
plt.plot(x_axis, yearly_averages[1])
plt.plot(x_axis, yearly_averages[2])
plt.show(gfd)
