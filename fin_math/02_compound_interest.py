"""
Chapter 02: compound interest

Compound interest is a method used to calculate the interest. It
increases your income in time (interest is the same but the amount
is increased).
"""

from math import e


def annual( PV, r ):
    '''
        FV - future value (end value)

        PV - present value,
        r - annual interest rate,
        n - number of years,
        m - number of compounding periods (per year);
    '''
    
    if ( isinstance( r, list ) ):
        for rate in r:
            FV = PV * ( 1 + rate )

    else: FV = PV * ( 1 + r )

    return FV


def sub_period( PV, r, n, m):
    '''
        FV - future value (end value)

        PV - present value,
        r - annual interest rate,
        n - number of years,
        m - number of compounding periods (per year);
    '''

    if ( isinstance( r, list ) ):
        for rate in r:
            FV = FV * ( 1 + (rate / m)**(m*n) )

    else: FV = PV * ( 1 + r )

    return FV


def continuous(PV, n, r):
    '''
        FV - future value
        
        PV - present value,
        r - annual interest rate,
        n - number of years;
    '''

    return PV * e**(r*n)