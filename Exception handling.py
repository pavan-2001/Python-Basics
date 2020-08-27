x=5
y=0
try:
    print(x/y)
except ZeroDivisionError as e:
    print('we cannot divide a number by zero')
else:
    print('something went wrong')
finally:
    print('You can run your program once again!!')
