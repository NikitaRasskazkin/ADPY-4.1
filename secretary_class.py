class Library:
    def __init__(self):
        self.documents = [
            {"type": "passport", "number": "2207_876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ]
        self.directories = {
            '1': ['2207_876234', '11-2', '5455_028765'],
            '2': ['10006'],
            '3': []
        }

    def document_owner_func(self, document_number: str):
        """(p) команда, которая спросит номер документа и выведет имя человека, которому он принадлежит
        document_owner ["номер документа"]"""
        for document in self.documents:
            if document['number'] == document_number:
                name = document["name"]
                print(f'Докумен № \"{document_number}\" принадлежит: {name}')
                break
        else:
            print(f'Документ с номером \"{document_number}\" не найден')
            name = None
        return name

    def shelf_number_func(self, document_number: str, is_print=True):
        """(s) команда, которая спросит номер документа и выведет номер полки, на которой он находится
        Возвращаемое значение №полки, или None если документ отсутствует в directories
        shelf_number <'номер документа'> [bool значение]
        Необязательный второй аргумент не будет выводить информация на экран про значении False. Default = True"""
        is_not_found = True
        found_shelf_number = None
        for number, docs in self.directories.items():
            if document_number in docs:
                if is_print:
                    print(f'Докумен № {document_number} лежит на полке: {number}')
                is_not_found = False
                found_shelf_number = number
                break
        if is_not_found and is_print:
            print(f'Документ с номером \"{document_number}\" не найден')
        return found_shelf_number

    def show_docs_func(self):
        """(l) команда, которая выведет список всех документов в формате <type> <number> <name>
        Параметры отсутствуют"""
        for document in self.documents:
            print(f'{document["type"]} \"{document["number"]}\" \"{document["name"]}\"')

    def add_doc_func(self, doc_number, doc_type, name, shelf_number):
        """(a) команда, которая добавит документ в каталог
        add_doc_func [номе документа][тип документа][имя][номер полки]"""

        def add_document():
            self.directories[shelf_number].append(doc_number)
            self.documents.append({"type": doc_type, "number": doc_number, "name": name})

        shelf_number = str(shelf_number)
        if shelf_number in self.directories and doc_number != '' and name != '':
            doc_number = str(doc_number)
            doc_type = str(doc_type)
            name = str(name)
            if self.shelf_number_func(doc_number, False) is None:
                add_document()
                print(f'Документ № {doc_number} добавлен')
            else:
                self.delete_doc_func(doc_number)
                add_document()
                print('База данных обновлена')
        else:
            print(f'Данные введены не корректно')

    def delete_doc_func(self, doc_number):
        """delete_doc_func <номер документа> - удаляет документ с указанным номером"""
        doc_number = str(doc_number)
        for index, document in enumerate(self.documents):
            if document['number'] == doc_number:
                del self.documents[index]
                self.directories[self.shelf_number_func(doc_number, False)].remove(doc_number)
                break
        else:
            print(f'Документ № \"{doc_number}\" не найден')

    def move_doc_func(self, doc_number, new_shelf_number):
        """move_doc_func <номер документа> <номер полки> - переносит документ на указанную полку"""
        past_shelf_number = self.shelf_number_func(doc_number, False)
        if past_shelf_number is None:
            print(f'Документ № {doc_number} не найден')
        elif new_shelf_number not in self.directories:
            print(f'Полки № {new_shelf_number} не существует')
        else:
            self.directories[past_shelf_number].remove(doc_number)
            self.directories[new_shelf_number].append(doc_number)
            print(f'Документ № {doc_number} перенесён с полки {past_shelf_number} на полку {new_shelf_number}')

    def add_shelf(self, shelf_number):
        """add_shelf <номер новой полки> - добавляет новую полку"""
        if shelf_number in self.directories:
            print(f'Полка № {shelf_number} уже существует')
        else:
            print(f"Добавить полку № {shelf_number}?\n"
                  f"\"Y\" - да, добавить. \"N\" - нет, не добавлять")
            command = self.read_line()[0]
            if command == 'y':
                self.directories.update({str(shelf_number): []})
                print(f'Полка № {shelf_number} добавлена')
            elif command == 'n':
                print(f'Добавление полки отменено')
            else:
                self.error_incorrect_command(command)
                print(f'Добавление полки отменено')

    def show_directories_func(self):
        for key, value in self.directories.items():
            print(f'Полка № {key}: {value}')

    @staticmethod
    def read_line():
        """считывает введённую пользователем строку. Возвращает список слов прочитаной строки"""
        while True:
            line = input('> ').lower()
            if line != '':
                return line.split()

    @staticmethod
    def error_incorrect_command(command):
        """Выводит на экран сообщение об ошибке некорректно введённой комманды"""
        print(f'Ошибка!!! Команды \"{command}\" не существует в данном контексте. Для справки введите \"help\"')

    @staticmethod
    def error_incorrect_arguments():
        """Выводит на экран сообщение об ошибке неверно введённых аргументов команды"""
        print(f'Ошибка!!! Неверное колличество аргументов. Для справки введите \"help\"')

    @staticmethod
    def help_func():
        print('exit - выход из программы\n\n'
              'help - вывод справки\n\n'
              'p <номер документа> -  выведет имя человека, которому он принадлежит документ с данным номером\n\n'
              's <номер документа> - выведет номер полки, на которой на которой находится документ с данным номером\n\n'
              'l - выведет список всех документов\n\n'
              'a <номер документа> <тип документа> <имя владельцы> <номер полки> - '
              'команда, которая добавит документ в каталог\n\n'
              'd <номер документа> - удаляет документ с указанным номером\n\n'
              'as <номер полки> - нодавляет новую полку с указанным номером\n\n'
              'm <номер документа> <номер полки> - переносит документ на указанную полку\n\n'
              'ld - выводит информацию directories')
