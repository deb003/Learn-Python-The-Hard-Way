ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split (' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", 
		"Boy"]

while len (stuff) != 10 :
	next_one = more_stuff.pop ()
	print "Adding: ", next_one
	stuff.append (next_one)
	print "There are %d items now." % len (stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

# Print value at index 1
print stuff[1]

# print value at the last index
print stuff[-1] # whoa! fancy

# print value at last index
print stuff.pop ()

# Join and form a string froma list
print ' '.join (stuff) # what? cool! and I'm writing these comments too :/

# Join and add # in between, I know why 3 and 5 is for.
print '#'.join (stuff[3:5]) # super stellar!
