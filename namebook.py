import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog

# Функции телефонного справочника
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
        result = 'Новый абонент успешно добавлен.'
    else:
        result = 'Ошибка: Неверное количество данных при добавлении абонента.'
    return result
        
def change_number(phone_book, last_name, new_number):
    for contact in phone_book:
        if contact['Фамилия'].strip() == last_name.strip():
            contact['Телефон'] = new_number.strip()
            return f'Номер телефона для абонента {last_name} успешно изменен.'
    return f'Абонент с фамилией {last_name} не найден.'

def delete_by_lastname(phone_book, last_name):
    for idx, contact in enumerate(phone_book):
        if contact['Фамилия'].strip() == last_name.strip():
            del phone_book[idx]
            return f'Абонент с фамилией {last_name} успешно удален.'
    return f'Абонент с фамилией {last_name} не найден. Ничего не удалено.'

def copy_data(destination_file, line_number):
    with open('phon.txt', 'r', encoding='utf-8') as source:
        lines = source.readlines()
    
    with open(destination_file, 'a', encoding='utf-8') as destination:
        destination.write(lines[line_number - 1])
    return "Данные успешно скопированы."

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
    with open(filename, 'w', encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s = ''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

# Графический интерфейс
class PhoneBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Телефонный Справочник")
        self.phone_book = read_txt("phon.txt")
        
        # Меню
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Файл", menu=self.file_menu)
        self.file_menu.add_command(label="Сохранить", command=self.save_to_file)
        self.file_menu.add_command(label="Выйти", command=root.quit)
        
        # Кнопки
        self.display_button = tk.Button(root, text="Отобразить весь справочник", command=self.display_contacts)
        self.display_button.pack(fill=tk.X)
        
        self.find_by_lastname_button = tk.Button(root, text="Найти абонента по фамилии", command=self.find_by_lastname)
        self.find_by_lastname_button.pack(fill=tk.X)
        
        self.find_by_number_button = tk.Button(root, text="Найти абонента по номеру телефона", command=self.find_by_number)
        self.find_by_number_button.pack(fill=tk.X)
        
        self.add_user_button = tk.Button(root, text="Добавить абонента", command=self.add_user)
        self.add_user_button.pack(fill=tk.X)
        
        self.change_number_button = tk.Button(root, text="Изменить номер телефона по фамилии", command=self.change_number)
        self.change_number_button.pack(fill=tk.X)
        
        self.delete_by_lastname_button = tk.Button(root, text="Удалить абонента по фамилии", command=self.delete_by_lastname)
        self.delete_by_lastname_button.pack(fill=tk.X)
        
        self.copy_data_button = tk.Button(root, text="Копирование данных выбранной строки", command=self.copy_data)
        self.copy_data_button.pack(fill=tk.X)
        
    def display_contacts(self):
        contacts = '\n'.join([f"{contact['Фамилия']}, {contact['Имя']}, {contact['Телефон']}, {contact['Описание']}" for contact in self.phone_book])
        messagebox.showinfo("Телефонный Справочник", contacts)
     
    def find_by_lastname(self):
        last_name = simpledialog.askstring("Найти абонента по фамилии", "Введите фамилию:")
        result = find_by_lastname(self.phone_book, last_name)
        messagebox.showinfo("Результаты поиска", result)
    
    def find_by_number(self):
        phone_number = simpledialog.askstring("Найти абонента по номеру телефона", "Введите номер:")
        result = find_by_number(self.phone_book, phone_number)
        messagebox.showinfo("Результаты поиска", result)
    
    def add_user(self):
        user_data = simpledialog.askstring("Добавить абонента", "Введите данные (Фамилия, Имя, Телефон, Описание):")
        result = add_user(self.phone_book, user_data)
        messagebox.showinfo("Добавление абонента", result)
    
    def change_number(self):
        last_name = simpledialog.askstring("Изменить номер по фамилии", "Введите фамилию:")
        new_number = simpledialog.askstring("Новый номер", "Введите новый номер:")
        result = change_number(self.phone_book, last_name, new_number)
        messagebox.showinfo("Изменение номера", result)
    
    def delete_by_lastname(self):
        last_name = simpledialog.askstring("Удалить абонента по фамилии", "Введите фамилию:")
        result = delete_by_lastname(self.phone_book, last_name)
        messagebox.showinfo("Удаление абонента", result)
    
    def copy_data(self):
        line_number = simpledialog.askinteger("Копировать данные", "Введите номер строки:")
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if filename and line_number is not None:
            result = copy_data(filename, line_number)
            messagebox.showinfo("Копирование данных", result)
    
    def save_to_file(self):
        write_txt("phon.txt", self.phone_book)
        messagebox.showinfo("Сохранение", "Справочник успешно сохранен в текстовом формате.")

root = tk.Tk()
app = PhoneBookApp(root)
root.mainloop()
