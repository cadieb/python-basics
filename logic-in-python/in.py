# in returns whether or not a value is inside of a container. We can use this to see if, for example, a smaller string is in a bigger string or if a certain item is in a list. in is one of the most useful features in Python, says Kenneth.

print("cheese" in "cheeseshop")

days_open = ['Monday', 'Tuesday']
today = 'Wednesday'
if today in days_open:
    print("Come in!")
else:
    print("We are closed.")

if today not in days_open:
    print("Seriously, we are closed.")
