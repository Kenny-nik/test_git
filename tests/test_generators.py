import pytest
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)


def test_filter_by_currency_not_valut(test_filter):
    result = filter_by_currency(test_filter)
    assert next(result) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {"name": "USD", "code": "USD"},
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }


def test_filter_by_currency(test_filter):
    result = filter_by_currency(test_filter, "RUB")
    assert next(result) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {"name": "руб.", "code": "RUB"},
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


def test_transaction_descriptions(test_filter):
    result = transaction_descriptions(test_filter)
    assert next(result) == "Перевод организации"


@pytest.mark.parametrize("a, b, expected", [(1, 1, "0000 0000 0000 0001")])
def test_card_number_generator(a, b, expected):
    s = card_number_generator(a, b)
    assert next(s) == expected


def test_card_num_nine():
    result = card_number_generator(9999999999999999, 9999999999999999)
    assert next(result) == "9999 9999 9999 9999"
