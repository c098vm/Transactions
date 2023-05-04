class Transaction:
    def __init__(self,
                date,
                description,
                fromho,
                toho,
                amount,
                currency):

        """
        Класс транзакции.
        :param date: дата операции
        :param description: описание операции
        :param fromho: отправитель
        :param toho: адресат
        :param amount: сумма операции
        :param currency: валюта операции

        """
        self.date = date
        self.description = description
        self.fromho = fromho
        self.toho = toho
        self.amount = amount
        self.currency = currency


    def get_date(self, data):
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


    def masking_card_number(self, data):
        """
        Маскирует номер карты
        :param data: полный номер карты
        :return: номер карты с маской
        """
        if data == None:
            return None
        card_number = data[-16:-12] + " " + data[-12:-10] + "** **** " + data[-4:]
        return card_number


    def masking_account_number(self, data):
        """
        Маскирует номер счета
        :param data: полный номер счета
        :return: номер счета с маской
        """
        if data == None:
            return None
        account_number = "**" + data[-4:]
        return account_number


    def card_account_choice(self, data):
        """
        В зависимости от наличия в реквизитах отправителя или получателя
        слова "Счет" определяет номер счета или номер карты
        и по результату вызывает нужную функцию маскирования
        :param data: номер счета или номер карты
        :return: номер счета или номер карты с маской
        """
        if data == None:
            return None
        if data[:4] == "Счет":
            return f"{data[:4]} {self.masking_account_number(data)}"
        return f"{data[:-17]} {self.masking_card_number(data)}"


    def make_report(self, date, description, fromho, toho, amount, currency):
        """
        Формирует и возвращает запись о транзакции в нужном формате
        :param date: дата операции
        :param description: описание операции
        :param fromho: отправитель
        :param toho: адресат
        :param amount: сумма операции
        :param currency: валюта операции
        :return: запись о транзакции в нужном формате
        """
        return f'{date} {description}\n' \
               f'{fromho} -> {toho}\n' \
               f'{amount} {currency}'


    def __repr__(self):
        return f'{self.__class__.__name__}(date={self.date}, ' \
               f'description={self.description}, fromho={self.fromho}, ' \
               f'toho={self.toho}, amount={self.amount}, currency={self.currency}'