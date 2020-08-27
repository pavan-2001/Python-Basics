country=input("What's your country : ")
price=input('The amount you paid sir : ')
province=input('what province do you live in : ')
if country.lower()=='canada':
    if province in('alberto','nuventus'):
        tax=0.05
    elif province =='ontario':
        tax=0.13
    else:
        tax=0.5
else:
    tax=0.00
print('Your total amount to be paid is (tax included) : '+str(tax*float(price)+float(price)) )
