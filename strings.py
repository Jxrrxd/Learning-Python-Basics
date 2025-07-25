#Strings

message = """Jarred's World
is awesome"""

print(message)

#Advanced Concepts - Strings

display = ' Hello '
print(display[0]) #return first character in the string
print(display[1]) #return second character in the string
print(display[2]) #return third character in the string
print(display[-1]) #return last character in the string

print(len(display)) #return the length of our string

milo = ' Hello, World '
print(milo.strip()) #remove leading and trailing whitespaces
print(milo.lower()) #convert all characters in the string to lowercase
print(milo.split(',')) #split the string into a list based on the position of the comma
print(milo.upper()) #convert all characters in the string to uppercase