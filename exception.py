from datetime import date
from dateutil import relativedelta

cal={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}

try:
    d=int(input("Enter your birth day:"))
    m=int(input("Enter your birth month:"))
    y=int(input("Enter your birth year:"))
    tdate=date(y,m,d)
    today=date.today()
    diff=relativedelta.relativedelta(today,tdate)
    print(diff.years)
    x=diff.years
    if x>20:
        print("Eligible!")
    else:
        raise Exception(x)
except Exception:
    print("Not eligible")
            