import sys
import os


class Menu():
    OPTIONS = {
        '1': 'Show all books',
        '2': 'Insert new book',
        '3': 'Search for a book',
        '4': 'Search by year',
        '5': 'Exit'
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
