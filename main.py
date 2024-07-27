from src.parser import ApiHH
from src.functions import vac_user, sorting
from src.work_with_file import WorkWithFile


def main():
    file_name = input("Введите имя фала:\n")
    user_vacancy = input('Введите вакансию для поиска на сайте hh.ru: \n')
    hh = ApiHH(user_vacancy)
    if hh.connect != 200:
        print(f"Ошибка: {hh.connect}")
    else:
        hh.load_vacancies()
        vacancies = hh.vacancies
        file_work = WorkWithFile(file_name)
        file_work.save_file(vacancies)
        name_criterion = input('Введите критерий для отбора вакансий: \n')
        file_work.get_data(name_criterion)
        processed_vacancies = vac_user(file_name)
        n = input('Введите количество вакансий для просмотра: \n')
        top_vacancies = sorting(processed_vacancies, int(n))
        for vac in top_vacancies:
            print(vac)
        delete = input("Удалить список вакансий?(Y/N)").upper()
        if delete == "Y":
            file_work.del_file()


if __name__ == '__main__':
    main()