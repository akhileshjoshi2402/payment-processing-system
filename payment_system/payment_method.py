from abc import ABC, abstractmethod

class PaymentMethod(ABC):

	@abstractmethod
	def set_payment_method(self):
		pass

class CreditCard(PaymentMethod):

	def __init__(self):
		self.__payment_method = ""

	def set_payment_method(self):
		self.__payment_method = "CreditCard"
		return self._CreditCard__payment_method

class UPI(PaymentMethod):

	def __init__(self):
		self.__payment_method = ""

	def set_payment_method(self):
		self.__payment_method = "UPI"
		return self._UPI__payment_method
