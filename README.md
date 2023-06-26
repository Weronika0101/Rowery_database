# Rowery_database

Skrypt tworzy strukturę relacyjnej bazy danych dla zbioru [Przejazdy Wrocławskiego Roweru Miejskiego (WRM) -
archiwalne](https://www.wroclaw.pl/open-data/dataset/przejazdy-wroclawskiego-roweru-miejskiego-archiwalne) w systemie
zarządzania SQLite, która pozwala na wstawienie, przechowywanie oraz odpytywanie danych o wypożyczeniach rowerów. Baza danych 
uwzględnia dwie tabele: zawierające wypożyczenia oraz stacje.

## Utworzenie bazy

Wywołanie polecenia `python create_databse.py rentals` w konsoli skutkowuje utworzeniem pliku rentals.sqlite3 zawierającego pustą
strukturę.

## Ładowanie danych z pliku do bazy

Przykładowo: `python load_data.py historia_przejazdow_2021-02.csv rentals`

## Lista stacji i operacje na bazie

Aby otworzyć tekstowym interfejsem użytkownika, który pozwoli
użytkownikowi wybrać stację z listy należy użyć polecenia `python bike_list.py`. Po wybraniu stacji dostajemy następujące informacje dodatkowe:
- średni czas trwania przejazdu rozpoczynanego na danej stacji,
- średni czas trwania przejazdu kończonego na danej stacji,
- liczbę różnych rowerów parkowanych na danej stacji,
- numer roweru który był najczęściej wypożyczany na danej stacji
