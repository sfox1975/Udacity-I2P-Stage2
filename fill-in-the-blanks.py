# IPND Stage 2 Final Project

#Stephen Fox
#April 11, 2016


#My quiz consists of four functions:

#1. welcome: lets the user select difficulty (easy, medium, hard) and then passes to 'game' function
#2. game: prompts the user to answer the quiz, using 'answer_check' to verify answers
#3. answer_check: checks the user's responses versus the correct answers
#4. repeat: allows the user to run the program again, if desired.

#For each difficulty level, the quiz data consist of a string and 2 lists, as shown below.
#The string contains the quiz. The first list contains the question prompts (e.g. __1__)
#and the second list contains the answers to each question:

quiz_easy = "A sequence of characters between quotes is called a __1__ in python. Parts of a __1__ can \
be extracted by using __2__.  For example, to return the first letter in the __1__ 'udacity', one can type \
'udacity'[__3__]. To return the last letter in 'udacity', one can type 'udacity[-1]. Even a number can be \
turned into a __1__, by using __4__(n), where n is the number in question."

questions_easy = ["__1__","__2__","__3__","__4__"]
answers_easy = ["string","indexing","0","str"]

quiz_medium = "In contrast to a string, which is a sequence of characters, a __1__ is a sequence of \
characters, strings, or numbers. A __1__ can be 'mutated' or changed, whereas strings cannot be mutated.\
There are several useful built in operations that can be performed on a __1__. The operation .__2__ \
adds to the end of a __1__. Using __3__(__1__ name) provides the 'length' or number of elements in a __1__. \
Python is an intuitive language. For example, __4__ (or not __4__) can be used to check if a value is in a \
given __1__, returning true (false) if the value is in the __1__ and false (true) if it is not."

questions_medium = ["__1__","__2__","__3__","__4__"]
answers_medium = ["list","append","len","in"]

quiz_hard = """Using strings and lists is a key part of programming in python. To split a string into a list, \
the .__1__ function can be used. The format is as follows: string.__1__(separator). If the separator is left \
blank, the string is split on the single __2__ character. If the separator is not left blank, the string is split \
on the character specified in the separator. To convert a list into a string, the .__3__ function can be used. \
If one wanted to separate each list element in the new string by a single space, the following format is used: \
" ".__3__(list). In many programs, it is useful to query the user for input. The __4__ function serves this \
purpose in python."""

questions_hard = ["__1__","__2__","__3__","__4__"]
answers_hard = ["split","space","join","raw_input"]

#answer_check function checks if the user's answer to a given quiz question is correct, by comparing the
#user answer to the answers stored in the answers lists, returning 'True' (if answer is right) or 'False'
#(if answer is wrong).

def answer_check(user_answer,answer):

    if user_answer == answer:
        print '\n' + "Correct!" + '\n'
        return True
    else:
        print '\n' + "Incorrect. Please try again."
        return False

#game function checks for remaining questions in the quiz by comparing the quiz string to the questions list.
#If a blank question is found in the quiz string, the user is prompted to answer the question and then the answer
#is checked using the answer_check function. If the answer is correct, the game function continues to loop through
#the quiz, looking for the next unanswered question. If the answer is incorrect, the function repeats the same
#question again. Once all questions have been successfully answered, the function returns the repeat function, which
#lets the user opt to repeat the quiz or not.

def game(quiz,question,answer):

    print '\n' + quiz

    i = 0
    while i < len(question):
        if question[i] in quiz:
            user_answer = raw_input('\n' + "What should be substituted in for " + question[i] + "?")
            if answer_check(user_answer,answer[i]) == True:
                quiz = quiz.replace(question[i],user_answer)
                print quiz
            else:
                i -= 1
        i += 1

    print '\n' + "Game completed. Well done!" + '\n'

    return repeat()

#The repeat function lets the user repeat the quiz if desired, thus letting them try all three difficulty levels
#without having to restart the program each time. If the user opts to repeat the quiz, the function returns the
#welcome function, thereby starting the program again.

def repeat():

    user_input = raw_input("Would you like to play again (type yes or no):")

    if user_input == "yes":
        return welcome()
    elif user_input == "no":
        print '\n' + "Thanks for playing. Goodbye!" + '\n'
    else:
        print '\n' + "Invalid input" + '\n'
        return repeat()

#The welcome function provides the first page for the user, letting them choose the quiz difficulty level
#and based on their response, returns the game function using the relevant quiz data (easy, medium or difficult)
#as the inputs to the game function.

def welcome():

    print " -------------------------------------------------"
    print "| Welome to the Introduction to Programming Quiz! |"
    print "|                                                 |"
    print "| By Stephen Fox                                  |"
    print " -------------------------------------------------" + '\n'

    user_input = raw_input("Please pick a difficulty level (type easy, medium, or hard):")

    if user_input == "easy":
        return game(quiz_easy,questions_easy,answers_easy)
    elif user_input == "medium":
        return game(quiz_medium,questions_medium,answers_medium)
    elif user_input == "hard":
        return game(quiz_hard,questions_hard,answers_hard)
    else:
        print '\n' + "Invalid input"
        return welcome()

welcome()