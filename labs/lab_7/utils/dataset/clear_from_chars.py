import re


def clear_from_extension(string: str) -> str:
    """
    Удалить расширение
    :param string:
    :return:
    """
    return string.split(".")[0]
