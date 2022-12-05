from addressbook import AddressBook, Record


def input_error(func):
    def wrapper(*args, **kwargs):
        #print('==================================')
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'Enter Correct Name!'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'Bot: Please use whitespace when entering name and phone'
        except TypeError:
            return 'Wrong Command !'
    return wrapper


contacts = AddressBook()


@input_error
def hello():
    return f'Bot: Hello, how can I help you?'


@input_error
def add(user_input):
    if len(user_input.split()) > 3:
        raise ValueError('Please provide data info in format "add <name> <phone>" example add Harry 0999999999.')
    if not user_input.split()[1].isalpha():
        raise ValueError('You provided wrong name')
    if not user_input.split()[2].isdigit():
        raise ValueError('You provided wrong phone')
    data = user_input.split()
    if data[1] in contacts:
        raise ValueError('Bot: This contact is already exist')
    for i in range(1, len(data[:3])):
        contacts[data[1]] = data[2]
        record = Record(data[1])
        record.add_phone(data[2])
        contacts.add_record(record)
    return f'Bot: You successfully added contacts'


@input_error
def show_all():
    all_contacts = 'List of contacts:\n'
    for k, record in contacts.get_all_record().items():
        all_contacts += f'{record.get_info()}\n'
    return all_contacts


@input_error
def change_addition(user_input):
    if len(user_input.split()) > 3:
        raise ValueError('Please provide data info in format "change <name> <phone>" example "change Harry 0999999999".')
    name, phones = user_input.split()[1], user_input.split()[2]
    record = contacts[name]
    record.change_phones(phones)
    return f'Additional phone {phones} with name {name.title()} was added'


@input_error
def update(user_input):
    if len(user_input.split()) > 3:
        raise ValueError('Please provide data info in format "update <name> <phone>" example "update Harry 0999999999".')
    name, new_phone = user_input.split()[1], user_input.split()[2]
    record = contacts[name]
    record.update_phone(new_phone)
    return f'Phone with name {name.title()} were updated to {new_phone}'


@input_error
def delete_phone_name(user_input):
    if len(user_input.split()) > 2 and ' '.join(user_input.split()[:2]) != 'delete phone':
        raise ValueError('Please provide data info in format "delete <name> <phone>" example "delete Harry".')
    name = user_input.split()[1]
    contacts.remove_record(name)
    return f'Success delete contact {name.title()}'


@input_error
def phone(user_input):
    if len(user_input.split()) > 2:
        raise ValueError('Please provide data info in format "phone <name>" example "phone Harry".')
    value = user_input.split()[1]
    return contacts.search(value).get_info()


@input_error
def delete_phone_number(user_input):
    phone, name = user_input.split()[3], user_input.split()[2]
    record = contacts[name]
    if record.delete_phone(phone):
        return f'Phone {phone} for {name} contact deleted.'
    return f'{name} contact does not have this number'


def wrong_input():
    return f'Bot: Wrong enter'


command = {
    'add': add,   # add new contact
    'hello': hello,  # hello func
    'show all': show_all,  # show list of all contacts
    'change': change_addition,  # addition of extra phone
    'phone': phone,  # find contact number using name
    'wrong_input': wrong_input,  # func to process wrong input
    'delete': delete_phone_name,  # delete contact using name
    'delete phone': delete_phone_number,  # delete phone number
    'update': update  # remove old phone and create new for contact
}


def main():
    key_words = ['good bye', 'bye', 'close', 'thank you', 'exit']
    while True:
        user_input = input('User: ').lower()
        if user_input.split()[0] == 'hello':
            print(command[user_input.split()[0]]())
        if user_input.split()[0] == 'add':
            print(command[user_input.split()[0]](user_input))
        if user_input == 'show all':
            print(command[user_input]())
        if user_input.split()[0] == 'change':
            print(command[user_input.split()[0]](user_input))
        if user_input.split()[0] == 'update':
            print(command[user_input.split()[0]](user_input))
        if user_input.split()[0] == 'phone':
            print(command[user_input.split()[0]](user_input))
        if user_input.split()[0] == 'delete':
            print(command[user_input.split()[0]](user_input))
        if ' '.join(user_input.split()[:2]) == 'delete phone':
            print(command[' '.join(user_input.split()[:2])](user_input))
        if user_input.split()[0] not in command and user_input not in key_words and user_input != 'show all':
            print(wrong_input())

        if user_input in key_words:
            print(f'Bot: Goodbye see you next time')
            break


if __name__ == '__main__':
    main()