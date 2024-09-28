import json
import os
from typing import Any, List

from src.external_api import currency_conversion_in_rub

PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")


def get_data_from_json(path: str) -> List[dict] | Any:
    """
    Принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(path, encoding="utf-8") as data_file:
            try:
                transactions = json.load(data_file)
                if isinstance(transactions, list):
                    return transactions
                else:
                    return []
            except json.JSONDecodeError:
                return []
    except FileNotFoundError:
        return []


def get_amount_in_rub(transaction: dict) -> float | str:
    """
    Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    при необходимости конвертирует суммы операции в рубли.
    """

    try:
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            return float(transaction["operationAmount"]["amount"])
        else:
            return currency_conversion_in_rub(transaction)
    except KeyError:
        return "Транзакция не найдена"
