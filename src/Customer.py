from src import Person, Count, Bank

class Customer(Person):
    # Constructor of objets customer
    def __init__(self, list_count, is_Customer):
        super().__init__()
        self.__list_count = [count for count in list_count]
        self.__is_Customer = is_Customer


    # Get information of customer
    def getListCount(self):
        return self.__list_count
    def getIsCustomer(self):
        return self.__is_Customer


    def viewCount(self):
        pass

    def makeTransfer(self, source_count: Count, destination_count: Count, amount):
        pass

    def depositMoney(self, source_count, amount):
        pass

    def withdrawMoney(self, source_count: Count, amount):
        pass

    def viewTransactionsHistory(self, bank: Bank):
        pass
