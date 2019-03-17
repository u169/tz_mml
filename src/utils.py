def not_empty_list(func):
    """Декоратор для функций, возващающих список
    Проверяет пустой список или нет
    Если пустой - бросается исключение

    :param func: функция, результат которой проверяется
    :return: обертка
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if len(result) == 0:
            err_msg = 'Function `{}` returned empty list'.format(func.__name__)
            raise ValueError(err_msg)

        return result
    return wrapper
