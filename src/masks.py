from typing import Union


def get_mask_card_number(card: Union[str, int]) -> Union[str, int]:
    """Принимает на вход номер карты и возвращает ее маску."""
    card_split = str(card)
    list_numbers = [i for i in card_split if i.isdigit()]
    if len(list_numbers) == 16:
        list_letters = [i for i in card_split]
        list_1 = [
            (
                list_letters[i]
                if i not in range(len(list_letters) - 10, len(list_letters) - 4)
                else "*"
            )
            for i in range(len(list_letters))
        ]
        list_1.insert(-4, " ")
        list_1.insert(-9, " ")
        list_1.insert(-14, " ")
        result = "".join(list_1)
        return result
    else:
        return "Некорректный ввод"


def get_mask_account(acc: Union[str, int]) -> Union[str, int]:
    """Принимает на вход номер счета и возвращает его маску."""
    acc_split = str(acc)
    list_numbers = [i for i in acc_split if i.isdigit()]
    if len(list_numbers) == 20:
        list_letters = [i for i in acc_split]
        list_1 = [
            (
                list_letters[i]
                if i not in range(len(list_letters) - 20, len(list_letters) - 4)
                else "*"
            )
            for i in range(len(list_letters))
        ]
        while list_1.count("*") > 2:
            list_1.remove("*")
        result = "".join(list_1)
        return result

    else:
        return "Некорректный ввод"
