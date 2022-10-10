# for index, number in enumerate("abcdefgh"):
#     print(index, number)

for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

index, character = (0, 'a')
print(index)
print(character)
