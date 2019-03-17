import json

from src.utils import not_empty_list


@not_empty_list
def data():
    """Получение данных по заправкам

    TODO Зависит от модуля, предоставляющего данные
    Данные могут быть преобразованы (>>> проводим упращенные расчеты [из ТЗ])

    :return: заглушка
    """
    return [1,1,1,1], [1,5,1,1], [1,10,1,1], [2,1,1,1], [10,10,10,10]


@not_empty_list
def coefficients():
    """Коэффициенты для каждого критерия заправки
    Загружаем из файла
    Подбирается эмпирически и согласовывается

    :return: список коэффициентов
    """
    path = '../coefficients.json'
    file = open(path, 'r', encoding='utf-8')
    result = json.load(file)
    return result
