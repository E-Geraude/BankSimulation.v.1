from src import Customer,Bank


class Person:
    # Construtor of objets person
    def __init__(self, first_name, last_name, adress, email, number_phone):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__adress = adress
        self.__email = email
        self.__number_phone = number_phone

    # Get information of person
    def getFirstName(self):
        return self.__first_name
    def getLastName(self):
        return self.__last_name
    def getAdress(self):
        return self.__adress
    def getEmail(self):
        return self.__email
    def getNumberPhone(self):
        return self.__number_phone

    # Modification of information of person
    def setFirstName(self, first_name):
        self.__first_name = first_name
    def setLastName(self, last_name):
        self.__last_name = last_name
    def setAdress(self, adress):
        self.__adress = adress
    def setEmail(self, email):
        self.__email = email
    def setNumberPhone(self, number_phone):
        self.__number_phone = number_phone


    def sendMoney(self,receiver_customer: Customer, amount):
        pass

    def become_customer(self, bank: Bank):
        pass

    def __str__(self):
        pass
