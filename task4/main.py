def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    name = args[0]

    if name in contacts:
        return contacts[name]
    else:
        return "Contact not found."


def show_all(contacts):
    result = ""

    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"

    return result


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")

        if not user_input.strip():
            print("Invalid command.")
            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            if len(args) == 2:
                print(add_contact(args, contacts))
            else:
                print("Invalid command.")

        elif command == "change":
            if len(args) == 2:
                print(change_contact(args, contacts))
            else:
                print("Invalid command.")

        elif command == "phone":
            if len(args) == 1:
                print(show_phone(args, contacts))
            else:
                print("Invalid command.")

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
