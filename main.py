from classes import (
    Name,
    Phone,
    Email,
    Address,
    Record,
    AddressBook,
    BirthDay,
    PhoneError,
    BDayError,
    EmailError,
    NoContactError,
)
from constants import (
    TITLE,
    FILENAME,
    NOTE_FILENAME,
    RED,
    BLUE,
    YELLOW,
    CYAN,
    GRAY,
    WHITE,
    RESET,
    MAGENTA,
)

from notes import (
    NotesBook,
    NoteError,
    Title,
    Content,
    Tags,
    Note
) 

from get_birthday_on_date import get_birthdays_on_date

# from notes import NotesBook

from sort_path import sorting

book = AddressBook()
notes = NotesBook()


def user_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return f"{RED}not enough params{RESET}\n\tFormat: '<command> <name> <args>'\n\tUse 'help' for information"
        except KeyError:
            return f"{RED}Unknown name {args[0]}. Try another or use help{RESET}"
        except ValueError:
            return f"{RED}time data does not match format 'dd-mm-YYYY' (dd<=31, mm<=12){RESET}"
        except BDayError:
            return f"{RED}time data does not match format 'dd-mm-YYYY' (dd<=31, mm<=12) {RESET}"
        except PhoneError:
            return f"{RED}the phone number must contains only digits, format: '0671234567' or '+380671234567'{RESET}"
        except EmailError as ee:
            return f"{RED} {ee}{RESET}"
        except AttributeError:
            return f"{RED}phone number {args[1]} is not among the contact numbers of {args[0]} {RESET}"
        except TypeError as ve:
            return f"{RED} {ve}{RESET}"
        except NoteError as ne:
            return f"{RED} {ne}{RESET}"

    return inner


def get_record_or_error(name, book, return_error=False):
    name_rec = Name(name)
    rec = book.get(str(name_rec))
    if not rec:
        error_message = (
            f"{RED}contact {WHITE}{name}{RED} not found in address book{RESET}"
        )
        if return_error:
            return error_message
        else:
            return rec
    return rec


@user_error
def add_birthday(*args):
    if get_record_or_error(args[0], book):
        return get_record_or_error(args[0], book).add_birthday((args[1]))
    else:
        return f"{RED}contact {WHITE}{args[0]}{RED} not found in address book{RESET}"


@user_error
def add_address(*args):
    addr_str = ""
    # join args with " " starting from 1
    addr_str = " ".join(args[1:])
    print(addr_str)
    return get_record_or_error(args[0], book).add_address((addr_str))


@user_error
def add_email(*args):
    return get_record_or_error(args[0], book).add_email(args[1])

# @user_error
# def add_note(*_):
#     title = input("Enter Note Title >>> ")
#     if not title:
#         raise NoteError("Note title cannot be empty")
#     title = Title(title)
#     content = input("Note Text >>> ")
#     if not content:
#         raise NoteError("Note text cannot be empty")
#     tags = input("Add Note Tags, separated by comma >>> ")
#     tags = [(tag.strip()) for tag in tags.split(",")] if tags else None
#     note = Note(title, content, tags)
#     notes.add_note(note)
#     return f"Note created successfully"


@user_error
def add_contact(*args):
    if get_record_or_error(args[0], book):
        return f"{RED}contact {Name(args[0])} already exist{RESET}\n\t{get_record_or_error(args[0], book)}\n\tUse 'add_phone' or 'change' command to add or change the phone"
    book.add_record(Record(args[0]))

    if len(args) > 1:
        if all([args[-1][2] == args[-1][5] == "-", len(args[-1]) == 10]):
            add_birthday(args[0], args[-1])
            args = args[:-1]
        add_phones(args[0], *args[1:])

    return f"contact {Name(args[0])} has been successfully added \n\t{get_record_or_error(args[0],book)}"


@user_error
def add_few_phones(rec, *args):
    result = ""
    for phone in args:
        rec.add_phone(phone)
        result += (
            f"phone number {Phone(phone)} has been added to {rec.name}'s contact list\n"
        )
    return result


@user_error
def add_phones(*args):
    rec = get_record_or_error(args[0], book)
    if rec:
        return add_few_phones(rec, *args[1:]) + f"\t{rec}"
    else:
        return f"{RED}contact {WHITE}{args[0]}{RED} not found in address book{RESET}"


@user_error
def change_name(*args):
    return book.change_name((args[0]), args[1])


@user_error
def change_phone(*args):
    return get_record_or_error(args[0], book).edit_phone(Phone(args[1]), Phone(args[2]))


@user_error
def change_email(*args):
    return get_record_or_error(args[0], book).edit_email(Email(args[1]), Email(args[2]))


