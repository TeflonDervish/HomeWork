from csv import DictReader, DictWriter
from os.path import exists
import os


class LenNumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


class CsvReader:

    def __init__(self, filename):
        self.file_name = filename

    @staticmethod
    def add_info():
        print("Введите данные для добавления в справочник:")
        first_name = input("Введите имя: ")
        last_name = input("Введите фамилию: ")
        is_valid_number = False

        while not is_valid_number:
            try:
                phone_number = int(input("Введите номер телефона: "))
                if len(str(phone_number)) != 11:
                    raise LenNumberError("Длина телефонного номера должна составлять 11")
                is_valid_number = True
                break
            except LenNumberError as err:
                print(err)
                continue
            except ValueError:
                print("Номер может содержать только цифры")
                continue

        return [first_name, last_name, phone_number]

    def create_file(self):

        with open(self.file_name, 'w', encoding='utf-8') as data:
            f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
            f_writer.writeheader()

    def read_file(self):

        with open(self.file_name, 'r', encoding='utf-8') as data:
            f_reader = DictReader(data)
            return list(f_reader)

    def write_file(self):
        res = self.read_file()
        user_data = self.add_info()

        for el in res:
            if el['телефон'] == str(user_data[2]):
                print("Пользователь с таким телефоном уже существует")
                return

        new_user = {'имя': user_data[0], 'фамилия': user_data[1], 'телефон': user_data[2]}
        res.append(new_user)

        with open(file_name, 'w', encoding='utf-8', newline='') as data:
            f_writer = DictWriter(data, fieldnames=['имя', 'фамилия', 'телефон'])
            f_writer.writeheader()
            f_writer.writerows(res)


file_name = 'phone.csv'


def main():
    csv_reader = CsvReader(file_name)
    while True:
        command = input("Введите команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                csv_reader.create_file()
            csv_reader.write_file()
        elif command == 'r':
            if not exists(file_name):
                print("Файл не создан. Создайте файл.")
                continue
            print(*csv_reader.read_file())
        elif command == 'c':
            pass


if __name__ == "__main__":
    main()
