from secretary_class import Library


if __name__ == '__main__':
    library = Library()
    is_continue_program = True
    while is_continue_program:
        line = library.read_line()
        command = line[0]
        arguments = line[1:]
        if command == 'p':
            if len(arguments) < 1:
                library.error_incorrect_arguments()
                continue
            else:
                library.document_owner_func(arguments[0])
        elif command == 's':
            if len(arguments) < 1:
                library.error_incorrect_arguments()
                continue
            else:
                library.shelf_number_func(arguments[0])
        elif command == 'l':
            library.show_docs_func()
        elif command == 'a':
            if len(arguments) < 4:
                library.error_incorrect_arguments()
                continue
            else:
                library.add_doc_func(arguments[0], arguments[1], arguments[2], arguments[3])
        elif command == 'd':
            if len(arguments) < 1:
                library.error_incorrect_arguments()
                continue
            else:
                library.delete_doc_func(arguments[0])
        elif command == 'm':
            if len(arguments) < 2:
                library.error_incorrect_arguments()
                continue
            else:
                library.move_doc_func(arguments[0], arguments[1])
        elif command == 'as':
            if len(arguments) < 1:
                library.error_incorrect_arguments()
                continue
            else:
                library.add_shelf(arguments[0])
        elif command == 'ld':
            library.show_directories_func()
        elif command == 'help':
            library.help_func()
        elif command == 'exit':
            is_continue_program = False
        else:
            library.error_incorrect_command(command)
