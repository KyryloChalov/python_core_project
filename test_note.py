from notes import Note, NotesBook
from constants import GREEN, RESET
from main import (
    add_note,
    show_notes,
    add_tag,
    delete_note,
    change_tag,
    delete_tag,
    search_notes,
)


if __name__ == "__main__":
    note_book = NotesBook()

    print(GREEN + "     створюємо нову нотатку" + RESET)
    print(add_note("000", "If you don’t have "))

    print(GREEN + "     створюємо нову нотатку з #tag" + RESET)
    print(add_note("first", "If you don’t have ", "#3"))

    print(GREEN + "      видаляємо нотатку"  + RESET)
    print(delete_note("first"))

    print(GREEN + "     створюємо нову нотатку з #tag" + RESET)
    print(add_note("first", "If you don’t have ", "#3"))

    print(GREEN + "     створюємо нову нотатку з двома #tags" + RESET)
    print(add_note("second", "If you don’t have ", "#3", "#5"))

    print(GREEN + "     додаємо #tags" + RESET)
    print(add_tag("000", "#8"))

    print(GREEN + "     додаємо #tags" + RESET)
    print(delete_tag("000", "#8"))

    print(GREEN + "     додаємо #tags" + RESET)
    print(add_tag("000", "#88"))

    print(GREEN + "     змінюємо #tags" + RESET)
    print(change_tag("000", "#88", "#99"))

    print(GREEN + "     додаємо #tags" + RESET)
    print(add_tag("000", "#88"))
    
    print(show_notes())

    print(GREEN + "     шукаємо #tags" + RESET)
    print(search_notes("DoN"))
