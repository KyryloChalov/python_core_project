from collections import UserDict
from constants import RED, GRAY, CYAN, MAGENTA, RESET, LEN_OF_NAME_FIELD
from datetime import datetime
import os.path
import pickle
from classes import Field


class NoteError(Exception):
    ...


class Title(Field):
    pass


class Content(Field):
    def __init__(self, content):
        super().__init__(content)

    def edit_content(self, new_content):
        self.value = new_content

    def lower(self):
        return self.value.lower()


class Tags(Field):
    def __init__(self, tags=None):
        super().__init__(tags or [])

    def add_tags(self, new_tags):
        self.value.extend(new_tags)
        # self.value += new_tags

    def __iter__(self):
        return iter(self.value)


class Note:
    def __init__(self, title, content, tags=None):
        self.title = Title(title)
        self.content = Content(content)
        self.tags = Tags(tags)

    def add_note(self, title, content):
        self.notes[title] = content
        return f"note {self.title} has been successfully added \n\t{self}"

    def edit_note(self, title, new_content):
        if title in self.notes:
            self.notes[title] = new_content
            return f"Note '{title}' edited."
        else:
            return f"Note '{title}' not found."

    def delete_note(self, title):
        if title in self.notes:
            del self.notes[title]
            return f"Note '{title}' deleted."
        else:
            return f"Note '{title}' not found."

    def __str__(self) -> str:
        tags_str = "".join(t.value for t in self.tags)
        tags_str = f"Tags {tags_str}" if tags_str else ""
        return f"Title: {self.title} Text: {self.content} {tags_str}"


class NotesBook(UserDict):
    
    def __init__(self):
        super().__init__()

    def add_tags(self, title, tags):  # метод для додавання тегів
        if title in self.data:
            self.data[title].tags.extend(tags)
            return f"Tags {', '.join(tags)} added to the note with title '{title}'."
        else:
            raise NoteError(f"Note with title '{title}' not found.")

    def search_notes_by_tag(self, tag, sort_by_keywords=False):
        matching_notes = [
            note
            for note in self.data.values()
            if tag.lower() in map(str.lower, note.tags)
        ]
        if sort_by_keywords:
            matching_notes.sort(key=lambda note: note.keywords)
        if matching_notes:
            return "\n".join(map(str, matching_notes))
        else:
            return "No notes found with the specified tag."

    def search_notes(self, keyword):
        result = []
        for title, content in self.data.items():
            if keyword.lower() in title.lower() or keyword.lower() in content.lower():
                result.append(f"Title: {title}\nContent: {content}\n")
        return result if result else "No matching notes found."

    def read_notes_from_file(self, fn):
        if os.path.exists(fn):
            with open(fn, "rb") as fh:
                self = pickle.load(fh)
            self.data = dict(sorted(self.items()))
        print(f"{GRAY}the notes has been successfully restored{RESET}")
        return self

    def write_notes_to_file(self, fn):
        with open(fn, "wb") as fh:
            pickle.dump(self, fh)
        return f"{GRAY}the notes has been saved successfully{RESET}"

    def iterator(self, n=None):
        counter = 0
        while counter < len(self):
            yield list(self.values())[counter : counter + n]
            counter += n
