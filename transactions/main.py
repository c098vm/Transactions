import utils
import modules

JSON_PATH = "data/operations.json"
TRANSACTIONS_NUMBER = 50

def main():
    data = utils.load_transactions(JSON_PATH)
    processed_data = utils.data_convert(data)

    for i in range(0, TRANSACTIONS_NUMBER):
        try:
            date = processed_data[i]["date"]
        except:
            date = None
        try:
            description = processed_data[i]["description"]
        except:
            description = None
        try:
            fromho = processed_data[i]["from"]
        except:
            fromho = None
        try:
            toho = processed_data[i]["to"]
        except:
            toho = None
        try:
            amount = processed_data[i]["operationAmount"]["amount"]
        except:
            amount = None
        try:
            currency = processed_data[i]["operationAmount"]["currency"]["name"]
        except:
            currency = None

        transaction_object = modules.Transaction(date, description, fromho, toho, amount, currency)
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






