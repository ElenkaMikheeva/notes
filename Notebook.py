import json
import os

import Note


class Notebook:
    filename = ""

    def __init__(self, filename):
        if not os.path.exists(filename):
            with open(filename, "w") as file:
                file.write("[]")
        elif not os.path.isfile(filename):
            raise Exception(filename + " is not file")
        self.filename = filename

    def new(self, note):
        if note.id == 0:
            note.id = self.next_id()
        notes = self.read_all()
        notes.append(note)
        self.save(notes)

    def save(self, notes):
        json_data = []
        for note in notes:
            json_data.append(note.to_json())
        with open(self.filename, "w") as file:
            json.dump(json_data, file, indent=2)

    def next_id(self):
        max_id = 0
        notes = self.read_all()
        for note in notes:
            if note.id > max_id:
                max_id = note.id
        return max_id + 1

    def read_all(self):
        with open(self.filename, "r") as file:
            dicts = json.load(file)
        notes = []
        for d in dicts:
            notes.append(Note.Note(note_dict=d))
        return notes

    def list(self, date):
        all_notes = self.read_all()
        if date is None:
            return all_notes

        notes = []
        date_format = "%Y%m%d"
        date_str = date.strftime(date_format)
        for note in all_notes:
            if note.updated_at.strftime(date_format) == date_str:
                notes.append(note)

        return notes

    def delete(self, note_id):
        notes = self.read_all()
        for i, note in enumerate(notes):
            if note.id == note_id:
                notes.pop(i)
                self.save(notes)
                return True
        return False

    def get(self, note_id):
        notes = self.read_all()
        for note in notes:
            if note.id == note_id:
                return note
        return None

    def replace(self, new_note):
        notes = self.read_all()
        for i, note in enumerate(notes):
            if note.id == new_note.id:
                notes[i] = new_note
                self.save(notes)
                return
