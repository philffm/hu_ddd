# Weekly Assignment 01
# Student name: 1690236
# Student numner: Phil Wornath

# Work in progress  🚧 (Partitially working)
# - Seen deadline on Canvas too late (No Email notifications?) 
# - Wanted to save time through recycling code from the coding assignment but should've started from scratch
# - Busy with moving / finding a place to stay (the biggest problem)
# - 1st free day for a while 
# - Please check on GitHub later

from unicodedata import name
import datetime
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
currentYear = date.year

# Global declarations
loggedin = False
loggedinUser = None
currentSDG = None

your_social_media_app_name = 'SustainableMe'


menuItems = ['1️⃣ 🛎 Login', '2️⃣ 📝 New user']
menuItemsLoggedIn = ['1️⃣👤 Profile', '2️⃣⛔️ Logout']

sustainabilityGoals = ["Goal 1. End poverty in all its forms everywhere",
"Goal 2. End hunger, achieve food security and improved nutrition and promote sustainable agriculture",
"Goal 3. Ensure healthy lives and promote well-being for all at all ages",
"Goal 4. Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all",
"Goal 5. Achieve gender equality and empower all women and girls",
"Goal 6. Ensure availability and sustainable management of water and sanitation for all",
"Goal 7. Ensure access to affordable, reliable, sustainable and modern energy for all",
"Goal 8. Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all",
"Goal 9. Build resilient infrastructure, promote inclusive and sustainable industrialization and foster innovation",
"Goal 10. Reduce inequality within and among countries",
"Goal 11. Make cities and human settlements inclusive, safe, resilient and sustainable",
"Goal 12. Ensure sustainable consumption and production patterns",
"Goal 13. Take urgent action to combat climate change and its impacts [n 10]",
"Goal 14. Conserve and sustainably use the oceans, seas and marine resources for sustainable development",
"Goal 15. Protect, restore and promote sustainable use of terrestrial ecosystems, sustainably manage forests, combat desertification, and halt and reverse land degradation and halt biodiversity loss",
"Goal 16. Promote peaceful and inclusive societies for sustainable development, provide access to justice for all and build effective, accountable and inclusive institutions at all levels",
"Goal 17. Strengthen the means of implementation and revitalize the Global Partnership for Sustainable Development"]

def menu():
    if (loggedin == True):
        print(*menuItemsLoggedIn, sep = '\n')
        menuItem = input ('Your selection ')
        if menuItem == '1':
            # giveUser(loggedinUser)
            checkFriendRequest()
        if menuItem == '2':
            # giveUser(loggedinUser)
            checkFriendRequest()

        
        
    elif (loggedin == False):
        print(*menuItems, sep = '\n')
        menuItem = input ('Your selection ')
        # Get page according to menu selection
        if menuItem == '1':
            authUser()
        elif menuItem == '2':
            regUser()
    


usersDB = {
    1: {"First name": "Boris", "Last name": "Borissov", "E-Mail": "boris@borissov.com", "Password": "IceCreamSandwich101", "Year": 2002, "SDG": 1},
    2: {"First name": "Daria", "Last name": "Abc", "E-Mail": "daria@abcconsulting.com", "Password": "IceCreamSandwich2000", "Year": 2002, "SDG": 1},
    3: {"First name": "Emma", "Last name": "van Westerdijk", "E-Mail": "emma@abcconsulting.com", "Password": "password", "Year": 2002, "SDG": 1}
}

def checkDB(i, searchInput, searchKey):
    while i < len(usersDB)+1:
        if searchInput == usersDB[i][searchKey]:
            return i
        else:
            i = i+1
    rejectUser(searchInput)


def giveUser(u):

    currentSDG = checkDB(1, u,"SDG")
    print(u, currentSDG)


def regUser():

    # firstname = input("What is your first name?")
    # lastname = input("What is your last name?")
    # email = input("What is your email?")
    # password = input("What is your password?")
    year = int(input("What is your year of birth?"))
    print("Wow, you are", date.year - year, "years old")

# --- STEP 2: Adding bias --- #
# Look at your variables and use an if-statement to create a label
# A very simple one could be age. If a user is 18+ the variable "safe_content" would be set to True.


# Using the age for now to identify boomers

    if (year <= 1970):
        sdg = 0
        print("Ok boomer, I think you should take care of the following sustaiability goal:",sustainabilityGoals[sdg])
    elif (year >= 1970):
        sdg = 1
        print("You are young and live by the sea? What about",sustainabilityGoals[sdg])



    # usersDB.add(1,firstname)
    # usersDB.add(2,lastname)
    # usersDB.add(3,email)
    # usersDB.add(4,password)
    # usersDB.add(5,year)
    # usersDB.add(6,sdg)
    # # doesn't work yet


    menu()


    # usersDB.append(firstname,lastname,email,password,year,sdg)


# --- STEP 1: Getting the data --- #
# ✅ Create a welcome message welcoming the user using the included your_social_media_app_name variable
# ✅ Ask the user for a username, password, year of birth, and any other relevant information for your social media app
# While doing so think of the bias your variables might enable
# Calculate the age using the year of birth and create an extra variable age
# Use input() for this and store each data type in a seperate variable


# --- STEP 6: Security measures --- #
# Let the user login using a if-statement
# The login only has to work once
# Display if the user successfully logged in or not


def authUser():
    
    currentUser = input("📧 Hey, what's your email?" + "\n")
    # Check if indicated email is valid
    validUser = checkDB(1, currentUser,"E-Mail")

    # If email found in dictionary, give password prompt - otherwise reject user
    if checkDB(validUser, currentUser, "E-Mail") == validUser:
        currentPass = input("🔑 Password please..." + "\n")

    # If validated email ID matches with indicated and validated password, grant access
        if checkDB(validUser, currentPass, "Password") == validUser:
            grantAccess(currentUser)
        else:
            rejectUser(currentUser)
    
    else:
        rejectUser()
        


def grantAccess(u):
    global loggedin 
    global loggedinUser 

    loggedin = True
    loggedinUser = u

    print("Hey, welcome", u, "to", your_social_media_app_name, ". Have a sunny day 😎")
    menu()
    

def rejectUser(u):
    print("⛔️ Sorry, " + u + ". No way either you or your password exists. Try again!!1")
    menu()








# --- STEP 4: Adding a friend --- #
# Nothing worse than a lecturer wanting to become your friend. 
# Ask the user if the your_new_friend can become their friend
# Use an if-statement to either display "Friend request accepted" or "Friend request declined"


def checkFriendRequest():
    your_new_friend = "Erik"

    if not your_new_friend:
        print("Helaas pindakaas, no new friends here!")
    else:
        print('🛎 You have 1️⃣ NEW FRIEND request from', your_new_friend)
        friendDecicion  = input("You want to accept? (y / n)")

        if friendDecicion == 'y':
            print('✅ Accepted! You are now a friend of', your_new_friend, 'good luck!')
            menu()


        


# --- STEP 5: Adding content --- #
# Ask the user to write a short content message (use a variable)
# Display the message and ask if the user wants to publish the message
# Use an if-statement to either display "Message posted" or "Message deleted"


menu()


