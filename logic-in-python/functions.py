# functions let us do work over and over again whenever we need it
# to create a function we use the keyword def which stands for define then the name of the function

def hows_the_parrot():
    print("He's pining for the fjords!")

# call the function:
hows_the_parrot()

# functions can take arguments then use them inside of the function
def lumberjack(name, pronoun):
    print("{}'s a lumberjack and {}'s ok!".format(name, pronoun))
    print("{} sleeps all night and {} works all day!".format(name, name))

lumberjack("Cadie", "she")

def average(num1, num2):
    return (num1+num2) / 2

avg = average(2, 8)
print(avg)
