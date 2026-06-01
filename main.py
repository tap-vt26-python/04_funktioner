
def add(x, y):
    return x + y

result = add(1, 1)
print(f"1 + 1 är {result}.")

result = add(12, 21)
print(f"12 + 21 är {result}.")


def view_menu():
    print("")
    print("** Välj ett alternativ **")
    print("1. Visa din todo-lista")
    print("2. Lägg till ny uppgift")
    print("0. Avsluta")


def view_todo_list():
    if len(todo_items) == 0:
        print("Listan är tom")

    else:
        for item in todo_items:
            print("+ " + item)


def add_todo():
    # be om input
    # lägg till i listan
    text = input("Vad vill du göra? ")
    todo_items.append(text)


# Här börjar att göra-programmet

todo_items = []
is_running = True

while is_running:
    view_menu()
    choice = input("> ")

    if choice == "1":
        view_todo_list()
    elif choice == "2":
        add_todo()
    elif choice == "0":
        is_running = False

