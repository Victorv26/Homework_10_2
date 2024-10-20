from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[int, str]:
    """Функция маскировки номера банковской карты"""
    if len(card_number) != 16:
        raise ValueError("Неверный формат номера")
    return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]}"


def get_mask_account(count_number: Union[int, str]) -> Union[int, str]:
    """Функция маскировки номера банковского счета"""
    if len(count_number) != 20:
        raise ValueError("Неверный формат номера")
    return f"**{str(count_number)[-4:]}"
