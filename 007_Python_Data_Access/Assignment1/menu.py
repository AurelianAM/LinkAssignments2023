import sys
import os

class Menu():
    OPTIONS = {
        '1' : 'Show all movies',
        '2' : 'Insert new movie',
        '3' : 'Add genre to existing movie',
        '4' : 'Exit'
    }

    def show(self):
        os.system('cls')
        for key, value in Menu.OPTIONS.items():
            print(f'{key} - {value}')
    @property
    def get_option(self):
        option = input('Choose an option: ')
        if option in list(Menu.OPTIONS.keys())[:-1]:
            return option
        else:
            print('Goodbye!')
            sys.exit()

if __name__ == '__main__':
    menu = Menu()
    menu.show()
    print(menu.get_option)