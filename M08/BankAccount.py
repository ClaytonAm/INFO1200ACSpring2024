class Bank:
    name: str
    balance: float
    interestRate: float

    def __init__(self, nm, blnc, ir):
        """Constructor Method to init all properties

        Args:
            nm (str): Name of account
            blnc (float): Initial balance
            ir (float): Interest rate
        """
        self.name = nm
        self.balance = blnc
        self.interestRate = ir

    def createUserName(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"{self.name}_1234"

    def applyRandomGift(self, gift):
        """_summary_

        Args:
            gift (_type_): _description_

        Returns:
            _type_: _description_
        """
        oldBalance = self.balance
        self.balance = self.balance + gift
        return f"Old Balance: {oldBalance}\n\
                 Gift: {gift}\n\
                 New Balance: {self.balance}"
