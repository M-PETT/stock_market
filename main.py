from my_package import stock
import sys
import time
import argparse

valid_firms = ["AAPL", "GOOGL"]

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
                        action= "store_true")
    args = parser.parse_args()
    return args

try:
    args= parsing_input()
    n, price= stock.get_price(args.stock_code)
    print("Company {} has a stock value of {}$".format(price, n))
    n, price= stock.get_price(args.stock_code2)
    print("Company {} has a stock value of {}$".format(price, n))
    time.sleep(5)
    exit()

except:
    if len(sys.argv)>2:
        print("Write correctly the arguments!")
        exit()
    else:
        print("Write all the required arguments!")
        exit()
