import random
r = random.randint(1, 100)
while True:
	a = input('請猜數字： ')
	a = int(a)
	if a == r:
		print('終於答對了')
		break
	elif a > r:
		print('比答案大')
	elif a < r:
		print('比答案小')
