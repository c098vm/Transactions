import json
from operator import itemgetter


def load_transactions(path):
    """Загружает данные из файла json"""
    with open(path) as file:
        content = file.read()
        data = json.loads(content)
        return data


def data_convert(data):
    """
    Получает из списка словарей новый список словарей,
    отфильтрованный по state="EXECUTED" и отсортированный
    по значению date в обратном порядке
    """
    data_no_empty_executed = [item for item in data if item != {} and item["state"] == "EXECUTED"]
    data_sorted = sorted(data_no_empty_executed, key=itemgetter("date"), reverse=True)
    return data_sorted


def make_report(date, description, fromho, toho, amount, currency):
    return f'{date} {description}' \
           f'{fromho} -> {toho}' \
           f'{amount} {currency}'
