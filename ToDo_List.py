import os
import sys
import random
from config import INPUT_DATA, MENU, FAREWELLS
from utils import List_mgmt as list
from utils import actions as acts

# Create the directory where the text files will be saved
if not os.path.exists(INPUT_DATA):
    os.mkdir(INPUT_DATA)



def add_task():
    # Ask if the user wants to continue or not
    goback = acts.show_selection_bckmenu(1)
    if goback:
        return
    print('You are about to add a new task. Before you do it, please input the following data:')
    task = list.read_task()
    category = list.task_category()
    is_deadline = list.is_deadline()
    deadline = None
    if is_deadline:
        deadline = list.task_deadline()
        data = {'task':task,
            'category':category,
            'deadline':deadline}
    else:
        data = {'task':task,
            'category':category,
            'deadline':'N/A'}

    # Show all task data
    input_summary(data)
    save = acts.confirm('Is the data of the task correct? (yes/no):')
    if save:
        list.new_task(task, category, is_deadline, deadline)
    return

def input_summary(data:dict):
    print('Task details...\n')
    tags = {'task':'Task', 
    'category':'Category', 
    'deadline':'Deadline'}
    data_txt = ''.join([f'{tags[i[0]]}: {i[1]}\n' for i in data.items()])
    # Print all data of a task which is about to be written
    print(data_txt)

if __name__ =="__main__":
    goback = True
    while goback:
        acts.welcome()
        selection = acts.get_selection()
        if 'exit' in MENU[selection].lower():
            # Select a farewell randomly
            print(FAREWELLS[random.randint(0, len(FAREWELLS)-1)])
            
            sys.exit()
        # An action is chosen from the menu
        elif selection==1:
            add_task()
        elif selection==2:
            list.remove_task()
        elif selection==3:
            list.show_all_tasks()
        
        if goback:
            continue
    print(FAREWELLS[random.randint(0, len(FAREWELLS)-1)])
