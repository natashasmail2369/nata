import json
from abc import ABC, abstractmethod


class FileWork(ABC):

    @abstractmethod
    def read_file(self):
        """
        Метод чтение файла
        """
        pass

    @abstractmethod
    def save_file(self, data):
        """
        Метод сохранения файла
        """
        pass

    @abstractmethod
    def del_file(self):
        """
        Метод удаление
        """
        pass


class WorkWithFile(FileWork):
    """
    Класс для работы с файлом
    """
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        """
        Метод чтение файла
        """
        with open(f"data/{self.file_name}.json", "r", encoding='utf-8') as file:
            return json.load(file)

    def save_file(self, data):
        """
        Метод сохранения файла
        """
        data.extend(data)
        with open(f"data/{self.file_name}.json", "w", encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def del_file(self):
        """
        Метод удаления файла
        """
        with open(f"data/{self.file_name}.json", "w") as file:
            pass

    def get_data(self, criterion):
        """
        Метод получения данных из файла по указанным критериям
        """
        criterion_vac = []
        with open(f"data/{self.file_name}.json", "r", encoding="utf8") as file:
            vacancies = json.load(file)
            for vac in vacancies:
                if not vac["snippet"]["requirement"]:
                    continue
                else:
                    if criterion in vac["snippet"]["requirement"]:
                        criterion_vac.append(vac)
        return criterion_vac