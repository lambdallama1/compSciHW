#!/bin/python3
def fact(n):
	if n == 0:
		return 1
	return n * fact(n - 1)

def binomial(n, k):
	return int(fact(n) / (fact(k) * fact(n - k)))

for row in range(1, 11):
	rowToPrint = []
	for element in range(row + 1):
		rowToPrint += [binomial(row, element)]
	print(*rowToPrint)	
