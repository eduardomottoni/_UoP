#Debugging study
#For this study I will try to develop a function, and I will register the bugs that apear
#And classify each bug in Precondition, Postcondition, or Return

#The function must return if a value is divisible by 2, and return if is even

def verifyEven(number):
    if isinstance(number, int) == True and number%2 == 0:
        return ' is even'
    else:
        return ' is not even'

def main():
    number = input('Enter the number to verify: ')
    number = int(number)
    result = verifyEven(number)
    print('The number ' + str(number) + result)
while(True):    
    main()
#The first error was TypeError: isinstance expected 2 arguments, got 1
#Because the function isinstance needs 2 arguments
#This is classified as Precondition error


#The seccond error found was not a crash.
#The verification if the number was integer was failling, because it was
#Not explicit, so I added the funciton int() to convert the variable number in the function main as a Integer
#This error was classified as Postcondition

#The third error I have found is a Return Error, since int variables can not be concatenated with strings
#This error was classified as Return Error,
#To solve it, I will just reconvert the number to string before concatenate it


#You can try the code above.
