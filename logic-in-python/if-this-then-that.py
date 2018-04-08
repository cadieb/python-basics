age = 24 * 365

if age > 10000:
    print("WOW! Over 10,000 days old!")
else:
    print("You're {} days old!".format(age))

age = 22000

if age > 20000:
    print("Time to retire!")
elif age > 10000:
    print("Lots of time left!")
else:
    print("Time to get started!")

# Test if a condition is false instead of if it's true

if not age > 25000:
    print("Whippersnapper")
