def kids_with_candies(candies, extra_candies):
    max_candies = max(candies)
    result = []
    for i in range(len(candies)):
        if candies[i] + extra_candies >= max_candies:
            result.append(True)
        else:
            result.append(False)
    return result


print(kids_with_candies([2, 3, 5, 1, 3], 3))
