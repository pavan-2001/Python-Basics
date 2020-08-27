from datetime import datetime,timedelta
birthday=input('enter your date of birth(dd/mm/yyyy): ')
birthday_date=datetime.strptime(birthday,'%d/%m/%Y')
print(str(birthday_date-timedelta(weeks=2)))
