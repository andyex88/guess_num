import random
r = random.randint(1, 100)
count = 0
while True:
	a = input('請猜數字： ')
	a = int(a)
	count = count + 1
	if a == r:
		print('終於答對了')
		print('你猜了', count, '次')
		break
	elif a > r:
		print('比答案大')
	elif a < r:
		print('比答案小')
	print('你猜了', count, '次')
