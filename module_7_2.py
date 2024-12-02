# def custom_write(file_name: str, strings: list):
#     '''
#     Функция записывает строки из strings в file_name.
#     Возвращает словарь с ключом в виде кортежа с номером строки и байтом начала
#     строки и значением в виде строки из strings.
#     file_name - название файла для записи
#     strings - список строк для записи
#     '''
#     strings_positions = {}
#     line_number = 1
#     file = open(file_name, 'w')
#     for string in strings:
#         line_byte = file.tell()
#         file.write(f'{string}\n')
#         strings_positions[(line_number, line_byte)] = string
#         line_number += 1
#     file.close()
#     return strings_positions
#
# if __name__ == '__main__':
#     info = [
#         'Text for tell.',
#         'Используйте кодировку utf-8.',
#         'Because there are 2 languages!',
#         'Спасибо!'
#         ]
#     result = custom_write('test.txt', info)
#     for elem in result.items():
#         print(elem)


def custom_write(file_name, strings):
    file = open(file_name, 'w+', encoding='utf-8')
    strings_positions={}
    for counter in range(0, len(strings)):
        file.read()
        bait_stroki = file.tell()
        file.write(f'{strings[counter]}\n')
        strings_positions[ (counter+1, bait_stroki)] = strings[counter]
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)