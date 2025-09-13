def get_todos(filepath="todos.txt"):
    """Lê o arquivo e retorna uma lista de tarefas (sem quebras de linha)."""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return [todo.strip() for todo in todos if todo.strip()]


def write_todos(todos, filepath="todos.txt"):
    """Grave a lista de tarefas no arquivo, cada uma em uma linha."""
    with open(filepath, 'w') as file:
        for todo in todos:
            file.write(todo + "\n")


if __name__ == '__main__':
    print('hello')
    print(get_todos())