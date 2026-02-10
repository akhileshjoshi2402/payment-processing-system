class Payment:

	def __init__(self):
		self.__balance = 0
		self.__transaction_history = []
		self._payment_method = ""

	def credit(self, amount, payment_method):
		self.__balance += amount
		self._payment_method = payment_method
		print(f"${amount} credited successfully via {payment_method}!")
		self.__transaction_history.append({"Payment Type": "Credit", "Payment Method": payment_method, "Amount": f"+ ${amount}", "Balance": f"${self.__balance}"})

	def refund(self, amount):
		if amount > self.__balance:
			print("Insufficient balance! Cannot be refunded!")

		else:
			self.__balance -= amount
			print(f"${amount} refunded successfully!")
			self.__transaction_history.append({"Payment Type": "Refund", "Payment Method": "SystemRefund", "Amount":f"- ${amount}", "Balance": f"${self.__balance}"})

	def show_balance(self):
		print(f"Available balance: ${self.__balance}")

	def show_transaction_history(self):
		if len(self.__transaction_history) == 0:
			print("No history recorded!")
	
		else:
			print("-" * 50)
			print("Payment Type | Payment Method | Amount | Balance |")
			print("-" * 50)

			for payment_history in self.__transaction_history:
				print(f"{payment_history['Payment Type']:^13}|", end="")
				print(f"{payment_history['Payment Method']:^16}|", end="")
				print(f"{payment_history['Amount']:^8}|", end="")
				print(f"{payment_history['Balance']:^9}|")
				print("-" * 50)