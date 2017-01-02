current = 1
new = 2
sum = 0
while new < 4000000:
	if new % 2 == 0:
		sum = sum + new
	prev = new
	new = new + current
	current = prev
print sum
	
	
