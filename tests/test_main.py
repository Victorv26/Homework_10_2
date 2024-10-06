import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('card_number, expected', [('1596837868705199', '1596 83** **** 5199')])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize('count_number, expected', [('64686473678894779589', '**9589')])
def test_get_mask_account(count_number, expected):
    assert get_mask_account(count_number) == expected


def test_get_mask_card_number_invalid_number(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


def test_get_mask_account_invalid_number(count_number):
    with pytest.raises(ValueError):
        get_mask_account(count_number)
