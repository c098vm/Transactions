from transactions import utils


def test_get_date():
    assert utils.get_date(None) == None
    assert utils.get_date("2019-08-26T10:50:58.294041") == "26.08.2019"


def test_masking_card_number():
    assert utils.masking_card_number("1596837868705199") == "1596 83** **** 5199"


def test_masking_account_number():
    assert utils.masking_account_number("Счет 64686473678894779589") == "**9589"


def test_card_account_choice():
    assert utils.card_account_choice(None) == None
    assert utils.card_account_choice("Счет 64686473678894779589") == "Счет **9589"
    assert utils.card_account_choice("Visa Gold 1596837868705199") == "Visa Gold 1596 83** **** 5199"


def test_make_report():
    report = "14.04.2018 Перевод организации\n" + \
             "Счет **8655 -> Visa Platinum 2256 48** **** 2539\n" + \
             "96995.73 руб."
    assert utils.make_report(
        utils.get_date("2018-04-14T19:35:28.978265"),
        "Перевод организации",
        utils.card_account_choice("Счет 27248529432547658655"),
        utils.card_account_choice("Visa Platinum 2256483756542539"),
        "96995.73",
        "руб."
    ) == "14.04.2018 Перевод организации\nСчет **8655 -> Visa Platinum 2256 48** **** 2539\n96995.73 руб."

    report = "14.04.2018 Перевод организации\n" + \
             "Visa Platinum 2256 48** **** 2539\n" + \
             "96995.73 руб."
    assert utils.make_report(
        utils.get_date("2018-04-14T19:35:28.978265"),
        "Перевод организации",
        utils.card_account_choice(None),
        utils.card_account_choice("Visa Platinum 2256483756542539"),
        "96995.73",
        "руб."
    ) == "14.04.2018 Перевод организации\nVisa Platinum 2256 48** **** 2539\n96995.73 руб."

    report = "14.04.2018 Перевод организации\n" + \
             "Счет **8655\n" + \
             "96995.73 руб."
    assert utils.make_report(
        utils.get_date("2018-04-14T19:35:28.978265"),
        "Перевод организации",
        utils.card_account_choice("Счет 27248529432547658655"),
        utils.card_account_choice(None),
        "96995.73",
        "руб."
    ) == "14.04.2018 Перевод организации\nСчет **8655\n96995.73 руб."


def test_data_convert():
    assert utils.data_convert(
        [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041"
            },
            {
                "id": 41428829,
                "state": "CANCELED",
                "date": "2019-07-03T18:35:29.512364"
            },
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572"
            }
        ]
    ) == [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041"
            },
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572"
            }
        ]

