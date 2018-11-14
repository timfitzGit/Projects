
# initialize global variables used in your code
import simplegui
import random
blr100 = False
blr1000 = False
intTarget = 0
intNumOfGuesses = 0

# define event handlers for control panel
def CheckGuess(strGuess):
    global blr100, blr1000
    
    if not blr100 and not blr1000:
        print "Select the game type first!"
    else:
        if strGuess == "":
            print "You must type in a number"
        else:
            intGuess = int(strGuess)
            if blr100:
                if intGuess <0 or intGuess > 99:
                    print "You must enter a number between 0 and 99"
                else:
                    get_input(intGuess)
            if blr1000:
                if intGuess <0 or intGuess > 999:
                    print "You must enter a number between 0 and 999"
                else:
                    get_input(intGuess)                

         #   print "You selected " + strGuess
    
    
def range100():
    # button that changes range to range [0,100) and restarts
    global blr100, blr1000, intTarget
    blr100 = True
    blr1000 = False
    intTarget = random.randint(0, 100)
   # print "Target is " + str(intTarget)
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    global blr100, blr1000, intTarget
    blr1000 = True
    blr100 = False
    intTarget = random.randint(0, 1000)
    
def get_input(guess):
    # main game logic goes here	
    global intNumOfGuesses, intTarget, blr100, blr1000

    intNumOfGuesses = intNumOfGuesses + 1
    print "This is guess number " + str(intNumOfGuesses) + " for you"
    
    if guess == intTarget:
        strHiLo = "CORRECT !!"
        print "Your guess of " +str(guess) + " is " + strHiLo
        print "** Game Over **"
        blr100 = False
        blr1000 = False
        intNumOfGuesses = 0
        
    elif guess < intTarget:
        strHiLo = "Low"
        print "Your guess of " +str(guess) + " is " + strHiLo
    elif guess > intTarget:
        strHiLo = "High"
        print "Your guess of " +str(guess) + " is " + strHiLo
        
   # print "The target is " + str(intTarget)

    
# create frame
frm = simplegui.create_frame("Guess the Number", 300, 400)
strGuess = frm.add_input("Enter your guess", CheckGuess, 110)
frm.add_button("Play 0 to 100", range100, 110)
frm.add_button("Play 0 to 1000", range1000, 110)


# register event handlers for control elements


# start frame
frm.start

