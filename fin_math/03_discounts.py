'''
Chapter 3: commercial discount

A commercial discount is a discount given to a
potential buyer of goods.
'''


def calc_discount( FV: float, d: float, t: float ):
    return FV * d * t



def calc_present_val( FV: float, d: float, t: float ):
    return FV * ( 1 - d * t )