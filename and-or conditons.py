gpa=float(input('Enter your gpa : '))
lowest_grade=float(input('Enter your lowest grade : '))
if gpa>=8.5 and lowest_grade>=7.0:
    honour_roll=True
else:
    honour_roll=False
if honour_roll:
    print('Well done!!!')
else:
    print('Sorry!!')
