# 4 - oy 5 dars
# homeworks
from decimal import Decimal
import random
from datetime import datetime
# 1 - masala
class Temperature:
    def __init__(self):
        self._temperature = None
        self._date = None

    def __set__(self, instance, value):
        temp = Decimal(value)
        if not (-50 <= temp <= 50):
            raise ValueError("Harorat me'yordan chiqib ketdi (-50°C dan 50°C gacha).")
        self._temperature = temp
        self._date = datetime.now()

    def __get__(self, instance, owner):
        return f"Harorat: {self._temperature}°C ({self._date.strftime('%Y-%m-%d')})."

class TemperatureSystem:
    temperature = Temperature()

temp_sys = TemperatureSystem()
try:
    temp_sys.temperature = random.uniform(-10, 40)  # Tasodifiy harorat
    print(temp_sys.temperature)
except ValueError as e:
    print(f"Xatolik: {e}")
#--------------------------------------------------------------
# 2 - masala
class InsufficientFundsError(Exception):
    pass

class Transaction:
    def __init__(self):
        self._balance = Decimal("0.00")

    def __get__(self, instance, owner):
        return self._balance

    def __set__(self, instance, value):
        value = Decimal(value)
        if self._balance + value < 0:
            raise InsufficientFundsError("Balans yetarli emas!")
        self._balance += value

class BankAccount:
    balance = Transaction()

    def __init__(self):
        self.transactions = []

    def deposit(self, amount):
        self.balance = amount
        self.transactions.append((amount, datetime.now()))

    def withdraw(self, amount):
        self.balance = -amount
        self.transactions.append((-amount, datetime.now()))

account = BankAccount()
try:
    account.deposit("500000")
    account.withdraw("600000")
    print(f"Hisobingiz: {account.balance} UZS")
except InsufficientFundsError as e:
    print(f"Xatolik: {e}")
#--------------------------------------------------------
# 3- masala
class TicketPrice:
    def __set__(self, instance, value):
        price = Decimal(value)
        if price <= 0:
            raise ValueError("Chipta narxi noto'g'ri kiritildi.")
        instance._price = price
        instance._sale_date = datetime.now()

    def __get__(self, instance, owner):
        return f"Chipta narxi: {instance._price} UZS. Sotish sanasi: {instance._sale_date.strftime('%Y-%m-%d')}."

class Ticket:
    price = TicketPrice()

ticket = Ticket()
try:
    ticket.price = "150000"
    print(ticket.price)
except ValueError as e:
    print(f"Xatolik: {e}")
#-------------------------------------------------------------------
# 4 - masala
class Salary:
    def __set__(self, instance, value):
        salary = Decimal(value)
        if salary <= 0:
            raise ValueError("Oylik maosh noto'g'ri kiritildi.")
        instance._salary = salary
        instance._payment_date = datetime.now()

    def __get__(self, instance, owner):
        return f"Ishchi oyligi: {instance._salary} UZS. To'lov sanasi: {instance._payment_date.strftime('%Y-%m-%d')}."

class Worker:
    salary = Salary()

worker = Worker()
try:
    worker.salary = "3200000"
    print(worker.salary)
except ValueError as e:
    print(f"Xatolik: {e}")

