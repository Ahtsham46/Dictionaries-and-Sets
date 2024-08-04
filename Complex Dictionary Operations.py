items_prices = {'apple': 1.2, 'banana': 0.5, 'cherry': 3.0, 'date': 2.5}
expensive_items = {item: price for item, price in items_prices.items() if price > 2}
print(expensive_items)