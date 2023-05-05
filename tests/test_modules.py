from transactions import modules

def test_get_date():
    assert modules.Transaction.get_date(None, "2019-08-26T10:50:58.294041") == "26.08.2019"

def test_masking_card_number():
    assert modules.Transaction.masking_card_number(None, "1596837868705199") == "1596 83** **** 5199"

def test_masking_account_number():
    assert modules.Transaction.masking_account_number(None, "Счет 64686473678894779589") == "**9589"
