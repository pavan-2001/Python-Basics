states=['Haryana','Telangana','Jammu and Kashmir']
print('Before adding new elements : ',states)

print()
#It inserts the element before the given index
states.insert(1,'Madhya pradesh')
#Adds the element at the back/end of the list
states.append('Rajasthan')

print('After adding new elements : ',states)
print()
print(f'The size of the list is : {len(states)}')
