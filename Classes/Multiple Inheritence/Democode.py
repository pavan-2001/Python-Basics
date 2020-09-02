class logger:    # class 1
    def __init__(self,title='default title'):
        self.title=title
    def log(self):
        print(f'Log message from {self.title}')
class connection:        # class 2
    def __init__(self,server='default server'):
        self.server=server
    def connect(self):
        print(f'Connecting to server {self.server}')
class sql_database(logger,connection):   # class 3
    def __init__(self,title,server):
        logger.__init__(self,title)
        connection.__init__(self,server)
def former(item):
    if isinstance(item,logger):
        item.log()
    if isinstance(item,connection):
        item.connect()
print('logger object : item1')
item1=logger('logger')
former(item1)
print()     # prints a blank line
print('connection object : item2')
item2=connection('server1')
former(item2)
print()
print('sql_database object : item3')
item3=sql_database('title','server2')
former(item3)

"""
Output-
logger object : item1
Log message from logger

connection object : item2
Connecting to server server1

sql_database object : item3
Log message from title
Connecting to server server2
"""
