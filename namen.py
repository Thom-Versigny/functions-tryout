def namenvragen(naam):
	naam = input("Type jouw naam of stop om te stoppen: ").lower()
	if naam == 'stop':
		return naam
	jaar = input("Type jouw leeftijd: ")
	print('hallo '+str(naam)+' en jouw leeftijd is '+str(jaar))

while True:
	if namenvragen('naam') == 'stop':
		input('press enter to exit')
		break
	namenvragen('naam')
