import re


def to_camel_case(text):
    """Задание №1.1"""
    return re.split('_|-', text)[0].title() + ''.join(word.title() for word in re.split('_|-', text)[1::])


class SingletonMeta(type):
    """Задание №1.2"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


"""Задание №1.3"""
count_bits = lambda n: bin(n).count("1")


def digital_root(n):
    """Задание №1.4"""
    return n if n < 10 else digital_root(sum(map(int, str(n))))


"""Задание №1.5"""
even_or_odd = lambda number: "Even" if number % 2 == 0 else "Odd"
