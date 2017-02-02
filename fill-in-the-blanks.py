#Basic rules of the game.
#The player starts with a given number of points. (POINTS)
#The player chooses between three levels.
#After this a text with blanks is diplayed according to the level chosen.
#The game is played by looping through the blanks until either all blanks are filled or the player has no more points left:
#   The player gets prompted with a blank to be filled in and has to guess on the answer.
#   If the players player gets the answer right the game is continued with the next blank.
#   If the player gets the answer wrong he looses one try and one point. After a given number of TRIES the game
#   continues with the next blank.
#Finally the players gets informed about his result and the full text with all the blanks filled in is displayed.





#These are global variables
POINTS=10 #number of points available to the player at the beginning, decreases
          #by one whenever the player makes a mistake
TRIES=3   #number of tries the player has per question
MAX_BLANKS=5 #Maximum number of blanks in one level
index=1
ENUM_LIST=[]    #serves as a helper variable to avoid typing
while index<=MAX_BLANKS:
    ENUM_LIST.append(' __'+str(index)+'__ ')
    index+=1
                                                                                          #is sufficiently long to support the number of blanks



#Function initializes the displayed text ('displayed_text') and the correct answers ('answers') for each level.
def initialize_text():
    displayed_text=["Anger is never without reason, but seldom with a"+ENUM_LIST[0]+"one. - Benjamin Franklin\n"+\
                    "All"+ENUM_LIST[1]+"jobs absorb and degrade the mind. - Aristotle\n"+\
                    "I haven't committed a crime. What I did was fail to comply with the"+ENUM_LIST[2]+". - David Dinkins\n"+\
                    "The"+ENUM_LIST[3]+"is expanding to meet the needs of the expanding"+ENUM_LIST[3]+". - unknown\n"+\
                    "I have no special"+ENUM_LIST[4]+". I am only passionately curious. - Albert Einstein",
                    "A"+ENUM_LIST[0]+"saved is a"+ENUM_LIST[0]+"earned. - Benjamin Franklin\n"+\
                    "We do not inherit the"+ENUM_LIST[1]+"from our ancestors, we borrow it from our children. - Native American\n"+\
                    "The man who moves a mountain begins by carrying away small"+ENUM_LIST[2]+". - Confucius\n"+\
                    "Two things are infinite: the"+ENUM_LIST[3]+"and human stupidity; and I'm not sure about the"+ENUM_LIST[3]+". - Albert Einstein\n"+\
                    "Twenty years from now you will be more disappointed by the things that you didn't"+ENUM_LIST[4]+"than by the ones you did"+ENUM_LIST[4]+". - unknown",
                    "An investment in"+ENUM_LIST[0]+"always pays the best interest. - Benjamin Franklin\n"+\
                    "Before God we are all equally"+ENUM_LIST[1]+"– and equally foolish. - Albert Einstein\n"+\
                    "There are only two ways to live your life. One is as though nothing is a"+ENUM_LIST[2]+". The other is as though everything is a"+ENUM_LIST[2]+". - Albert Einstein\n"+\
                    "The way to get started is to quit"+ENUM_LIST[3]+"and begin doing. - Walt Disney\n"+\
                    "The only thing worse than being"+ENUM_LIST[4]+"about is not being"+ENUM_LIST[4]+"about. - Oscar Wilde"]
    answers=[['good','paid','law','bureaucracy','talents'],['penny','earth','stones','universe','do'],['knowledge','wise','miracle','talking','talked']]
    return displayed_text,answers


#Function to let the player choose his/her level.
#Input: None
#Output: level in {'e','m','h'} (easy,medium,hard)
#Functions asks the player to choose a level and returns 'e' (easy),'m' (medium) or 'h' (hard) respectively
#If the player enters an invalid input the player will be asked again.
def choose_level():
    level_chosen=False
    while not level_chosen:
        print "There are three levels:"
        print "           Easy   (funny quotes),"
        print "           Medium (popular quotes),"
        print "           Hard   (wisdom quotes)."
        possible_input=['e','m','h']
        level=raw_input("Please choose a level by typing 'e' or 'm' or 'h': ")
        if level not in possible_input:
            print "This was not a correct input. "
        else:
            level_chosen=True
            return level

