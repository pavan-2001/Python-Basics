price=input()
if float(price)>=1.0:
     tax=.7
else:
     tax=0
print(tax*float(price)+float(price))  
