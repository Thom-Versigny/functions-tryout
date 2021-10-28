def addition(number1, number2):
		eind = number1+number2
		return str(number1) +" + "+str(number2)+" = "+str(eind)
def subtraction(number1, number2):
		eind = number1-number2
		return str(number1) +" - "+str(number2)+" = "+str(eind)
def multiplication(number1, number2):
		eind = number1*number2
		return str(number1) +" x "+str(number2)+" = "+str(eind)
def adivision(number1, number2):
		eind = number1/number2
		return str(number1) +" / "+str(number2)+" = "+str(eind)
def increment(number):
	eind = number+1
	return str(number) +" + 1 = "+str(eind)
def decrement(number):
	eind = number-1
	return str(number) +" - 1 = "+str(eind)

print(addition(3,30))
print(addition(67,9))
print(addition(76,7))

print(subtraction(3,30))
print(subtraction(67,9))
print(subtraction(76,7))

print(multiplication(3,30))
print(multiplication(67,9))
print(multiplication(76,7))

print(adivision(3,30))
print(adivision(67,9))
print(adivision(76,7))

print(increment(8))
print(increment(9328))
print(increment(3998))

print(decrement(845))
print(decrement(93498))
print(decrement(842))