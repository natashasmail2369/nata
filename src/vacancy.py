class Vacancy:
    """
    Класс для работы с вакансиями
    """
    name: str
    salary: dict
    alternative_url: str
    requirement: str

    def __init__(self, name: str, salary: dict, alternative_url: str, requirement: str):
        self.name = name
        self.salary = salary
        self.alternative_url = alternative_url
        self.requirement = requirement

    def __str__(self):
        return (f'Название: {self.name}\n'
                f"Зарплата: от {self.salary['from']} до {self.salary['to']} {self.salary['currency']}\n"
                f'Ссылка: {self.alternative_url}\n'
                f'Требования: {self.requirement}\n')

    def __repr__(self):
        return (f"{Vacancy.__class__.__name__}({self.name}, "
                f"{self.salary}, {self.alternative_url}, {self.requirement})")

    def __gt__(self, other):
        return self.salary['to'] > other.salary['to']

    def __lt__(self, other):
        return self.salary['to'] < other.salary['to']

    def __eq__(self, other):
        return self.salary['to'] == other.salary['to']