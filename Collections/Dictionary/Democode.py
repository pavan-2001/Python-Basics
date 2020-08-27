states={'State_1':'Hydrabad','State_2':'Telangana'}
print('Before ading new key-value pairs : ',states)

states['State_3']='Maharashtra'
states['State_4']='Rajasthan'
print()
print('After adding new key-value pairs : ',states)
print()
print('All key-value pairs ')
for item in states.items():
    print(item)
print()
print('The size of the Dictionary is : ',len(states))
