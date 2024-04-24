year=int(input("year: "))
month=int(input("month: "))
if month == 1 or month == 2:
    month += 12
    year -=1
    
day= int(input("day: "))
result = (day+13*(month+1) // 5+year+year // 4-year//100+year//400)%7
weekend = {0: "saturday",1: "sunday",2:"monday",3:"tuesday",4:"wednesday",5:"thursday",6:"friday"}
print("the day is " +weekend[int(result)] + ".")