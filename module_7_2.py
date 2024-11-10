
def custom_write(name, string):
    name = 'file_name'
    string_positions = {}
    file = open(name, 'w', encoding='utf-8')
    for i, string in enumerate(string, start=1):  #добавляет счётчик к итерируемому объекту и возвращает его.
                                                   # Она создаёт объект-итератор, который генерирует кортежи,
                                                   #содержащие индекс элемента и сам элемент.
        position = file.tell()
        file.write(string + '\n')
        string_positions[(i, position)] = string

    return string_positions
    file.close()

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)