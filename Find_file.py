import os


migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
m_dir = os.path.join(current_dir, migrations)             # генерируем абсолютный путь до Migrations

def find_sql(files):
    new_files = []
    for name in files:
        filename, file_extension = os.path.splitext(name)
        if file_extension == ".sql":
            new_files.append(name)
    return new_files

def find_text(s, commands):
    new_commands = []
    for command in commands:
        with open(join_file(command)) as f:
            if s.lower() in f.read().lower():
                new_commands.append(command)
    return new_commands

def join_file(file_name):
    return os.path.join(m_dir, file_name)


if __name__ == '__main__':
    os.chdir("..")          # Для проверки доп задания меняем директорию
    names = find_sql(os.listdir(m_dir))
    while(True):
        s = input("Введите строку: ")
        names = find_text(s, names)
        for i in range(len(names)):
            print(names[i])
        print("Всего:",  len(names))

