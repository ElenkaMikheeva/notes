from datetime import datetime
import Notebook
import Note

notebook = Notebook.Notebook("notebook.json")
err_text = "ID должен быть целым положительным числом"


def get_command():
    return input("Введите команду (help - список команд): ")


def print_help():
    print("""
help - показать это сообщение
exit - завершить работу программы
show - показать заметку
edit - редактировать заметку
new  - создать заметку
del  - удалить заметку
list - список заметок""")


def new():
    title = input("Введите заголовок: ")
    body = input("Введите заметку: ")
    note = Note.Note(title=title, body=body)
    notebook.new(note)


def get_id_and_find_note():
    try:
        note_id = int(input("Введите ID заметки: "))
    except ValueError:
        raise ValueError(err_text)
    if note_id <= 0:
        raise ValueError(err_text)

    note = notebook.get(note_id)
    if note is None:
        raise ValueError(f"Заметка с ID {note_id} не найдена")

    return note


def show():
    try:
        print(get_id_and_find_note())
    except ValueError as error:
        print(error)


def edit():
    try:
        note = get_id_and_find_note()
    except ValueError as error:
        print(error)
        return

    print(f"Заметка с ID {note.id} сейчас содержит:\n{note.show_middle()}")

    title = input("Введите новый заголовок (Enter - не менять): ")
    body = input("Введите новую заметку (Enter - не менять): ")
    if title == "" and body == "":
        print("Ничего не изменилось")
        return

    if title != "":
        note.title = title
    if body != "":
        note.body = body
    note.updated_at = datetime.now()

    notebook.replace(note)


def delete():
    try:
        note_id = int(input("Введите ID заметки: "))
    except ValueError:
        print(err_text)
        return
    if note_id <= 0:
        print(err_text)
        return

    if not notebook.delete(note_id):
        print(f"Заметка с ID {note_id} не найдена")


def notes_list():
    date = None

    date_str = input("Введите дату в формате ГГГГ-ММ-ДД (Enter - вывести все заметки): ")
    if date_str != "":
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Неверный формат даты")
            return

    notes = notebook.list(date)
    if len(notes) == 0:
        print("Ничего не найдено")
        return

    for note in notes:
        print(note.show_short())


while True:
    command = get_command().lower()

    if command == "exit" or command == "учше":
        break

    elif command == "help" or command == "рудз":
        print_help()

    elif command == "show" or command == "ырщц":
        show()

    elif command == "edit" or command == "увше":
        edit()

    elif command == "new" or command == "туц":
        new()

    elif command == "del" or command == "вуд":
        delete()

    elif command == "list" or command == "дшые":
        notes_list()

    else:
        print("Неизвестная команда")
