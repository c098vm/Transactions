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


