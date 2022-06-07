from asyncio.proactor_events import _ProactorBaseWritePipeTransport


class ATM :
    def __init__(self, cardnumber, pin ):
        self.cardnumber = cardnumber
        self.pin = pin

    def balenceinquiry(self):
        print("You balence is : $100")

    def cashwidthdrawl(self):
        print("Cash is Withdrawn!! ")

cash = ATM("9146311","7002")
print(cash.cardnumber)
cash.balenceinquiry()
cash.cashwidthdrawl()
