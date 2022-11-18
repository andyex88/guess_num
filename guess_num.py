import random
begin = input('Please enter a beginning value of your random number\'s range：')
begin = int(begin)
end = input('Please enter an ending value of your random number\'s range：')
end = int(end)
r = random.randint(begin, end)
count = 0
while True:
	a = input('Please guess a number： ')
	a = int(a)
	count = count + 1
	if a == r:
		print('You got it right!')
		print('You have guessed', count, 'times')
		break
	elif a > r:
		print('Your guess is more')
	elif a < r:
		print('Your guess is less')
	print('You have guessed', count, 'times')
