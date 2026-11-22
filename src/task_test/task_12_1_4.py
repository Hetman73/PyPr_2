import datetime

date_obj = datetime.datetime.now()
date_str = date_obj.strftime("%d/%m/%Y %H:%M:%S")
print(date_obj.year)
print(date_obj.month)
print(date_obj.day)
print(date_obj.hour)
print(date_obj.minute)
print(date_obj.second)
print(date_obj.microsecond)
print(date_str)