def isprime(num):
	if num > 1:
   		# check for factors
   		for i in range(2,num):
       			if (num % i) == 0:
           			return False 
   		return True

def largest_prime_factor(bignumber):
	prime = 2
	while bignumber != 1:
		if bignumber % prime == 0:
			bignumber = bignumber / prime
		else:
			prime = prime + 1
			while isprime(prime) == False:
				prime = prime+1
	return prime
number = 600851475143
print largest_prime_factor(number)
