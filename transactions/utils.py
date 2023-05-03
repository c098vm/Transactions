import json
from operator import itemgetter

def load_transactions(path):
    with open(path) as file:
        content = file.read()
        data = json.loads(content)
        return data


def list_no_empty_convert(data):
    data_no_empty_dic = [item for item in data if item != {}]
    # for item in data:
    #     if item != {}:
    #         data_no_empty_dic.append(item)
    return data_no_empty_dic


def list_reverse_sort(data, key):
    data_sorted = sorted(data, key=itemgetter(key), reverse=True)
    return data_sorted


def make_report(date, description, fromho, toho, amount, currency):
    return f'{date} {description}' \
           f'{fromho} -> {toho}' \
           f'{amount} {currency}'
