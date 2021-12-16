#Write a function called estimate_pi that uses this formula to compute and return an estimate of
#π. It should use a while loop to compute terms of the summation until the last term is smaller than
#1e-15 (which is Python notation for 10−15). You can check the result by comparing it to math.pi.
import math
from decimal import Decimal, getcontext

def estimate_pi():
    out_of_somatory = Decimal(2*math.sqrt(2)/9801)
    k = 0
    epsilon = 0.00000000000000000000000000000001
    pi = Decimal(0)
    pi = Decimal(0)
    decimal_pi = Decimal(1/math.pi)
    getcontext().prec=1000000 #precision of decimal points
    while True:
        
        temp = (math.factorial(4*k) * (1103+26390*k))
        temp = temp/((math.factorial(k)**4)*(396**(4*k)))
        temp = Decimal(temp)
        pi = pi + temp
        pi_print = pi*out_of_somatory
        print(1/pi_print)
        k = k + 1
        
        if abs(pi*out_of_somatory - decimal_pi) < epsilon:
            break

def main():
    estimate_pi()

main()
