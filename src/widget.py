from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    '''Функция маскирующая счет/карту'''
    text_result = ''
    digit_count = 0
    for symbol in type_and_number:
        if symbol.isalpha():
            text_result += symbol
        elif symbol.isdigit():
            digit_count += 1
    if digit_count > 16:
        return text_result + str(get_mask_account)
    else:
        return text_result + str(get_mask_card_number)

#print(mask_account_card('Счет 35383033474447895560'))


def get_date(date_str: str) -> str:
    '''Функция принимает строку и возвращает дату в формате ДД.ММ.ГГГГ'''
    date_slice = date_str[0:10].split('-')
    return '.'.join(date_slice[::-1])