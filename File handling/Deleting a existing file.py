import os
if os.path.exists("text_file.txt"):
    os.remove("Text_file.txt")
else:
    print("There is no existing file named text_file.txt")
