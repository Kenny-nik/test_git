from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: Any) -> Any:
    """Возвращает строку с замаскированным номером."""
    list_numbers = []
    for i in card:
        if i.isdigit():
            list_numbers.append(i)
    if len(list_numbers) == 16:
        return get_mask_card_number(card)
    else:
        return get_mask_account(card)


def get_date(date: str) -> str:
    """Возвращает строку с датой в формате 'ДД.ММ.ГГГГ'."""
    if len(date) != 26:
        return "Некорректный ввод"
    else:
        return f"{date[8:10]}.{date[5:7]}.{date[:4]}"
