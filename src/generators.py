def filter_by_currency(transactions_list: list, valuet: str="USD") -> dict:
    """
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.
    """
    if transactions_list == []:
        return "Список транзакций пустой"
    else:
        for i in transactions_list:
            if i['operationAmount']['currency']['code'] == valuet:
                yield i


def transaction_descriptions(transactions_list: list) -> str:
    """
    Возвращает описание каждой операции по очереди.
    """
    if transactions_list == []:
        return "Список транзакций пустой"
    else:
        for i in transactions_list:
            yield i["description"]


def card_number_generator(start_gen: int, stop_gen: int) -> str:
    """
    Генерирует номера карт в заданном диапазоне.
    """
    for i in range(start_gen, stop_gen+1):
        card_num = "0000000000000000"
        num = card_num[:-len(str(i))] + str(i)
        yield f"{num[0:4]} {num[4:8]} {num[8:12]} {num[12:16]}"
