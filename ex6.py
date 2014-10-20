# Constructing the base joke
x = "There are %d types of people." % 10

# Filling in the gaps
binary = "binary"
do_not = "don't"


y = "Those who know %s and those who %s" % (binary, do_not)

# Showing the first part of the joke to the user.
print x

# Showing the punchline to the user.
print y

# Repeting the joke, this time puting a string inside of a string.
print "I said: %r." % x # String is printed as raw data. It prints the single quotes too!

print "I also said: '%s'." % y # string is prinnted a string. Beware that it is between single quotes when printed.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # This constructs a string with the forma inside.

print joke_evaluation % hilarious # This string adds the question + format + variable to show. I have learnt this today!

w = "this is the left side of..."
e = "a string with a right side."

# Concatenating strings as usual.
print w + e
