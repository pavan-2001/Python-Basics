# Writing a file

f=open("text_file.txt","w")
f.write("If you open a file in append mode and write something to it . It adds that content to the end of that file.")
f.close()

f=open("text_file.txt","r")
print(f.read())

"""
Output-
If you open a file in append mode and write something to it . It adds that content to the end of that file.
"""
