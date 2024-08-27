from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """Возвращает строку с замаскированным номером."""
    list_numbers = []
    for i in card:
        if i.isdigit():
            list_numbers.append(i)
    if len(list_numbers) == 16:
        return get_mask_card_number(card)
    elif len(list_numbers) == 0:
        return "Вы не ввели номер карты или счета!"
    else:
        return get_mask_account(card)


def get_date(date: str) -> str:
    """Возвращает строку с датой в формате 'ДД.ММ.ГГГГ'."""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


user_date = "2024-03-11T02:26:18.671407"
print(get_date(user_date))

user_input = input()
print(mask_account_card(user_input))
