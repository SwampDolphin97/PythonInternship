item_price = [1050, 2200, 8575, 485, 234, 150, 399]
a = sorted(item_price)
print("Price of costliest item sold in retail store:" , a[-1])
print("Number of items in the Retail store:" , len(item_price))
print("Prices of items in increasing order:"  , sorted(item_price))
print("Prices of items in decreasing order:"  , sorted(item_price , reverse = True))
