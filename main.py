"""Complete the accumulate() function below, according to its docstring."""

# chars =['a','b','c','d','e']


# def accumulate(chars):
#   strs = ''
#   for char in chars:
#     strs = strs+char
#   return strs

# print(accumulate(chars))


"Integer Accumulator:"

# num_list = [1, 2, 3, 4, 5]

# num_sum = 0
# for num in num_list:
#     num_sum += num

# print(num_sum)


"Filtered Accumulator"


mixed_data = [1, 'a', 2, 'b', 3, 'c', 4, 'd', 5]

num_sum = 0
for val in mixed_data:
    if isinstance(val, int):
        num_sum = num_sum + val

print(num_sum)