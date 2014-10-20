from sys import argv

script, filename = argv

print "Opening the file..."
target = open(filename, 'r+w')

print "The file %r contains:" % filename

text = target.read()

print "%s" % text

print "We are going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If youdo want that, hit RETURN."

raw_input("?")


print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")

TotalLine = line1 + "\n" + line2 + "\n" + line3 + "\n"

print "I'm going to write these to the file."

target.write(TotalLine)

print "And finally, we clse it."
target.close()