@user_error
def del_phone(*args):
    return get_record_or_error(args[0], book).remove_phone(Phone(args[1]))


@user_error
def del_email(*args):
    return get_record_or_error(args[0], book).remove_email(Email(args[1]))

# @user_error
# def delete_note(*args):
#     ...
#     return f"Not implemented yet"

@user_error
def change_address(*args):
    return get_record_or_error(args[0], book).edit_address(args[1])


@user_error
def del_address(*args):
    return get_record_or_error(args[0], book).remove_address()


@user_error
def delete_record(*args):
    return book.delete_record(args[0])


@user_error
def name_find(*args):
    return book.find_name(args[0])


# --- Notes
@user_error
def add_tag(*args):
    title = args[0]
    tags = args[1:]
    return notes.add_tags(title, tags)


@user_error
def search_notes_by_tag(*args):
    tag = args[0]
    sort_by_keywords = args[1:].lower() == "true" if len(args) > 1 else False
    return notes.search_notes_by_tag(tag, sort_by_keywords)


@user_error
def add_note(*args):
    title = args[0]
    content_start_index = 1
    tags = []
    #  теги в аргументах
    content = " ".join(args[content_start_index:])
    for i, arg in enumerate(args[content_start_index:], start=content_start_index):
        if arg.startswith("#"):
            tag = (
                arg.lstrip("#, ").rstrip(", ").replace("#", "")
            )  # видаляємо # і зайві пробіли
            tags.append(tag)
            content = " ".join(args[content_start_index:i])

    # content = " ".join(args[content_start_index:args.index(f"--tags={+tags[0]}") if tags else len(args)])
    new_note = Note(title, content, tags)
    notes.data[title] = new_note
    return f"Note 'Title: {title} Content:{content} Tags:{', '.join(tags)}' added."


@user_error
def edit_note(title, new_content):
    # Перевірка наявності тайтлу в notes
    if title in notes.data:
        # Змінюємо тільки content
        notes.data[title].content.edit_content(new_content)
        return f"Note '{title}' changed. New content: '{new_content}'"
    else:
        return f"Нотатка '{title}' не знайдена."



@user_error
def search_notes(keyword, notes):
    matching_notes = [
        f"Note 'Title: {title}' Content: {note.content} Tags:{', '.join(note.tags)}"
        for title, note in notes.items()
        if keyword.lower() in title.lower() or keyword.lower() in note.content.lower()
    ]
    if matching_notes:
        return "\n".join(matching_notes)
    else:
        return "No matching notes found."



@user_error
def delete_note(*args):
    title = args[0]
    if title in notes.notes:
        del notes.notes[title]
        return f"Note '{title}' deleted."
    else:
        return f"Note '{title}' not found."


# --- Notes


def search(*args):
    result = ""
    if not args:
        return f"{RED}searching string is required{RESET}"
    seek = args[0].lower()
    for record in book.data.values():
        if seek.isdigit():
            if record.seek_phone(seek):
                result += f"\t{BLUE}[   Phone match] {RESET}{record}\n"
            if record.birthday:
                date_str = record.birthday.value.strftime("%d-%m-%Y")
                if date_str.find(seek) != -1:
                    result += f"\t{MAGENTA}[Birthday match] {RESET}{record}\n"

        if seek in record.name.value.lower():
            result += f"\t{CYAN}[ Name match] {RESET}{record}\n"
        if record.seek_email(seek):
            result += f"\t{BLUE}[Email match] {RESET}{record}\n"
        if record.address:
            addr_str = record.address.value.lower()
            if addr_str.find(seek) != -1:
                result += f"\t{GRAY}[ Address match] {RESET}{record}\n"

    if result:
        return f"data found for your request '{seek}': \n{result[:-1]}"
    else:
        return f"{RED}nothing was found for your request '{seek}'{RESET}"


def show_all(*args):
    pages = int(args[0]) if args else len(book.data)
    print(f"  === Address book ===")
    count = 0
    for _ in book.iterator(pages):
        for item in _:
            print(item)
            count += 1
        if count < len(book):
            input(f"  Press Enter for next page: ")
    return "  --- End of List ---"


