"""Classes used throughout project"""
class QnA:
    
    #Specify instance-specific attributes. 
    def __init__(self, question, correct, wrong):
        
        #question attribute
        self.question = question
        
        #correct answer attribute
        self.correct = correct
        
        #wrong answer attribute
        self.wrong = wrong
        
        
#My Question base:
## I directly input the prompts into the qustion attribute, and have the rest either in the correct answer or wrong answer attribute. Wrong answer is made into a list which would be later unpacked to be offered as choices.
promptbook = [QnA("What is the first studio album ever released by Kanye West?", ["The College Drop Out"], ["Graduation", "My Beautiful Dark Twisted Fantasy", "ye"]), 
              QnA("How many studio albums did Kanye West released?", ["12"], ["11", "9", "8"]),
              QnA("Which of the following songs is not in the 2007 album 'Graduation'?", ["Power"], ["Stronger", "I Wonder", "Flashing Lights"]),
              QnA("Who did Kanye West married?", ["Kim Kardashian"], ["Psalm West", "Khloe Kardashian", "Kylie Jenner"]),
              QnA("Who did Kanye West worked with on the 'Kids See Ghost' group?", ["Kid Cudi"], ["Ty Dollar $ign", "PARTYNEXTDOOR", "Chief Keef"]),
              QnA("Which of the following album does not have Jay-Z featured?", ["Graduation"], ["My Beautiful Dark Twisted Fantasy", "Watch The Throne", "Late Registration"]),
              QnA("Which of the following songs does not have Rhianna featured?", ["Waves"], ["FourFiveSeconds", "Famous", "All of the Lights"]),
              QnA("Which of the following songs is not performed solo by Kanye West?", ["Ghost Town"], ["Yikes", "Heartless", "Closed On Sunday"]),
              QnA("Which of the following indie rock band worked with Kanye West the most?", ["Bon Iver"], ["Coldplay", "Maroon 5", "Radiohead"]),
              QnA("Which of the following artists is not featured in the 2018 EP 'ye'?", ["Travis Scott"], ["Kid Cudi", "070 Shake", "Nicki Minaj"]),
              QnA("Which of the following songs has the most featured artists?", ["The Morning"], ["Sin City", "Monster", "Waves"]),
              QnA("Which of the following albums is not produced by Kanye West?", ["Astroworld"], ["NASIR", "The Blueprint 3", "DAYTONA"]),
              QnA("WWhich of the following artists never worked with Kanye West?", ["J Cole"], ["Paul McCartney", "Adam Levine", "Travis Scott"]),
              QnA("Which album of Kanye West is never nominated for Grammy?", ["808s & Heartbreak"], ["Graduation", "My Beautiful Dark Twisted Fantasy", "Jesus Is King"]),
              QnA("Which of the following kids is not Kanye's child?", ["Loretta West"], ["Psalm West", "Saint West", "Chicago West"]),
              QnA("How many times is Kanye West nominated for Grammy?", ["70"], ["50", "10", "18"]),
              QnA("Which analog was used in '808s & Heartbreak'?", ["Roland Tr-808"], ["Roland TB-303", "Serum", "Moog"]),
              QnA("Who was sampled on 'I Wonder' in th 2007 album 'Graduation'? ", ["Labi Siffre"], ["Pastor T.L. Barrett", "Daft Punk", "Pondersora Twins Plus One"]),
              QnA("Which album has the least biblical reference?", ["808s & Hearbreaks"], ["Yeezus", "Gruadation", "Late Registration"]),
              QnA("Which of the following album tours used a tilted staage?", ["The Life of Pablo"], ["Yeezus", "My Beautiful Dark Twistd Fantasy", "Jesus Is King"]),
              QnA("Which city in China did Kanye go to for the exchange program?", ["Nanjing"], ["Beijing", "Shanghai", "Guangzhou"]),
              QnA("Which of the following songs is not produced by Mike Dean?", ["Bound 2"], ["Fade", "Power", "Hold My Liquor"]),
              QnA("Which of the following songs is implicit (does not include explicit swearing words)?", ["Heartless"], ["Hey Mama", "Hold My Liquor", "Yikes"]),
              QnA("How many samples are used in total in 'The Life of Pablo'?", ["44"], ["18", "24", "3"]),
              QnA("Which of the following producers never worked with Kanye West?", ["Jack Antonoff"], ["Mike Dean", "Noah Goldstein", "Justin Vernon"])]