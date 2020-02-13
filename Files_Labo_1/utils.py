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
	"""Approximates the integral of a fonction between two bounds
	
	Pre: 'function' is a valid Python expression with x as a variable,
		'lower' <= 'upper',
		'function' continuous and integrable between 'lower‘ and 'upper'.
	Post: Returns an approximation of the integral from 'lower' to 'upper'
		of the specified 'function'.

	Hint: You can use the 'integrate' function of the module 'scipy' and
		you'll probably need the 'eval' function to evaluate the function
		to integrate given as a string.
	"""
	pass

if __name__ == '__main__':
	print(fact(5))
	print(roots(2, 5, 1))
	print(integrate('x ** 2 - 1', -1, 1))
