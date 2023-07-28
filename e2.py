user_prompt = "Enter to do list:"

todos = []

while True:
    todo = input(user_prompt)
    print(todo.title())
    todos.append(todo)
    print(todos)
