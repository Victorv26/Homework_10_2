from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date, list_dict


print(mask_account_card('MasterCard 7158300734726758'))

print(get_date('2019-07-03T18:35:29.512364'))

print(filter_by_state(list_dict))

print(sort_by_date(list_dict))