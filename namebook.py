def find_by_lastname(phone_book, last_name):
    results = [surename for surename in phone_book if surename['Фамилия'].strip() == last_name.strip()]
    return results if results else 'Абонент с такой фамилией не найден.'

def find_by_number(phone_book, phone_number):
    results = [pnumber for pnumber in phone_book if pnumber['Телефон'].strip() == phone_number.strip()]
    return results if results else 'Уточните номер телефона.'

def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    new_data = user_data.split(',')

    if len(new_data) == len(fields):
        record = dict(zip(fields, [item.strip() for item in new_data]))
        phone_book.append(record)
        print('Новый абонент успешно добавлен.')
    else:
        print('Ошибка: Неверное количество данных при добавлении абонента.')
        
def change_number(phone_book, last_name, new_number):
    for contact in phone_book:
        if contact['Фамилия'].strip() == last_name.strip():
            contact['Телефон'] = new_number.strip()
            print(f'Номер телефона для абонента {last_name} успешно изменен.')
            return
    print(f'Абонент с фамилией {last_name} не найден.')

def delete_by_lastname(phone_book, last_name):
    for idx, contact in enumerate(phone_book):
        if contact['Фамилия'].strip() == last_name.strip():
            del phone_book[idx]
            print(f'Абонент с фамилией {last_name} успешно удален.')
            return
    print(f'Абонент с фамилией {last_name} не найден. Ничего не удалено.')

def copy_data(destination_file, line_number):
    with open('phon.txt', 'r', encoding='utf-8') as source:
        lines = source.readlines()
    
    with open(destination_file, 'a', encoding='utf-8') as destination:
        destination.write(lines[line_number - 1])




def work_with_phonebook():
	

    choice=show_menu()

    phone_book=read_txt("phon.txt")

    while (choice!=9):

        if choice==1:
            print(phone_book)
        elif choice==2:
            last_name=input('Введите фамилию: ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            phone_number=input('Введите телефонный номер: ')
            print(find_by_number(phone_book,phone_number))
        elif choice == 4:
            user_data = input('Введите данные нового абонента в формате "Фамилия, Имя, Телефон, Описание": ')
            add_user(phone_book, user_data)
            write_txt('phon.txt', phone_book)
        elif choice == 5:
            last_name = input('Введите фамилию абонента, номер телефона которого нужно изменить: ')
            new_number = input('Введите новый номер телефона: ')
            change_number(phone_book, last_name, new_number)
            write_txt('phon.txt', phone_book)
        elif choice == 6:
            last_name = input('Введите фамилию абонента, которого нужно удалить: ')
            delete_by_lastname(phone_book, last_name)
            write_txt('phon.txt', phone_book)
        elif choice == 7:
            write_txt('phon.txt', phone_book)
            print("Справочник успешно сохранен в текстовом формате.")
        elif choice == 8:
            line_number = int(input("Введите номер строки для копирования: "))
            copy_data('destination_file.txt', line_number)
            print("Данные успешно скопированы.")


        choice=show_menu()


def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Изменить номер телефона по фамилии\n"
          "6. Удалить абонента по фамилии\n"
          "7. Сохранить справочник в текстовом формате\n"
          "8. Копирование данных выбранной строки\n"
          "9. Закончить работу")

    choice = input("Введите номер действия: ")
    while not choice.isdigit() or int(choice) not in range(1, 10):  # Проверяем, что введенное значение в диапазоне от 1 до 8
        print("Пожалуйста, выберите номер из списка действий.")
        choice = input("Введите номер действия: ")

    return int(choice)




#Иванов,       Иван ,   111,  описание Иванова
#Петров,      Петр ,    222,  описание Петрова
#Васичкина , Василиса , 333 , описание Васичкиной
#Питонов,    Антон,     777,    умеет в Питон




def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            data = line.strip().split(',')
            if len(data) == len(fields):  # Проверка, что количество полей совпадает
                record = dict(zip(fields, [item.strip() for item in data]))
                phone_book.append(record)

    return phone_book



def write_txt(filename, phone_book):

    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():

                s = s + v + ','

            phout.write(f'{s[:-1]}\n')



work_with_phonebook()