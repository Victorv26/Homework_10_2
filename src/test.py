from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Функция маскирующая счет/карту"""
    if len(type_and_number.split()[-1]) == 20:
        return f"{"".join(type_and_number.split()[:-1])} {get_mask_account(type_and_number.split()[-1])}"
    elif len(type_and_number.split()[-1]) == 16:
        return f"{"".join(type_and_number.split()[:-1])} {get_mask_card_number(type_and_number.split()[-1])}"


print(mask_account_card('MasterCard 7158300734726758'))