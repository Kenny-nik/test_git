import re
from collections import Counter


def search_by_pattern(transactions: list, pattern: str) -> list:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка.
    """
    result = []
    for transaction in transactions:
        for val in transaction.values():
            if re.search(pattern.lower(), str(val).lower()):
                result.append(transaction)
    return result


def counter_description(transactions: list, descriptions: list) -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    result = {}
    count_description = Counter(
        item["description"] for item in transactions if item.get("description") in descriptions
    )
    for description, count in count_description.items():
        result[description] = count
    return result