state=input('In which case do you want to print your name ?')
name=input('Enter your name : ')
if state.lower()=='upper':
    print(name.upper())
elif state.lower()=='lower':
    print(name.lower())
else :
    print(name.capitalize())
