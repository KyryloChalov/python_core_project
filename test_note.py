from notes import Note, NotesBook, add_note
from constants import GREEN, RESET



if __name__ == "__main__":
    note_book = NotesBook()

    print(GREEN + "     створюємо нову нотатку" + RESET)
    print(add_note("first", "If you don’t have big dreams and goals you’ll end up working really hard for someone who does."))
