with open('test_file.txt','w') as file:
    file.write('You have opened the file using with which automatically closes the file for you !\n')
    file.write("Now you don't have to worry about closing the file")
