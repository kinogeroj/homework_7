# Модуль работы с данными телефонного справочника

file_name = 'phonebook.txt'

def search_contact_record() -> str:

    """ Фунцкия ищет контакт в телефонном справочнике """

    search_name = input('Введите имя контакта, который Вы ищите: ')
    
    rem_name = search_name[1:]
    
    first_char = search_name[0]
    
    search_name = first_char.upper() + rem_name
    
    with open('phonebook.txt', 'r', encoding = 'utf-8') as f:
        file_contents = f.readlines()
     
    found = False
     
    for line in file_contents:
        
        if search_name in line:

            print('Вы искали контакт: ', end = ' ')
            
            print (line)
            
            found = True
            
            break
    
    if  found == False:
        
        print('К сожалению, контакт с именем ' + search_name + 'не найден.')

def input_fname() -> str:

    """ Функция подставляет верхний регистр к Имени """

    fname = input('Введите имя контакта: ')

    rem_fname = fname[1:]
    
    first_char = fname[0]
    
    return first_char.upper() + rem_fname

def input_lname() -> str:

    """ Функция подставляет верхний регистр к Фамилии """
    
    lname = input('Введите фамилию контакта: ')
    
    rem_lname = lname[1:]
    
    first_char = lname[0]
    
    return first_char.upper() + rem_lname

def enter_contact_record() -> str:

    """ Функция внесения записи в справочник """
   
    first = input_fname()

    last = input_lname()

    phone = input('Введите телефонный номер: ')

    contact = ('[' + first + ' ' + last + ', ' + phone + ']\n')

    with open('phonebook.txt', 'a', encoding = 'utf-8') as f:
        f.writelines(contact)

    print( 'Контакт \n ' + contact + 'добавлен в справочник.')

def show_contacts() -> str:

    """Функция отображает телефонный справочник"""

    with open('phonebook.txt', 'r', encoding='utf-8') as f:
        file_contents = f.read()

        if len(file_contents) == 0:
            
            print('Телефонный справочник пуст')
        
        else:
            
            print (file_contents)