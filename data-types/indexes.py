# INDEX
# Strings and lists have indexes. First item starts at 0. We can also index things from the end, by using negative numbers. The last item is -1 (not 0!).

alpha = 'abcde'
indexof = alpha.index('a')
# The index method of the stirng class returns the index of the first instance of whatever we are looking for. We can't really rely on it if the string has multiple instances of what we are looking for in the stringself.
alpha_list = list(alpha)
indexoflist = alpha_list.index('b')

print(alpha[0])

# DELETION
trash = 99;
del trash
del alpha_list[2]
# del cannot delete more than one item and we cannot delete things from strings
