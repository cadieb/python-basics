# Python has two loops: the for loop and the while loop.
# For loops let us do an action a certain # of times
# While loops run an unknown # of times, until the condition we gives them becomes falsey

my_list = ['hello', 'how', 'are', 'you']

for word in my_list:
    print(word)

# we can loop through anything that is iterable -- anything that has more than one item in it (lists and strings)

for letter in 'abc':
    print(letter.upper())

for num in [1,2,3,4]:
    if num % 2 == 0:
        print(num)

start = 10
while start:
    print(start)
    start -= 1
    #yay countdown

#sometimes you will have to stop a loop early so that it's not infinite
names = ['Cadie', 'Amy', 'Andrew', 'quit', 'lacy']
for name in names:
    if name == 'quit':
        break
        #breaking lets us stop the loop
    print(name)

for name in names:
    if name == 'quit':
        continue
        # continue skips the current step (like playing hopscotch)
    print(name)
