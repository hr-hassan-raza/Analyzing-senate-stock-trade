#import util as u
##### 1b. Ticker Analysis (15 pts)
from senate_stock_trades import util as u
from collections import defaultdict
import datetime
def count_trades(start_date=None, end_date=None): ### Counting trades of senators according dates
    ans = {}
    module = u.get_data()
    senators = [d['senator'] for d in module]
    if start_date != None and end_date != None:
        a = start_date.split('-')
        b = end_date.split('-')
        #print(a)
        first_date = datetime.date(int(a[0]), int(a[1]), int(a[2]))
        second_date = datetime.date(int(b[0]), int(b[1]), int(b[2]))
        for i in senators:
            count = 0
            for d in module:
                x = d['transaction_date']
                x = x.split('/')
                #print(x)
                x = datetime.date(int(x[2]),int(x[0]),int(x[1]))
                if d['senator'] == i and x >= first_date and x <= second_date:
                    count = count + 1
            ans[i] = count 
    else:  
        for i in senators:
            count = len([d for d in module if d.get('senator')==i])
            ans[i] = count
    return ans
def sum_trades(start_date=None, end_date=None): ### Sum of trades according to dates
    ans = defaultdict(list)
    module = u.get_data()
    senators = [d['senator'] for d in module]
    for i in senators:
        ans[i] = [0,0]
    if start_date != None and end_date != None:
        a = start_date.split('-')
        b = end_date.split('-')
        #print(a)
        first_date = datetime.date(int(a[0]), int(a[1]), int(a[2]))
        second_date = datetime.date(int(b[0]), int(b[1]), int(b[2]))
    for i in module:
        #print(i['senator'])
        if start_date != None and end_date != None:
            x = i['transaction_date']
            x = x.split('/')
            #print(x)
            x = datetime.date(int(x[2]),int(x[0]),int(x[1]))
            if x >= first_date and x <= second_date:
                ans[i['senator']] =  u.add_amount_ranges(ans[i['senator']], i['amount_range'] )
        else:
            ans[i['senator']] =  u.add_amount_ranges(ans[i['senator']], i['amount_range'] )
    return ans
#print(sum_trades('2016-08-01', '2017-07-01'))