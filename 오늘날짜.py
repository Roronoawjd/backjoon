import datetime

current =  datetime.datetime.now()
UTC0 = current + datetime.timedelta(hours=9)
# YYYY-MM-DD 형식
print("%04d-%02d-%02d" %(UTC0.year, UTC0.month, UTC0.day))

#print(UTC0.strftime("%Y-%m-%d"))
#print(str(UTC0)[:10])