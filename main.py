from my_package import stock
import sys
import time

if len(sys.argv)>2:
    n,price=stock.get_price(sys.argv[1])
    print("Company {} has a stock value of {}$".format(price, n))
    n,price=stock.get_price(sys.argv[2])
    print("Company {} has a stock value of {}$".format(price, n))
else:
    print("Give me 2 arguments as input!")
    exit()


