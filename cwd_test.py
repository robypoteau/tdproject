import os, os.path #, sys

#print os.getcwd()

#print os.path.abspath(1)

#print os.path.dirname(os.path.realpath(__file__))

tom = os.path.dirname(os.path.realpath(__file__))

filename = "jim"

print os.path.join(tom, filename)

#print sys.path