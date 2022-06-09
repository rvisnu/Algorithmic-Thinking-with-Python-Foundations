def coin_count(total):
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    coin_used = []
    new_total = total
    latest = len(coins) - 1
    while True:
        if new_total == 0:
            break
        elif new_total >= coins[latest]:
            coin_used.append(coins[latest])
            new_total -= coins[latest]
        elif new_total < coins[latest]:
            latest -= 1
    return coin_used

print(coin_count(500))