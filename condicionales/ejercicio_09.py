num_1 = int(input('dime el num_1: '))
num_2 = int(input('dime el num_2: '))
num_3 = int(input('dime el num_3: '))

if num_1 > num_2 and num_1 > num_3:
	if num_2 > num_3:
		print(num_1, '', num_2, '', num_3)
	else:
		print(num_1, '', num_3, '', num_2)

if num_2 > num_1 and num_2 > num_3:
	if num_1 > num_3:
		print(num_2, '', num_1, '', num_3)
	else:
		print(num_2, '', num_3, '', num_1)

if num_3 > num_1 and num_3 > num_2:
	if num_1 > num_2:
		print(num_3, '', num_1, '', num_2)
	else:
		print(num_3, '', num_2, '', num_1)
