def min_cost_to_buy_magnets(n, k, magnets):
    from collections import defaultdict

    count = defaultdict(int)
    total_cost = 0
    unique_count = 0 
    min_cost = float('inf')

    left = 0

    for right in range(n):
        magnet_type = magnets[right]
        total_cost += magnet_type

        if 1 <= magnet_type <= k:
            if count[magnet_type] == 0:
                unique_count += 1
            count[magnet_type] += 1

        while unique_count == k:
            min_cost = min(min_cost, total_cost)

            left_magnet_type = magnets[left]
            total_cost -= left_magnet_type

            if 1 <= left_magnet_type <= k:
                count[left_magnet_type] -= 1
                if count[left_magnet_type] == 0:
                    unique_count -= 1
            
            left += 1

    return min_cost

n, k = map(int, input().split())
magnets = list(map(int, input().split()))

print(min_cost_to_buy_magnets(n, k, magnets))
