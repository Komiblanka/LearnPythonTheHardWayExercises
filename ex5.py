my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

# Conversion to international metrics
height = 74 * 2.54 # cms
weight = 180 * 0.453592 # kg

print "Let's talk about %s." % my_name
print "He's %d inches tall. In cms: %f" % (my_height, height)
print "He's %d pounds heavy. In kg: %f" % (my_weight, weight)
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % (my_teeth)

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %r." % (my_age, height, weight, my_age + height + weight)
