def get_mask_card_number(card: str) -> str:
    """Принимает на вход номер карты и возвращает ее маску."""
    return f"{card[0:4]} {card[4:6]}** **** {card[12:16]}"


def get_mask_account(acc: str) -> str:
    """Принимает на вход номер счета и возвращает его маску."""
    return f"** {acc[12:16]}"


card_number = input()
account = input()

print(get_mask_card_number(card_number))
print(get_mask_account(account))
