import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    @abstractmethod
    def load_vacancies(self, **kwargs):
        pass


class ApiHH(Parser):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self, keyword):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': keyword, 'page': 0, 'per_page': 3, 'only_with_salary': True}
        self.vacancies = []

    def load_vacancies(self, **kwargs):
        """
        Метод подключения к api HH
        """
        while self.params.get('page') != 3:
            response = requests.get(self.__url, headers=self.__headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

    @property
    def connect(self):
        """
        Метод вывода статуса соединения
        """
        return requests.get(self.__url).status_code


class CB(Parser):
    """
    Класс для работы с api ЦБ
    """
    def __init__(self):
        self.__url = "https://www.cbr-xml-daily.ru/daily_json.js"
        self.Exchange = dict

    def load_vacancies(self, **kwargs):
        """
        Метод подключения к api ЦБ
        """
        response = requests.get(self.__url)
        self.Exchange = response.json()['Valute']

    @property
    def show_exchange(self):
        """
        Метод показывает курсы валют
        """
        return self.Exchange

    def __str__(self):
        return f"{CB.__class__.__name__}({self.Exchange})"