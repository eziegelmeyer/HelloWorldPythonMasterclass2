data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
# data = [104, 101, 4, 105, 308, 103, 5,
#         107, 100, 306, 106]
# data = [104, 101, 4, 105, 103, 5,
#         107, 100, 106, 102, 108]
# data = [104, 101, 105, 308, 103,
#         107, 100, 306, 106, 102, 108]
# data = []
# data = [101, 102, 103, 104, 105, 106, 107]

min_valid = 100
max_valid = 200

print(data)

# for index in range(len(data) - 1, - 1, - 1):
#     if data[index] < min_valid or data[index] > max_valid:
#         print(index, data)
#         del data[index]

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]

print(data)
