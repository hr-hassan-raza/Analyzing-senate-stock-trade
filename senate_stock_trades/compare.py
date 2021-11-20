#### 1c. Comparison (15 pts)
from senate_stock_trades import ticker as t
from senate_stock_trades import util as u
def count_diff(name_1, name_2,start_date=None, end_date=None): ###### 3a. [CSCI 503 Only] Add Date Filtering (20 pts)

    count = t.count_trades(start_date, end_date)
    if name_1 not in count.keys() or name_2 not in count.keys():
        print("Senator not found")
        return 'None'
    else: 
        return count[name_1] - count[name_2]
def amount_diff(name_1, name_2,start_date=None, end_date=None): ##### 3b. Add Filtering to the Program (10 pts)

    sum_trades = t.sum_trades(start_date, end_date)
    if name_1 not in sum_trades.keys() or name_2 not in sum_trades.keys():
        print("Senator not found")
        return 'None'
    else:
        return u.sub_amount_ranges(sum_trades[name_1],sum_trades[name_2]) 


