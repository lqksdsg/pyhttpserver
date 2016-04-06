import os
def open_file(file_name):
    with open(file_name,'r') as f:
        if f.read() == 0:
            print "error"
def hello():
    print "hello"
    print "How stupid you are!"