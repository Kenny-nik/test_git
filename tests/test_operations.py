import pytest

from src.operations import counter_description, search_by_pattern


def test_search_by_pattern(data_transaction: list) -> None:
    assert search_by_pattern(data_transaction, "Visa") == [
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]
    assert search_by_pattern(data_transaction, "вклад") == []
    assert search_by_pattern([], "счет") == []


def test_counter_description(data_transaction: list, description_list: list) -> None:
    assert counter_description(data_transaction, description_list) == {
        "Перевод организации": 2,
        "Перевод со счета на счет": 2,
        "Перевод с карты на карту": 1,
    }
    assert counter_description([], []) == {}