def show_fruits():
    conn_str_2017 = (
        r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
        r'DBQ=Data\2017AnthisFruit.accdb;'
        )
    cnxn_2017 = pyodbc.connect(conn_str_2017)
    crsr_2017 = cnxn_2017.cursor()
    crsr_2017.execute("select * from FruitSale")
    columns_2017 = [column[0] for column in crsr_2017.description]
    available_fruit = []
    for data in columns_2017:
        if data != "ID" and data != "teacherCode" and data != "StudentLastName"\
                and data != "AmountOwed" and data != "Sheet"\
                and data != "StudentFirstName":
            available_fruit.append(data)

    for fruit in available_fruit:
        print(f"\t- '{fruit}'")
    return available_fruit



def make_visual():
    while True:

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

        """Query the user and their input"""

        fruit = input("\nWhat fruit are you checking for? : ")
        if fruit.title() == "Quit" or fruit.title() == "End":
            print("Visualization procress discontinued..."
                  "\nending..")
            break
        if fruit not in available_fruit:
            print("Please enter a valid fruit in the fruit list...")
            continue


        """Retrieve all fruits and puts into a list"""

        holder_2017, holder_2018, holder_2019 = [], [], []

        """Appends specified 2017 'fruit' """
        for column in crsr_2017.fetchall():
            if fruit == columns_2017[4]:
                holder_2017.append(column[4])

            if fruit == columns_2017[5]:
                holder_2017.append(column[5])

            if fruit == columns_2017[6]:
                holder_2017.append(column[6])

            if fruit == columns_2017[7]:
                holder_2017.append(column[7])

            if fruit == columns_2017[8]:
                holder_2017.append(column[8])

            if fruit == columns_2017[9]:
                holder_2017.append(column[9])

            if fruit == columns_2017[10]:
                holder_2017.append(column[10])

            if fruit == columns_2017[11]:
                holder_2017.append(column[11])

            if fruit == columns_2017[12]:
                holder_2017.append(column[12])

            if fruit == columns_2017[13]:
                holder_2017.append(column[13])

            if fruit == columns_2017[15]:
                holder_2017.append(column[15])

        """Appends all 2018 'fruit' """
        for column in crsr_2018.fetchall():
            if fruit == columns_2018[4]:
                holder_2018.append(column[4])

            if fruit == columns_2018[5]:
                holder_2018.append(column[5])

            if fruit == columns_2018[6]:
                holder_2018.append(column[6])

            if fruit == columns_2018[7]:
                holder_2018.append(column[7])

            if fruit == columns_2018[8]:
                holder_2018.append(column[8])

            if fruit == columns_2018[9]:
                holder_2018.append(column[9])

            if fruit == columns_2018[10]:
                holder_2018.append(column[10])

            if fruit == columns_2018[11]:
                holder_2018.append(column[11])

            if fruit == columns_2018[12]:
                holder_2018.append(column[12])

            if fruit == columns_2018[13]:
                holder_2018.append(column[13])

            if fruit == columns_2018[15]:
                holder_2018.append(column[15])

        """Appends all 2019 'fruit' """
        for column in crsr_2019.fetchall():
            if fruit == columns_2019[4]:
                holder_2019.append(column[4])

            if fruit == columns_2019[5]:
                holder_2019.append(column[5])

            if fruit == columns_2019[6]:
                holder_2019.append(column[6])

            if fruit == columns_2019[7]:
                holder_2019.append(column[7])

            if fruit == columns_2019[8]:
                holder_2019.append(column[8])

            if fruit == columns_2019[9]:
                holder_2019.append(column[9])

            if fruit == columns_2019[10]:
                holder_2019.append(column[10])

            if fruit == columns_2019[11]:
                holder_2019.append(column[11])

            if fruit == columns_2019[12]:
                holder_2019.append(column[12])

            if fruit == columns_2019[13]:
                holder_2019.append(column[13])

            if fruit == columns_2019[15]:
                holder_2019.append(column[15])

        total_2017 = add(holder_2017)
        total_2018 = add(holder_2018)
        total_2019 = add(holder_2019)
        average = average_list(total_2017,total_2018,total_2019)


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

