class person:
    def __init__(self,first_name='Default_first_name',second_name='Default_second_name'):
        self.first_name=first_name
        self.second_name=second_name
    
    def hello(self):
        print(f'Hey user this is a member function that says HELLO to the person')
        print(f'Hello !! ',self.first_name,self.second_name)

p1=person('pavan','kumar')
print(f'Lets call the member function of class person :')
p1.hello()

"""

Output:
Lets call the member function of class person :
Hey user this is a member function that says HELLO to the person
Hello !!  pavan kumar

"""
