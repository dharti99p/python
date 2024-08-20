import datetime

a=datetime.datetime.now()

print(a)

# print(datetime.datetime.now())
print(a.year)
print(a.strftime('%A'))# name of the weekday

a = datetime.datetime(2020, 5, 17)
print(a)

a = datetime.datetime(2018, 6, 1)
print(a.strftime("%B"))# month

a = datetime.datetime.now()
print(a.strftime("%a")) # short version weekday

print(a.strftime("%w")) # weekday as a number 0-6 , 0 is sunday 

print(a.strftime("%d")) # day of month 01 - 31

print(a.strftime("%b")) # month name, short version

print(a.strftime("%m")) # month as a number 01 - 12

print(a.strftime("%y")) # year, short verion without century

print(a.strftime("%Y")) # year, full version

print(a.strftime("%H")) # hour 00 - 23

print(a.strftime("%I")) # hour 00 - 12

print(a.strftime("%p")) # am / pm

print(a.strftime("%M")) # minute 00 - 59

print(a.strftime("%S")) # second 00 - 59

print(a.strftime("%f")) # microsecond 000000 - 999999

print(a.strftime("%z")) # UTC offset

print(a.strftime("%Z")) # Time zone

print(a.strftime("%j")) # day nuber of year 001 - 366

print(a.strftime("%U")) # week num of year, sunday as the first day week, 00 - 53

print(a.strftime("%c")) # local version of date and time

print(a.strftime("%C")) # century

print(a.strftime("%x")) # local verion of date

print(a.strftime("%X")) # local version time

print(a.strftime("%%")) # A % character

print(a.strftime("%G")) # ISO 8601 year

print(a.strftime("%u")) # ISO 8601 weekday( 1 - 7)

print(a.strftime("%V")) # ISO 8601 weeknymber (01 - 53)