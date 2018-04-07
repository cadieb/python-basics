single = 'Hey'
double = "Yep"
with_apostrophe = "He's right"
escape_quotes = 'He\'s right'
triple_quotes_double = """He's right"""
triple_quotes_single = '''He's right'''

tip = "Strings with triple quotes can hold on to tabs and new lines if you need those in your strings!"
long_string = """Here's a new line!
...
... It's right there!"""

print(long_string)

# Just like numbers you can add strings together
print('Hello ' + 'there')

name = "Cadie"
name += " B"

print('a' + str(5))

# SUPEPR COOL TIP: You can multiply strings!!
print('=' * 20)

status_message = "Hey, we have {} {} reading these notes right now..."
# The curly braces mark where we want to put a value. Strings give us a method named format that lets us pass in the values we want to fill the holes.
print(status_message.format(7, 'penguins'))
