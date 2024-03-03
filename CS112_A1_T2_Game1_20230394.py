# File: CS112_A1_T2_Game1_20230394.py
# Purpose: Two players start from 0 and alternatively add a number from 1 to 10 to the sum . The player who reaches 100 wins.
# Author: Mariam Abdelrahman Youssef Mohamed
# ID: 20230394

valid_option = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # list of all valid numbers that a player can choose

while True:  # loop for validating whether to exit or play the game
    final_num = 0
    print("Welcome to The 100 Game, please choose A or B: ")  # a menu for the player to choose from
    print("A) Play 100 Game")
    print("B) Exit the Game")
    option = input().upper()

    if option == "A":  # if the player chooses to play
        while final_num < 100:
            try:
                num1_input = input("Player 1 Pick a number from 1-10: ")
                num1 = int(num1_input)
                if num1 not in valid_option:
                    print("Please enter a valid number (1-10)")
                    continue
                
                final_num += num1

                if final_num <= 100:
                    print("Total = ", final_num)

                if final_num == 100:
                    print("Player 1 wins")
                    break
                elif final_num > 100:
                    print("Invalid choice, choose a number to reach 100 only or less")
                    final_num -= num1
                    continue
            except ValueError:
                print("Invalid input. Please enter a valid integer between 1 and 10.")
                continue

            while True :
                try :
                    num2_input = input("Player 2 Pick a number from 1-10: ")
                    num2 = int(num2_input)
                    if num2 not in valid_option:
                        print("Please enter a valid number (1-10)")
                        continue

                    final_num += num2

                    if final_num <= 100:
                        print("Total = ", final_num)
                        break

                    if final_num == 100:
                        print("Player 2 wins")
                        break
                    elif final_num > 100:
                        print("Invalid choice, choose a number to reach 100 only or less")
                        final_num -= num2
                        continue

                except ValueError:
                    print("Invalid input. Please enter a valid integer between 1 and 10.")
                    continue

    elif option == "B":  # if the player chooses to exit
        print("You are now exiting the game, Goodbye ^_^")
        break
    else:  # if the player inputs an invalid option
        print("Please choose a valid option")