# Writing a file

f=open("text_file.txt","a")       #append mode
f.write("If you open a file in append mode and write something to it . It adds that content to the end of that file.")
f.close()

f=open("text_file.txt","r")
print(f.read())

"""
Output-
You have opened the file !
You are using python .
This file is for testing purpose .
Ok the file is closing.
If you open a file in append mode and write something to it . It adds that content to the end of that file.
"""
