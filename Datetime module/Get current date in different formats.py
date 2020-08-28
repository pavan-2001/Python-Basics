from datetime import date 
today=date.today()

print('Format (dd/mm/yy) : ',today.strftime('%d/%m/%y'))

print('Format (mm/dd/yyyy) : ',today.strftime('%m/%d/%Y'))

print('Format (Textual month/dd/yyyy) : ',today.strftime('%B-%d-%Y'))

print('Format (Month abrev.-dd-yyyy) : ',today.strftime('%b-%d-%Y'))
"""
Output

Format (dd/mm/yy) :  28/08/20
Format (mm/dd/yyyy) :  08/28/2020
Format (Textual month/dd/yyyy) :  August-28-2020
Format (Month abrev.-dd-yyyy) :  Aug-28-2020

"""
