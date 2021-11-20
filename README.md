# Analyzing-senate-stock-trade
Analyzing Senate Stock Data


we will again be working with data from the Senate Stock Watcher, built by Timothy Carambat That data is located http://faculty.cs.niu.edu/~dakoop/cs503-2021fa/a3/senate-stock-trades.json.


Remember that once loaded, the data is a list of dictionaries where each dictionary has ten key-value pairs. Those keys and a brief description are:

transaction_date: the date of the transaction as a string in mm/dd/yyyy format
owner: the owner of the stock (the senator or a family member)
ticker: the stock ticker symbol (e.g. AAPL)
asset_type: whether the asset is a stock, bond, cryptocurrency, etc.
type: the type of transaction (purchase or sale)
amount_range: the amount of the transaction (a range specified by a tuple (min_amount, max_amount)). max_amount can be None to indicate no upper bound
senator: the name of the senator involved in the transaction




1. Senate Stock Trades Package 
Create three new Python modules, one for reading the dataset, one for analyzing trades by ticker symbol, and one for comparing two senators. Put the three modules (util.py, ticker.py, and compare.py) into a package named senate_stock_trades.

1a. Data Utilities 
Create a util.py module that has three methods: get_data, add_amount_ranges, and sub_amount_ranges.

The get_data method should read and parse the senate-stock-trades.json datafile and store it in a module variable. Assume that the data file resides in the same directory as util.py. You can then get its absolute path via the __file__ variable of the module via:

import os
fname = os.path.join(os.path.dirname(__file__),'senate-stock-trades.json')
Use the json module to load the data from the file. Your get_data method should only read and parse the file from disk once, otherwise returning the pre-loaded data.

The add_amount_ranges and sub_amount_ranges should add and subtract two amount ranges, respectively. Recall that an amount range is a tuple (min, max) where max can be None indicating it has no upper bound. Two ranges (a,b) +/- (c,d) = (a+/-c, b+/-d) unless at least one of b or d is None, in which case the result is (a+/-c, None).

Hints
Initialize the module variable to a sentinel value to indicate when the data has not been read.
You can use %autoreload to automatically reload modules as you edit them. Do note, however, that this will mask the effects of trying to not keep reloading the data! You can also use importlib.reload to do this manually.
1b. Ticker Analysis 
Create an ticker.py module that has two methods that both take one parameter, the ticker symbol. Use the get_data method from the data module to obtain the data. The first method, count_trades, should return a dictionary of the form {<senator>: <count>} with the counts of trades for each senator. The second method, sum_trades, should return a dictionary of the form {<senator>: (<min_value>,<max_value)} with the range of possible trade values. Use the util.add_amount_ranges method from Part 1a to add the amount ranges.

Hints
Make sure to import the util module! You might consider using relative imports to do this from a sibling module.
You may use collections.Counter for count_trades.
You could consider using collections.defaultdict to help with sum_trades. You can use a lambda function as the argument to defaultdict to initialize the key-value pairs with a tuple.
1c. Comparison 
Create a compare.py module that calculates comparative information between two senators. Given two senators’ names as parameters, the count_diff method should return the difference between the number of transactions between the two senators, and the amount_diff method should return the ranged difference between the amounts of all trades. This difference should be computed by using the util.sub_amount_ranges method from Part 1a.

Hints
Consider testing the functions via code in a notebook. You may also do this in the modules themselves, but remember to make sure they only run when the module is run as a script.
1d. Package 
Make sure all three analysis modules live in a single senate_stock_trades package. Add an __init__.py file for completeness. It may contain documentation and the pass keyword.

2. Stock Analysis Program 
Create a analyze_trades.py program that uses the package from Part 1 to identify trades of interest and compare senators. The script should process two subcommands; the first is “ticker” and the second is “compare”. The first subcommand prints the results from the count_trades and sum_trades methods, and the second subcommand takes the names of two senators as arguments and prints the results from the count_diff and amount_diff methods. You can test your script via the IPython magic command %run analyze_trades.py ... or via the shell command !/opt/conda/envs/py39/bin/python analyze_trades.py ... (you will need to adjust the path if not using tiger). Make sure to print a usage method if the user misses or provides incorrect arguments. Some sample output:

