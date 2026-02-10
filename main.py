from payment_system import *

def main():
	print("Welcome to Payment System:")

	user_payment = Payment()

	while True:
		print("-" * 50)
		print("Press 1 for add cash to the system")
		print("Press 2 to refund the money")
		print("Press 3 to check balance")
		print("Press 4 to check the transaction history")
		print("Press 5 to exit the system")
		print("-" * 50)

		try:
			choice = int(input("Enter your choice: "))
		except Exception as e:
			print("Choice should be an integer from 1 to 5!")
			continue

		if choice == 1:
			print("-" * 50)
			print("Please select the payment method:")
			payment_method = input("Enter 'C' for credit card and 'U' for UPI: ").upper().strip().replace(" ", "")

			if payment_method == 'C':
				try:
					amount = float(input("Enter amount to be credited: "))

					if amount <= 0.0:
						print("Amount should be a positive value!")
					else:
						user_payment.credit(amount, CreditCard().set_payment_method())
				
				except Exception as e:
					print("Amount should be a float value!")

			elif payment_method == 'U':
				try:
					amount = float(input("Enter amount to be credited: "))
		
					if amount <= 0.0:
						print("Amount should be a positive value!")
					else:
						user_payment.credit(amount, UPI().set_payment_method())

				except Exception as e:
					print("Amount should be a float value!")

			else:
				print("Enter 'C' or 'U' for payment method!")

		elif choice == 2:
			try:
				amount = float(input("Enter amount to be refunded: "))

				if amount <= 0.0:
					print("Amount should be a positive value!")
				else:
					user_payment.refund(amount)

			except Exception as e:
				print("Amount should be a float value!")
				

		elif choice == 3:
			user_payment.show_balance()

		elif choice == 4:
			user_payment.show_transaction_history()

		elif choice == 5:
			print("Exiting the application...")
			break

		else:
			print("Invalid choice! Choice should be between 1 to 5!")

if __name__ == "__main__":
	main()