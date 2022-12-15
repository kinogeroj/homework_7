# Модуль просмотра данных справочника

import os

import logger

file_name = 'phonebook.txt'

def show_main_menu():

    ' Функция показывает главное меню телефонного справочника '

    os.system('cls')

    print('\n      Меню телефонного справочника\n'+
          '----------------------------------------\n'+
          'Введите 1, 2, 3 или 4:\n'+
          'Введите 1, чтобы отобразить все контакты\n' +
          'Введите 2, чтобы добавить новый контакт\n'+
          'Введите 3 для поиска контактов по имени\n'+
          'Введите 4, чтобы выйти из справочника\n'+
          '----------------------------------------')
    
    choice = input('Введите пункт меню: ')
    
    if choice == '1':

        logger.show_contacts()
        
        input('Нажмите Enter, чтобы продолжить ...')
        
        show_main_menu()
    
    elif choice == '2':
    
        logger.enter_contact_record()

        input('Нажмите Enter, чтобы продолжить ...')

        show_main_menu()
    
    elif choice == '3':

        logger.search_contact_record()

        input('Нажмите Enter, чтобы продолжить ...')

        show_main_menu()
    
    elif choice== '4':
        
        exit
    
    else:
        
        print('Неправильный ввод, пожалуйста введите пункт от 1 до 4.\n')
        
        input('Нажмите Enter, чтобы продолжить ...')
        
        show_main_menu()