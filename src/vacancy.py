class JobVacancy:
    def __init__(self, name: str, salary: dict, url: str, requirement: str):
        if not isinstance(salary, dict):
            raise TypeError("Salary must be a dictionary")
        self.name = name
        self.url = url
        self.requirement = requirement
        self.salary = self.__validation(salary)

    def __str__(self):
        return (
            f"Название: {self.name}\n"
            f"Зарплата: от {self.salary['from']} до {self.salary['to']} {self.salary['currency']}\n"
            f"Ссылка: {self.url}\n"
            f"Требования: {self.requirement}\n"
        )

    @staticmethod
    def __validation(salary):
        if salary["currency"] is None:
            salary["currency"] = "Валюта не определена"
        if salary["from"] is None:
            salary["from"] = 0
        if salary["to"] is None:
            salary["to"] = 0
        return salary

    def well(self, cb):
        """Перевод валюты по курсу"""
        if self.salary["currency"] != "RUR" and self.salary["currency"] != "" and "BYR" != self.salary["currency"]:
            currency = self.salary["currency"]
            self.salary["from"] = round(self.salary["from"] * cb.Exchange[currency]["Value"] / cb.Exchange[currency]["Nominal"])
            self.salary["to"] = round(self.salary["to"] * cb.Exchange[currency]["Value"] / cb.Exchange[currency]["Nominal"])
            self.salary["currency"] = f"RUR, выплата в {currency}"

    def __repr__(self):
        return f"{JobVacancy.__class__.__name__}({self.name}, {self.salary}, {self.url}, {self.requirement})"

    def __gt__(self, other):
        return self.salary['to'] > other.salary['to']

    def __lt__(self, other):
        return self.salary['to'] < other.salary['to']
