"""! @file math_library.py
@brief Mathematical functions for the calculator.
@author xhnato00, xlanro00, xmacho12, xslivk03
"""

# Global Constant
# Pi number
PI = 3.14159265358979323846264338327950288419716939937510

# Euler number
E = 2.71828182845904523536028747135266249775724709369995

# Global variable to work as epsilon when approximating.
PRECISION = 1e-9

def add(*argv):
    """! Calculates sum of given numbers.
    """
    result = 0
    for n in argv:
        result += float(n)
    return result


def subtract(a, *argv):
    """! Calculates difference of given numbers.
    """
    for n in argv:
        a -= float(n)
    return a


def multiply(*argv):
    """! Calculates multiplicand of given numbers.
    """
    result = 1
    for n in argv:
        result *= float(n)
    return result


def divide(a, *argv):
    """! Calculates quotient of given numbers.
    """
    result = a
    for n in argv:
        result /= float(n)
    return result


def factorial(num):
    """! Calculates n-th factorial of a number.
    @param num Factorial of this number is calculated.
    @return The n-th factorial of num.
    """
    if num < 0:
        raise TypeError("Calling factorial of number below 0")
    if not float(num).is_integer():
        raise TypeError("Calling factorial of non-integer number")
    num = int(num)
    product = 1
    for i in range(1, num+1):
        product = product * i
    return product

def sqrt(radicand, precision=PRECISION):
    """! Calculates square root of a number.
    Root is calculated with Newton`s method.
    @param radicand Square root of this number is calculated.
    @return The square root of radicand.
    """
    oldApprox = 0
    newApprox = radicand

    while abs(newApprox - oldApprox) > precision:
        oldApprox = newApprox
        fx = oldApprox*oldApprox - radicand
        dfx = 2 * oldApprox
        newApprox = oldApprox - fx / dfx

    return newApprox

def intExponentiate(base, exponent):
    """! Calculates an integer power of a number.
    @param base Number to be exponentiated.
    @param exponent The exponent of number.
    @return Float product of exponentiation.
    """
    if not float(exponent).is_integer():
        Exception("Cannot raise a number to the power of a negative number")

    exponent = int(exponent)

    inverse = False
    if exponent < 0:
        inverse = True
        exponent = -exponent

    result = 1
    for i in range(exponent):
        result *= base

    if inverse:
        result = 1 / result

    return result

def exponentiate(base, exponent):
    """! Calculates float power of a number.
    0 to the power of 0 is not defined.
    @param base  This is positive base for the calculation.
    @param exponent The exponent of a number.
    @return The n-th power of base number.
    """
    if float(exponent).is_integer():
        num = int(base)
        return intExponentiate(base, exponent)

    if base < 0:
        raise Exception("Cannot raise a negative number")

    inverse = False
    if exponent < 0:
        inverse = True
        exponent = -exponent

    # exponentiates the base to the power of (two to the power of exp)
    # exponent is int, base is float
    def expByTwoToPower(base, exp):
        result = base

        if exp >= 0:
            for i in range(exp):
                result = result * result
            return result

        exp = -exp
        for i in range(exp):
            result = sqrt(result)
        return result

    # fraction will be expanded by 2^5
    expand = 50

    numerator = int(exponent * 2 ** expand)
    result = 1
    # start from the last place of the binary number
    currentPlace = -expand

    while numerator != 0:
        if numerator & 1:
            result *= expByTwoToPower(base, currentPlace)

        numerator >>= 1
        currentPlace += 1

    if inverse:
        return 1 / result

    return result

def root(radicand, index = 2):
    """! Calculates n-th root of a number.
    @param radicand Root of this number is calculated.
    @param index The index of root. Implied value is 2 (square root).
    @return The index-th root of radicand.
    """
    return exponentiate(radicand, 1 / index)


def absolute(x):
    """! Returns absolute value of given number.
    """
    if (x < 0):
        return -x
    else:
        return x


def logarithm(argument, base=10, precision=PRECISION):
    """! Calculates logarithm using bisection method.
    @param argument Calculate logarithm of this number.
    @param base Base of the logarithm.
    @return Logarithm of given number in given base.
    """
    if argument <= 0 or base <=0:
        raise Exception('Outside of defined range')

    if base == 1:
        raise Exception('Base of logarithm cannot be 1')

    invert = False
    if base < 1:
        invert = True
        base = 1 / base

    end = max(argument, base)
    start = -end

    while abs(start - end) > precision:
        midpoint = (start + end) / 2
        value = exponentiate(base, midpoint)

        if value > argument:
            end = midpoint
        elif value < argument:
            start = midpoint
        else:
            break

    result = (start + end) / 2

    if invert:
        return -result
    return result


def sine(num):
    """! Calculates sine of num.
    Function works with radians.
    Sine is calculated with Taylor series.
    @param num  This is angle of which sine is calculated.
    @return The sine of num.
    """
    angle = num % (2*PI)
    _sum = 0
    sign = 1
    odd = 1
    for i in range(0, 33):
        _sum = _sum + sign*exponentiate(angle, odd)/factorial(odd)
        sign = sign*-1
        odd = odd+2
    return _sum


def cosine(num):
    """! Calculates cosine of num.
    Function works with radians.
    Cosine is calculated with Taylor series.
    @param num  This is angle of which cosine is calculated.
    @return The cosine of num.
    """
    angle = num % (2 * PI)
    _sum = 1
    sign = -1
    even = 2
    for i in range(0, 33):
        _sum = _sum + sign*exponentiate(angle, even)/factorial(even)
        sign = sign*-1
        even = even+2
    return _sum


def tangent(num):
    """! Calculates tangent of num.
    Function works with radians.
    Tangent is calculated as sine/cosine.
    @param num  This is angle of which sine is calculated.
    @return The tangent of num.
    """
    if absolute(num) % (PI*2) == PI/2:
        raise Exception("Calling tangent of PI/2 results in dividing by zero")
    return sine(num)/cosine(num)
