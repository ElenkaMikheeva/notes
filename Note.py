from datetime import datetime


class Note:
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
    id = 0
    title = ""
    body = ""
    updated_at = None

    def __init__(self, title="", body="", note_dict=None):
        if note_dict is not None:
            self.id = note_dict["id"]
            self.title = note_dict["title"]
            self.body = note_dict["body"]
            self.updated_at = datetime.strptime(note_dict["updated_at"], self.DATETIME_FORMAT)
        else:
            self.title = title
            self.body = body
            self.updated_at = datetime.now()

    def __str__(self):
        return f"""ID: {self.id}
Заголовок: {self.title}
Заметка: {self.body}
Последнее редактирование: {self.updated_at.strftime(self.DATETIME_FORMAT)}"""

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "body": self.body,
            "updated_at": self.updated_at.strftime(self.DATETIME_FORMAT),
        }

    def show_short(self):
        return str(self.id) + ": " + self.title

    def show_middle(self):
        return f"Заголовок: {self.title}\nЗаметка: {self.body}"
