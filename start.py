from pprint import pprint

import kidneys


def do():
    filelist = kidneys.get_dicoms('C:\\Users\\Olga\\Desktop\\work_directory\\Pochki_2')
    pprint(filelist)


if __name__ == '__main__':
    do()
