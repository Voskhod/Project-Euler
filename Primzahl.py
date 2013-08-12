from math import *

def is_prime(num): 
	sqrt_nr = ceil(sqrt(num))
	i = 2
	while i <= sqrt_nr:
		if not num % i and i != num:
			return false
		i = incr(1)
	return True

def incr(i):
	if i <= 2:
		return i + 1
	else:
		return i + 2

def find_next_prime(prime):
	prime = incr(prime)
	while not is_prime(prime):
		prime = incr(prime)
	return prime

i = 2
prime = 3
while i < 10001:
	prime = find_next_prime(prime)
	i = i + 1
print " Prime %d is %d\n" % (i, prime)

