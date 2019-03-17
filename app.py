from src.counting import better_index
from src.params import data


def post_process(index, variants):
    """TODO
    Пример итогового выхлопа

    :param index: индекс лучшего варианта
    :param variants: список вариантов
    """
    better_val = variants[index]
    msg = 'Better variant:\n\tIndex: [{}]\n\tValue {}'.format(index, better_val)
    print(msg)


def main():
    variants = data()
    better_ind = better_index(variants)
    post_process(better_ind, variants)


if __name__ == '__main__':
    main()
