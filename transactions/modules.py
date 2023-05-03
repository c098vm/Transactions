class Transaction:
    def __int__(
            self,
            date,
            description,
            fromho,
            toho,
            amount,
            currency
    ):
        self.date = date
        self.description = description
        self.fromho = fromho
        self.toho = toho
        self.amount = amount
        self.currensy = currency


    def get_date(self, data):
        dd = data[8:10]
        mm = data[5:7]
        YYYY = data[:4]
        return f"{dd}.{mm}.{YYYY}"

    def masking_card_number(self, data):
        card_number = data[-16:-12] + " " + data[-12:-10] + "** **** " + data[-4:]
        return card_number


    def masking_account_number(self, data):
        account_number = "**" + data[-4:]
        return account_number

    def card_account_choice(self, data):
        if data[:4] == "Счет":
            return f"{data[:4]} {self.masking_account_number(data)}"
        return f"{data[:-17]} {self.masking_card_number(data)}"


    def __repr__(self):
        return f'{self.__class__.__name__}(date={self.date}, ' \
               f'description={self.description}, fromho={self.fromho}, ' \
               f'toho={self.toho}, amount={self.amount}, currency={self.currensy}')

