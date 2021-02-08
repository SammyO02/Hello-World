#Stores python2 syntax hello world
Python2Cmd = "print 'Hello world':"
#Tries to print hello world using python3 syntax
try: print("Hello World")
except: exec(cmd) #If using python2, this will run
