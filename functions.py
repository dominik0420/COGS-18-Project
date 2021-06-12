"""A collection of function for doing my project."""

#require shuffle function from random library
from random import shuffle

#This is the rank dictionary.
ye_rankdic = {"Bronze": "Dude, you know nothing about Kanye",
              "Silver": "Okay mate you kinda know a bit about Kanye but you're still trash",
              "Gold": "Huh, nice work, but I believe you can do better. There's more to know",
              "Platinum": "Nice!!! You already know more than 57.1428% of Kanye fans",
              "Diamond!": "Holy smokes, you know more than 71.4286% of Kanye fans!",
              "Saint Pablo!!": "Yeah, you're lookin' at the church in the night sky, Wonderin' whether God's gonna say hi. God's gonna say hi now, you're the Saint Pablo",
              "Yeezus!!!": "You can fully sing 'I'm A God' now, cuz you are the one true Yeezus himself. You know more than every Kanye fan out there!!!"}


#A function that returns a rank for users based on their score
def rankcheck(rankdic, userscore):
    
    #turn the rankdictionary input into lists by separating keys and items
    a = list(rankdic.keys())
    b = list(rankdic.values())

    
    #if user score is in the range, returns the keys (the rank level) and the items (the description of the rank)
    if userscore < -18:
        print(str(a[0]) + "\n" + str(b[0]))
        
    elif userscore > -18 and userscore < -10:
        print(str(a[1]) + "\n" + str(b[1]))
        
    elif userscore > -10 and userscore < -3:
        print(str(a[2]) + "\n" + str(b[2]))
        
    elif userscore > -3 and userscore < 5:
        print(str(a[3]) + "\n" + str(b[3]))
        
    elif userscore > 5 and userscore < 12:
        print(str(a[4]) + "\n" + str(b[4]))
        
    elif userscore > 12 and userscore < 19:
        print(str(a[5]) + "\n" + str(b[5]))
        
    elif userscore > 19 and userscore <= 25:
        print(str(a[6]) + "\n" + str(b[6]))   

        
#a function that picks question, displays, and shows input for the user. 
def question_pick(qdatabase, score):
    
    #a loop counter
    counter = 0
    
    #Shuffle the entire database of the promptbook
    shuffle(qdatabase)
    
    #iterate through the promptbook
    for items in qdatabase:
        
        #print out the question for the user
        print(items.question)
        
        #create a list for answers by retrieving attributes of each item in the promptbook.
        answer_list = items.wrong + items.correct
        shuffle(answer_list)
        
        #use \n to break the answers in multiple lines and print the answer options for users
        print("A." + answer_list[0] + "\n" + "B." + answer_list[1] + "\n" + "C." + answer_list [2] + "\n" + "D." + answer_list[3])
        
        #counter += 1 each time the loop is ran
        counter += 1
    
        #create input
        user_answer = input()
        
        #check if the answer is correct
        if user_answer in items.correct:
            print("\n --- Nice work. Saint Pablo loves you <3. --- \n")
            score += 1
            
        #check if the answer is wrong and print a result
        else:
            print("\n --- Bruh, you got it wrong :( --- \n" + "\n" + "It is" + str(items.correct) + "! \n")
            score -= 1
        
        #stops the loop once it reaches 3, meaning that only 3 questions are displayed each time the trivia is ran. I would like to encourage the user to take the test multiple times to get a high rank
        if counter == 3:
            break
        
    #displays the score
    print("Your Score: " + str(score))
    
    #displays the rank and the rank description
    return(rankcheck(ye_rankdic, score))
    return(score)


                  