from sys import argv
from os.path import exists

script, filetowrite = argv

indata = open(filetowrite)

data = indata.read()

print "The file contains: \n" + data

print """
Type something to write into the file:
"""
newtext = raw_input()
indata.close()

print "Writing %r" % newtext
out_file = open(filetowrite, 'aw')
out_file.write(newtext+"\n")

print "Alright, all done."

#in_file.close()
out_file.close()
