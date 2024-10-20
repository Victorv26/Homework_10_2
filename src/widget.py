from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Функция маскирующая счет/карту"""
    new_number = type_and_number.split()
    if len(new_number[-1]) == 20:
        return f"{" ".join(new_number[:-1])} {get_mask_account(new_number[-1])}"
    elif len(new_number[-1]) == 16:
        return f"{" ".join(new_number[:-1])} {get_mask_card_number(new_number[-1])}"


def get_date(date_str: str) -> str:
    """Функция принимает строку и возвращает дату в формате ДД.ММ.ГГГГ"""
    date_slice = date_str[0:10].split("-")
    if date_str[4] != '-' and date_str[7] != '-':
        raise ValueError('Неверный формат даты')
    return ".".join(date_slice[::-1])
