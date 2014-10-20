from sys import argv

script, first, second, third = argv

print "The script is called: ", script
print "Your first variable is: ", first
print "Your second variable is: ", second
print "your third variable is: ", third

first = raw_input("Giver your first parameter a new value: ")
second = raw_input("Giver your second parameter a new value: ")
third = raw_input("Giver your third parameter a new value: ")

print "\nYour first variable is:", first
print "Your second variable is:", second
print "your third variable is:", third + "\n"

