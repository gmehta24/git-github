

while True:
    user_action = input("add item or show or exit or edit :")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            with open('todo.txt', 'r') as file:
                todos = file.readlines()
            todo = input("Enter to do list Item:") + "\n"
            todos.append(todo)
            with open('todo.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todo.txt', 'r') as file:
                todos = file.readlines()


             # new_todos =[item.strip('\n') for item in todos]
            for index, item in enumerate(todos):
                item = item.strip('\n').title()
                row = f"{index}-{item}"
                print(row)
        case 'edit':
            item_number = int(input('please enter item number to edit'))
            item_number = item_number - 1
            new_item = input('please enter new item')
            todos[item_number] = new_item
        case 'complete':
            item_number = int(input('please enter item number to be marked as completed'))
            todos.pop(item_number-1)
        case 'exit':
            break
        case _:
            print("you have entered invalid command")

print("bye!")



