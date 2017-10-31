import os


migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))
m_dir = os.path.join(current_dir, migrations)             # генерируем абсолютный путь до Migrations и сохраняем в переменную m_dir

def find_sql(list):
    new_list = []
    for name in list:
        filename, file_extension = os.path.splitext(name)
        if file_extension == ".sql":
            new_list.append(name)
    return new_list

def find_text(s, list):
    new_list = []
    for name in list:
        with open(join_file(name)) as f:
            for str in f:
                if s.lower() in str.lower():
                    new_list.append(name)
                    break
    return new_list

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