def add(*args):
    help_list = []
    help_list.append(
        f"\t{YELLOW}add_contact {CYAN}<name> <phone>{GRAY}*n {CYAN}<birthday>  {RESET} - add a new contact with a phone number(s) and birthday(optional)"
    )
    help_list.append(
        f"\t{GRAY}                                                (you can enter several phone numbers for a contact){RESET}"
    )
    help_list.append(
        f"\t{YELLOW}add_phone {CYAN}<name> <new_phone>{GRAY}*n           {RESET} - add the new phone number for an existing contact"
    )
    help_list.append(
        f"\t{GRAY}                                                (you can enter several phone numbers for a contact){RESET}"
    )
    help_list.append(
        f'\t{YELLOW}add_bd {CYAN}<name> <birthday>                 {RESET} - add the birthday data ("dd-mm-yyyy") for an existing contact'
    )
    help_list.append(
        f"\t{YELLOW}add_email {CYAN}<name> <email>                 {RESET} - add the e-mail for an existing contact"
    )
    help_list.append(
        f"\t{YELLOW}add_address {CYAN}<name> <address>             {RESET} - add the address for an existing contact"
    )
    help_list.append(
        f'\t{YELLOW}add_note {CYAN}<name> <note>                 {RESET} - add the birthday data ("dd-mm-yyyy") for an existing contact'
    )

    return "\n".join(help_list)


def change(*args):
    help_list = []
    help_list.append(
        f"\t{YELLOW}change_name {CYAN}<name> <new_name>            {RESET} - change the name for an existing contact"
    )
    help_list.append(
        f"\t{YELLOW}change_phone {CYAN}<name> <phone> <new_phone>  {RESET} - change the phone number for an existing contact"
    )
    help_list.append(
        f"\t{YELLOW}change_bd {CYAN}<name> <new_birthday>          {RESET} - change the phone number for an existing contact"
    )
    help_list.append(
        f"\t{YELLOW}change_email {CYAN}<name> <email> <new_email>  {RESET} - change the email for an existing contact"
    )
    help_list.append(
        f"\t{YELLOW}change_address {CYAN}<name> <new_address>      {RESET} - change the address for an existing contact"
    )
    help_list.append(
        f"\t{YELLOW}change_note {CYAN}<name> <note>          {RESET} - change the phone number for an existing contact"
    )
    return "\n".join(help_list)


def delete(*args):
    help_list = [TITLE]
    help_list.append(
        f"\t{YELLOW}delete_phone {CYAN}<name> <phone>              {RESET} - delete one phone number from an existing contact"
    )
    help_list.append(
        f"\t{YELLOW}delete_record {CYAN}<name>                    {RESET} - remove an existing contact"
    )
    help_list.append(
        f"\t{YELLOW}delete_email {CYAN}<name> <email>              {RESET} - remove an email from existing contact"
    )
    help_list.append(
        f"\t{YELLOW}delete_address {CYAN}<name>                    {RESET} - remove an address from listexisting contact"
    )
    help_list.append(
        f"\t{YELLOW}delete_note {CYAN}<name> <phone>            {RESET} - remove an existing contact"
    )
    return "\n".join(help_list)


def help_page(*args):
    help_list = [TITLE]
    help_list.append(
        f"\t{YELLOW}add_contact {CYAN}<name> <phone>{GRAY}*n {CYAN}<birthday>  {RESET} - add a new contact with a phone number(s) and birthday(optional)"
    )
    help_list.append(
        f"\t{GRAY}                                                (you can enter several phone numbers for a contact){RESET}"
    )
    help_list.append(
        f"\t{YELLOW}add_phone {CYAN}<name> <new_phone>{GRAY}*n           {RESET} - add the new phone number for an existing contact"
    )
    help_list.append(
        f"\t{GRAY}                                                (you can enter several phone numbers for a contact){RESET}"
    )
    help_list.append(
        f'\t{YELLOW}add_bd {CYAN}<name> <birthday>                 {RESET} - add the birthday data ("dd-mm-yyyy") for an existing contact'
    )
    help_list.append(
        f"\t{YELLOW}change_name {CYAN}<name> <new_name>            {RESET} - change the name for an existing contact"
    )
    help_list.append(
        f"\t{YELLOW}change_phone {CYAN}<name> <phone> <new_phone>  {RESET} - change the phone number for an existing contact"
    )
    help_list.append(
        f"\t{YELLOW}change_bd {CYAN}<name> <new_birthday>          {RESET} - change the phone number for an existing contact"
    )
    help_list.append(
        f"\t{YELLOW}delete_phone {CYAN}<name> <phone>              {RESET} - delete one phone number from an existing contact"
    )
    help_list.append(
        f"\t{YELLOW}delete_contact {CYAN}<name>                    {RESET} - remove an existing contact"
    )
    help_list.append(
        f"\t{YELLOW}find {CYAN}<anything>                          {RESET} - search for any string (>= 3 characters) in the contact data"
    )
    help_list.append(
        f"\t{YELLOW}birthdays {CYAN}<days>                          {RESET} - shows a list of contacts after a certain number of days"
    )
    help_list.append(
        f"\t{YELLOW}name {CYAN}<name>                              {RESET} - search record by the name"
    )
    help_list.append(
        f"\t{YELLOW}list {GRAY}<pages>                             {RESET} - show all contacts, {GRAY}<pages>(optional) - lines per page{RESET}"
    )
    help_list.append(
        f'\t{YELLOW}hello                                    {RESET} - "hello-string"'
    )
    help_list.append(
        f"\t{YELLOW}exit                                     {RESET} - exit from PhoneBook"
    )
    help_list.append(
        f"\t{YELLOW}help                                     {RESET} - this help-page"
    )
    return "\n".join(help_list)


