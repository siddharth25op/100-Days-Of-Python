# # with open("./weather_data.csv", "r") as data:
# #     x = data.readlines()
# #     print(x)
#
# # import csv
# # import pandas
# #
# # with open("weather_data.csv") as data:
# #     x = csv.reader(data)
# #     temperature = []
# #     for row in x:
# #         if row[1] != "temp":
# #             temperature.append(int(row[1]))
# #
# # print(temperature)
#
# import pandas
# data = pandas.read_csv("./weather_data.csv")
# # print(data)
# # print(data["temp"])
# #
# # datadict = data.to_dict()
# # print(datadict)
#
# # temp_list = data["temp"].to_list()
# # print(temp_list)
#
# # average = sum(temp_list) / len(temp_list)
# # print(round(average, 2))
#
# # print(round(data["temp"].mean(), 2))
# # print(data["temp"].max())
#
# #Get Data in Columns
# # print(data.condition)
#
# #Get data in Row
# # print(data[data.day == "Monday"])
#
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == "Monday"]
# # monday_temp = monday.temp
# # monday_temp_F = monday_temp * 9/5 + 32
# # print(monday_temp_F)
#
# #create dataframe from scratch
# data_dict = {
#     "student": ["Any", "Siddharth", "Tanjiro"],
#     "scores": [10, 20, 30]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("newdata.csv")
#
#

import pandas

data = pandas.read_csv("squirril_data.csv")
grey_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, cinnamon_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

