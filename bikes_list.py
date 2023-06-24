import sqlite3


def calculate_results(station_id, cursor):
    # Średni czas trwania przejazdu rozpoczynanego na stacji
    cursor.execute("SELECT AVG(duration) FROM rents WHERE rent_station=?", (station_id,))
    avg_start_duration = cursor.fetchone()[0]

    # Średni czas trwania przejazdu kończonego na stacji
    cursor.execute("SELECT AVG(duration) FROM rents WHERE return_station=?", (station_id,))
    avg_end_duration = cursor.fetchone()[0]

    # Liczba różnych rowerów parkowanych na stacji
    cursor.execute("SELECT COUNT(DISTINCT bike_number) FROM rents WHERE rent_station=?", (station_id,))
    bike_count = cursor.fetchone()[0]

    cursor.execute('''
    SELECT bike_number, COUNT(bike_number) AS count
    FROM rents
    WHERE rent_station = ?
    GROUP BY bike_number
    ORDER BY count DESC
    LIMIT 1''', (station_id,))
    popular_bike = cursor.fetchone()[0]

    print(f"Średni czas trwania przejazdu rozpoczynanego na danej stacji: {avg_start_duration} minut")
    print(f"Średni czas trwania przejazdu kończonego na danej stacji: {avg_end_duration} minut")
    print(f"Liczba różnych rowerów parkowanych na danej stacji: {bike_count}")
    print(f"Najczęściej wypożyczany rower na danej stacji ma numer: {popular_bike}")


if __name__ == '__main__':

    db_name = 'rentals'
    conn = sqlite3.connect(f"{db_name}.sqlite3")
    c = conn.cursor()

    c.execute('SELECT station_id, station_name FROM stations')
    stations = c.fetchall()

    print("Lista stacji:")
    for station in stations:
        print(f"{station[0]} - {station[1]}")

    station_id = input("Wpisz ID stacji: ")

    if 0 <= int(station_id) < len(stations):
        calculate_results(station_id, c)
    else:
        print("Stacja o podanym ID nie istnieje!")

    conn.close()
