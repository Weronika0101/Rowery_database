import sys
import sqlite3
import csv


def current_stations(cursor):
    cursor.execute('SELECT station_id, station_name FROM stations')
    stations_list = cursor.fetchall()
    stations_dict = {}
    for tup in stations_list:
        stations_dict[tup[1]] = tup[0]
    return stations_dict


def load(file_name, database_name):
    try:
        db = sqlite3.connect(f'{database_name}.sqlite3')
        c = db.cursor()
        curr_stations_dict = current_stations(c)
        try:
            with open(file_name, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)
                rentals = []
                stations_dict = {}
                station_id = len(curr_stations_dict)

                for line in reader:
                    rental_id = int(line[0])
                    bike_number = int(line[1])
                    start_time = line[2]
                    end_time = line[3]
                    rental_station = line[4]
                    return_station = line[5]
                    duration = line[6]

                    rentals.append((rental_id, bike_number, start_time, end_time, rental_station, return_station,
                                    duration))
                    # print(return_station)

                    if rental_station not in stations_dict and rental_station not in curr_stations_dict:
                        stations_dict[rental_station] = station_id
                        station_id += 1
                    if return_station not in stations_dict and return_station not in curr_stations_dict:
                        stations_dict[return_station] = station_id
                        station_id += 1

            stations = []
            for elem in stations_dict:
                stations.append((stations_dict[elem], elem))

        except FileNotFoundError:
            print('Podany plik nie istnieje')
            return False

        c.executemany('''
        INSERT INTO stations (station_id, station_name)
        VALUES (?, ?)
        ''', stations)
        db.commit()
        print(rentals)
        curr_stations_dict2 = current_stations(c)

        for i in range(len(rentals)):
            rentals[i] = (rentals[i][0], rentals[i][1], rentals[i][2], rentals[i][3], curr_stations_dict2[rentals[i][4]], curr_stations_dict2[rentals[i][5]], rentals[i][6])

        c.executemany('''
                   INSERT INTO rents (rent_id, bike_number, start_date, end_date, rent_station, return_station, duration)
                   VALUES (?, ?, ?, ?, ?, ?,?)
               ''', rentals)

        db.commit()

        db.close()
    except sqlite3.OperationalError:
        print('Podano nieprawidłową nazwę bazy danych')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Wpisz nazwe pliku csv oraz bazy')
        sys.exit(1)
    load(sys.argv[1], sys.argv[2])
