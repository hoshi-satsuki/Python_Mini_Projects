# Lesson 3.3: Use Classes
# Mini-Project: Check Profanity

# Typos can be embarassing! Imagine how you'd feel if you
# accidentally sent your boss an email that said "I'll take
# a sh!t at it" instead of "I'll take a shot at it". Write
# a program that can detect curse words in a string of text.

# Use this space to describe your approach to the problem.
#
#
#
#

import urllib

def read_text():
    quotes=open("/home/satsuki/meins/IPND/Stage3/c_profanity_editor/movie_quotes.txt")
    contents=quotes.read()
    quotes.close()
    # print contents
    check_profanity(contents)

def check_profanity(text):
    connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output=connection.read()
    connection.close()
    if "true" in output:
        print "There is a profane word in the text."
    elif "false" in output:
        print "The document is fine."
    else:
        print "Could not scan document."
    
read_text()
