from datetime import datetime
date=input('Enter your date of birth (dd/mm/yyyy) : ')
date1=datetime.strptime(date,"%d/%m/%Y")
print(date1.strftime('%d-%B-%Y'))

"""
Input-07/01/2001
Output-07-January-2001
"""
