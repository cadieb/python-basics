# Lists are a lot like arrays in other languages. Python arrays can hold any amount of items and any type of item. EVERYTHING can go in a list! You can change the contents of a list however often you need to and it'll still be the same list.

my_list = [1, 2, 3]

# You can make lists, add lists to lists and multiply lists.

my_list = my_list + [4, 5]
my_list += [6, 7]

print(my_list)

# You might not want to use math to change a list. There are two methods that can change listsself.

# append - only takes one argument. If you append a list in a list, then you get a list in your list.
my_list.append(8)

# extend - adds multiple items to a list
my_list.extend([9,10,11])

list_in_list = [1, 2, 3, [4, 5, 6]]

# remove removes a particular value from a list if it's there, if it's not you get a value error
list_in_list.remove([4, 5, 6])

# example of a list with strings & ints
colors = ['red', 22, 'blue', 78, 'pink']
