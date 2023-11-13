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

    # def search_notes_by_tag(self, tag, sort_by_keywords=False):
    #     matching_notes = [
    #         f"Title: {title}\nContent: {note['content']}\nTags: {', '.join(note['tags'])}"
    #         for title, note in self.notes.items()
    #         if tag.lower() in map(str.lower, note["tags"])
        #]

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


# notes = NotesBook()


# # @user_error
# def add_tag(*args):
#     title = args[0]
#     tags = args[1:]
#     return notes.add_tags(title, tags)


# # @user_error
# def search_notes_by_tag(*args):
#     tag = args[0]
#     sort_by_keywords = args[1:].lower() == "true" if len(args) > 1 else False
#     return notes.search_notes_by_tag(tag, sort_by_keywords)


# # @user_error
# def add_note(*args):
#     title = args[0]
#     content_start_index = 1
#     tags = []
#     #  теги в аргументах
#     content = " ".join(args[content_start_index:])
#     for i, arg in enumerate(args[content_start_index:], start=content_start_index):
#         if arg.startswith("#"):
#             tag = (
#                 arg.lstrip("#, ").rstrip(", ").replace("#", "")
#             )  # видаляємо # і зайві пробіли
#             tags.append(tag)
#             content = " ".join(args[content_start_index:i])

#     # content = " ".join(args[content_start_index:args.index(f"--tags={+tags[0]}") if tags else len(args)])
#     new_note = Note(title, content, tags)
#     notes.data[title] = new_note
#     return f"Note 'Title: {title} Content:{content} Tags:{', '.join(tags)}' added."


# # @user_error
# def edit_note(title, new_content):
#     # Перевірка наявності тайтлу в notes
#     if title in notes.data:
#         # Змінюємо тільки content
#         notes.data[title].content.edit_content(new_content)
#         return f"Note '{title}' changed. New content: '{new_content}'"
#     else:
#         return f"Нотатка '{title}' не знайдена."



# # @user_error
# def search_notes(keyword, notes):
#     matching_notes = [
#         f"Note 'Title: {title}' Content: {note.content} Tags:{', '.join(note.tags)}"
#         for title, note in notes.items()
#         if keyword.lower() in title.lower() or keyword.lower() in note.content.lower()
#     ]
#     if matching_notes:
#         return "\n".join(matching_notes)
#     else:
#         return "No matching notes found."



# # @user_error
# def delete_note(*args):
#     title = args[0]
#     if title in notes.notes:
#         del notes.notes[title]
#         return f"Note '{title}' deleted."
#     else:
#         return f"Note '{title}' not found."


# from collections import UserDict
# from constants import RED, GRAY, CYAN, MAGENTA, RESET, LEN_OF_NAME_FIELD
# from datetime import datetime
# import os.path
# import pickle
# from classes import Field


# class Note:
#     def __init__(self, title: str, content: str):
#         self.title = title
#         self.notes = content

#     def add_note(self, title, content):
#         self.notes[title] = content

#     def edit_note(self, title, new_content):
#         if title in self.notes:
#             self.notes[title] = new_content
#             return f"Note '{title}' edited."
#         else:
#             return f"Note '{title}' not found."

#     def delete_note(self, title):
#         if title in self.notes:
#             del self.notes[title]
#             return f"Note '{title}' deleted."
#         else:
#             return f"Note '{title}' not found."


# class NotesBook(UserDict):
#     def __init__(self):
#         self.notes = {}

#     def add_tags(self, title, tags): # метод для додавання тегів
#         if title in self.notes:
#             self.notes[title].tags.extend(tags)
#             return f"Tags {', '.join(tags)} added to the note with title '{title}'."
#         else:
#             raise NoteError(f"Note with title '{title}' not found.")


#     def search_notes(self, keyword):
#         result = []
#         for title, content in self.notes.items():
#             if keyword.lower() in title.lower() or keyword.lower() in content.lower():
#                 result.append(f"Title: {title}\nContent: {content}\n")
#         return result if result else "No matching notes found."
# if __name__ == "__main__":
#     print(add_note("Заголовок", "Зміст нотатки", "#тег1,#тег2"))
#     print(edit_note("Заголовок", "ще та маячня"))
#     print(search_notes("маячня", notes))
#     # print(add_note("kkk"))
    # print(add_note("kkk"))
    # print(add_note("kkk"))
    # print(add_note("kkk"))
