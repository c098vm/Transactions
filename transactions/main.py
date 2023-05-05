import utils
import modules

# Путь к json-файлу
JSON_PATH = "/home/airat/PycharmProjects/transactions/transactions/data/operations.json"

# Количество выводимых транзакций (по умолчанию - 5, но можно изменить)
TRANSACTIONS_NUMBER = 5


def main():
    """Основная функция исполнения"""

    """
    В переменную data записываем содержимое json-файла,
    конвертируем полученный список с помощью функции data_convert
    и записываем в переменную processed_data
    """
    data = utils.load_transactions(JSON_PATH)
    processed_data = utils.data_convert(data)

    # Зацикливаемся на количество выводимых транзакций
    for i in range(0, TRANSACTIONS_NUMBER):

        # В итерации вытаскиваем значения словарей по ключам и записываем их в переменные
        date = processed_data[i]["date"]
        description = processed_data[i]["description"]
        amount = processed_data[i]["operationAmount"]["amount"]
        currency = processed_data[i]["operationAmount"]["currency"]["name"]

        # Исключаем ошибку отсутствия номера карты счета отправителя или получателя
        try:
            fromho = processed_data[i]["from"]
        except:
            fromho = None
        try:
            toho = processed_data[i]["to"]
        except:
            toho = None


        transaction_object = modules.Transaction(
            date,
            description,
            fromho,
            toho,
            amount,
            currency
        )
        report = transaction_object.make_report(
            transaction_object.get_date(date),
            transaction_object.description,
            transaction_object.card_account_choice(fromho),
            transaction_object.card_account_choice(toho),
            transaction_object.amount,
            transaction_object.currency
        )

        print(f"{report}\n")


if __name__ == "__main__":
    main()






