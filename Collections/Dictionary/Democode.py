#-------------------------------------------Dictionary--------------------------------------------
""" 
Dictionaries holds key/value pairs.
We represent Dictionaries by Curly Braces-{}
Key's=={'State_1','State_2','State_3'}
Key-value pairs-
State_1=Hydrabad
State_2=Telangana
State_3=Maharashtra
State_4=Rajasthan
-> we cannot use append or insert to add an item in Dictionary .
-> If we want to add a new key-value pair this is the way you can do that 
  Dictionary_name['Key']='value'
->it will add a new element if there is no key in the existing Dictionary with the same key.
else it will change the value of existing key to the new value .
-> You can access elements by their corresponding key.
------------------Note-------------------
append- Is used to add elements at the end of Collections.
insert-Is used to add elements at an apropriate place .
len(Collection name)- Returns an integer which represents the size of a particular collection.

"""
#--------------------------------------------Demo Code on Dicionary----------------------------------------------
states={'State_1':'Hydrabad','State_2':'Telangana'}
states['State_3']='Maharashtra'
states['State_4']='Rajasthan'
print(states)
print(states['State_1'])
print(states['State_2'])
print(states['State_3'])
print(states['State_4'])
print(len(states))
