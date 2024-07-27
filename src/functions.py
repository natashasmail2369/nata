from src.parser import CB
from src.vacancy import Vacancy
import json


def vac_user(file_name):
    """Приводит полученные данные к данным для вывода"""
    with open(f"data/{file_name}.json", "r", encoding="utf8") as f:
        vacancies = json.load(f)
    user_vac = []
    for vac in vacancies:
        if not vac.get("salary"):
            vac["salary"] = {"from": 0, "to": 0, "currency": ""}
        else:
            if vac["salary"] is None or not isinstance(vac["salary"], dict):
                vac["salary"] = {"from": 0, "to": 0, "currency": ""}
            else:
                if vac["salary"]["currency"] is None:
                    vac["salary"]["currency"] = "Валюта не определена"

                if vac["salary"]["from"] is None:
                    vac["salary"]["from"] = 0
                if vac["salary"]["to"] is None:
                    vac["salary"]["to"] = 0

        vac["snippet"]["requirement"] = vac["snippet"].get("requirement", "Информация отсутствует")
        user_vac.append(vac)

    return user_vac


def sorting(vacancies, n: int):
    """Сортировка N вакансий"""
    sort_vac = []
    cb = CB()
    cb.load_vacancies()
    for vac in vacancies:
        try:
            if vac["salary"]["currency"] != "RUR" and vac["salary"]["currency"] != "" and vac["salary"]["currency"] != "BYR":
                currency = vac["salary"]["currency"]
                vac["salary"]["from"] = round(vac["salary"]["from"] * cb.Exchange[currency]["Value"] / cb.Exchange[currency]["Nominal"])
                vac["salary"]["to"] = round(vac["salary"]["to"] * cb.Exchange[currency]["Value"] / cb.Exchange[currency]["Nominal"])
                vac["salary"]["currency"] = f"RUR, выплата в {currency}"

            sort_vac.append(Vacancy(vac['name'], vac['salary'], vac['alternate_url'], vac["snippet"]['requirement']))
        except TypeError as e:
            print(f"Ошибка при обработке вакансии: {vac}")
            print(e)
            continue

    sorted_vacancies = sorted(sort_vac, key=lambda x: x.salary["to"], reverse=True)
    return sorted_vacancies[:n]