import csv

import week8.db_base as db

class Veggies:

    def __init__(self, row):
        self.name = row[0]
        self.common_color = row[1]
        self.peal = row[2]
        self.type = row[3]

class CsvLab(db.DBbase):
    def reset_or_create_db(self):
        try:
            sql = """
                DROP TABLE IF EXISTS Veggies;

                Create TABLE Veggies (
                    name TEXT NOT NULL PRIMARY KEY UNIQUE,
                    common_color TEXT,
                    peal TEXT,
                    type TEXT
                );
            """
            super().execute_script(sql)
        except Exception as e:
            print(e)


    def read_data(self, file_name):
        self.veggie_list = []

        try:
            with open(file_name, 'r') as record:
                csv_contents = csv.reader(record)
                next(record)
                for row in csv_contents:
                    print(row)
                    veggie = Veggies(row)
                    self.veggie_list.append(veggie)

        except Exception as e:
            print(e)


    def save_to_database(self):
        print("Number of records to save:", len(self.veggie_list))
        save = input("Continue, y/n ? ").lower()

        if save == "y":
            for item in self.veggie_list:
                try:
                    super().get_cursor.execute(
                        """
                        INSERT INTO Veggies
                        (name, common_color, peal, type)
                            VALUES( ?,?,?,?)
                        """,
                        (item.name, item.common_color, item.peal, item.type)
                    )
                    super().get_connection.commit()
                    print("Saved item: ", item.name, item.type)

                except Exception as e:
                    print(e)
        else:
            print("Save to DB aborted")

csv_lab = CsvLab("VeggieDB.sqlite")
csv_lab.reset_or_create_db()
csv_lab.read_data('veggies.csv')
csv_lab.save_to_database()