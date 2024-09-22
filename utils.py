import csv


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

# id, date, description, amount, category
# def print_pattern(columns, rows):
#     table = PrettyTable()
#     table.field_names = columns

#     row_list = []
#     for row in rows:
#         row_list.append(row)

#     table.add_row(row_list)
#     print(table)

