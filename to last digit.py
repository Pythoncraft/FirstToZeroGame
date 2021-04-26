stack = 86

# print(user_nr)
while stack != 0:
	user_nr = input('your number: ')
	stack = int(stack) - int(user_nr)
	print(stack)
	stack = int(stack) - (6 - int(user_nr))
	print ('after CPU turn:', stack)
	if stack == 0:
		print ('you won!')
		break