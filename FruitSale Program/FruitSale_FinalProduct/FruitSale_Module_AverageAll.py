import pyodbc
from plotly.graph_objs import Bar, Layout
from plotly import offline
from FruitSale_Module_ReturnData import return_fruit_datas

def make_averageAll_visual():
        average = return_fruit_datas("average")

        x_value = ['Clementines', 'SmallBaskets', 'LargeBaskets',
                   'SmallGrapefruit', 'LargeGrapefruit', 'LargeOranges',
                   'SantaOranges', 'SmallOranges', 'RedApples', 'GoldApples',
                   'GalaApples']
        y_value = [average[0], average[1], average[2],
                   average[3], average[4], average[5],
                   average[6], average[7], average[8],
                   average[9], average[10]]

        data = [Bar(x=x_value, y = y_value)]
        x_axis_config = {"title": "Years", "dtick": 1}
        y_axis_config = {"title": "Amount of fruit sold",}
        my_layout = Layout(title=f"3 Years of average of all fruits sale quantity",
                          xaxis= x_axis_config, yaxis= y_axis_config)
        offline.plot({"data": data, "layout": my_layout},
                     filename=f"Stored_Visual\All_fruits_all_year.html")

