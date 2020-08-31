square=lambda x:x*x
print(f'Square of 5 is {square(5)}')

raise_to_power=lambda x,y: x**y
print(f'5 raise to power 3 is {raise_to_power(5,3)}')

table=[9,7,8,5,4,6,3,1,2]
table=list(map(lambda num:num**2,table))
table.sort()
print(table)
"""
Output-
Square of 5 is 25
5 raise to power 3 is 125
[1, 4, 9, 16, 25, 36, 49, 64, 81]
"""
