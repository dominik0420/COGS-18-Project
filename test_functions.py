"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from my_module.classes import promptbook
##
##

def direct_test():

    #test to make sure the trivia runs with the correct database and make sure it runs normally
    assert len(promptbook) == 25
    assert type(promptbook) == list
    assert score == None
    


def rank_test():
    
    #i copied the rankcheck function here. I changed the name and also the print() to return(), to make sure it returns string, and hence the original function will definitely print out a string (but the print() type would still be NoneType. This test is to make sure the correct outcome is produced. 
    def testrankcheck(rankdic, userscore):
    
        #turn the rankdictionary input into lists by separating keys and items
        a = list(rankdic.keys())
        b = list(rankdic.values())

        #if user score is in the range, returns the keys (the rank level) and the items (the description of the rank)
    
        #bronze
        if userscore < -18:
            return(str(a[0]) + "\n" + str(b[0]))
    
        #silver
        elif userscore > -18 and userscore < -10:
            return(str(a[1]) + "\n" + str(b[1]))
    
        #goldd
        elif userscore > -10 and userscore < -3:
            return(str(a[2]) + "\n" + str(b[2]))
    
        #plat
        elif userscore > -3 and userscore < 5:
            return(str(a[3]) + "\n" + str(b[3]))
    
        #diamond
        elif userscore > 5 and userscore < 12:
            return(str(a[4]) + "\n" + str(b[4]))
        
        #saint pablo
        elif userscore > 12 and userscore < 19:
            return(str(a[5]) + "\n" + str(b[5]))
        
        #yeezus
        elif userscore > 19 and userscore <= 25:
            return(str(a[6]) + "\n" + str(b[6]))  
    
    #to assert the outcome is correct for bronze
    assert (testrankcheck(ye_rankdic, -22)) == 'Bronze\nDude, you know nothing about Kanye'
    
    #to assert the outcome is correct for silver
    assert (testrankcheck(ye_rankdic, -15)) == "Silver\nOkay mate you kinda know a bit about Kanye but you're still trash"
    
    #to assert the outcome is correct for gold
    assert (testrankcheck(ye_rankdic, -8)) == "Gold\nHuh, nice work, but I believe you can do better. There's more to know"
    
    #to assert the outcome is correct for platinum
    assert (testrankcheck(ye_rankdic, 3)) == 'Platinum\nNice!!! You already know more than 57.1428% of Kanye fans'
    
    #to assert the outcome is correct for diamond
    assert (testrankcheck(ye_rankdic, 8)) == 'Diamond!\nHoly smokes, you know more than 71.4286% of Kanye fans!'
    
    #to assert the outcome is correct for saint pablo
    assert (testrankcheck(ye_rankdic, 13)) == "Saint Pablo!!\nYeah, you're lookin' at the church in the night sky, Wonderin' whether God's gonna say hi. God's gonna say hi now, you're the Saint Pablo"
    
    #to assert the outcome is correct for yeezus
    assert (testrankcheck(ye_rankdic, 22)) == "Yeezus!!!\nYou can fully sing 'I'm A God' now, cuz you are the one true Yeezus himself. You know more than every Kanye fan out there!!!"
    
    
    
    



                 
    