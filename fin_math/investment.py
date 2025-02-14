'''
chapter 6: investment appraisal metrics

Metrics, that halp in decision-making on investing.
'''


def calc_current_val( CF_t: list, r: float, t: float ):

    npv = 0.0    

    for t, cf in enumerate( CF_t ):
        npv += cf / ( 1 + rate )**t

    investment_decision = npv > 0.0

    return npv, investment_decision



# def calc_payback( CF_t: list ):

#     count_sum = sum( CF_t )
#     payback = min(  )

#     return 