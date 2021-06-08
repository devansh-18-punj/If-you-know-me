print("***      Welcome to if_you_know_me game      ***\n")
print("You will be given random choices to answer quiz related to me")
print("But, if you get randomly 0, then the code will exit automatically, bad for you")
print("You will have to answer all the questions in small letters")
print("If you give 5 or more correct answers to the quiz, you will have a secret message :) \n")

import random
import playsound

def start():
    your_points = 0
    def yoyo():
        birth = int(input("Please enter birth date of Devansh in numbers to unlock further program : "))
        if birth == 26:
            print("Hello my buddy, welcome to the program")
        else:
            print("You don't know me at all")
            playsound.playsound("sad.mp3")
            exit()
    yoyo()
    lst = [0, 1, 2]
    le = random.choice(lst)
    if le == 0:
        print("But I am soo Sorry but you are bad at your fate according to my code, because you got 0 at random choice:)\n")
        print("Better luck next time!")
        playsound.playsound("sad.mp3")
        exit()
    else:
        n = int(input("Please guess number between 0 to 7 : "))
        if n == le:
            print("Congo! You are one of the luckiest person according to my code\n")
            playsound.playsound("oh-my-god_5.mp3")
            your_points = your_points + 1
            print("Now, Your points are, ", your_points)
            print("Your guess is", n, "and computer's guess is also", le)
            print("Now, you are given ", le, "chances to guess the correct option of quiz\n")
        else:
            print("Now, you are given ", le, "chance by random to guess the correct option of quiz\n")
        print("Question 1 : ")
        for c in range(le):
            color = input("Which is the favourite color of Devansh(please write in small letters) : ")
            if color == "black":
                playsound.playsound("oh-my-god_5.mp3")
                your_points = your_points + 1
                print("Congo! you have,", your_points, "points\n")
                break
            else:
                your_points = your_points
                print("You are wrong here buddy")
                print("You have now,", your_points, "points\n")
                playsound.playsound("oh_no_1.mp3")
        print("Question 2 : ")
        for c in range(le):
            num = int(input("Which is the favourite number of Devansh(please write in numeral) : "))
            if num == 18:
                playsound.playsound("oh-my-god_5.mp3")
                your_points = your_points + 1
                print("Congo! you have,", your_points, "points now\n")
                break
            else:
                your_points = your_points
                print("You are wrong here buddy")
                print("You have now,", your_points, "points\n")
                playsound.playsound("oh_no_1.mp3")
        print("Question 3 : ")
        for c in range(le):
            num = input("Which is the favourite sport of Devansh(please write in small letters) : ")
            if num == "football":
                playsound.playsound("oh-my-god_5.mp3")
                your_points = your_points + 1
                print("Congo! you have,", your_points, "points now\n")
                break
            else:
                your_points = your_points
                print("You are wrong here buddy")
                print("You have now,", your_points, "points\n")
                playsound.playsound("oh_no_1.mp3")
        print("Question 4 : ")
        for c in range(le):
            num = input("Which is the favourite flavour of ice cream of Devansh(please write in small letters) : ")
            if num == "chocolate":
                playsound.playsound("oh-my-god_5.mp3")
                your_points = your_points + 1
                print("Congo! you have,", your_points, "points now\n")
                break
            else:
                your_points = your_points
                print("You are wrong here buddy")
                print("You have now,", your_points, "points\n")
                playsound.playsound("oh_no_1.mp3")
        print("Question 5 : ")
        for c in range(le):
            num = input("Who is the favourite player of Devansh in cricket(please write in small letters) : ")
            if num == "virat kohli":
                playsound.playsound("oh-my-god_5.mp3")
                your_points = your_points + 1
                print("Congo! you have,", your_points, "points now\n")
                break
            else:
                your_points = your_points
                print("You are wrong here buddy")
                print("You have now,", your_points, "points\n")
                playsound.playsound("oh_no_1.mp3")
        print("Question 6 : ")
        for c in range(le):
            num = input("Which is the favourite movie type of Devansh(please write in small letters) : ")
            if num == "romantic":
                playsound.playsound("oh-my-god_5.mp3")
                your_points = your_points + 1
                print("Congo! you have,", your_points, "points now\n")
                break
            else:
                your_points = your_points
                print("You are wrong here buddy")
                print("You have now,", your_points, "points\n")
                playsound.playsound("oh_no_1.mp3")
        print("Question 7 : ")
        for c in range(le):
            num = input("Do Devansh wear spectacles?(yes or no) (please write in small letters) : ")
            if num == "no":
                playsound.playsound("oh-my-god_5.mp3")
                your_points = your_points + 1
                print("Congo! you have,", your_points, "points now\n")
                break
            else:
                your_points = your_points
                print("You are wrong here buddy")
                print("You have now,", your_points, "points\n")
                playsound.playsound("oh_no_1.mp3")
        print("Question 8 : ")
        for c in range(le):
            num = input("Who is the favourite player of Devansh in football(please write in small letters)(only second name) : ")
            if num == "ronaldo":
                playsound.playsound("oh-my-god_5.mp3")
                your_points = your_points + 1
                print("Congo! you have,", your_points, "points now\n")
                break
            else:
                your_points = your_points
                print("You are wrong here buddy")
                print("You have now,", your_points, "points\n")
                playsound.playsound("oh_no_1.mp3")
        if your_points >= 5:
            k = input("Can you please write your name for me : ")
            with open("Your_buddy.txt", "a") as f:
                f.write(k + "," + "you are real buddy of Devansh\n" + "Let's plan to meet as fast as possible and have a date ")
            print("Now, please check Your_buddy.txt file in your folder and smile more and more")
            playsound.playsound("Dance.mp3")
        else:
            print("You played well, but lose the game")
            playsound.playsound("sad.mp3")
start()
