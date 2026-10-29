def add_expense(expense_lst):
    while True:
        dict1 = {'date': input('enter the date: '), 'category': input('enter the category: '),
                'description': input('enter the description: ')}
        while True:
            try:
                dict1['amount'] = float(input('enter the amount: '))
                if dict1['amount'] >= 0:
                    expense_lst.append(dict1)
                    save_expenses(expense_lst)
                    break
                else:
                    print('amount cannot be negative number')
            except ValueError:
                print('amount should be a number')
        add_more_expense = input('do you want to add more expense (y/n): ')
        if add_more_expense == 'y':
            continue
        else:
            break
    return expense_lst

def view_expense(expense_lst):
    #print(expense_lst)
    if expense_lst:
        for i, expense in enumerate(expense_lst, start = 1):
            print(f"{i}. {expense['date']}  |  {expense['category']}  |  {expense['description']}  |  {expense['amount']}")
    else:
        print('empty list')

def show_total_expense(expense_lst):
    if expense_lst:
        total_amount = 0
        for i in expense_lst:
            total_amount = total_amount + i['amount']
        print(f'total expense is Rs.{total_amount}')
    else:
        print('empty list')

def show_expense_by_category(expense_lst):
    if expense_lst:
        catotal = {}
        for i in expense_lst:
            if i['category'] not in catotal:
                catotal[i['category']] = i['amount']
            else:
                catotal[i['category']] = catotal[i['category']] + i['amount']
        print(f'total expense by category is {catotal}')
    else:
        print('empty list')

def delete_expense(expense_lst):
    if expense_lst:
        while True:
            try:
                expense_number = int(input('enter the expense number to be deleted: '))
                if expense_number not in range(1, len(expense_lst)+1):
                    print(f'enter number from 1 to {len(expense_lst)}')
                else:
                    while True:
                        ans = input(f'are you sure that you want to delete expense number {expense_number}, (y/n): ')
                        if ans.lower().strip() == 'y':
                            expense_lst.pop(expense_number - 1)
                            print('expense has been deleted')
                            save_expenses(expense_lst)
                            break
                        elif ans.lower().strip() == 'n':
                            break
                        else:
                            print('please enter y or n')
                    break
            except ValueError:
                print(f'enter number from 1 to {len(expense_lst)}')
    else:
        print('empty list')

def save_expenses(expense_lst):
    #import json
    with open('expenses.json', 'w') as f:
        json.dump(expense_lst, f, indent=4)

print('=' * 10, 'EXPENSE TRACKER', '=' * 10, '1. add expense', '2. view expenses', '3. show total expense',
      '4. show expense by category', '5. delete expense', '6. exit')
import json
try:
    with open('expenses.json', 'r') as f:
        data = json.load(f)
    list1 = data
except FileNotFoundError:
    list1 = []
while True:
    while True:
        try:
            task = int(input('select the number from 1 to 6: '))
            if task not in range(1,7):
                print('enter number from 1 to 6')
            else:
                break
        except ValueError:
            print('enter number from 1 to 6')
    if task == 1:
        list1 = add_expense(list1)
    elif task == 2:
        view_expense(list1)
    elif task == 3:
        show_total_expense(list1)
    elif task == 4:
        show_expense_by_category(list1)
    elif task == 5:
        delete_expense(list1)
    else:
        break
