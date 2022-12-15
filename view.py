# Модуль просмотра данных справочника

import os

import logger

file_name = 'phonebook.txt'

def show_main_menu():

    ' Функция показывает главное меню телефонного справочника '

    os.system('cls')

    print('\n   Меню телефонного справочника\n'+
          '-------------------------------------\n'+
          'Введите 1,2,3 или 4:\n'+
          'Введите 1, чтобы отобразить все контакты\n' +
          'Введите 2, чтобы добавить новый контакт\n'+
          'Введите 3 для поиска контактов\n'+
          'Введите 4, чтобы выйти из справочника\n'+
          '-------------------------------------')
    
    choice = input('Введите пункт меню: ')
    
    if choice == '1':

        show_contacts()
        
        ent = input('Нажмите Enter, чтобы продолжить ...')
        
        show_main_menu()
    
    elif choice == '2':
    
        logger.enter_contact_record()

        ent = input('Нажмите Enter, чтобы продолжить ...')

        show_main_menu()
    
    elif choice == '3':
        
        logger.search_contact_record()

        ent = input('Нажмите Enter, чтобы продолжить ...')

        show_main_menu()
    
    elif choice== '4':
        
        exit
    
    else:
        
        print('Неправильный ввод, пожалуйста введите пункт от 1 до 4.\n')
        
        ent = input('Нажмите Enter, чтобы продолжить ...')
        
        show_main_menu()

def show_contacts() -> str:

    """Функция отображает телефонный справочник"""

    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        file_contents = f.read()

        if len(file_contents) == 0:
            print('Телефонный справочник пуст')
        
        else:
            print (file_contents)