

favoriteThings = []
favoriteThingsCount = 0
favoriteThingsLimit = 3


def addThing():
    newThing=input('Input your favourite stuff ▶️ ')
    newThing = newThing.lower()
    
    if newThing == 'offenbach':
        print('Wrong answer')
    else:
        favoriteThings.append(newThing)
    global favoriteThingsCount
    favoriteThingsCount+=1


while favoriteThingsCount < favoriteThingsLimit:
    addThing()
    print(favoriteThingsLimit - favoriteThingsCount,'left')
    if favoriteThingsCount == favoriteThingsLimit:
        print(favoriteThings, 'your most favourite thing is',favoriteThings[0])
