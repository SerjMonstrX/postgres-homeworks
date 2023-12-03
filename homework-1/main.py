import csv
import psycopg2
from password import pgsql_pass
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password=pgsql_pass)
try:
    with conn:
        with conn.cursor() as curr:
            tables_data = [
                (os.path.join(current_dir, 'north_data', 'employees_data.csv'), 'employees'),
                (os.path.join(current_dir, 'north_data', 'customers_data.csv'), 'customers'),
                (os.path.join(current_dir, 'north_data', 'orders_data.csv'), 'orders')
            ]
            for file_path, table_name in tables_data:
                with open(file_path, 'r', newline='', encoding='utf-8') as file:
                    csv_reader = csv.reader(file)
                    next(csv_reader)  # Пропустить заголовок
                    for row in csv_reader:
                        curr.execute(f"INSERT INTO {table_name} VALUES ({','.join(['%s'] * len(row))})", row)

finally:
    conn.close()
