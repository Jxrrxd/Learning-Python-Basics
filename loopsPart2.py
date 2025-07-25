#Loop Control Statements

#using for loops
fruits = ["apple", "banana", "cherry", "dates"]

for fruit in fruits:
    if fruit == "cherry":
        break               #Exits the loop if cherry is found
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        continue            #Skips cherry and moves through the iteration
    print(fruit)
    
print()

for fruit in fruits:
    if fruit == "cherry":
        pass                #Placeholder, no action is needed for cherry
    print(fruit)

#using while loops
count = 0

while count < 5:
    print(count)
    count +=1           #Increments the count by 1
    if count == 3:
        break           #Exits the loop when the count is reached - 3