%run analyze_trades.py
Usage: python analyze_trades.py [ticker <ticker> | compare <senator1> <senator2>]

%run analyze_trades.py ticker
Usage: python analyze_trades.py [ticker <ticker> | compare <senator1> <senator2>]

%run analyze_trades.py ticker NFLX
Number of trades:
  Pat Roberts: 43
  Ron L Wyden: 8
  Sheldon Whitehouse: 8
  David A Perdue , Jr: 4
  Christopher A Coons: 4
  John Hoeven: 1
Sum of trade values:
  Pat Roberts: (1343043, 3420000)
  Ron L Wyden: (71008, 240000)
  Sheldon Whitehouse: (50008, 225000)
  David A Perdue , Jr: (60004, 200000)
  John Hoeven: (50001, 100000)
  Christopher A Coons: (4004, 60000)

%run analyze_trades.py compare "Kelly Loeffler" "David A Perdue , Jr"
Kelly Loeffler has -2318 trades with value +(10969682, 68780000) than David A Perdue , Jr

%run analyze_trades.py compare "Kelly Loeffler" "James M Inhofe"
Kelly Loeffler has +50 trades with value -(12291950, None) than James M Inhofe
Hints
Create a usage method that can be called whenever there is trouble
You will need to pass the names in quotes because of the spaces which the shell will otherwise decompose into separate arguments.
You will need a different number of arguments depending on which subcommand is called
Note that showing the +/- sign for the range will require figuring out whether the amounts are less than or greater than zero
3. [CSCI 503 Only] Add Date Filtering (20 pts)
For this part, you will add date filtering to the package and program you wrote in Parts 1 and 2. This should not require significant changes to the overall logic, and your final package and library should work both for unfiltered data and for filtered data. Turn in this final package and program with the additional filtering added.

3a. Add Filtering to the Package 
Add the ability to restrict the calculations by date to the compare.py module. Thus, count_diff and amount_diff should take two optional parameters that set the start date and end date, respectively. If they are not set, the start date is the earliest date in the data, and the end date is the latest date. The range is inclusive. The methods should now return the differences for the senators for only the trades between those dates, inclusive.

You may choose to parse the transaction_date in the data to a tuple (as in Assignment 3) or to a date object using the datetime.date library. You may also choose which format the count_diff and amount_diff methods take (e.g. a tuple (year, month, day) or a date object), but you need to document this as a docstring in those methods. You will be passing arguments that adhere to your format in Part 3b.

Hints
Use a sentinel value to indicate when the start or end date are not set. You can use an or expression to check if either date is unset or the criteria is satisfied.
3b. Add Filtering to the Program (10 pts)
Add support for the date filtering in your script. To do so, we will require that the user specify the argument after the senators’ names and specify the date range in the format YYYY-mm-dd:YYYY-mm-dd. If the date range is specified, pass the parsed individual dates to the correct parameters of count_diff and amount_diff. You will need to parse the string to split the two dates and convert them to the form required by Part 3a. Some sample output:

%run analyze_trades.py compare
Usage: python analyze_trades.py [ticker <ticker> | compare <senator1> <senator2> [start-date:end-date]]

%run analyze_trades.py compare "David A Perdue , Jr" "Kelly Loeffler" 2016-08-01:2017-07-01
David A Perdue , Jr has +296 trades with value +(2330296, 8800000) than Kelly Loeffler

%run analyze_trades.py compare "Kelly Loeffler" "James M Inhofe" 2018-01-01:
Kelly Loeffler has +180 trades with value +(42140180, 176475000) than James M Inhofe
Hints:
Use the split function multiple times to parse the date string
Make sure to parse the extracted strings to integers
Make sure your code still runs if the entire date range is not specified
Make sure to detect when either the start or end date is not specified
Remember to update the usage string
