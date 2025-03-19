from config import MENU

def welcome()->None:
    print('\nWelcome to your To-Do List')
    print('---------------------------------------------------------\n')

    print('Please select an action:')
    # Print main menu
    menu_pp = ''.join([f'{i[0]}. {i[1]}\n' for i in MENU.items()])
    print(menu_pp)

def get_selection()->int:
    selection = 0
    while selection not in range(1, len(MENU.keys())+1):
        try:
            options = f'1-{len(MENU.keys())}'
            selection = int(input(f'Please enter the number of the action you want to select ({options}): '))
        except ValueError:
            selection = 0
        print(selection)
        if selection not in range(1, len(MENU.keys())+1):
            print('ERROR: Input invalid!')
    return selection

# Check if the user wants to continue or to go back in the menu
def show_selection_bckmenu(selection:int, msg='If you want to go back to the previous menu input 0; if you want to continue press enter.\n'):
    
    selection_txt = MENU[selection]
    print(f'\n-------------------------{selection_txt}-------------------------\n')
    confirm = input(msg)
    return True if confirm=='0' else False

# Verify with the user that the data entered were correct
def confirm(msg='Do you want to change your input? (yes/no): '):
    modify = input(msg)
    correct = True if modify.lower() in ['yes', 'y', 'true', 't'] or modify==1 else False
    return correct
