import os, sys, inspect

def taunt(name):
	taunt = "Hey %s, you're stupid." % (name)
	return taunt

def fib(n):    # write Fibonacci series up to n
  a, b = 0, 1
  while b < n:
    print b,
    a, b = b, a+b

def fib2(n): # return Fibonacci series up to n
  result = []
  a, b = 0, 1
  while b < n:
    result.append(b)
    a, b = b, a+b
  return result

if __name__ == "__main__":
	import sys
	print __name__
	print taunt(sys.argv[1])
	print(sys.argv[0])
