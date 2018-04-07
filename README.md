# python-basics
Learning Python with the 'Python Basics' Treehouse Course


## Notes
_"Everything's an object"_

**Some Rules for Writing Python**
- blocks are indented 4 spaces
- blocks start with a colon
- variables and functions should be lowercase and use underscores
- no use for semicolons at the end of lines
- Python variables don't have sitchels, or symbols at the beginning of them

```Python
def answer_the_phone():
    greeting = "Wazzzzzup"
    print(greeting)
```

### Data Types
#### Variables
Create a variable: `variable_name = "variable name"`
Delete a variable: `del variable_name`

* Deleting variables in Python is not that common. Python keeps a count of how many times that variable is used or mentioned somewhere and when the reference count becomes 0, Python just throws the variable away.


#### Numbers
Adding, subtracting and multiplying always gives us back ints, unless we're working with floats. But division gives us a float.

Also, dividing by 0 always creates an error.

`0.1 + 0.1 + 0.1 - 0.3`

That should give back 0, instead it gives back `5.551115123125783e-17`

`round()` gives us the integer that's closest to the float that we have.

`int()` chops off the float portion and just turns in into ints.. It also lets us turn strings into int, that's assuming that the string is just an int (ex: `int('56')`)

`float` gives us a float for the number.

```Python
round(5.551115123125783e-17)
>>> 0
int(5.551115123125783e-17)
>>> 5
```
