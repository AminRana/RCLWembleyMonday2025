def simple_quiz():
    score = 0
    
    print("Welcome to the Simple Quiz!Test your wine wisdom whit my free quiz.Get a question wrong?Taka a sip.. Answer with A, B, or C.\n")
    
    # Question 1

    print("1.From which fruits is wine typically made ?")
    print("A) Appels")
    print("B) Grapes")
    print("C) Pears")
    answer1 = input("Your answer: ").upper()
    if answer1 == "B":
        print("Well done!\n")
        score += 1
    else:
        print("Sorry! The correct answer is B) Grapes.\n")
    
    # Question 2
    print("2 What is used to ferment wine.'?")
    print("A) Bacteria")
    print("B) Yeast")
    print("C) Mold")
    answer2 = input("Your answer: ").upper()
    if answer2 == "B":
        print("Correct!\n")
        score += 1
    else:
        print("Cheers,now you need to have a glass of Wine! The correct answer is B) Yeast.\n")
    
    # Question 3
    print("3 What is the standard amount in most wine bottles. ?")
    print("A) 500 ml")
    print("B) 750 ml")
    print("C) 1 litter")
    answer3 = input("Your answer: ").upper()
    if answer3 == "B":
        print("Correct!\n")
        score += 1
    else:
        print("Wrong!Take a sip.. The correct answer is b) 750 ml.\n")
    

    
    # Question 4
    print("4.How many wine bottles are there in a case.?")
    print("A) 4")
    print("B) 6")
    print("C) 12")
    answer1 = input("Your answer: ").upper()
    if answer1 == "c":
        print("Well done!\n")
        score += 1
    else:
        print("Sorry! The correct answer is B) 12.\n")

     # Question 5
    print("5.Prosecco is produced in which Italian region.?")
    print("A) Tuscany")
    print("B) Veneto")
    print("C) Piedmant")
    answer1 = input("Your answer: ").upper()
    if answer1 == "B":
        print("Well done!\n")
        score += 1
    else:
        print("Sorry! The correct answer is B) Veneto.\n")

     # Question 6
    print("6. Which country has the largest total area of vineyards?.")
    print("A) France")
    print("B) Spain")
    print("C) Italy")
    answer1 = input("Your answer: ").upper()
    if answer1 == "B":
        print("Well done!Cheers\n")
        score += 1
    else:
        print("Sorry! The correct answer is B) Spain.\n")

      # Question 7
    print("7 What is the most popular wine varietal in the world?. ")
    print("A) Merlot")
    print("B) Caberne Sauvignon")
    print("C) Pinot Noir")
    answer1 = input("Your answer: ").upper()
    if answer1 == "B":
        print("Well done!Cheers\n")
        score += 1
    else:
        print("Sorry! The correct answer is B) Caberne Sauvignon.\n")   

      # Question 8
    print("8 Which kind of wine is often paired with fish?.")
    print("A) Red winr-Shiraz")
    print("B) Ddessert wine-Moscatel")
    print("C)Dry white wine- chardonny")
    answer1 = input("Your answer: ").upper()
    if answer1 == "C":
        print("Hio,hip hooray\n")
        score += 1
    else:
        print("Sorry! The correct answer is C) Chardonny.\n")
        

       # Question 9
    print("9 White wine can be produced from which colour grapes ? . ")
    print("A) White grapes")
    print("B) Red grapes")
    print("C) All colors")
    answer1 = input("Your answer: ").upper()
    if answer1 == "C":
        print("Well done!Cheers\n")
        score += 1
    else:
        print("Sorry! The correct answer is C) All colors.\n")

          # Question 10
    print("10 What do we call a knowledgeable and trained wine professional who often works in fine restaurants?  . ")
    print("A) A connoiseur")
    print("B) A cicerone")
    print("C) A sommelier")
    answer1 = input("Your answer: ").upper()
    if answer1 == "C":
        print("Well done!Cheers\n")
        score += 1
    else:
        print("Sorry! The correct answer is C) A sommelier.\n")  
      
    print(f"🎉 **Quiz Complete!** Your score: {score}/10")
    if score >= 9:
        print("🌟 **Wine Expert!** You know your stuff!")
    elif score >= 5:
        print("🍾 **Wine Enthusiast!** Good knowledge!")
    else:
        print("🍇 **Keep Tasting!** Try again!")
      
   

simple_quiz()
