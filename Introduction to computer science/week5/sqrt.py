def sqrt(a):
    x = a/2
    y = 0
    while True:
        print(x)
        y = (x + a/x)/2
        if x == y:
            break
        x = y

def main():
    number = input('number: ')
    sqrt(int(number))

while True:
    main()
