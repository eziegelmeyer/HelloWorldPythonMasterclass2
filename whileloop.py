# for i in range (10):
#     print("i is now {}".format(i))

# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1

# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break


# for i in range(1, 20, 3 and 5):
#     if i % 3 != 0:
#         print(i)

for i in range(21):
    if i % 3 != 0 and i % 5 != 0:
        print(i)

# using continue
# for x in range(21):
#     if x % 3 == 0 or x % 5 == 0:
#         continue
#     print(x)

# without continue
# for x in range(21):
#     if x % 3 != 0 and x % 5 != 0:
#         print(x)