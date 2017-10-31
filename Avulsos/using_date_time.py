import datetime


#AN EXCELENTE RESOURSE https://pymotw.com/2/datetime/

#print 2017-10-23 22:23:09.860431
print(datetime.datetime.now())

#GETING A PIECE OF THE DATA
today = datetime.date.today()
print (today)
print ('ctime:', today.ctime())
print ('tuple:', today.timetuple())
print ('ordinal:', today.toordinal())
print ('Year:', today.year)
print ('Mon :', today.month)
print ('Day :', today.day)

""" THE output
2017-10-23
ctime: Mon Oct 23 00:00:00 2017
tuple: time.struct_time(tm_year=2017, tm_mon=10, tm_mday=23, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=296, tm_isdst=-1)
ordinal: 736625
Year: 2017
Mon : 10
Day : 23

"""

#seting a especific date
myBirthday = datetime.datetime(1985,3,8,0,0,0,0)
print(myBirthday)

#calculating days of life
#output: 11917 days, 22:35:18.415810
timeLife = (datetime.datetime.now() - myBirthday)
print("Time Life: "+str(timeLife))

now = datetime.datetime.now()

from dateutil.relativedelta import relativedelta

difference = relativedelta(now, myBirthday)
print("My years: "+str(difference.years))
print("My Months: "+str(difference.months))
print("My days: "+str(difference.days))
print("My hours: "+str(difference.hours))
print("My minutes: "+str(difference.minutes))

"""
out put 

My years: 32
My Months: 7
My days: 15
My hours: 23
My minutes: 32
"""

secondsOfLife = (datetime.datetime.now() - myBirthday).total_seconds()
print("Seconds: "+str(secondsOfLife))





#SITE TO GET STRINGS (ESPECIAL) OF TIME
#http://strftime.org/

#formating caracterys


now = datetime.datetime.now()
print("---"*5)
print(now.strftime("%Y-%m-%d-%H-%M-%S-%f"))
#output: 2017-10-23-22-56-50-490031

print(now.strftime("%B %Y %d"))
#Output: October 2017 23

