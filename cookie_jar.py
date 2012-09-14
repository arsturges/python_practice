class CookieJar:
	num_pennies = 0
	num_nickels = 0
	num_dimes = 0
	num_quarters = 0
	num_transactions_completed = 0

	#calc_change(3.45) → {"quarter": 2, "dime": 0, "nickel": 1, "penny": 0}
	def calc_change(amt):
