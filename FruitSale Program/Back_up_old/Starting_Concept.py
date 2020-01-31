import pyodbc
from add import add, average_list

""" Retrieve datas from microsoft access files of every years"""
conn_str_2017 = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=Data\2017AnthisFruit.accdb;'
    )
cnxn_2017 = pyodbc.connect(conn_str_2017)
crsr_2017 = cnxn_2017.cursor()
crsr_2017.execute("select * from FruitSale")
columns_2017 = [column[0] for column in crsr_2017.description]

conn_str_2018 = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=Data\2018AnthisFruit.accdb;'
    )
cnxn_2018 = pyodbc.connect(conn_str_2018)
crsr_2018 = cnxn_2018.cursor()
crsr_2018.execute("select * from FruitSale")
columns_2018 = [column[0] for column in crsr_2018.description]

conn_str_2019 = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=Data\2019AnthisFruit.accdb;'
    )
cnxn_2019 = pyodbc.connect(conn_str_2019)
crsr_2019 = cnxn_2019.cursor()
crsr_2019.execute("select * from FruitSale")
columns_2019 = [column[0] for column in crsr_2019.description]

available_fruit = []
for data in columns_2017:
    if data != "ID" and data != "teacherCode" and data != "StudentLastName"\
            and data != "AmountOwed" and data != "Sheet"\
            and data != "StudentFirstName":
        available_fruit.append(data)

"""Appends all 2018 'fruit' """

for column in crsr_2017.fetchall():
    Clementines_2017.append(column[4])
    Clementines_total_2017 = add(Clementines_total_2017)
    SmallBasket_2017.append(column[5])
    LargeBaskets_2017.append(column[6])
    SmallGrapefruit_2017.append(column[7])
    LargeGrapefruit_2017.append(column[8])
    LargeOranges_2017.append(column[9])
    SantaOranges_2017.append(column[10])
    SmallOranges_2017.append(column[11])
    RedApples_2017.append(column[12])
    GoldApples_2017.append(column[13])
    GalaApples_2017.append(column[15])


"""Appends all 2018 'fruit' """

for column in crsr_2018.fetchall():
    Clementines_2018.append(column[4])
    SmallBasket_2018.append(column[5])
    LargeBaskets_2018.append(column[6])
    SmallGrapefruit_2018.append(column[7])
    LargeGrapefruit_2018.append(column[8])
    LargeOranges_2018.append(column[9])
    SantaOranges_2018.append(column[10])
    SmallOranges_2018.append(column[11])
    RedApples_2018.append(column[12])
    GoldApples_2018.append(column[13])
    GalaApples_2018.append(column[15])

    """Appends all 2019 'fruit' """

for column in crsr_2019.fetchall():
    Clementines_2019.append(column[4])
    SmallBasket_2019.append(column[5])
    LargeBaskets_2019.append(column[6])
    SmallGrapefruit_2019.append(column[7])
    LargeGrapefruit_2019.append(column[8])
    LargeOranges_2019.append(column[9])
    SantaOranges_2019.append(column[10])
    SmallOranges_2019.append(column[11])
    RedApples_2019.append(column[12])
    GoldApples_2019.append(column[13])
    GalaApples_2019.append(column[15])


conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=Data\2017AnthisFruit.accdb;'
    )
cnxn = pyodbc.connect(conn_str)
crsr = cnxn.cursor()
crsr.execute("select * from FruitSale")

clementines, small_basket, large_basket = [], [], []
small_grapefruit, large_grapefruit = [], []
large_oranges, santa_oranges, small_oranges = [], [], []
red_apple, gold_apple, gala_apple = [], [], []



x_value = ['Year - 2017', 'Year - 2018',
                   'Year - 2019', 'Average of 3 years']
y_value = [total_2017, total_2018, total_2019, average]

data = [Bar(x=x_value, y = y_value)]
x_axis_config = {"title": "Years", "dtick": 1}
y_axis_config = {"title": "Amount of fruit sold",}
my_layout = Layout(title=f"3 Years of {fruit} sales",
                   xaxis= x_axis_config, yaxis= y_axis_config)
offline.plot({"data": data, "layout": my_layout},
             filename=f"Stored_Visual\{fruit}_all_year.html")





