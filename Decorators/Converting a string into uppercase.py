def split_string(function):
    def wrapper():
        func=function()
        splitted_string=func.split()
        return splitted_string
    return wrapper
def upper_decorator_function(function):
    def wrapper():
        func=function()
        make_upper=func.upper()
        return make_upper
    return wrapper

@upper_decorator_function
def say_hello():
    return 'hello there'

print(f'Output_1 : {say_hello()}')

@split_string
def say_hello():
    return 'hello there'

print(f'Output_2 : {say_hello()}')

@split_string
@upper_decorator_function
def say_hello():
    return 'hello there'
print(f'Output_3 : {say_hello()}')


"""
Output-
Output_1 : HELLO THERE
Output_2 : ['hello', 'there']
Output_3 : ['HELLO', 'THERE']
"""
