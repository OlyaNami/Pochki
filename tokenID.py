import json
from pprint import pprint

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
    database = list_alljsons(inpath)  # сколько всего клиентов, загружаем содержимое файла по пути inpath в переменную
    # my_list
    client_name_key: str = 'TokenID'
    all_client_entries = [entry[client_name_key] for entry in database if
                          client_name_key in entry.keys()]  # пишем в переменную сколько клиентов (не уникальных)
    unique_clients = set(all_client_entries)  # пишем в переменную сколько клиентов (уникальных)

    # number_of_unique_values = len(unique_clients)  # сколько там клиентов, считаем значения в этом списке

    # print(number_of_unique_values)  # печатаем для проверки сколько этих уникальных клиентов
    # for entry in a_set:  # считаем сколько раз встречается в списке каждый клиент
    #     print(f'{entry} : {values_of_key.count(entry)}')

    client_unique_studies = {}  # пустой словарь для уникальных исследований клиента

    for client in unique_clients:
        client_studies = [entry['StudyUID'] for entry in database if
                          'StudyUID' in entry.keys() and entry['TokenID'] == client]  # считаем все исследования
        # для каждого клиента в базе данных
        # для каждой записи в базе данных (переменная датабейз)
        # достать значение по ключу СтадиУИД если СтадиУИД есть среди ключей этой записи
        # и если по ключу ТокенАйди записан текущий клиент

        client_unique_studies[client] = set(client_studies)  # добавляем запись уникальных исследований
        # в словарь используя клиента как ключ

    count_of_studies = {key: len(value) for (key, value) in client_unique_studies.items()}
    pprint(count_of_studies)


if __name__ == '__main__':
    main()
