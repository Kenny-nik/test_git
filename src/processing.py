def filter_by_state(list_of_dictionary: list, key: str = "EXECUTED") -> list:
    """
    Возвращает новый список словарей, содержащий только те словари,
    у которых ключ state cоответствует указанному значению.
    """

    new_list_of_dictionary = []

    for object in list_of_dictionary:
        if object["state"] == key:
            new_list_of_dictionary.append(object)

    return new_list_of_dictionary


def sort_by_date(list_of_dictionary: list, is_reverse: bool = True) -> list:
    """
    Принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date)
    """

    sorted_list_of_dictionary = sorted(
        list_of_dictionary, key=lambda data: data["date"], reverse=is_reverse
    )

    return sorted_list_of_dictionary
