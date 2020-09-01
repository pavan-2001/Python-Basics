class person:
    def __init__(self,first_name='Default_first_name',second_name='Default_second_name'):
        self.first_name=first_name
        self.second_name=second_name

print("If we don't pass any argument it default initializes the data-members : ")
p1=person()
print(f'First_name : {p1.first_name} \nSecond_name : {p1.second_name}')
print()
print('If we pass arguments : ')
p2=person('pavan','kumar')
print(f'First_name : {p2.first_name} \nSecond_name : {p2.second_name}')


"""
Output:
If we don't pass any argument it default initializes the data-members :
First_name : Default_first_name
Second_name : Default_second_name

If we pass arguments :
First_name : pavan
Second_name : kumar
"""
