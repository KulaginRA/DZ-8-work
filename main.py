
class Contact:
    def __init__(self, last_name, first_name, patronymic, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic} | {self.phone_number}"

class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        for index, contact in enumerate(self.contacts, start=1):
            print(f"{index}. {contact}")

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.last_name.lower() or query.lower() in contact.first_name.lower()]
        return results

    def edit_contact(self, index, new_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = new_contact
            print("Контакт успешно обновлён.")
        else:
            print("Некорректный индекс.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]
            print("Контакт успешно удалён.")
        else:
            print("Некорректный индекс.")

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            for contact in self.contacts:
                file.write(f"{contact.last_name}|{contact.first_name}|{contact.patronymic}|{contact.phone_number}\n")

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                last_name, first_name, patronymic, phone_number = line.strip().split('|')
                self.add_contact(Contact(last_name, first_name, patronymic, phone_number))

    def copy_contact_to_file(self, source_filename, destination_filename, line_number):
        try:
            with open(source_filename, 'r', encoding='utf-8') as source_file:
                lines = source_file.readlines()
                if 1 <= line_number <= len(lines):
                    contact_line = lines[line_number - 1]
                    with open(destination_filename, 'a', encoding='utf-8') as dest_file:
                        dest_file.write(contact_line)
                    print("Контакт успешно скопирован.")
                else:
                    print("Некорректный номер строки.")
        except FileNotFoundError:
            print("Исходный файл не найден.")

def main():
    phone_book = PhoneBook()

    while True:
        print("\n1. Добавить контакт")
        print("2. Показать все контакты")
        print("3. Поиск контакта")
        print("4. Редактировать контакт")
        print("5. Удалить контакт")
        print("6. Сохранить в файл")
        print("7. Загрузить из файла")
        print("8. Копировать контакт в другой файл")
        print("9. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            patronymic = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            contact = Contact(last_name, first_name, patronymic, phone_number)
            phone_book.add_contact(contact)

        elif choice == '2':
            phone_book.display_contacts()

        elif choice == '3':
            query = input("Введите имя или фамилию для поиска: ")
            results = phone_book.search_contact(query)
            if results:
                for contact in results:
                    print(contact)
            else:
                print("Контакты не найдены.")

        elif choice == '4':
            index = int(input("Введите номер контакта для редактирования: ")) - 1
            if 0 <= index < len(phone_book.contacts):
                last_name = input("Введите новую фамилию: ")
                first_name = input("Введите новое имя: ")
                patronymic = input("Введите новое отчество: ")
                phone_number = input("Введите новый номер телефона: ")
                new_contact = Contact(last_name, first_name, patronymic, phone_number)
                phone_book.edit_contact(index, new_contact)
            else:
                print("Некорректный индекс.")

        elif choice == '5':
            index = int(input("Введите номер контакта для удаления: ")) - 1
            phone_book.delete_contact(index)

        elif choice == '6':
            filename = input("Введите имя файла для сохранения: ")
            phone_book.save_to_file(filename)
            print("Данные сохранены.")

        elif choice == '7':
            filename = input("Введите имя файла для загрузки: ")
            phone_book.load_from_file(filename)
            print("Данные загружены.")
        
        elif choice == '8':
            source_file = input("Введите имя исходного файла: ")
            destination_file = input("Введите имя целевого файла: ")
            line_number = int(input("Введите номер строки для копирования: "))
            phone_book.copy_contact_to_file(source_file, destination_file, line_number)

        elif choice == '9':
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()
