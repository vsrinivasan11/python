n = 20

def fibonacci(myNumber = 4):
    if myNumber == 2 or myNumber == 1:
        return 1
    else:
        return fibonacci(myNumber - 1) + fibonacci(myNumber - 2)


#for i in range(n):
    #print fibonacci(i+1)

#TODO fix definition
myList = [fibonacci(i+1) for i in range(n)]

print fibonacci()