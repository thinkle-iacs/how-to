# Here is a quick tutorial about lists.

# You can put any set of items in a list in python
ilst = [1,2,3] #integers!
slst = ['foo','bar','baz'] # strings
mlst = [1,True,'foo',3,4.25] # a mixture
nlst = [[1,2,3],['red','yellow','blue'],[4.25,1,23,7,54]] # other lists ("nested lists")!

# The list is one of the most handy generic structures for keeping
# track of data of any kind. You can add to lists with the "append" method.

lst = ['foo','bar']
lst.append('baz')
print lst # => ['foo','bar','baz']

# You can access an item of a list with the index method.

lst[2] # -> 'baz'
lst[1] # -> 'bar'

# You can change out an item of a lst by assigning to an index.
lst[1] = 37.2
print lst # -> ['foo',37.2,'baz']

# You can get a "slice" of a list by using the handy slice syntax below
# lst[a:b] gets the items starting at index A and ending before B
lst = [1,2,3,4,5,6,7,8,9,10]
lst[2:4] # -> [3,4]
# You can leave off A or B to get all items from A forward or all items 
# *before* B
lst[5:] # -> [6,7,8,9,10]
lst[:5] # -> [1,2,3,3,4,5]

# If you wanted to, you could even assign to a slice
lst[2:4] = 6,7,8
lst # -> [1, 2, 6, 7, 8, 5, 6, 7, 8, 9, 10]

# You can use the handy "in" operator to test whether
# a list contains an item at all
if 8 in lst: 
    print "Yes!"

if 72 in lst: 
    print "Yes!" #won't print anything

# You can find the index of an item in the list with the
# index function
lst.index(1) #->0

# You can remove an item by using the remove function.
# This will remove all values with a name
lst.remove(1)
lst # -> [2, 6, 7, 8, 5, 6, 7, 8, 9, 10] 
slst = ['A','B','C','D']
slst.remove('B')
slst # -> ['A','C','D']

# Tricks for using lists
# The easiest way to work with a list is with the 
# for loop

for item in slst:  # item is a new variable; you can call it anything
    print item

for n in lst:  # n is just another variable; you can use any variable you like
    print n

# If you want to destroy a list as you use it, you can use "pop"
# Pop takes the last item from a list (or another item if you give
# it an argument) and does something with it

# This basically moves backwards through the list
while lst:
    print lst.pop()

# And now there is no list...
lst # -> []

# Finally, it's useful to know there are some handy tools
# for working with nested lists.
# 
# Let's suppose I make a nested list of people, ages, and
# favorite colors.

pac_data = [['Tom',36,'Blue'],
            ['Katharine',35,'Blue'],
            ['Grace',7,'Green'],
            ['Clara',6,'Pink'],
            ['Lila',4,'Blue']]

# Now I can iterate through this list by using *multiple variables*
# separated by commas in my for statement.
# Watch

for person, age, color in pac_data:
    print
    print '*'*10
    print person,'is',age,'years old.'
    print 'Favorite color:',color
    print '*'*10

# Did your jaw drop? Isn't that awesome?

# Looping through a nested list will break, however, if you add any
# item to the list that does not fit the given structure -- for example
# if some items in the list have four items and some have three, you will
# get an error.

## Uncomment the three lines below to see an error!
# pac_data.append(['Mary',25]) # This would break the loop above
# pac_data.append(['Bob',27,'blue','yellow'] # So would this!
# for person,age,color in pac_data: print person,age,color # This will throw an error


# Sometimes it's very handy to go through lists and numbers at the same time.
# For that purpose, python provides a convenience function enumerate, which 
# works like this:

lst = ['Red','Yellow','Blue','Purple']
enumerate(lst) # -> [(0,'Red'),(1,'Yellow'),(2,'Blue'),(3,'Purple')]

# You can use it with a for-loop like this:
for n,color in enumerate(lst):
    print 'Color #',n,'is',color

# Lists are also sortable. By default, python does what you probably expect when I say
# sort.

lst = [9,4,7,2,10,1]
lst.sort()
lst # -> [1, 2, 4, 7, 9, 10]
lst = ['Mary','Meredith','Fiona','Zeus','Bacchus']
lst.sort()
lst # -> ['Bacchus', 'Fiona', 'Mary', 'Meredith', 'Zeus']

# If you want a reverse sort, you can use the reverse() method
# after sorting...
lst.sort()
lst.reverse()
lst # -> ['Zeus', 'Meredith', 'Mary', 'Fiona', 'Bacchus']

# Or, you can hand sort the reverse argument...
lst.sort(reverse=True)
lst # -> ['Zeus', 'Meredith', 'Mary', 'Fiona', 'Bacchus']

# If you have a nested lst and you want to sort by an item inside it,
# You can hand sort a "key" function.

scores = [['Tom',4],
          ['Mary',7],['Bob',3],['Zeus',3000],['Ruby',150]]

scores.sort() # By default, nested lists are sorted by the first item

# But what if I want to sort the list by the score?
# You can hand sort a function!
# 
# You have two options. 
# If you hand it a key function, your function must return the key to
# sort by.
#
# 
scores # -> [['Bob', 3], ['Mary', 7], ['Ruby', 150], ['Tom', 4], ['Zeus', 3000]]

def key_sorter (person_and_score): 
    '''Return score to sort on.'''
    return person_and_score[1] # return the 1th item

scores.sort(key=key_sorter)
scores # -> [['Bob', 3], ['Tom', 4], ['Mary', 7], ['Ruby', 150], ['Zeus', 3000]]
scores.sort(key=key_sorter,reverse=True) # high-to-low
scores # -> [['Zeus', 3000], ['Ruby', 150], ['Mary', 7], ['Tom', 4], ['Bob', 3]]
    

# There are some clever uses of the key function. For example, if I
# wanted to sort a list of names based on their length, I could do so
# with the len function. Watch!

lst = ['Ira','Chyrsanthemum','Mirabel','Zadie','Bo','Jonathan','Lily']
lst.sort(key=len)
lst #-> ['Bo', 'Ira', 'Lily', 'Zadie', 'Mirabel', 'Jonathan', 'Chyrsanthemum']


# A few more tricks -- if you just want to iterate through numbers
# in order, you can use the amazing range function built into python

# By default, range goes from 0 to the number you said
range(10) # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# since it's zero-indexed, it's confusing -- here's how you
# do what you might have thought of when I said range(10)
range(1,11) # -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# you can also count by twos or threes or any other number...
range(2,11,2) # -> [2, 4, 6, 8, 10]
range(0,51,3) # -> [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]
range(0,1000,100) # -> [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
