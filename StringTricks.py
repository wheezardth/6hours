course = 'Python for Beginners'
# len() gives string length (and other things!)
print(len(course)) # len() is a FUNCTION
course.upper() # .something() is a METHOD because it belong to a class
print(course) # the original variabe is not affected
capString = course.upper()
print(capString) # the new one is tho

print(course.find("n")) # returns the index of the 1st instance of the search term
print(course.find("Beginners"))
print(course.find("*")) # returns -1 because term cant be found

print(course.replace("Beginners","Genuine Retards")) # replace does ..replace

# "Python" in course # this is an actual expression in Python that returns BOOL

content = "Python" in course # bool type is assigned automatically!
print(type(content))
print(content)