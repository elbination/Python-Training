# Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise.
# def is_multiple(n, m):
#     try:
#         if int(n) % int(m) == 0:
#             return True
#         else:
#             return False
#     except ValueError:
#         print('Number must be an integer.')
#
# print(is_multiple(9, 3)) # True

# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.
# def min_max(data):
#     sorted_data = sorted(data)
#     result = []
#     result.extend([sorted_data[0], sorted_data[-1]])
#     return tuple(result)
# print(min_max([2, 4, 6, 1, 6, 9])) # (1, 9)

# Write a short Python function that takes a positive integer n and
# returns the sum of the squares of all the positive integers smaller than n
# def sum_of_squares(n):
#     i = 0
#     total = 0
#     while i < n:
#         total += i * i
#         i += 1
#     return total
# print(sum_of_squares(10)) # 285

# def sum_of_squares(n):
#     return sum([pow(x, 2) for x in range(n)]) if n > 0 else False
# print(sum_of_squares(9)) # 204

# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally
# print([chr(x) for x in range(ord('a'), ord('z') + 1)])
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Write a Python program to create all possible strings
# by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
# from itertools import permutations # Hoán vị
# def possible_strings(data):
#     permutated_data = permutations(data)
#     result = []
#     for string in permutated_data:
#         result.append(''.join(string))
#     return len(result)
# print(possible_strings(['c', 'a', 't', 'd', 'o'])) # 120

# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.
def repreatedly_divide(n):
    count = 0
    while n % 2 == 0:
        x = n / 2
        n = x
        count += 1
        if x < 2:
            break
    return count
print(repreatedly_divide(80))  # 4
