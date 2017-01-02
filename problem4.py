def is_palindrom(number):
	num = number
	num1 = 0 
	i=6
	while number > 0:
		num1 = num1*10 + number % 10
		number = number / 10
	if num == num1:
		return True
	else:
		return False
all_palindrom = []

def test():

	number = 999999
	while number > 100000:
		if is_palindrom(number):
			all_palindrom.append(number)
		number -= 1
	for i in all_palindrom:
		j = 999
		while j>100:
			if i%j == 0:
				if i/j > 100 and i/j<= 999:
					return j, i/j, i
			j -= 1
print test()
		
