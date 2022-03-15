import plotly.express as px
from mainSheets import getSheetValue

# using the iris dataset

dataList = getSheetValue()

x_data = []

for data in dataList:
    x_data.append(data[0])
    data.pop(0)
    print(data)



# plotting the bar chart
