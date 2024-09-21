import pandas

CINNAMON = "Cinnamon"
GRAY = "Gray"
BLACK ="Black"
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
black = len(data[data["Primary Fur Color"] == BLACK])
cinnamon = len(data[data["Primary Fur Color"] == CINNAMON])
gray = len(data[data["Primary Fur Color"] == GRAY])

squirrel_dict = {
    "fur color" : ["black", "cinnamon", "gray"],
    "count": [black, cinnamon, gray]
}
data = pandas.DataFrame(squirrel_dict)
data.to_csv("squirrel_count.csv")