menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]


# write code to print all the meals in the menu
# but with spam removed
# you can choose which approach to use
# 1 - remove spam from each list, then print the list
# 2 - print out the items in each list, as long as
# it's not spam

# SOLUTION THAT WORKS FOR SINGLE LIST
# catty_list = ["egg", "bacon", "spam", "beans"]
# snack = "spam"
#
# for banana in catty_list:
#     if "spam" == banana:
#         catty_list.remove("spam")
#
# print(catty_list)

# 1 - remove spam from each list, then print the list
for meal in menu:
    for item in meal:
        if "spam" == item:
            meal.remove("spam")
print(menu)

print("Solution 2:")

# 2 - print out the items in each list, as long as
# it's not spam

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item)
