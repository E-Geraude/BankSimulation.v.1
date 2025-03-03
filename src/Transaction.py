

class Transaction():
    # Create transaction
    def __init__(self, amount, date_transaction, count_source, count_destination, state_transaction):
        self.__amount = amount
        self.__date_transaction = date_transaction
        self.__count_source = count_source
        self.__count_destination = count_destination
        self.__state_transaction = state_transaction

    # Get information of transaction
    def getAmount(self):
        return self.__amount
    def getDateTransaction(self):
        return self.__date_transaction
    def getSource(self):
        return self.__source
    def getDestination(self):
        return self.__destination
    def getStats(self):
        return self.__stats

    # Modification of information of transaction
    def setAmount(self, amount):
        self.__amount = amount
    def setDateTransaction(self, date_transaction):
        self.__date_transaction = date_transaction
    def setSource(self, source):
        self.__source = source
    def setDestination(self, destination):
        self.__destination = destination
    def setStats(self, stats):
        self.__stats = stats

    def checkFundsSufficient(self):
        pass
    def showDetails(self):
        pass
    def confirm(self):
        pass
    def recordHistory(self):
        pass
    def calculateFees(self):
        pass