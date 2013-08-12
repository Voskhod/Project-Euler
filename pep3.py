def prime_factors(n):
	factors = [] 									# Creating a list, which will contain the prime factors
	d = 2  		 									# Set counter to first prime
	while n > 1: 								    # creating a loop that returns as long as n is larger than one
		while n % d == 0:            				# Creating a loop which runs as long as d is not a factor of n
			factors.append(d)						# Add the factor to the list
			n = n / d 								# If n is devidable by d, then is try n / d
		d = d + 1									# when 
		if d*d > n:
			if n > 1: factors.append(n)
			break
	return factors

pfs = prime_factors(600851475143)
largest_prime_factor = max(pfs)
print largest_prime_factor