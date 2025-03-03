import Customer
import Count


class Bank:
    """Classe banque : gère les clients, les comptes et les transactions"""

    def __init__(self, bank_name):
        self.__bank_name = bank_name
        self.__customers_list = []
        self.__transactions_list = []
        self.__counts_list = []

    def set_bank_name(self, bank_name):
        """méthode qui définit le nom de la banque"""
        pass

    def get_bank_name(self):
        """méthode qui renvoie le nom de la banque"""
        pass

    def add_customer(self, customer_to_add: Customer):
        """methode pour ajouter les clients"""
        pass

    def delete_customer(self, customer_to_delete: Customer):
        """"méthode pour supprimer un membre de la banque"""
        pass

    def find_customer(self, look_for_customer: Customer):
        """méthode pour réchercher un client de la banque"""
        pass

    def create_count(self, new_customer: Customer, count_number: Count, initial_balance=0.0):
        """méthode pour créer un compte au sein de la banque"""
        pass

    def send_money(self, count_src: Count, count_dest: Count, amount):
        """"méthode pour envoyer de l'argent d'un client à un autre"""
        pass

    def display_all_customers(self):
        """méthode pour afficher tous les membres de la banque"""
        pass

    def display_all_transactions(self):
        """méthode pour afficher toutes les transactions"""
        pass


