from datetime import datetime,date
d1=date.today()
d2=date(year=2021,month=1,day=7)
diff_between_dates=d2-d1
print(f'The difference between to dates is :  {diff_between_dates}\n')
t1=datetime.now()
t2=datetime(year=2020,month=8,day=28,hour=4,minute=3,second=48)
print(f'The difference between time is : {t2-t1}\n')

"""
Output-
The difference between to dates is :  132 days, 0:00:00

The difference between time is : -1 day, 7:57:56.380327
"""
