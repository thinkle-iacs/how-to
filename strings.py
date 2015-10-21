## Strings are sequences in python, which means many of the same
## things that work with lists work with strings.


foo = 'This is a string'
# variable[INTEGER] gets the INTEGERth letter of the string
foo[3] #-> 's' (gets the 3th item of the list)
# variable[INTEGER:INTEGER] gets a *slice* of the string
foo[5:7] # -> 'is'
foo[5:] # -> 'is a string'
foo[:5] # -> 'This '

## There are also some handy string methods that do common
## operations on a string and give you back a new, modified
## string.

# string.replace replaces one letter with another

'Tom'.replace('T','M') #-> 'Mom'
'One sentence has many letter "e"s'.replace('e','!') #-> 'On! s!nt!nc! has many l!tt!r "!"s'

# There are convenience methods for handling upper and lower case
'Tom'.lower() # -> 'tom'
'Tom'.upper() # -> 'TOM'
'tom'.capitalize() # -> 'Tom'

# Strings also support the 'in' operator

letter = 'i'
sentence = 'This is a string'

if letter in sentence:
    print 'There is a',letter,'in',sentence
else:
    print 'There is no',letter,'in',sentence

# You can combine the power of upper and lower
# to do case insensitive search...

text = 'This is some text I might want to search.'
word = 'SOME'

word in text # returns False...
word.lower() in text.lower() # returns True

# Finally, there is the *find* method which tells you where
# in a string a substring is...

sentence = 'Where is the letter p?'
search = 'p'
sentence.find(search) # -> 20
sentence[20] # -> 'p'

# A few other conveniences...
# Some math works with strings

'foo' + 'bar' #-> 'foobar'
'foo' * 10 #-> 'foofoofoofoofoofoofoofoofoofoo'

# You can also do alphabetical comparisons
'Z' > 'A' # True

# But careful about case...
'Z' > 'a' # False # ACK!!!!

# Usually what you want is to use upper() or lower() before
# comparing alphabetically...
'Z'.upper() > 'a'.upper() # -> True


