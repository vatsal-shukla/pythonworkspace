from datetime import date, time, datetime

def howold():
	todaydate=date.today()

	mydob = date(1991,9,1)
	momdob = date(1967,7,15)
	daddob = date(1962,2,5)

	meold=todaydate-mydob
	momold = todaydate-momdob
	dadold=todaydate-daddob

	# print(type(meold))
	print("I am " +str(int(meold.days/365))+ " years old")
	print("Mumma is " +str(int(momold.days/365))+ " years old")
	print("Dad is " +str(int(dadold.days/365))+ " years old")

howold()