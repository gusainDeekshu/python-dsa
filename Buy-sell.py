def maxProfit(prices):
  min_price=float('inf')
  max_profit=0;
  for i,price in enumerate(prices):
    if min_price > price:
      min_price=price
    elif price - min_price > max_profit:
      max_profit=price -min_price

  return max_profit





# Buy at 1, sell at 6 → profit = 5
prices = [7,1,  5, 3, 6, 4 ]

print(maxProfit(prices))

