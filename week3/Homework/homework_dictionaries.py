market = {"dairy": ["yogurt", "cheese"],"fruits": ["banana", "apple", "orange", "lemon", "apple", "banana", "banana"]}
print(market)

market["candies"] = ["mars", "kinder", "twix"]
print(market)

market_sorted = (sorted(market['fruits']))
print(market_sorted)

finaldata = sorted(set(market['fruits']))
print(finaldata)
print(market)