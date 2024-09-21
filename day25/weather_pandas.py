import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data['temp'])

data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(len(temp_list))

average = sum(temp_list)/len(temp_list)
print(average)

#print mean value from temp using pandas built in
print(data["temp"].mean())

#print max value from temp using pandas built in
print(data["temp"].max())

# Get data in columns
print(data["condition"])
print(data.condition)

# Get data in rows
print(data[data.day =="Monday"])
print(data[data.temp == data.temp.max()])


monday = data[data.day =="Monday"]
print(monday.condition)


# create dataframe from scratch

example_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(example_dict)
print(data)
data.to_csv("new_data.csv")