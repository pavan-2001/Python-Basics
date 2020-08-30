def fact_num(a):
    fact=1
    while a>0:
        fact*=a
        a-=1
    return fact
num=int(input('Enter the nummber : '))
print(f'The Factorial of {num} is {fact_num(num)}')
"""

Output-
Enter the nummber : 5
The Factorial of 5 is 120

"""
