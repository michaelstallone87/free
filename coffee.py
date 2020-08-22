from datetime import datetime


today = datetime.today().strftime('%c')
print(f'[today is {today}]')

while True:
	coffee = input('coffee situation:\n')
	if coffee == 'empty':
		print('fill')
	elif coffee == 'full':
		print('drink')
		break
	else:
		print("it's ok")
	pass
print('so proceed...')