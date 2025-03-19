from config import INPUT_DATA, TODO_LIST_FILE
import os
from datetime import datetime
from utils import actions as acts

def read_data():
    date = datetime.today().strftime('%m-%d-%Y')
    path = f'{INPUT_DATA}/{TODO_LIST_FILE} {date}.txt'
    with open(path, 'r') as file:
        lines = file.readlines()
        number_of_lines = len(lines)
    return lines, number_of_lines

def read_task():
    modify = True
    while modify:
        task = input('Enter the task you want to add: ')
        print(f'The task entered was: {task}')
        modify = acts.confirm()
        if not modify:
            return task

def task_category():
    modify = True
    while modify:
        category = input('What is the category of the new task?: ')
        print(f'The category entered was: {category}')
        modify = acts.confirm()
        if not modify:
            return category

def is_deadline():
    is_deadline = acts.confirm('Does the new task have a deadline? (yes/no): ')
    return is_deadline

def task_deadline():
    correct = False
    while not correct:
        # Manually sets a deadline date
        month = input('Input the deadline month: (01-12) ')
        day = input('Input the deadline day: (1-31) ')
        year = input('Input the deadline year: () ')
        time = input('Input time of day in 24h format: (hh:mm) ')
        try:
            deadline = f'{day}/{month}/{year} {time}'
            print(f'The input date is {deadline}')
            modify = acts.confirm()
            if not modify:
                return deadline
        except ValueError:
            print(f'Please input the deadline again.')
            correct = False
    return deadline

def new_task(task, category, is_deadline, deadline):
    date = datetime.today().strftime('%m-%d-%Y')
    path = f'{INPUT_DATA}/{TODO_LIST_FILE} {date}.txt'
    if not os.path.exists(path):
        mode = 'w'
        # Create the text file if it didn't exist previously
        with open(path, mode=mode) as file:
            file.write('To-Do List ' + date + '\n')
    mode = 'a'
    # Reading of the text file
    number_of_lines = read_data()[1]
    if is_deadline:
        # Writing the task in the text file
        with open(path, mode=mode) as file:
            file.write(f'{str(number_of_lines)}. ({category}) {task}. Deadline: {deadline} \n')
    else:
        with open(path, mode=mode) as file:
            file.write(f'{str(number_of_lines)}. ({category}) {task}. Deadline: N/A \n')

def remove_task():
    goback = acts.show_selection_bckmenu(2)
    if goback:
        return
    date = datetime.today().strftime('%m-%d-%Y')
    path = f'{INPUT_DATA}/{TODO_LIST_FILE} {date}.txt'
    if not os.path.exists(path):
        print('There is not a To-Do List of today yet.')
    else:
        # Reading of the text file
        lines = read_data()[0]
        number_of_lines = read_data()[1]
        if number_of_lines == 1:
            print("The To-Do List is empty.")
        else:
            not_modify, correct = False, False
            while not not_modify and not correct:
                print('You are about to remove a task.')
                print("Current tasks:")
                # Printing all tasks in console
                n = 0
                for i in lines:
                    if n > 0:
                        print(f'{i}')
                    n += 1
                try:
                    task_index = int(input("Enter the number of the task you want to remove: "))
                except ValueError:
                    print('Please select a valid option')
                    correct = False
                    continue
                try:
                    print(f'The task selected to be removed is {lines[task_index]}.')
                except IndexError:
                    print("Invalid task number. Please enter a number whitin the list.")
                    correct = False
                    continue
                not_modify = acts.confirm('Are you sure this is the one you want to erase? (yes/no): ')
                if not_modify:
                    del lines[task_index]
                    # Rewriting the text file
                    for i in range(len(lines)):
                        if i > task_index:
                            lines[i] = lines[i].replace(f'{i}', f'{i-1}')
                    mode = 'w'
                    with open(path, mode=mode) as file:
                        file.writelines(lines)
                    print('Task removed successfully!')
                    not_modify = True
                else:
                    exit = acts.confirm('Do you want to go back to the main menu? (yes/no): ')
                    not_modify = True

def show_all_tasks():
    goback = acts.show_selection_bckmenu(3)
    if goback:
        return
    date = datetime.today().strftime('%m-%d-%Y')
    path = f'{INPUT_DATA}/{TODO_LIST_FILE} {date}.txt'
    if not os.path.exists(path):
        print('There is not a To-Do List of today yet.')
    else:
        lines = read_data()[0]
        number_of_lines = read_data()[1]
        if number_of_lines == 1:
            print("The To-Do List is empty.")
        else:
            print('You selected to view all of your tasks. Here they are:')
            n = 0
            for i in lines:
                if n > 0:
                    print(f'{i}')
                n += 1
