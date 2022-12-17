# Модуль контроллера телефонного справочника

import os

import view
import logger

def run() -> str:

    """Функция организует взаимодействие пользователя и модулей"""
    
    os.system('cls')
    
    view.show_main_menu()

    choice = input('Введите пункт меню: ')

    if choice == '1':
        
        logger.show_contacts()
        
        input('Нажмите Enter, чтобы продолжить ...')
        
        run()
    
    elif choice == '2':
    
        logger.enter_contact_record()

        input('Нажмите Enter, чтобы продолжить ...')

        run()
    
    elif choice == '3':

        logger.search_contact_record()

        input('Нажмите Enter, чтобы продолжить ...')

        run()
    
    elif choice== '4':
        
        exit
    
    else:
        
        print('Неправильный ввод, пожалуйста введите пункт от 1 до 4.\n')
        
        input('Нажмите Enter, чтобы продолжить ...')
        
        run()