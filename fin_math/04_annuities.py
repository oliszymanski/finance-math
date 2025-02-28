'''
Chapter 5: annuities
'''

def calc_present_val( PMT: float, r: float, n: float ):
    return PMT * ( 1 - (1 + r)**(-n) )/r



def calc_future_val( PMT: float, r: float, n: float):
    return PMT * ( (1 + r)**n - 1 )/r



def calc_perpurity( PMT: float, r: float ):
    return PMT/r