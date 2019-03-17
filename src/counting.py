from src.params import coefficients

COEFFICIENTS = coefficients()


def better_index(*variants):
    """Ищет лучший вариант из предложенных

    :param variants: список вариантов (матрица);
    элемент списка - список переменных: расстояние до заправки, лимит времени и т.п.
    :return: лучший вариант
    """
    max_profit = max(variants, key=__avg_profit)
    index = variants.index(max_profit)
    return index


def __avg_profit(criteria):
    """Средний профит
    Выбрал средний, т.к. на вход (гипотетически) можем получить неизвестные данные
    Допустим мы не знаем сколько у нас есть свободного времени (значение = None)
    Неизвестные отфильтровываем
    Т.к не знаем сколько будет всего критериев, берем среднее арифметическое

    Каждый критерий имеет определенный коэффициент (последний подбирается индивидуально (эмпирически))
    Перемножаем пары: коэффициент - значение критерия

    :param criteria: Критерии варианта заправки: расстояние до заправки, лимит времени и т.п.
    :return: (int) Средний профит по паре
    """
    pairs = zip(COEFFICIENTS, criteria)

    # фильтруем и убираем неизвестные критерии
    pairs = filter(
        lambda x: x[0] is not None and x[1] is not None,
        pairs)

    # получаем список `субпрофитов` (коэффициент * критерий)
    sub_profits = map(
        lambda p: p[0]*p[1],
        pairs)

    # генератор -> список
    sub_profits = list(sub_profits)
    result = sum(sub_profits) / len(sub_profits)
    return result
