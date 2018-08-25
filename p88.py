"""
Implement division of two positive integers without using the division, 
multiplication, or modulus operators. Return the quotient as an integer, 
ignoring the remainder.
"""


def find_division(dividend, divisor):
    """
    Finds the quotient of the two numbers sans decimal without using a divison,
    multipy or modulus operator. 
    
    From the problem statement we will assume the dividend and divisor are both
    positive.

    Basically we will check if the dividen is greater than divisor. If not
    quotient is zero.

    Then we will write for loop in increments of the divisor and till the
    sum is greater than those increments. We will keep a count of number of
    increments. The count-1 when the number exceeds the dividend is our
    quotient

    """
    if divisor == 0:
        print ("Human you can't get to infinity")
        return None
    if dividend < divisor:
        return 0
    quotient = 1
    divisor_incremented = divisor
    while divisor_incremented < dividend:
        quotient += 1
        divisor_incremented += divisor
        # print (divisor_incremented)
    if divisor_incremented != dividend:
        # not a multiple quotient will be one higher 
        quotient -= 1

    # print (quotient)
    return quotient


if __name__ == "__main__":
    dividend = 20
    divisor = 4
    quotient = find_division(dividend, divisor)
    print(quotient)

        
