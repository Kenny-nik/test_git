import logging
import os

from typing import Union

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "../logs/masks.log")
abs_file_path = os.path.abspath(rel_file_path)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(abs_file_path, mode="w", encoding="utf-8")
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")


def get_data_from_json(path: str) -> List[dict] | Any:
    """
    Принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        logger.info('Открытие файла operations.json')
        with open(path, encoding="utf-8") as data_file:
            try:
                logger.info('Преобразование транзакций из JSON-файла в список словарей')
                transactions = json.load(data_file)
                if isinstance(transactions, list):
                    return transactions
                else:
                    logger.info('Пустой файл')
                    return []
            except json.JSONDecodeError as ex:
                logger.error(f'Ошибка {ex}')
                return []
    except FileNotFoundError:
        logger.error('Ошибка FileNotFoundError')
        return []


def get_amount_in_rub(transaction: dict) -> float | str:
    """
    Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    при необходимости конвертирует суммы операции в рубли.
    """

    try:
        logger.info('Открытие файла operations.json')
        if transaction["operationAmount"]["currency"]["code"] == "RUB":
            logger.info('Возврат суммы транзакции')
            return float(transaction["operationAmount"]["amount"])
        else:
            logger.info('вызов функции конвертации валют')
            return currency_conversion_in_rub(transaction)
    except KeyError:
        logger.error('Ошибка KeyError')
        return "Транзакция не найдена"
