def countup(number):
    number = int(number) #to not incur in sintaxt problems, must convert the number to integer
    if number < 0:
        print(number)
        countup(number+1)
    elif number == 0:
        print('Blastoff'); #this is the core of the program
    elif number > 0:
        countdown(number)
def countdown(number):
    if number > 0:
        print(number)
        countdown(number-1)
    elif number == 0:
        print('Blastoff')

def invalidnumb(): # at the first interation, I block positive numbers, so, this function is now useless.
    number = input("Enter a number")
    countup(number)

invalidnumb() #here starts the program
