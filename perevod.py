#Функция для целочисленного деления, т.к в отрицательных числах питоновская работает некорректно

def cel(d1, d2):
	if d2 > 0:
		return d1 // d2

	elif d1 % d2 == 0:
		t = int(d1/d2)
		return t

	elif d2 < 0 and d1 > 0:
		t = int(d1/d2)
		return t

	elif d2 < 0 and d1 < 0:
		t = int(d1/d2)
		return t + 1

	else:
		print('Error')
		return -1

#Функция для нахождения остатка от деления, т.к в отрицательных числах питоновская работает некорректно

def ost(d1, d2):
	if d2 > 0:
		return d1 % d2

	elif d1 % d2 == 0:
		t = int(d1/d2)
		t = d1 - t * d2
		return t

	elif d2 < 0 and d1 > 0:
		t = int(d1/d2)
		t = d1 - t * d2
		return t

	elif d2 < 0 and d1 < 0:
		t = int(d1/d2)
		t += 1
		return d1 - t * d2

	else:
		print('Error')
		return -1

#Сам перевод

def sys(num, sys):
	res = ''
	while num != 0:
		res = str(ost(num, sys)) + res
		num = cel(num, sys)
	return res

while True:
	a = int(input('0 - для выхода. Число: '))
	if a == 0:
		break
	b = int(input('0 - для выхода. Система счисления: '))
	if b == 0:
		break
	print(sys(a, b))