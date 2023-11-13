TITLE = "\tPersonal Assistant\tteam K-9 project"
FILENAME = 'addressbook.bin'
NOTE_FILENAME = 'notes.bin'

BLACK = "\033[30m"
RED =   "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE =  "\033[34m"
MAGENTA = "\033[35m"
CYAN =  "\033[36m"
WHITE = "\033[37m"
GRAY =  "\033[90m"  
RESET = "\033[0m"

LEN_OF_NAME_FIELD = 12          # довжина поля для виводу імені 

HELP_LIST = {
    1: f"\t{YELLOW}add_contact {CYAN}<name> <phone>{GRAY}*n {CYAN}<birthday>  {RESET} - add a new contact with a phone number(s) and birthday(optional)",
    2: f"\t{GRAY}                                                (you can enter several phone numbers for a contact){RESET}",
    3: f"\t{YELLOW}add_phone {CYAN}<name> <new_phone>{GRAY}*n           {RESET} - add the new phone number for an existing contact",
    4: f"\t{GRAY}                                                (you can enter several phone numbers for a contact){RESET}",
    5: f'\t{YELLOW}add_bd {CYAN}<name> <birthday>                 {RESET} - add the birthday data ("dd-mm-yyyy") for an existing contact',
    6: f"\t{YELLOW}change_name {CYAN}<name> <new_name>            {RESET} - change the name for an existing contact",
    7: f"\t{YELLOW}change_phone {CYAN}<name> <phone> <new_phone>  {RESET} - change the phone number for an existing contact",
    8: f"\t{YELLOW}change_bd {CYAN}<name> <new_birthday>          {RESET} - change the phone number for an existing contact",
    9: f"\t{YELLOW}delete_phone {CYAN}<name> <phone>              {RESET} - delete one phone number from an existing contact",
    10: f"\t{YELLOW}delete_contact {CYAN}<name>                    {RESET} - remove an existing contact",
    11: f"\t{YELLOW}find {CYAN}<anything>                          {RESET} - search for any string (>= 3 characters) in the contact data",
    12: f"\t{YELLOW}birthdays {CYAN}<days>                          {RESET} - shows a list of contacts after a certain number of days",
    13: f"\t{YELLOW}name {CYAN}<name>                              {RESET} - search record by the name",
    14: f"\t{YELLOW}list {GRAY}<pages>                             {RESET} - show all contacts, {GRAY}<pages>(optional) - lines per page{RESET}",
    15: f"\t{YELLOW}list_notes {GRAY}<pages>                      {RESET} - show all notes, {GRAY}<pages>(optional) - lines per page{RESET}",
    16: f'\t{YELLOW}hello                                    {RESET} - "hello-string"',
    17: f"\t{YELLOW}exit                                     {RESET} - exit from PhoneBook",
    18: f"\t{YELLOW}help                                     {RESET} - this help-page",
        }
 