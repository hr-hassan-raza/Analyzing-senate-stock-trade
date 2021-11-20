# Analyzing-senate-stock-trade
Analyzing Senate Stock Data



we will again be working with data from the Senate Stock Watcher, built by Timothy Carambat. That data is located http://faculty.cs.niu.edu/~dakoop/cs503-2021fa/a3/senate-stock-trades.json




Senate Stock Trades Package

Ticker Analysis

Create an ticker.py module that has two methods that both take one parameter, the ticker symbol. Use the get_data method from the data module to obtain the data. The first method, count_trades, should return a dictionary of the form {<senator>: <count>} with the counts of trades for each senator. The second method, sum_trades, should return a dictionary of the form {<senator>: (<min_value>,<max_value)} with the range of possible trade values. Use the util.add_amount_ranges method from Part 1a to add the amount ranges.


Comparison

Create a compare.py module that calculates comparative information between two senators. Given two senators’ names as parameters, the count_diff method should return the difference between the number of transactions between the two senators, and the amount_diff method should return the ranged difference between the amounts of all trades. This difference should be computed by using the util.sub_amount_ranges method from Part 1a.

Stock Analysis Program

Create a analyze_trades.py program that uses the package from Part 1 to identify trades of interest and compare senators. The script should process two subcommands; the first is “ticker” and the second is “compare”. The first subcommand prints the results from the count_trades and sum_trades methods, and the second subcommand takes the names of two senators as arguments and prints the results from the count_diff and amount_diff methods. You can test your script via the IPython magic command %run analyze_trades.py ... or via the shell command !/opt/conda/envs/py39/bin/python analyze_trades.py

Add Date Filtering 

For this part, you will add date filtering to the package and program you wrote in Parts 1 and 2. This should not require significant changes to the overall logic, and your final package and library should work both for unfiltered data and for filtered data. Turn in this final package and program with the additional filtering added.



Add the ability to restrict the calculations by date to the compare.py module. Thus, count_diff and amount_diff should take two optional parameters that set the start date and end date, respectively. If they are not set, the start date is the earliest date in the data, and the end date is the latest date. The range is inclusive. The methods should now return the differences for the senators for only the trades between those dates, inclusive.

Add support for the date filtering in your script. To do so, we will require that the user specify the argument after the senators’ names and specify the date range in the format YYYY-mm-dd:YYYY-mm-dd. If the date range is specified, pass the parsed individual dates to the correct parameters of count_diff and amount_diff. You will need to parse the string to split the two dates and convert them to the form required by Part 3a. 
