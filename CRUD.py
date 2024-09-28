import csv
import os
import datetime as dt
import re
from utils import id_auto_increment, print_pattern, count_expense


CSV_FILE = 'expense.csv'
CSV_BUDGET = 'budget.csv'

COLUMNS = ['ID', 'Date', 'Description', 'Amount', 'Category', 'Limit']
BUDGET_COLUMNS = ['Month', 'Budget']


def create_file():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'wt', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(COLUMNS)

    if not os.path.exists(CSV_BUDGET):
        with open(CSV_BUDGET, 'wt', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(BUDGET_COLUMNS)



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
        print_pattern(columns=COLUMNS, rows=csv_reader)


def summary(choice=None, limit=False):
    with open(CSV_FILE, 'rt', encoding='utf-8', newline='') as file:
        csv_reader = csv.DictReader(file)

        current_year = dt.datetime.now().strftime('%Y')
        amount_list = []

        if choice is not None:
            if choice != 0:
                if choice < 10:
                    pattern = rf'\b\d{{2}}\.0{choice}\.{current_year}\b'
                else:
                    pattern = rf'\b\d{{2}}\.{choice}\.{current_year}\b'
                for row in csv_reader:
                    if re.match(pattern, row['Date']):
                        amount_list.append(row['Amount'])
                if limit is True:
                    total = count_expense(amount_list=amount_list,
                                            month=choice,
                                            year=current_year,
                                            limit=True)
                    return total
                else:
                    count_expense(amount_list=amount_list,
                                  month=choice,
                                  year=current_year)

            else:
                for row in csv_reader:
                    amount_list.append(row['Amount'])
                count_expense(amount_list=amount_list)


def monthly_limit(limit=None, show=False):
    with open(CSV_BUDGET, 'rt', encoding='utf-8', newline='') as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)

        current_month = dt.datetime.now().strftime('%m')
        current_year = dt.datetime.now().strftime('%Y')

        budget_date = f'{current_month}.{current_year}'
        limitation = next((item for item in data if item['Month'] == budget_date),
                            None)

        if limit is not None:
            if limitation is None:
                limitation = {'Month': budget_date, 
                                'Budget': limit}
                data.append(limitation)
            else:
                limitation['Budget'] = limit

            print(f'Budget limit for {current_month} month is {limit}.')

            with open(CSV_BUDGET, mode='w', encoding='utf-8', newline='') as file:
                csv_writer = csv.DictWriter(file, fieldnames=BUDGET_COLUMNS)
                csv_writer.writeheader()
                csv_writer.writerows(data)

        if show is True:
            total = summary(choice=int(current_month), limit=True)
            difference = int(limitation['Budget']) - total
            if difference > 0:
                print(f'Yet {difference} to spend.')
            else:
                print('Warning!')
                print(f'Exceeded limit by {abs(difference)}.')


def filter_by_category(filter=None):
    with open(CSV_FILE, 'rt', encoding='utf-8', newline='') as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)

        categories = set()
        for row in data:
            categories.add(row['Category'])

        if filter is None:
            print('List of categories:')
            for category in categories:
                print(f'-{category}')
        elif filter in categories:
            data = [item for item in data if item['Category'] == filter]
            print_pattern(columns=COLUMNS, rows=data)
        else:
            print('No category found.')


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


def delete(id):
    with open(CSV_FILE, 'rt', encoding='utf-8', newline='') as file:
        csv_reader = csv.DictReader(file)
        data = list(csv_reader)

        delete_expense = next((item for item in data if item['ID'] == id),
                              None)
        
        if delete_expense is None:
            print('Wrong ID')
            return
        else:
            print(f'ID {id}: Deleted.')
            data.remove(delete_expense)

    with open(CSV_FILE, mode='w', encoding='utf-8', newline='') as file:
        csv_writer = csv.DictWriter(file, fieldnames=COLUMNS)
        csv_writer.writeheader()
        csv_writer.writerows(data)
