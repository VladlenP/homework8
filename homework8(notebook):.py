def read_txt(filename): 
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Номер', 'Описание']

    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book

def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for entry in phone_book:
            phout.write(','.join(entry.values()) + '\n')

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить всю записную книжку\n"
          "2. Найти абонента по фамилии\n"
          "3. Изменить номер абонента по фамилии\n"
          "4. Удалить абонента из записной книжки\n"
          "5. Найти абонента по номеру телефона\n"
          "6. Добавить нового абонента\n"
          "7. Копировать строку из одного файла в другой\n"
          "8. Завершить работу")
    choice = int(input())
    return choice

def print_result(phone_book):
    for entry in phone_book:
        print(entry)

def find_by_lastname(phone_book, last_name):
    found_entries = [entry for entry in phone_book if entry['Фамилия'] == last_name]
    return found_entries if found_entries else "Абонент с такой фамилией не найден"

def change_number(phone_book, last_name, new_number):
    for entry in phone_book:
        if entry['Фамилия'] == last_name:
            entry['Номер'] = new_number
            return f"Номер абонента {last_name} успешно изменен на {new_number}"
    return f"Абонент с фамилией {last_name} не найден"

def delete_by_lastname(phone_book, last_name):
    deleted_entries = [entry for entry in phone_book if entry['Фамилия'] == last_name]
    phone_book[:] = [entry for entry in phone_book if entry['Фамилия'] != last_name]
    return deleted_entries if deleted_entries else f"Абонент с фамилией {last_name} не найден"

def find_by_number(phone_book, number):
    found_entries = [entry for entry in phone_book if entry['Номер'] == number]
    return found_entries if found_entries else "Абонент с таким номером не найден"

def add_user(phone_book, user_data):
    new_entry = dict(zip(['Фамилия', 'Имя', 'Номер', 'Описание'], user_data.split(',')))
    phone_book.append(new_entry)

def copy_record(source_file, destination_file):
    try:
        line_number = int(input('Введите номер строки для копирования: '))
        with open(source_file, 'r', encoding='utf-8') as source:
            lines = source.readlines()
            if 0 < line_number <= len(lines):
                with open(destination_file, 'a', encoding='utf-8') as destination:
                    destination.write(lines[line_number - 1])
                print('Строка успешно скопирована.')
            else:
                print('Введен некорректный номер строки.')
    except ValueError:
        print('Введен некорректный номер строки.')

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_txt('phonebook.txt')

    while choice != 8:
        if choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Фамилия: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('Фамилия: ')
            new_number = input('Новый номер: ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            last_name = input('Фамилия: ')
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            number = input('Номер: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('Новые данные: ')
            add_user(phone_book, user_data)
            write_txt('phonebook.txt', phone_book)
        elif choice == 7:
            copy_record('phonebook.txt', 'phonebook_copy.txt')
        choice = show_menu()

work_with_phonebook()