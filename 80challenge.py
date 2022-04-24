# available_actions = 1, 2, 3, 4, 5, 0
# options = "Please choose your option from the list below:\n1. Learn Python\n2. Learn Java\n3. Go swimming\n4. Have dinner\n5. Go to bed\n0. Exit"
#
# chosen_exit = ""
# while chosen_exit != available_actions:
#     chosen_exit = int(input(options))
#     if chosen_exit != 0:
#         print("You guessed", chosen_exit, ". Please try again.")
#     else:
#         print("All done!")
#         break

# correct solution
# print("please choose an option:")
# print("1:\tLearn Python")
# print("2:\tLearn Java")
# print("3:\tGo swimming")
# print("5.\tGo to bed")
# print("0:\tExit")
choice = "-"
while choice != "0":
    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("please choose an option:")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("5.\tGo to bed")
        print("0:\tExit")

    choice = input()




# ------ other iterations ----
#chosen_exit = ""
#while chosen_exit not in available_actions:
 #   chosen_exit = input("Please choose your option from the list below:\n1. Learn Python\n2. Learn Java\n3. Go swimming\n4. Have dinner\n5. Go to bed\n0. Exit")
  #  if chosen_exit.casefold() == "0":
   #     print("All done!")
    #    break
#    elif chosen_exit.casefold() == "1":
#        print("You chose 1. Learn Python. Nice one.")
#    elif chosen_exit.casefold() == "2":
#        print("You chose 2. Learn Java. Nice one.")
#    elif chosen_exit.casefold() == "3":
#        print("You chose to go swimming. Nice one.")
#    elif chosen_exit.casefold() == "4":
#        print("You ate dinner, big win.")
#    elif chosen_exit.casefold() == "5":
#        print("Bedtime, nighty night!")



# testing a push from my work computer
print(testing)