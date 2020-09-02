class person_name:
    def __init__(self,first_name='default',second_name='default'):
        self.first_name=first_name         #first_name is public
        self.__second_name=second_name   #second_name is private member
    def get_second_name(self):          #function to return second_name
        return self.__second_name
    def set_first_name(self,first_name):   #function to set first_name
        self.first_name=first_name
    def set_second_name(self,second_name): #function to set second_name
        self.__second_name=second_name

class person_details(person_name):
    def __init__(self,first_name='default',second_name='default',age=0,location='default'):
        super().__init__(first_name,second_name)          #parent class constructor or initializer
        self.__age=age           #age is private member
        self.location=location
    def get_age(self):            #function to return private member
        return self.__age
    def set_location(self,location):      #function to location
        self.location=location
    def set_age(self,age):       #function to set age
        self.__age=age
    def ALL(self):            #function that print all the attributes of the object
        print(f'First name : {self.first_name}')
        print(f'Second name : {self.get_second_name()}')
        print(f'Age : {self.get_age()}')
        print(f'Location : {self.location}')

p1=person_details('pavan','kumar',19,'bathinda')
p1.ALL()

"""
Output-
First name : pavan
Second name : kumar
Age : 19
Location : bathinda
"""
