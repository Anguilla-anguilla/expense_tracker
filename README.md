# Expanse tracker

## Introduction
The CLI Expense Tracker is a command-line tool designed to help you manage your personal expenses. It allows you to perform CRUD (Create, Read, Update, Delete) operations on your expenses, summarize your monthly expenses, filter expenses by category, and set limits to warn you if you exceed your budget.

## Installation
To install the CLI Expense Tracker, follow these steps:

1. Clone the Repository:

```git clone https://github.com/Anguilla-anguilla/expense_tracker.git```

```cd expense_tracker```

2. Install Dependencies:

```pip install -r requirements.txt```

## Usage

### Adding an Expense

To add a new expense, use the following command:

```python expense.py add --description "Fish" --amount 30 --category "Food"```

#### Options (Optional):
- **--description**: A brief description of the expense.
- **--amount**: The amount spent.
- **--category**: The category of the expense

### Viewing Expenses

To view all expenses, use:

```python expense.py list```

### Filtering by category

To view all existing categories:

```python expense.py list```

To view expenses for a specific category:

```python expense.py list --category "Food"```

### Updating an Expense

To update an existing expense, use **update** command followed by id:

```python expense.py update 17 --description "Lunch" --amount 30 --date 17.08.2024 --category "Other"```

#### Options (Optional):
- **--description**: New description.
- **--amount**: New amount.
- **--category**: New category.
- **--date**: New date.

### Deleting an Expense

To delete an expense, **delete** command followed by id:

```python expense.py delete 12```

### Summarizing Monthly Expenses

To summarize all expenses, use:

```python expense.py summary```

To summarize expenses for a specific month, use:

```python expense.py summary --month 10```

### Setting and Checking Expense Limits

To set a monthly for a current month expense limit, use:

```python expense.py limit --set 2000```

To check if you have exceeded any limits, use:

```python expense.py limit --show```

[Project URL](https://roadmap.sh/projects/expense-tracker)