#Function to go through each blank.
#Input: "no_points": Number of points the player has
#       "prompt": The text to prompt the player for the answer (includes the number of the blank)
#       "correct": The correct answer for the blank.
#Output: "no_points": The number of points the player has left after the blank
#Function prompts the user guess on the answer for the blank.
#Function loops through tries until one of the following occurs: (Player got it right) or (Number of tries reaches TRIES) or (player has no more points left).

def each_question(no_points,prompt,correct):
    no_tries=0
    while no_points>0 and no_tries<TRIES:
        user_input=raw_input(prompt+": ")
        if user_input==correct:
            print "You did it! You currently have "+str(no_points)+" points."
            print
            break
        else:
            no_tries+=1
            no_points-=1
            print "That was wrong. You currently have "+str(no_points)+" points."
            print
    return no_points




#Function to display the results
#Input: "disp": Complete text to the be displayed with all the blanks filled out
#       "no_points": number of points the player has at the end of the game
#Output: None
#Function displayes whether the player has won or lost the game. In case he/she won, it displayes the number of points.
#In any case it displays the full text with all the blanks filled in.
def game_ending(disp,no_points):
    if no_points>0:
        print "Congratulations! You won the game with "+str(no_points)+" points. :)"
        print
        print disp
    else:
        print "Sorry, you have lost the game! :("
        print "The complete answer would have been:"
        print
        print disp


#Function to loop through the blanks.
#Input: "disp": text to be displayed
#       "ans": list of answers
#Output: None
#Function loops through the blanks. For each blank it displays the text calls the function "each_question" and passes it the number of
#of points the player has ("no_points"), the text to be prompted (showing the number of the blank) ("ENUM_LIST[k]") and
#the correct answer ("correct"). After this function it replaces the blank with the appropriate answer.
#The loop ends when all the blanks are filled or the number of points the player has left reaches zero.
#In case the player has lost the game it replaces the left blanks with the appropriate answers. It then calls the function
#"game ending", passing it the text to display ("disp") and the number of points the player has ("no_points").
def play_game(disp,ans):
    k=0
    no_points=POINTS
    print "You are starting with "+str(no_points)+" points."
    print
    for correct in ans:
        print disp
        print
        no_points=each_question(no_points,ENUM_LIST[k],correct)
        disp=disp.replace(ENUM_LIST[k]," "+correct+" ")
        k+=1
        if no_points<=0:
            break
    if no_points<=0:
        j=k
        while j<len(ans):
            disp=disp.replace(ENUM_LIST[j]," "+ans[j]+" ")
            j+=1
    game_ending(disp,no_points)
    

                
                

#Function to set up the game.
#Input: "level" in {'e','m','h'} (easy,medium,hard)
#       "displayed_text": list of text for levels easy, medium, hard
#       "answers"       : list of list of answers for levels easy, medium,hard
#Output: None
#Function selects the appropriate element of "displayed_text" and "answers" according to the "level". It then starts
#the game by calling the function "play_game" and passing it the above elements.
#Furthermore it explains the game to the player.
def setup_game(level,displayed_text,answers):
    if level=='e':
        text='funny'
        no=0
    if level=='m':
        text='popular'
        no=1
    if level=='h':
        text='wisdom'
        no=2
    print "You will be given some"+text+" quotes. Try and fill in the blanks."
    print "You will start with a number of "+str(POINTS)+" points. Each mistake you make will cost you one point. If your number of points reaches 0 you have lost the game."
    print "Good luck!"
    print
    print
    play_game(displayed_text[no],answers[no])

    
    
       

#Main program:
#   -initializes the variables "displayed_text" and "answers" using function "initialize_text".
#       "displayed_text": list of text for levels easy, medium, hard
#       "answers"       : list of list of answers for levels easy, medium,hard
#   -greets player
#   -lets player choose his level using function "choose_level()", which returns
#       "level" in {'e','m','h'} (easy,medium,hard)
#   -starts the game calling function "setup_game" passing it "level", "displayed_text" and "answers"
[displayed_text,answers]=initialize_text()
print "Welcome to the game of quotes!"
level=choose_level()
setup_game(level,displayed_text,answers)





