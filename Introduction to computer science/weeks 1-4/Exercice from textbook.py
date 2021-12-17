#For this study I will write 3 functions.
#is_divisible returns true if the first argument is divisible by the second.
#is_between will receive 3 arguments and return if the second argument is between the others
#is_power will return if the first argument can be write as exponential of the second.


def is_divisible(x, y):
    return x % y == 0

def is_between(x, y, z):
    return x <= y <= z

def is_power(x, y):
    x = int(x)
    y = int(y)
    if y == 1:
        #Potential is True for every exponential when it is 1
        return True
    elif x == y:
        #Verify if are equal before beggin recursions
        return False
    elif is_divisible(x, y) == True :
        x = x/y
        if x == y:
            #Verify if are equal after some iteration
            return True
        return is_power(x, y)
    else:
        return False

def main():
    print("is_power(10, 2) returns: ", is_power(10, 2))
    print("is_power(27, 3) returns: ", is_power(27, 3))
    print("is_power(1, 1) returns: ", is_power(1, 1))
    print("is_power(10, 1) returns: ", is_power(10, 1))
    print("is_power(3, 3) returns: ", is_power(3, 3))
    #Expect False, True, True, True, False

main()
