import json

inpath = 'C:\\Workdir\\DCM_read\\downloads.json'


def list_alljsons(inpath):
    '''
    :param inpath: принимает путь к файлам .json
    :return: возвращает список словарей .json, которые можно обработать в питоне
    '''

    with open(inpath, 'r') as jf:
        my_list = json.load(jf)

    return my_list


def main():
    my_list = list_alljsons(inpath) # сколько всего клиентов, создаем лист он же список
    a_key: str = "TokenID"
    values_of_key = [entry[a_key] for entry in my_list if
                     a_key in entry.keys()]
    a_set = set(values_of_key) # пишем в переменную сколько клиентов (не уникальных)
    number_of_unique_values = len(a_set) # сколько там уникальных клиентов, считаем уникальные значения в этом списке
    print(number_of_unique_values)  # печатаем для проверки сколько этих уникальных клиентов
    for entry in a_set:             # считаем сколько раз встречается в списке каждый клиент
        print(f'{entry} : {values_of_key.count(entry)}')


if __name__ == '__main__':
    main()
