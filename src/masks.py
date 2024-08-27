def get_mask_card_number(card: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""
    card_split = card.split()
    list_name_card = []
    list_numbers = []

    for i in card_split:
        if i.isalpha():
            list_name_card.append(i)

    for i in card:
        if i.isdigit():
            list_numbers.append(i)

    name_card = " ".join(list_name_card)
    numbers_card = "".join(list_numbers)
    return f"{name_card} {numbers_card[0:4]} {numbers_card[4:6]}** **** {numbers_card[12:16]}"


def get_mask_account(acc: str) -> str:
    """Принимает на вход номер счета и возвращает его маску."""
    card_split = acc.split()
    list_name_card = []
    list_numbers = []

    for i in card_split:
        if i.isalpha():
            list_name_card.append(i)

    for i in acc:
        if i.isdigit():
            list_numbers.append(i)

    name_card = " ".join(list_name_card)
    numbers_card = "".join(list_numbers)
    return f"{name_card} **{numbers_card[12:16]}"
