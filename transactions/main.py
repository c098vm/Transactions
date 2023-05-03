import utils

PATH = "data/operations.json"

data = utils.load_transactions(PATH)

# n = 100
# date_data = d[n]['date']
# from_data = d[n]['from']
# to_data = d[n]['to']
# amount_data = d[n]['operationAmount']['amount']
# currency_name_data = d[n]['operationAmount']['currency']['name']
# print(utils.convert_date(date_data), d[n]['description'])
# print(f"{utils.card_account_choice(from_data)} -> {utils.card_account_choice(to_data)}")
# print (amount_data, currency_name_data)
