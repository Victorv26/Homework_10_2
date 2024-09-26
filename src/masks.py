from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> Union[int, str]:
    """Функция маскировки номера банковской карты"""
    return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[12:]}"


if __name__ == "__main__":
    print(get_mask_card_number(1596837868705199))


def get_mask_account(count_number: Union[int, str]) -> Union[int, str]:
    """Функция маскировки номера банковского счета"""
    return f"**{str(count_number)[-4:]}"


if __name__ == "__main__":
    print(get_mask_account(64686473678894779589))
