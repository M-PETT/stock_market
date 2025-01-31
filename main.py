from my_package import stock
import sys
import time
import argparse

valid_firms = ["AAPL", "GOOGL"]
# this function requires two positional arguments to identify the companies and an optional argument that allow the user to get more explicit information about the program"
def parsing_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("stock_code",
                        help= "The ticker symbol of the company.",
                        choices= valid_firms)
    parser.add_argument("stock_code2",
                        help= "The ticker symbol of the company.",
                        choices= valid_firms)
    parser.add_argument("-v", 
                        help= "Increases verbosity of the program.",
                        action= "store_true", default= False)
    args = parser.parse_args()
    return args

#the following code gives the value of the stock price of the input companies
try:
    args= parsing_input()
    n, price= stock.get_price(args.stock_code)
    if args.v:
       print("Successfully fetched data")
       print("Company {} has a stock value of {}$".format(price, n))
    else:
        print("{} = {}$".format(price, n))

    n, price= stock.get_price(args.stock_code2)
    if args.v:
       print("Successfully fetched data")
       print("Company {} has a stock value of {}$".format(price, n))
    else:
        print("{} = {}$".format(price, n))

#this code helps the user to check if he wrote correctly the inputs
except:
    if len(sys.argv)>2:
        print("Write correctly the arguments!")
        exit()
    else:
        print("Write all the required arguments!")
        exit()
