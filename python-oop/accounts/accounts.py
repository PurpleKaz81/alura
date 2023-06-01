from account import Account
from client import Client
import clients

# creating accounts and adding to the list
account_1 = Account(123, clients.client_1, 1000)
account_2 = Account(321, clients.client_2, 100)
account_3 = Account(666, clients.client_3, 2679, 2000)
account_4 = Account(222, clients.client_4, 140000, 600000)
