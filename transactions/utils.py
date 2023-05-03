import json
from operator import itemgetter

def load_transactions(path):
    with open(path) as file:
        content = file.read()
        data = json.loads(content)
        return data


def convert_date(data):
    dd = data[8:10]
    mm = data[5:7]
    YYYY = data[:4]
    return f"{dd}.{mm}.{YYYY}"


def masking_card_number(data):
    card_number = data[-16:-12] + " " + data[-12:-10] + "** **** " + data[-4:]
    return card_number


def masking_account_number(data):
    account_number = "**" + data[-4:]
    return account_number


def card_account_choice(data):
    if data[:4] == "Счет":
        return f"{data[:4]} {masking_account_number(data)}"
    return f"{data[:-17]} {masking_card_number(data)}"


def list_no_empty_convert(data):
    data_no_empty_dic = [item for item in data if item != {}]
    # for item in data:
    #     if item != {}:
    #         data_no_empty_dic.append(item)
    return data_no_empty_dic


def list_reverse_sort(data, key):
    data_sorted = sorted(data, key=itemgetter(key), reverse=True)
    return data_sorted