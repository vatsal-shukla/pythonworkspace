
from datetime import date, time, datetime
from datetime import timedelta
# from datetime import time
# from datetime import datetime

def main():
	# toda1=date.today()
	# myborn=date(1991,9,1)
	# print (toda1-myborn)
	
	# today = datetime.now()
	# print(today.strftime("%Y"))
	
	# print(datetime.now())
	# print(date.today())
	# datetimeobj=datetime.now()
	# print(datetimeobj.strftime("%Y"))
	
	print(timedelta(days=365, hours=5, minutes=1))
	now = datetime.now()
	print (now)
	
	print ("one year from now : " +str(now + timedelta(days=2, weeks=3)))
	
if __name__ == "__main__":
	main()

