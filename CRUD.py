import csv
import os
import datetime as dt
from utils import id_auto_increment
from prettytable import PrettyTable


CSV_FILE = 'expense.csv'

COLUMNS = ['ID', 'Date', 'Description', 'Amount', 'Category']


def create_file():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'wt', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(COLUMNS)


def create(description, amount, category):

    id = id_auto_increment(CSV_FILE)
    date = dt.datetime.now().strftime('%d.%m.%Y')

    data = [id, date, description, amount, category]

    with open(CSV_FILE, 'rt', encoding='utf-8', newline='') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)

    with open(CSV_FILE, mode='a', encoding='utf-8', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)

    print(f'Expense added successfully (ID: {id})')


def read():
    with open(CSV_FILE, 'rt', encoding='utf-8', newline='') as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            


def update():
    pass


def delete():
    pass
