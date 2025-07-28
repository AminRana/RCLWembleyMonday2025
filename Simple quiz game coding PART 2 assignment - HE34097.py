#COM4302 - Computer Science Fundamentals
#Student Name: Araib Arif Gill
#SID: HE34097

#Importing the time module. This will contain time related functions and it is used to create delays, making the interaction smoother and giving user time to read the messages
import time

#Welcome the user
print("Welcome to Life in the UK - Simple Quiz Game!")
time.sleep(1)

#Chances
chances = 1
print("You will have",chances, "chance to answer correctly.\nPlease put the alphabet of the answer\n")
time.sleep(2)

#Score- initializing the value to 0
score = 0

#question 1
question_1 = print("1) What is the capital of England?\n(a) London\n(b) Paris\n(c) Madrid\n(d) Cardiff\n\n")
answer_1 = "a"
#The for loop iterates over a range defined by chances, allowing players to answer the question based on the number of chances allowed.
for i in range(chances):
    answer = input("Answer: ")  #prompts user for their answer
    if (answer.lower() == answer_1): #converts the user's input to lowercase to ensure case insensitivity.
        print("Correct! Good job.\n")
        score = score + 1   # if the answer is corret it will increase player's score.
        break
    else:
        print ("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is", answer_1, "\n\n")   #if the ans is incorrect, the program prints the corret answer after a slight pause.     
time.sleep (2)
               
#question 2
question_2 = print("2) Which nation of the United Kingdom is not a part of Great Britain?\n(a) England\n(b) Scotland\n(c) Wales\n(d) Northern Ireland\n\n")
answer_2 = "d"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_2):
        print("Correct! Good job.\n")
        score = score + 1
        break
    else:
        print ("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is", answer_2, "\n\n")
time.sleep (2)

#question 3
question_3 = print("3) Which city/town is not in the county of South Yorkshire?\n(a) Sheffield\n(b) Doncaster\n(c) Bradford\n(d) Barnsley\n\n")
answer_3 = "c"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_3):
        print("Correct! Good job.\n")
        score = score + 1
        break
    else:
        print ("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is", answer_3, "\n\n")
time.sleep (2)

#question 4
question_4 = print("4) What was the name of the British monarch who reigned from 1837 to 1901?\n(a) Queen Elizabeth 1\n(b) Queen Victoria\n(c) Queen Anne\n(d) Queen Charlotte\n\n")
answer_4 = "b"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_4):
        print("Correct! Good job.\n")
        score = score + 1
        break
    else:
        print ("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is", answer_4, "\n\n")
time.sleep (2)

#question 5
question_5 = print("5) Which king, who died in 1485 at the Battle of Bosworth Field, was re-buried at Leicester  Cathedral in 2015?\n(a) King James II\n(b) King Charles 1\n(c) King Richard III\n(d) King Henry VIII\n\n")
answer_5 = "c"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_5):
        print("Correct! Good job.\n")
        score = score + 1
        break
    else:
        print ("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is", answer_5, "\n\n")
time.sleep (2)

#question 6
question_6 = print("6) Which holiday is celebrated on the 25th of December in the UK?\n(a) Easter\n(b) Christmas\n(c) Halloween\n(d) Thanksgiving day\n\n")
answer_6 = "b"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_6):
        print("Correct! Good job.\n")
        score = score + 1
        break
    else:
        print ("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is", answer_6, "\n\n")
time.sleep (2)

#question 7
question_7 = print("7) What is the name of the UK's national flower?\n(a) Rose\n(b) Daffodil\n(c) Daisy\n(d) Sunflower\n\n")
answer_7 = "a"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_7):
        print("Correct! Good job.\n")
        score = score + 1
        break
    else:
        print ("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is", answer_7, "\n\n")
time.sleep (2)

#question 8
question_8 = print("8) What is the name of the British monarch as of 2023?\n(a) Queen Victoria\n(b) Queen Elizabeth II\n(c) King Charles III\n(d) Prince William\n\n")
answer_8 = "c"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_8):
        print("Correct! Good job.\n")
        score = score + 1
        break
    else:
        print ("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is", answer_8, "\n\n")
time.sleep (2)

#question 9
question_9 = print("9) Which famous clock tower is located at the north end of the Palace of Westminster in London?\n(a) Big Ben\n(b) Tower Bridge\n(c) The Shard\n(d) London Eye\n\n")
answer_9 = "a"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_9):
        print("Correct! Good job.\n")
        score = score + 1
        break
    else:
        print ("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is", answer_9, "\n\n")
time.sleep (2)

#question 10
question_10 = print("10) What is the name of the river that flows through London?\n(a) River Mersey\n(b) River Severn\n(c) River Clyde\n(d) River Thames\n\n")
answer_10 = "d"
for i in range(chances):
    answer = input("Answer: ")
    if (answer.lower() == answer_10):
        print("Correct! Good job.\n")
        score = score + 1
        break
    else:
        print ("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is", answer_10, "\n\n")
time.sleep (2)


#Print the score
while score >6 and score <= 10:   #setup conditions (these conditions provide feedback to the player based on their score at the end of the quiz.
    print ("Well done! Your score was", score)
    break
while score <= 6:
    print("Better luck next time! Your score was", score)
    break
#Goodbye
print ("Thank you for playing the Simple Quiz!")
