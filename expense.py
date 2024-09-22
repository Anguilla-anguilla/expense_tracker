import argparse
from CRUD import (create_file, create)


def main():
    create_file()

    parser = argparse.ArgumentParser(prog='expense',
                                     description='Expense tracker')

    subparsers = parser.add_subparsers(dest='command')

    parser_add = subparsers.add_parser('add', help='Add a new expense')
    parser_add.add_argument('--description', type=str, help='Description')
    parser_add.add_argument('--amount', type=int, help='Amount')
    parser_add.add_argument('--category', type=str, help='Category')

    subparsers.add_parses('list', help='Expenses list')
    

    args = parser.parse_args()

    if args.command == 'add':
        if args.description:
            description = args.description
        else:
            description = ''
        if args.amount:
            amount = args.amount
        else:
            amount = 0
        if args.category:
            category = args.category
        else:
            category = ''
        create(description=description,
               amount=amount,
               category=category)
    elif args.command == 'list':
        pass
    else:
        print('Wrong command.')

if __name__ == '__main__':
    main()