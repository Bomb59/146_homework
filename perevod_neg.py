#Функция для целочисленного деления, т.к в отрицательных числах питоновская работает некорректно

def cel(d1, d2):
	if isinstance(d1, str):
		d1 = int(d1)
	if isinstance(d2, str):
		d2 = int(d2)
	if d2 > 0:
		return d1 // d2

	elif d1 % d2 == 0:
		t = int(d1/d2)
		return t

	elif d2 < 0 and d1 > 0:
		t = int(d1/d2)
		return t

	elif d2 < 0 and d1 < 0:
		t = int(str(d1/d2))
		return t + 1

	else:
		print('Error')
		return -1

#Функция для нахождения остатка от деления, т.к в отрицательных числах питоновская работает некорректно

def ost(d1, d2):
	if isinstance(d1, str):
		d1 = int(d1)
	if isinstance(d2, str):
		d2 = int(d2)
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

def syst1(num, sys):
	res = ''
	num = int(num)
	while num != 0:
		res = str(num % sys) + res
		num = num // sys
	return res

def syst2(num, sys1, sys2):
#	a = "0123456789ABCDEFGHIJK" # 
	num = int(str(num), sys1)

	if num // sys2 != 0:
		return syst2(num // 10, sys1, sys2) + num % 10

	else:
		return num

def sys(num, sys1, sys2):
	a = syst2(num, sys1, sys2)
	return syst1(a, sys2)




while True:
	a = int(input('0 - для выхода. Число: '))
	if a == 0:
		break
	b = int(input('0 - для выхода. Система счисления1: '))
	if b == 0:
		break
	c = int(input('0 - для выхода. Система счисления2: '))
	if c == 0:
		break
	print(sys(a, b, c))