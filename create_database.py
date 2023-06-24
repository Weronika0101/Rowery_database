import sqlite3
import sys


def create(name):
    mydb = sqlite3.connect(f"{name}.sqlite3")

    cursor = mydb.cursor()
    cursor.execute(
        '''CREATE TABLE
        stations([station_id] INTEGER PRIMARY KEY NOT NULL,
         [station_name] STRING[100]) ''')

    cursor.execute('''CREATE TABLE
    rents([rent_id] INTEGER PRIMARY KEY,
    [bike_number] INTEGER,
    [start_date] DATE,
    [end_date] DATE,
    [rent_station] INTEGER,
    [return_station] INTEGER,
    [duration] INTEGER,
    FOREIGN KEY (rent_station) REFERENCES stations(station_id),
    FOREIGN KEY (return_station) REFERENCES stations(station_id))''')

    mydb.commit()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Podaj nazwę bazy danych!")
    else:
        database_name = sys.argv[1]
        create(database_name)
