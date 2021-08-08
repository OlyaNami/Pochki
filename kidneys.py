import os
import pydicom


def get_dicoms(path_to_folder):
    """
    :param path_to_folder: путь к папке, которая содержит dicom-файлы
    :return: список dicom-файлов, содержащихся в папке
    """
    spisok = []

    for address, dirs, files in os.walk(path_to_folder):
        for file in files:
            filepath = os.path.join(address, file)

            try:
                dataset = pydicom.dcmread(filepath, stop_before_pixels=True)
                studyid = dataset.StudyInstanceUID
            except pydicom.errors.InvalidDicomError:
                continue
            except AttributeError as error:
                print(f'For file: {filepath} exception has occured {error}')
                continue

            spisok.append((studyid, filepath))

    return spisok
