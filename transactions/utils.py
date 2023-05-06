import json
from operator import itemgetter


def load_transactions(path):
    """Загружает данные из файла json"""
    try:
        with open(path) as file:
            content = file.read()
            data = json.loads(content)
            return data
    except Exception:
        print('Файл не найден')
        exit()


def data_convert(data):
    """
    Получает из списка словарей новый список словарей,
    отфильтрованный по state="EXECUTED" и отсортированный
    в обратном порядке по значению date
    """
    data_no_empty_executed = [item for item in data if item != {} and item["state"] == "EXECUTED"]
    data_sorted = sorted(data_no_empty_executed, key=itemgetter("date"), reverse=True)
    return data_sorted


def get_date(data):
    """
    Преобразует данные из формата DateTime
    в требуемый формат ДД.ММ.ГГГГ
    :param data: данные в формате DateTime
    :return: дата в требуемом формате ДД.ММ.ГГГГ
    """
    if data == None:
        return None
    dd = data[8:10]
    mm = data[5:7]
    yyyy = data[:4]
    return f"{dd}.{mm}.{yyyy}"


def masking_card_number(data):
    """
    Маскирует номер карты
    :param data: полный номер карты
    :return: номер карты с маской
    """
    card_number = data[-16:-12] + " " + data[-12:-10] + "** **** " + data[-4:]
    return card_number


def masking_account_number(data):
    """
    Маскирует номер счета
    :param data: полный номер счета
    :return: номер счета с маской
    """
    account_number = "**" + data[-4:]
    return account_number


def card_account_choice(data):
    """
    В зависимости от наличия в реквизитах отправителя или получателя
    слова "Счет" определяет номер счета или номер карты
    и по результату вызывает нужную функцию маскирования
    :param data: номер счета или номер карты
    :return: номер счета или номер карты с маской
    """
    if data == None:
        return data
    if data[:4] == "Счет":
        return f"{data[:4]} {masking_account_number(data)}"
    return f"{data[:-17]} {masking_card_number(data)}"


def make_report(date, description, fromho, toho, amount, currency):
    report = ""
    """
    Формирует и возвращает запись о транзакции в нужном формате
    с учетом возможного отсутствия:
    - номера счета (карты) отправителя при открытии нового счета
    - номера счета (карты) получателя при закрытии счета
    :param date: дата операции
    :param description: описание операции
    :param fromho: отправитель
    :param toho: адресат
    :param amount: сумма операции
    :param currency: валюта операции
    :return: запись о транзакции в нужном формате
    """
    report += f'{date} {description}\n'
    if fromho == None:
        report += toho
    elif toho == None:
        report += fromho
    else:
        report += f'{fromho} -> {toho}'
    report += '\n' + f'{amount} {currency}'
    return report

