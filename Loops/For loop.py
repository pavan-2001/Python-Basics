def fact_num(a):
    fact=1
    for count in range(1,a+1):
        fact=fact*count
    return fact
num=int(input('Enter the nummber : '))
print(f'The Factorial of {num} is {fact_num(num)}')

"""

Output-
Enter the nummber : 5
The Factorial of 5 is 120

"""
