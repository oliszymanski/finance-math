"""
Chapter 01: simple interest

Simple interest is a type of interest charged on a loan
or earned on an investment, based solely on the original principal amount.
"""

def future_val( PV: float, r: float, n: float ):
    '''
        FV – future value (final capital)

        PV – present value (initial capital),
        r – annual interest rate (expressed as a decimal),
        n – time period in years.
    '''

    return PV * ( 1 + r * n )



def present_val( FV: float, r: float, n: int ):
    '''
        PV - present value

        r - interest rate,
        n - time period in years.
    '''
    
    return FV / ( 1 + r * n )



def calc_interest( PV:float, r:float, n: int ):
    '''
        I - interest capital
        PV - present value
        r - annual interest rate
        n - time periodc in years.
    '''

    return PV * r * n



def calc_interest_rate( I: float, PV: float, n: int ):
    '''
        r - interest rate

        I - interest capital
        PV - present value
        n - time period in years.
    '''

    return I / ( PV * n )