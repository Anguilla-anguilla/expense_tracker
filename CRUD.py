import csv
import os
import datetime as dt
import re
from utils import id_auto_increment, print_pattern, summary


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


def read(choice=None):
    with open(CSV_FILE, 'rt', encoding='utf-8', newline='') as file:
        csv_reader = csv.DictReader(file)

        if choice is None:
            print_pattern(columns=COLUMNS, rows=csv_reader)

        elif choice is not None:
            current_year = dt.datetime.now().strftime('%Y')
            amount_list = []
            if choice != 0:
                if choice < 10:
                    pattern = rf'\b\d{{2}}\.0{choice}\.{current_year}\b'
                else:
                    pattern = rf'\b\d{{2}}\.{choice}\.{current_year}\b'
                for row in csv_reader:
                    if re.match(pattern, row['Date']):
                        amount_list.append(row['Amount'])
                summary(amount_list=amount_list,
                        month=choice,
                        year=current_year)
            else:
                for row in csv_reader:
                    amount_list.append(row['Amount'])
                summary(amount_list=amount_list)


def update(id, description=None, date=None, amount=None, category=None):
    
    with open(CSV_FILE, 'rt', encoding='utf-8', newline='') as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)

        update_expense = next((item for item in data if item['ID'] == id),
                               None)

        if update_expense is None:
            print('Wrong ID')
            return

        if description is not None:
            update_expense['Description'] = description
            print(f'ID {id}: Description is updated.')
        if date is not None:
            update_expense['Date'] = date
            print(f'ID {id}: Date is updated.')
        if amount is not None:
            update_expense['Amount'] = amount
            print(f'ID {id}: Amount is updated.')
        if category is not None:
            update_expense['Category'] = category
            print(f'ID {id}: Category is updated.')
        
    with open(CSV_FILE, mode='w', encoding='utf-8', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=COLUMNS)
        csv_writer.writeheader()
        csv_writer.writerows(data)


def delete():
    pass
