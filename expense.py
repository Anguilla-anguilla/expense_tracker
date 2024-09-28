import argparse
from CRUD import (create_file, create,
                  read, update, delete,
                  summary, filter_by_category,
                  monthly_limit)


def main():
    create_file()

    parser = argparse.ArgumentParser(prog='expense',
                                     description='Expense tracker')

    subparsers = parser.add_subparsers(dest='command')

    parser_add = subparsers.add_parser('add', help='Add a new expense')
    parser_add.add_argument('--description', type=str, help='Description')
    parser_add.add_argument('--amount', type=int, help='Amount')
    parser_add.add_argument('--category', type=str, help='Category')

    subparsers.add_parser('list', help='Expenses list')

    parser_summary = subparsers.add_parser('summary', help='Summary')
    parser_summary.add_argument('--month', type=int, help='Monthly summary',
                                nargs='?', choices=[i for i in range(1, 13)])
    
    parser_limit = subparsers.add_parser('limit', help='Limit')
    parser_limit.add_argument('--set', type=int, help='Set limit')
    parser_limit.add_argument('--show', nargs='?', const=True, help='Show limit')

    parser_filter = subparsers.add_parser('filter', help='Delete')
    parser_filter.add_argument('--category', type=str, help='Expense ID')
    
    parser_update = subparsers.add_parser('update', help='Update')
    parser_update.add_argument('id', type=str, help='Expense ID')
    parser_update.add_argument('--date', type=str, help='Update date')
    parser_update.add_argument('--description', type=str,
                                help='Update description')
    parser_update.add_argument('--amount', type=int, help='Update amount')
    parser_update.add_argument('--category', type=str, help='Update category')

    parser_delete = subparsers.add_parser('delete', help='Delete')
    parser_delete.add_argument('id', type=str, help='Expense ID')

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
        read()
    elif args.command == 'summary':
        if not args.month:
            summary(0)
        else:
            summary(args.month)
    elif args.command == 'limit':
        if args.set:
            monthly_limit(args.set)
        if args.show:
            monthly_limit(show=True) 
    elif args.command == 'filter':
        if not args.category:
            filter_by_category()
        else:
            filter_by_category(args.category)
    elif args.command == 'update':
        if args.description:
            update_description = args.description
        else:
            update_description = None
        if args.date:
            update_date = args.date
        else:
            update_date = None
        if args.amount:
            update_amount = args.amount
        else:
            update_amount = None
        if args.category:
            update_category = args.category
        else:
            update_category = None
        update(id=args.id,
               description=update_description,
               date=update_date,
               amount=update_amount,
               category=update_category)
    elif args.command == 'delete':
        delete(args.id)
    else:
        print('Wrong command.')


if __name__ == '__main__':
    main()
