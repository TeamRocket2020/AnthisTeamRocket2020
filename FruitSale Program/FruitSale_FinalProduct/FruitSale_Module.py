from plotly.graph_objs import Bar, Layout
from plotly import offline
import pyodbc
from lins_math import add, average_list
from FruitSale_Module_ReturnData import return_fruit_datas
from FruitSale_Module_AverageAll import make_averageAll_visual

def show_query():

    conn_str_2017 = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=Data\2017AnthisFruit.accdb;'
        )
    cnxn_2017 = pyodbc.connect(conn_str_2017)
    crsr_2017 = cnxn_2017.cursor()
    crsr_2017.execute("select * from FruitSale")
    columns_2017 = [column[0] for column in crsr_2017.description]
    available_query = []
    for data in columns_2017:
        if data != "ID" and data != "teacherCode" and data != "StudentLastName"\
                and data != "AmountOwed" and data != "Sheet"\
                and data != "StudentFirstName":
            available_query.append(data)
    available_query.append("AverageAllYear")

    for query in available_query:
        print(f"\t- '{query}'")
    return available_query



def make_visual():
    while True:
        conn_str_2017 = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=Data\2017AnthisFruit.accdb;'
        )
        cnxn_2017 = pyodbc.connect(conn_str_2017)
        crsr_2017 = cnxn_2017.cursor()
        crsr_2017.execute("select * from FruitSale")
        header = [column[0] for column in crsr_2017.description]

        available_query = []
        for data in header:
            if data != "ID" and data != "teacherCode" and data != "StudentLastName"\
                    and data != "AmountOwed" and data != "Sheet"\
                    and data != "StudentFirstName":
                available_query.append(data)
        available_query.append("AverageAllYear")

        """Query the user and their input"""

        query = input("\nWhat Query type are you checking for? : ")
        if query.title() == "Quit" or query.title() == "End":
            print("Visualization procress discontinued..."
                  "\nending..")
            break
        if query not in available_query:
            print("Please enter a valid fruit in the fruit list...")
            continue
        f2017 = return_fruit_datas("2017")
        f2018 = return_fruit_datas("2018")
        f2019 = return_fruit_datas("2019")
        if query == "AverageAllYear":
            make_averageAll_visual()
            continue


        if query == header[4]:
            total_2017 = f2017[0]
            total_2018 = f2018[0]
            total_2019 = f2019[0]

        if query == header[5]:
            total_2017 = f2017[1]
            total_2018 = f2018[1]
            total_2019 = f2019[1]

        if query == header[6]:
            total_2017 = f2017[2]
            total_2018 = f2018[2]
            total_2019 = f2019[2]

        if query == header[7]:
            total_2017 = f2017[3]
            total_2018 = f2018[3]
            total_2019 = f2019[3]

        if query == header[8]:
            total_2017 = f2017[4]
            total_2018 = f2018[4]
            total_2019 = f2019[4]

        if query == header[9]:
            total_2017 = f2017[5]
            total_2018 = f2018[5]
            total_2019 = f2019[5]

        if query == header[10]:
            total_2017 = f2017[6]
            total_2018 = f2018[6]
            total_2019 = f2019[6]

        if query == header[11]:
            total_2017 = f2017[7]
            total_2018 = f2018[7]
            total_2019 = f2019[7]

        if query == header[12]:
            total_2017 = f2017[8]
            total_2018 = f2018[8]
            total_2019 = f2019[8]

        if query == header[13]:
            total_2017 = f2017[9]
            total_2018 = f2018[9]
            total_2019 = f2019[9]

        if query == header[15]:
            total_2017 = f2017[10]
            total_2018 = f2018[10]
            total_2019 = f2019[10]

        average = average_list(total_2017,total_2018,total_2019)

        x_value = ['Year - 2017', 'Year - 2018',
                   'Year - 2019', 'Average of 3 years']
        y_value = [total_2017, total_2018, total_2019, average]

        data = [Bar(x=x_value, y = y_value)]
        x_axis_config = {"title": "Years", "dtick": 1}
        y_axis_config = {"title": "Amount of fruit sold",}
        my_layout = Layout(title=f"3 Years of {query} sales",
                          xaxis= x_axis_config, yaxis= y_axis_config)
        offline.plot({"data": data, "layout": my_layout},
                     filename=f"Stored_Visual\_{query}_all_year.html")

