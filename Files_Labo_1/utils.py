# utils.py
# Math library
# Author: Sébastien Combéfis
# Version: February 8, 2018
import math
from cmath import sqrt

def fact(n):
	return math.factorial(n)

def roots(a, b, c):
	delta = (b**2 - 4*a*c)
	root1 = (-b + sqrt(delta))/(2*a)
	root2 = (-b - sqrt(delta))/(2*a)
	if root1 != root2:
		return (root1, root2)
	if root1 == root2:
		return(root1)

def integrate(function, lower, upper):
	import scipy.integrate as integrate
	import math
	result= integrate.quad(lambda x: eval(function), lower,upper)
	answer= result[0]
	return answer




if __name__ == '__main__':
	print(fact(5))
	print(roots(2, 5, 1))
	print(integrate('x ** 2 - 1', -1, 1))
