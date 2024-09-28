import csv
from prettytable import PrettyTable

def id_auto_increment(csv_file):
    with open(csv_file, 'rt', encoding='utf-8', newline='') as file:
        csv_reader = csv.DictReader(file)
        last_id = None
        for row in csv_reader:
            last_id = row['ID']
        if last_id == None:
            return 1
        else:
            id = int(last_id) + 1
            return id


def print_pattern(columns, rows):
    table = PrettyTable()
    table.field_names = columns
    for row in rows:
        table.add_row([row[columns[i]] for i in range(len(columns))])
    print(table)


def count_expense(amount_list, month=None, year=None, limit=False):
    total = 0
    for amount in amount_list:
        amount = int(amount)
        total += amount
    if month:
        if limit is True:
            return total
        else:
            print(f'Total expenses for {month}/{int(year)-2000} - {total}')
    else:
        print(f'Total expenses - {total}')

