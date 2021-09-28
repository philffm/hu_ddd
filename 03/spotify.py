# Weekly Assignment 03
# Student name: 1690236
# Student numner: Phil Wornath

# Note: while this assignment supports you in the creation and testing of functions, it will not mount up to a working system with an interface where the user can make selections. If you are up for the challenge we dare you to create one!

import json
import time

# import os
# os.chdir('/Users/phil/dev/hu_ddd/03/')


# Global declarations

dialogWaitingTime = 1.5
# adding funky colors
colorStart = '\x1b[6;30;42m'
colorEnd = '\x1b[0m'

loggedin = False
loggedinUser = None

app_name = 'Spotispy'
app_icon = '🎸'

playlist = []
users = []
songs = []


menuItems = ['1️⃣ ✏️ 🔑 Login ', '2️⃣ Register']
menuItemsLoggedIn = [ '1️⃣ 👶 Add Family member','2️⃣ 🎸 Add Song To Playlist', '🔟 🗑 Log off']

def open_file(file_name):
    # filename = './' + filename
    with open (file_name,'r') as file_content:
        file_content = json.load(file_content)
        print(file_content)
        return file_content 


def save_file(array, file_name):
    with open (file_name, 'w') as file_content:
        json.dump (array, file_content)        
       
def giveDialogue(message):
    print(colorStart, message, colorEnd) 
    time.sleep(dialogWaitingTime)


def addSong(artist, album, song):
    newSong = {"artist": artist, "album": album, "song": song}
    playlist.append(newSong)

# Make a function that counts the number of users and prints it
def countx(whatever):
    countx = len(whatever)
    return countx

def showPlaylist():
    for s in playlist:
        print(s["song"], "by", s["artist"],"found on",s["album"])

def playSong(songtitle):
    for s in playlist:
        if(songtitle == s["song"]):
            print("Currently playing", s["song"],"by",s["artist"])


def search_db (db,key,input_value):
 return list(filter(lambda x:x[key]==input_value,db))



def grantAccess(u):
    global loggedin 
    global loggedinUser 

    loggedin = True
    loggedinUser = u

    print("Hey, welcome", u, "to", app_icon, app_name, ". Have a sunny day 😎")
    menu()

# ✅ Make a function where a user with the role "owner" can add a new user with the role "family member". The owner has to be logged in to do this.

def add_family():
    global loggedinUser
    
    if search_db(users,'user',loggedinUser)[0]['role'] == 'owner':
        print('you have 2 family members left')
        user = input('username for family member please')
        password = input('password please')
        users.append({'user': user, 'password': password, 'role': 'family member'})
        save_file(users,'users.json')
        successMessage = '✅ Successfully added', user, 'to your family'
        giveDialogue(successMessage)

    else:
        featureUnavailable()

# ✅ Make a function where a user can add a song to the playlist. The user has to be logged in. If you are feeling adventurous, you can also add the name of the user that added the song to the playlist as an extra field.

def add_playlist():

    # for song in songs:
    #     print(song)

    song = input('song please 👉 ')
    addsong = search_db(songs,'song',song)
    playlist.append(addsong)
    save_file(playlist,'playlist.json')
    successMessage = '✅ Successfully added', song, 'to your playlist'
    giveDialogue(successMessage)   
    

def rejectUser(u):
    print("⛔️ Sorry, " + u + ". No way either you or your password exists. Try again!!1")
    menu()

def featureComingSoon():
    print("👶 This feature is coming soon")
    menu()

def featureUnavailable():
    print("⛔️ Sorry, This feature is not availabile")
    menu()

# ✅ Make a function where a user can log in (hint: look at the code from last week)

def authUser():
    
    currentUser = input("📧 Hey, what's your username?" + "\n")
    # Check if indicated user is valid
    # If user found in dictionary, give password prompt - otherwise reject user
    if  search_db(users,'user',currentUser):
        currentPass = input("🔑 Password please..." + "\n")
        # If validated email ID matches with indicated and validated password, grant access
        if  search_db(users,'user',currentUser)[0]['password'] == currentPass: 
                grantAccess(currentUser)
    else:
        rejectUser(currentUser)



    

def menu():
    global loggedin 
    global loggedinUser
    if (loggedin == True):
        print(*menuItemsLoggedIn, sep = '\n')
        menuItem = input ('Your selection ')
        if menuItem == '1':
            add_family()

        if menuItem == '2':
            add_playlist()

        # if menuItem == '3':
        #     menu()


        if menuItem == '10':
            loggedin = False;
            loggedinUser = None;
            print("⛔️ Logging out...")
            menu()

    elif (loggedin == False):
        print(*menuItems, sep = '\n')
        menuItem = input ('Your selection ')
        # Get page according to menu selection
        if menuItem == '1':
            authUser()
        elif menuItem == '2':
            # regUser()
            featureUnavailable()
        

# deprecated
# def openPlaylist():
#     with open("songs.json") as json_file:
#         data = json.load(json_file)
#         return data

# def savePlaylist():
#     with open("songs.json", "w") as outfile:
#         json.dump(playlist, outfile)



#✅ Make a function that opens users.json    

playlist = open_file('songs.json')
users = open_file('users.json')
songs = open_file('songs.json')

print('Welcome to',app_icon,app_name)
print('__________________')
print('About us', '|', 'Careers', '|', countx(users), 'happy', app_name, 'users' )

menu()



