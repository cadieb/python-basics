# note: ints aren't iterable (iterable means 'can be looped through')

list('string')
# so we can send iterable things into the list function and we get a list

first_split = 'hello'.split()
#split breaks up a string on white space
another_split = 'hello there students'.split()
print(another_split)

seperated_by_colons = "red:blue:green".split(':')
print(seperated_by_colons)

# turn a list into a string
# this is a little weird
flavors = ['chocolate', 'mint', 'strawberry']
#we join lists into strings by using a strings
flavors_string = ', '.join(flavors)
print(flavors_string)
#python is smart enough to not put your 'joiner' after the last item

# we can use this with regular strings
joined_string = "My fav flavors are: " + ', '.join(flavors)
print(joined_string)

# we can also use it with format
complicated = "My fav flavors are: {}".format(", ".join(flavors))
# you can ONLY join string items with join
