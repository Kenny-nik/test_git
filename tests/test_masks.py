import pytest
from src.masks import get_mask_card_number, get_mask_account


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
    assert get_mask_card_number(data) == mask


@pytest.mark.parametrize(
    "data, mask",
    [
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Счет 736541084135874305", "Некорректный ввод"),
        (" ", "Некорректный ввод"),
        ([], "Некорректный ввод"),
    ],
)
def test_acc(data, mask):
    assert get_mask_account(data) == mask
