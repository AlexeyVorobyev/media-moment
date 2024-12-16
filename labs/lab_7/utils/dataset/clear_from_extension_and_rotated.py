def clear_from_extension_and_rotated(string: str) -> str:
    """
    Удалить расширение и поворот
    :param string:
    :return:
    """
    return string.split(".")[0].split('_')[0]
