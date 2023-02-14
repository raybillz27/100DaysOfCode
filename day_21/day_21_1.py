# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# temp_len = len(temp_list)
# print(temp_len)
# average = sum(temp_list) / temp_len
# print(average)
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # get data in column
# print(data["condition"])
# print(data.condition)

# how to get data in rows
# print(data[data.day == "Monday"])
# print(data[data.day == "Sunday"])
# print(data[data.temp == data.temp.max()])
# sunday = (data[data.day == "Sunday"])
# print(sunday.condition)
# celsius = sunday.temp
# finale = (celsius * 9/5) + 32
# print(finale)

# create data frame from scratch


squirrel_count = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(squirrel_count[squirrel_count["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(squirrel_count[squirrel_count["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(squirrel_count[squirrel_count["Primary Fur Color"] == "Black"])


squirrel_dict = {
    "Fur color": ["Gray", "Cinnamon"," Black"],
    "count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(squirrel_dict)
data_frame = pandas.DataFrame(squirrel_dict)
data_frame.to_csv("squirrel_count")








