import pyodbc
from lins_math import add, average_list


def return_fruit_datas(return_data_type):
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

    """Appends all 2018 'fruit' """
    clementines_2017, smallBaskets_2017 = [], []
    largeBaskets_2017, smallGrapefruit_2017 = [], []
    largeGrapefruit_2017 = []
    largeOranges_2017, santaOranges_2017 = [], [],
    smallOranges_2017, redApples_2017 = [], []
    goldApples_2017, galaApples_2017 = [], [],

    for column in crsr_2017.fetchall():
        clementines_2017.append(column[4])
        smallBaskets_2017.append(column[5])
        largeBaskets_2017.append(column[6])
        smallGrapefruit_2017.append(column[7])
        largeGrapefruit_2017.append(column[8])
        largeOranges_2017.append(column[9])
        santaOranges_2017.append(column[10])
        smallOranges_2017.append(column[11])
        redApples_2017.append(column[12])
        goldApples_2017.append(column[13])
        galaApples_2017.append(column[15])

    clementines_2017_holder = add(clementines_2017)
    smallBaskets_2017_holder = add(smallBaskets_2017)
    largeBaskets_2017_holder = add(largeBaskets_2017)
    smallGrapefruit_2017_holder = add(smallGrapefruit_2017)
    largeGrapefruit_2017_holder = add(largeGrapefruit_2017)
    largeOranges_2017_holder = add(largeOranges_2017)
    santaOranges_2017_holder = add(santaOranges_2017)
    smallOranges_2017_holder = add(smallOranges_2017)
    redApples_2017_holder = add(redApples_2017)
    goldApples_2017_holder = add(goldApples_2017)
    galaApples_2017_holder = add(galaApples_2017)


    """Appends all 2018 'fruit' """

    clementines_2018, smallBaskets_2018 = [], []
    largeBaskets_2018, smallGrapefruit_2018 = [], []
    largeGrapefruit_2018 = []
    largeOranges_2018, santaOranges_2018 = [], [],
    smallOranges_2018, redApples_2018 = [], []
    goldApples_2018, galaApples_2018 = [], [],

    for column in crsr_2018.fetchall():
        clementines_2018.append(column[4])
        smallBaskets_2018.append(column[5])
        largeBaskets_2018.append(column[6])
        smallGrapefruit_2018.append(column[7])
        largeGrapefruit_2018.append(column[8])
        largeOranges_2018.append(column[9])
        santaOranges_2018.append(column[10])
        smallOranges_2018.append(column[11])
        redApples_2018.append(column[12])
        goldApples_2018.append(column[13])
        galaApples_2018.append(column[15])

    clementines_2018_holder = add(clementines_2018)
    smallBaskets_2018_holder = add(smallBaskets_2018)
    largeBaskets_2018_holder = add(largeBaskets_2018)
    smallGrapefruit_2018_holder = add(smallGrapefruit_2018)
    largeGrapefruit_2018_holder = add(largeGrapefruit_2018)
    largeOranges_2018_holder = add(largeOranges_2018)
    santaOranges_2018_holder = add(santaOranges_2018)
    smallOranges_2018_holder = add(smallOranges_2018)
    redApples_2018_holder = add(redApples_2018)
    goldApples_2018_holder = add(goldApples_2018)
    galaApples_2018_holder = add(galaApples_2018)

    """Appends all 2019 'fruit' """

    clementines_2019, smallBaskets_2019 = [], []
    largeBaskets_2019, smallGrapefruit_2019 = [], []
    largeGrapefruit_2019 = []
    largeOranges_2019, santaOranges_2019 = [], [],
    smallOranges_2019, redApples_2019 = [], []
    goldApples_2019, galaApples_2019 = [], [],

    for column in crsr_2019.fetchall():
        clementines_2019.append(column[4])
        smallBaskets_2019.append(column[5])
        largeBaskets_2019.append(column[6])
        smallGrapefruit_2019.append(column[7])
        largeGrapefruit_2019.append(column[8])
        largeOranges_2019.append(column[9])
        santaOranges_2019.append(column[10])
        smallOranges_2019.append(column[11])
        redApples_2019.append(column[12])
        goldApples_2019.append(column[13])
        galaApples_2019.append(column[15])

    clementines_2019_holder = add(clementines_2019)
    smallBaskets_2019_holder = add(smallBaskets_2019)
    largeBaskets_2019_holder = add(largeBaskets_2019)
    smallGrapefruit_2019_holder = add(smallGrapefruit_2019)
    largeGrapefruit_2019_holder = add(largeGrapefruit_2019)
    largeOranges_2019_holder = add(largeOranges_2019)
    santaOranges_2019_holder = add(santaOranges_2019)
    smallOranges_2019_holder = add(smallOranges_2019)
    redApples_2019_holder = add(redApples_2019)
    goldApples_2019_holder = add(goldApples_2019)
    galaApples_2019_holder = add(galaApples_2019)

    if return_data_type == "2017":
        return clementines_2017_holder, smallBaskets_2017_holder,\
               largeBaskets_2017_holder, smallGrapefruit_2017_holder,\
               largeGrapefruit_2017_holder, largeOranges_2017_holder,\
               santaOranges_2017_holder, smallOranges_2017_holder,\
               redApples_2017_holder, goldApples_2017_holder,\
               galaApples_2017_holder

    if return_data_type == "2018":
        return clementines_2018_holder, smallBaskets_2018_holder,\
               largeBaskets_2018_holder, smallGrapefruit_2018_holder,\
               largeGrapefruit_2018_holder, largeOranges_2018_holder,\
               santaOranges_2018_holder, smallOranges_2018_holder,\
               redApples_2018_holder, goldApples_2018_holder,\
               galaApples_2018_holder

    if return_data_type == "2019":
        return clementines_2019_holder, smallBaskets_2019_holder,\
               largeBaskets_2019_holder, smallGrapefruit_2019_holder,\
               largeGrapefruit_2019_holder, largeOranges_2019_holder,\
               santaOranges_2019_holder, smallOranges_2019_holder,\
               redApples_2019_holder, goldApples_2019_holder,\
               galaApples_2019_holder


    """Average of every item"""
    average_Clementines = average_list(clementines_2017_holder,clementines_2018_holder,clementines_2019_holder)
    average_SmallBaskets = average_list(smallBaskets_2017_holder,smallBaskets_2018_holder,smallBaskets_2019_holder)
    average_LargeBaskets = average_list(largeBaskets_2017_holder,largeBaskets_2018_holder,largeBaskets_2019_holder)
    average_SmallGrapefruit = average_list(smallGrapefruit_2017_holder,smallGrapefruit_2018_holder,smallGrapefruit_2019_holder)
    average_LargeGrapefruit = average_list(largeGrapefruit_2017_holder,largeGrapefruit_2018_holder,largeGrapefruit_2019_holder)
    average_LargeOranges = average_list(largeOranges_2017_holder,largeOranges_2018_holder,largeOranges_2019_holder)
    average_SantaOranges = average_list(santaOranges_2017_holder,santaOranges_2018_holder,santaOranges_2019_holder)
    average_SmallOranges = average_list(smallOranges_2017_holder,smallOranges_2018_holder,smallOranges_2019_holder)
    average_RedApples = average_list(redApples_2017_holder,redApples_2018_holder,redApples_2019_holder)
    average_GoldApples = average_list(goldApples_2017_holder, goldApples_2018_holder, goldApples_2019_holder)
    average_GalaApples = average_list(galaApples_2017_holder, galaApples_2018_holder, galaApples_2019_holder)

    if return_data_type == "average":
        return average_Clementines, average_SmallBaskets, average_LargeBaskets,\
               average_SmallGrapefruit, average_LargeGrapefruit,\
               average_LargeOranges, average_SantaOranges,\
               average_SmallOranges, average_RedApples, average_GoldApples,\
               average_GalaApples


fruit_2017 = return_fruit_datas("2017")
fruit_2018 = return_fruit_datas("2018")
fruit_2019 = return_fruit_datas("2019")
print(fruit_2017)
print(fruit_2018)
print(fruit_2019)

