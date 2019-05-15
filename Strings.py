# triple quotes allow to use single & double quotes in strings
# No Need For Escape characters! (Yet...)
course = '''***Monty-Python's Course for "smart" people***'''
print(course)

wisdom = '''
 Triple quotes also allow to write
 string with line breaks in them.
 
 This is super convenient.
 
 Serial.print(vomit)
 
 '''
print(wisdom)

# keep in mind that the quotes themselves cant be on a new line
# realWisdom =
# '''
# This doesn't work.
# ''

# Strings behave a bit like arrays of characters (which they are) and
# can be addressed by an index, which will return the character.
# The discrete character data type is not a thing in Python
print(course[0])
print(course[3])
print(type(course))    # this returns string class
print(type(course[0])) # this returns string class too
print(course[-4])      # this allows you to warp around and index back to front


# Using column allows you to extract a substring between the index numbers!
# It will INCLUDE the start index
# But will EXCLUDE the end index
# If it didn't there'd be a dash after Monty
print(course[3:8])
# There are defaults too
print(course[3:]) # all the way to the end
print(course[:8]) # all the way from the start
print(course[:])  # all the stuff