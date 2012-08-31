'''
Breakout Session Work
consider the following data (file: airline.py):
1. print out a schedule organized by airline:
2. print out a schedule organized by time
hint: you'll need to do a manual sorting on the last
element of each flight element, before beginning the
printing loop
'''
from airline import flights, airports 

print "Airline" + "\t" + "Flight Number" + "\t" + "Destination" + "\t" + "Gate" + "\t" + "Time"
print "-"*70
for flight in flights:
	print flight[0] +"\t" + str(flight[1]) + "\t" + airports[flight[2]] + "\t" + str(flight[3]) + "\t" + str(flight[4])













def cheeseshop(kind, *arguments, **keywords):
	'''Here's the docstring. Text and help.'''
	print("Kind is:",kind)
	print("Arguments are:")
	for arg in arguments:
		print(arg)
	print("-"*40)
	for keyword in keywords:
		print(keyword)

cheeseshop("Camembert", "John Cloose", 5, 3.25593, color="gree", flavor="mild")
print("__name__ is:", __name__)
