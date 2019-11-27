from stock import get_price

'''
once imported the stock function we difene the output sentences that the program will return when used for Apple and google.
'''

n,price=get_price("AAPL")
print("Company {} has a stock value of {}$".format(price, n))
n,price=get_price("GOOGL")
print("Company {} has a stock value of {}$".format(price, n))


