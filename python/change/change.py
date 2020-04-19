
coins = [1, 2, 3, 4, 5]
k = 7




def combinations(coins, target):
    valid_list = []
    
    def _combs(i, combination, sum_combination):
        if sum_combination == target:
            valid_list.append(combination)
        else: 
            for j in range(i, len(coins)):
                if sum_combination <= target:
                    _combs(j, combination + [coins[j]], sum_combination + coins[j])
                    
    _combs(0, [], 0)
    return valid_list

combinations(coins, 3)

print(combinations(coins, k))

def find_fewest_coins(combinations):
    smallest_comb = combinations[0]
    for combination in combinations:
        #compare combination to previous smallest combination
        if len(combination) < len(smallest_comb):
            smallest_comb = combination
    return smallest_comb
    
print(find_fewest_coins(combinations(coins, k)))