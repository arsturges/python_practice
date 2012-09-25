import MySQLdb as msd # sudo apt-get install python-mysqldb

# PEP 249 defines how the Python database API works:
# http://www.python.org/dev/peps/pep-0249/

# These methods take a connection object, 
# then create their own cursors, execute the query,
# and close their cursors.

def sum_tWhs(connection_object, aeo_edition, case_id):
	params = (aeo_edition, case_id)
	sql_string = "SELECT SUM(Value) \
		AS sum_tWhs FROM `Elec_Gen_Cap` \
		WHERE `Category` = 'Generation' \
		AND `Region` = 'US' \
		AND `AEO_Edition` = %s \
		AND `CaseID` = %s;"

	cursor = connection_object.cursor()
	cursor.execute(sql_string, params) 
	rows = cursor.fetchall()
	cursor.close()
	return rows[0][0]

def sum_quads(connection_object, aeo_edition, case_id):
	params = (aeo_edition, case_id)
	sql_string = "SELECT SUM(Value) \
		AS sum_quads FROM `Fuel_Consumption` \
		WHERE `Category` = 'Consumption' \
		AND `Region` = 'US' \
		AND `AEO_Edition` = %s \
		AND `CaseID` = %s;"

	cursor = connection_object.cursor()
	cursor.execute(sql_string, params) 
	rows = cursor.fetchall()
	cursor.close()
	return rows[0][0]

def show_distinct_cases(connection_object):
	from pprint import pprint
	sql_string = "SELECT DISTINCT CaseID \
		FROM Fuel_Consumption;"
	cursor = connection_object.cursor()
	cursor.execute(sql_string) 
	rows = cursor.fetchall()
	cursor.close()
	pprint(rows)

def heat_rate(btus, kWhs):
	#assert btus = integer or float
	#assert kWhs = integer or float
	heat_rate = btus/kWhs
	return heat_rate

def capacity_factor(average_load, rated_capacity):
	# average_load and rated_capacity are in units kW
	capacity_factor = average_load / rated_capacity
	return capacity_factor
	# Units: percentage 

def load_factor(average_load, peak_load):
	# average_load and peak_load are in units kW
	load_factor = average_load / peak_load
	return load_factor
	# Units: percentage


if __name__ == '__main__':
	# The module 'secret' holds the username and password.
	# Import it instead of storiing in this file as plain text
	# so that this file can be put in version control.
	# Don't put the module 'secret.py' in version control.
	import secret

	user = secret.user
	passwd = secret.passwd

	conn = msd.connect(
		host="ead5.lbl.gov",
		user = user,
		passwd = passwd,
		db="TestUser",
		use_unicode = True,
		charset = "utf8",
		init_command='SET NAMES utf8')

	with conn:
		fan_quads_3001 = sum_quads(conn, '2011','commcl3001')
		fan_quads_3002 = sum_quads(conn, '2011','commcl3002')
		fan_tWhs_3001 = sum_tWhs(conn, '2011','commcl3001')
		fan_tWhs_3002 = sum_tWhs(conn, '2011','commcl3002')

	print heat_rate(fan_quads_3001*10**15, fan_tWhs_3001*10**9)	
