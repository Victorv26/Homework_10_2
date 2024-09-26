from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Функция маскирующая счет/карту"""
    text_result = ""
    digit_result = ""
    digit_count = 0
    for symbol in type_and_number:
        if symbol.isalpha():
            text_result += symbol
        elif symbol.isdigit():
            digit_count += 1
            digit_result += symbol
    if digit_count == 20:
        return f"{text_result} {get_mask_account(digit_result)}"
    elif digit_count == 16:
        return f"{text_result} {get_mask_card_number(digit_result)}"


print(mask_account_card("Maestro 1596837868705199"))


def get_date(date_str: str) -> str:
    """Функция принимает строку и возвращает дату в формате ДД.ММ.ГГГГ"""
    date_slice = date_str[0:10].split("-")
    return ".".join(date_slice[::-1])
