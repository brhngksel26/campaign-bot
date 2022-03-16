import plotly.express as px
from mainSheets import getSheetValue
import pandas as pd
import plotly.graph_objects as go

# using the iris dataset

dataList = getSheetValue()

x_data = []

header_graph = dataList[0]
header_graph.pop(0)
dataList.pop(0)

#print(header_graph)
counter = 0
for data in dataList:
    
    x_data.append(data[0])
    title = data[0]
    data.pop(0)

    df = pd.DataFrame({
        "header" :  header_graph,
        "value"  :  data
    })


    # plotting the histogram
    fig = px.histogram(df, x=header_graph, y=data)
    fig.show()
    counter= counter +1

    if counter == 3:
        break



    #print(data)

#print(x_data)
#print(dataList)



# plotting the bar chart
