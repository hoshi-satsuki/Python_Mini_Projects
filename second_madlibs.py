import string

#print string.ascii_uppercase

def word_in_pos(word, parts_of_speech):
    ##select uppercase letters
    new_word=""
    for elt in word:
        if elt in string.ascii_uppercase:
            new_word+=elt
    ##compare with part_of_speec
    if new_word in parts_of_speech:
        return new_word
    else:
        return None

#This function was given in the lecture.
#I do not use it since it does not deal well
#with the NOUN and PLURALNOUN situation
def word_in_pos2(word,parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(ml_string, parts_of_speech):
    ml_list=ml_string.split()
    replaced=[]
    for elt in ml_list:
        pos=word_in_pos(elt,parts_of_speech)
        if pos is not None:
            user_input=raw_input("Type in a "+pos+": ")
            elt=elt.replace(pos,user_input)
        replaced.append(elt)
        replaced2=" ".join(replaced)
    return replaced2


test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
parts_of_speech = ["PERSON","NOUN","PLURALNOUN","PLACE"]

#print word_in_pos(test_cases[0], parts_of_speech)
#print word_in_pos(test_cases[1], parts_of_speech)
#print word_in_pos(test_cases[2], parts_of_speech)
#print word_in_pos(test_cases[3], parts_of_speech)

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

print play_game(test_string, parts_of_speech)
