def invest(amount, rate, years):
    for year in range(1, years + 1):
        amount = amount + amount * rate
        print(f'year {year}: ${(amount):.2f} ')

invest(100, .05, 4)