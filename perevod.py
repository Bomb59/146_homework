def sys(num, sys1, sys2):
	num = int(str(num), sys1)
	a = ''.join([chr(__) for __ in range(48, 58)] + [chr(_) for _ in range(65, 91)] + [chr(___) for ___ in range(97, 123)])
	if num < sys2:
	    return a[num]
	else:
	    return sys(num // sys2, sys1, sys2) + a[num % sys2]

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