def say_hello(*args):
    return "How can I help you?"


def say_good_bay(*args):
    print(book.write_contacts_to_file(FILENAME))
    exit("Good bye!")


def unknown(*args):
    return f"{RED}Unknown command. Try again{RESET}"


# =============================================
#                main
# =============================================


COMMANDS = {
    add: ("add", "+"),
    add_contact: ("add_record", "add_contact"),
    add_phones: ("add_phone", "phone_add"),
    add_birthday: ("add_birthday", "add_bd", "change_birthday", "change_bd"),
    add_address: ("add_address", "add_adr", "change_address", "change_adr"),
    add_email: ("add_email", "email_add"),
    add_note: ("add_note", "note_add"),
    change: ("change", "edit"),
    change_name: ("change_name", "name_change"),
    change_phone: ("change_phone", "phone_change", "edit_phone"),
    change_address: ("change_address", "change_adr", "edit_address", "edit_adr"),
    change_email: ("change_email", "email_change"),
    # change_note:
    delete: ("delete", "del"),
    del_phone: ("del_phone", "delete_phone"),
    delete_record: ("delete_contact", "del_contact", "delete_record", "del_record"),
    del_address: ("delete_address", "delete_adr", "del_adr"),
    del_email: ("delete_email", "del_email"),
    delete_note: ("delete_note", "del_note"),
    name_find: ("name", "find_name"),
    get_birthdays_on_date: ("birthdays", "find_birthdays", "bd"),
    search: ("search", "seek", "find"),
    help_page: ("help",),
    say_hello: ("hello", "hi"),
    show_all: ("show_all", "show", "list"),
    say_good_bay: ("exit", "good_bay", "by", "close", "end"),
}


def parser(text: str):
    for func, cmd_tpl in COMMANDS.items():
        for command in cmd_tpl:
            data = text.strip().lower().split()
            if len(data) < 1:
                break
            if data[0] == command:
                return func, data[1:]
    return unknown, []


from prompt_toolkit.completion import NestedCompleter

# from terminal_tips import completer
from prompt_toolkit import prompt

# COMMANDS = dict(sorted(COMMANDS.keys(), reverse=True))


def func_completer(CMD: dict):
    comp_dict = {}
    # print(f"{CMD.values() = }")
    # sorted_command = sorted(CMD.keys())
    sorted_command = [
        "add_address",
        "add_contact",
        "add_birthday",
        "add_contact",
        "add_email",
        "add_note",
        "add_phones",
        "change_name",
        "change_phone",
        "change_address",
        "change_email",
        "del_phone",
        "delete_record",
        "del_address",
        "del_email",
        "delete_note",
        "edit_name",
        "edit_phone",
        "edit_address",
        "edit_email",
        "get_birthdays_on_date",
        "help",
        "find_name",
        "search",
        "hello",
        "show_all",
        "list",
        "good_bay",
        "by",
    ]
    for key in sorted_command[1:]:
        matching_key = next(
            (
                existing_key
                for existing_key in comp_dict.keys()
                if key.startswith(existing_key)
            ),
            None,
        )
        if matching_key is None:
            comp_dict[key] = None
        else:
            key_suffix = key[len(matching_key) :].strip()
            if comp_dict[matching_key] is None:
                comp_dict[matching_key] = {key_suffix}
            else:
                comp_dict[matching_key].add(key_suffix)
    return comp_dict


completer = NestedCompleter.from_nested_dict(func_completer(COMMANDS))


def main():
    global book
    global notes
    book = book.read_contacts_from_file(FILENAME)
    #notes = notes.read_notes_from_file(NOTE_FILENAME)
    print("\n" + BLUE + TITLE + RESET + "\t\tType 'help' for information")
    while True:
        user_input = prompt(">>>", completer=completer)
        # user_input = input(f"{BLUE}>>{YELLOW}>>{RESET}")
        func, data = parser(user_input.strip().lower())
        print(func(*data))
        if func not in [
            say_good_bay,
            show_all,
            say_hello,
            help_page,
            search,
            name_find,
            get_birthdays_on_date,
        ]:
            book.write_contacts_to_file(FILENAME)
            #notes.write_notes_to_file(NOTE_FILENAME)


if __name__ == "__main__":
    main()
