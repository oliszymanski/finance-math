'''
Chapter 5: loans
Loans are lent money with rates (so that the bank makes more money on
ledning).
'''


def calc_loan_rate( PV: float, r: float, n: float ):
    return PV * ( r/( 1 - ( 1 + r )**(-n) ) )



def calc_balance( PMT: float, r: float, n: float, k: float ):
    return PMT * ( 1 - ( 1 + r )**( -( n-k ) ) ) / r