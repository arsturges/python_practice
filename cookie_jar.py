import numpy as np
class CookieJar:
	num_pennies = 0
	num_nickels = 0
	num_dimes = 0
	num_quarters = 0
	num_transactions_completed = 0


def calc_change(amt):
	change = np.ceil(amt) - amt
	print(change)
	num_quarters = int(np.floor(change/0.25))
	change = change - num_quarters * 0.25
	print(change)
	num_dimes = int(np.floor(change/0.10))
	change = change - num_dimes * 0.10
	print(change)
	num_nickels = int(np.floor(change/0.05))
	change = change - num_nickels * 0.05
	print(change)
	num_pennies = int(change * 100)
	coins = {"quarter": num_quarters, "dime": num_dimes, "nickel": num_nickels, "penny": num_pennies}
	return coins
