from sqlite3.dbapi2 import paramstyle

import pytest
from mypy.types import NoneTyp

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('type_and_number, expected', [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                                       ('Счет 64686473678894779589', 'Счет **9589'),
                                                       ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                                                       ('Счет 35383033474447895560', 'Счет **5560'),
                                                       ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                                       ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
                                                       ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
                                                       ('Счет 73654108430135874305', 'Счет **4305')])
def test_mask_account_card(type_and_number, expected):
    '''Тестируется маскировка номера карты'''
    assert mask_account_card(type_and_number) == expected


@pytest.mark.parametrize('date_str, expected', [('2024-03-11T02:26:18.671407', '11.03.2024'),
                                                ('2024-05-12T02:26:18.671407', '12.05.2024')])
def test_get_date(date_str, expected):
    '''Тестируется функция преобразования даты в формат ДД.ММ.ГГГГ'''
    assert get_date(date_str) == expected


def test_get_date_incorrect(date_str):
    '''Тестируется функция на ввод некорректного формата даты'''
    with pytest.raises(ValueError):
        get_date('202403-11T02:26:18.671407')
