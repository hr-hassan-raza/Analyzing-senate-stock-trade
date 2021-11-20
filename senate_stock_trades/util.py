
##### 1a. Data Utilities (15 pts)
import os
import json
def get_data(): ###Get data function
    fname = os.path.join(os.path.dirname(__file__),'senate-stock-trades.json')
    module = -1000000000 ### sentinel value
    if module == -1000000000: 
        f = open(fname,)
        module = json.load(f)
    return module
def add_amount_ranges(amount_range_1, amount_range_2 ): ### add amount ranges function
    if amount_range_1[0] != None and amount_range_2[0] != None:
        sum_range_min = int(amount_range_1[0]) + int(amount_range_2[0])
    else:
        sum_range_min = None
    if amount_range_1[1] != None and amount_range_2[1] != None:
        sum_range_max = int(amount_range_1[1]) + int(amount_range_2[1])
    else:
        sum_range_max = None
    ans = (sum_range_min, sum_range_max)
    return ans
def sub_amount_ranges(amount_range_1, amount_range_2): ### Subtract amount ranges function
    if amount_range_1[0] != None and amount_range_2[0] != None:
        diff_range_min = int(amount_range_1[0]) - int(amount_range_2[0])
    else:
        diff_range_min = None
    if amount_range_1[1] != None and amount_range_2[1] != None:
        diff_range_max = int(amount_range_1[1]) - int(amount_range_2[1])
    else:
        diff_range_max = None
    ans = (diff_range_min, diff_range_max)
    return ans