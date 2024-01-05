"""
In this challenge, you must discount a price according to its value.

If the price is 300 or above, there will be a 30% discount.

If the price is between 200 and 300 (200 inclusive), there will be a 20% discount.

If the price is between 100 and 200 (100 inclusive), there will be a 10% discount.

If the price is less than 100, there will be a 5% discount.

If the price is negative, there will be no discount.

"""


price = 50

if price >= 300:
    price *= 0.7 # (1- 0.3)
elif price >= 200:
    price *= 0.8 # (1- 0.2)
elif price < 100 and price >= 0:
    price *= 0.95 # (1- 0.05)

print(price)

