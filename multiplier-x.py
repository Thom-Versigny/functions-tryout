def tafels(getal: int):
	getal = int(input("Van welk getal wilt u de tafel zien?"))
	for x in range(1,11):
		eind = getal*x
		print(str(getal) +" x "+str(x)+" = "+str(eind))

tafels('getal')
input("press enter to exit")
