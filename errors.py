"""This bad boy shows error handling.  The while loop will keep it going
until it receives a good answer.  The try's are checking for a Type error or a
Value Error ie numbnuts enters a letter"""

def number_returner():
    """Same as what it says above"""
    waiting = True
    while waiting:
        try: #try will try this block of code
            result = int(input("Gimme a number son "))

        except TypeError: #if the above gives a type error, print this
                          #(Won't happen, anything entered is converted already)
            print("What did you even enter?")
            continue

        except ValueError: #catches a ValueError.  Could happen if letter/sym
            print("That ain't a number son, try again")
            continue

        else: #if input works, return this and break
            print("Good answer")
            waiting = False
            #break
            #the waiting variable replaces the need for a break statement

        finally: #always runs no matter what
            print(".............................")
    print("Your number is " + str(result))

number_returner()
