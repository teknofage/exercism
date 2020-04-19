import sys

sys.setrecursionlimit(3000)

coins = [5,10]
k = 94

def combinos(coins, target):
    valid_list = []
    
    def _combs(i, combination, sum_combination):
        if sum_combination == target:
            valid_list.append(combination)
        else: 
            for j in range(i, len(coins)):
                if sum_combination + coins[j] <= target:
                    _combs(j, combination + [coins[j]], sum_combination + coins[j])
                    
    _combs(0, [], 0)
    return valid_list

combinos(coins, 3)

print(combinos(coins, k))

def find_fewest_coins(coins, target):
    combinations = combinos(coins, target)
    if len(combinations) == 0:
        raise ValueError "Computer says no."
    smallest_comb = combinations[0]
    for combination in combinations:
        #compare combination to previous smallest combination
        if len(combination) < len(smallest_comb):
            smallest_comb = combination
    return smallest_comb
    
