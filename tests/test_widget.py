import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "data, mask",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Visa Gold 59994128426353", "Некорректный ввод"),
        (" ", "Некорректный ввод"),
        ([], "Некорректный ввод"),
    ],
)
def test_card(data, mask):
    assert mask_account_card(data) == mask


@pytest.mark.parametrize(
    "data, format_data",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2024-03-11T02:26:18.67140", "Некорректный ввод"),
    ],
)
def test_date(data, format_data):
    assert get_date(data) == format_data
