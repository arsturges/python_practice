import random

voc = ['x','x',' ','+','-','*','/','1','2','3']
evaluation_range = xrange(-10,11)

#expression = x**2 + 2 # 8 chars
random_expression = []
for i in range(8):
	random_expression.append(voc[random.randint(0, len(voc)-1)])
string = "".join(random_expression)
exec(string)
