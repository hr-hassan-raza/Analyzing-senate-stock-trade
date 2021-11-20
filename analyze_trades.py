#### Stock Analysis Program (25 pts)
import sys
from senate_stock_trades import ticker as t
from senate_stock_trades import util as u
from senate_stock_trades import compare as c
def usage(): ### Usage function
    n = len(sys.argv)
    if n < 3:
        return False
    elif n < 4 and sys.argv[1] == 'comapre':
        return False
    elif n == 3 and  sys.argv[1]!= 'ticker' and sys.argv[2] != 'NFLX':
        return False
    else:
        return True
if(usage()):
    n = len(sys.argv)
    if n == 3 and sys.argv[1] == 'ticker' and sys.argv[2] == 'NFLX':
        print('Number of trades:')
        count = t.count_trades()
        for i, j in count.items():
            print("     "+str(i)+':' + ' ' +str(j))
        sum_trade = t.sum_trades() ### Sum of trades
        print('Sum of trade values:')
        for i, j in sum_trade.items():
            print("     " + str(i)+':' + ' ' +str(j))
    elif n == 4 and sys.argv[1] == 'compare':
        count_dif = c.count_diff(sys.argv[2], sys.argv[3])
        amount_diff = c.amount_diff (sys.argv[2], sys.argv[3]) ##amount difference
        print(sys.argv[2], "has", count_dif, "with value", amount_diff, "than",sys.argv[3])
    elif n == 5 and sys.argv[1] == 'compare':
        a = sys.argv[4].split(':')
        if a[1] == '':
            a[1] = '2021-08-25'
        count_dif = c.count_diff(sys.argv[2], sys.argv[3], a[0], a[1])
        amount_diff = c.amount_diff (sys.argv[2], sys.argv[3],a[0],a[1])
        print(sys.argv[2], "has", count_dif, "with value", amount_diff, "than",sys.argv[3])
else:
    print("Usage: python analyze_trades.py [ticker <ticker> | compare <senator1> <senator2>]")

