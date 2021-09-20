# Weekly Assignment 02
# Student name: 1690236
# Student numner: Phil Wornath

# you are going to create a shopping list for a supermarket

import time

dialogWaitingTime = 1.5
# adding funky colors
colorStart = '\x1b[6;30;42m'
colorEnd = '\x1b[0m'

def giveDialogue(message):
    print(colorStart, message, colorEnd) 
    time.sleep(dialogWaitingTime)


# create an empty shopping list
menuItems = ['1️⃣ ✏️ Add product ', '2️⃣ 📝 Show list','3️⃣ 💰 Total value', '4️⃣🔎 Find product','5️⃣✍️ Change product qty',  '🔟 🗑 Clear list']


shoppingList = {'productname': ['banana','apple'],
                'quantity': [2,3],
                'price': [4,2]}

# ✅ create a function that adds a product with the following fields: productname, quantity, price per one item
def addProduct(productname, quantity, price):
    global shoppingList
    shoppingList['productname'].append(productname)
    shoppingList['quantity'].append(quantity)
    shoppingList['price'].append(price)
    successMessage = '✅ Successfully added', quantity, 'pieces of', productname, 'to your list'
    giveDialogue(successMessage)
    menu()

# ✅  create function that calculates the total price of the shopping list
def calcTotalValue():
    global shoppingList
    totalValue = 0
    i = len(shoppingList['quantity'])-1
    
    while i >= 0:
        itemValue = shoppingList['quantity'][i]*shoppingList['price'][i]
        totalValue += itemValue
        i -= 1

    # didn't work - but why 🤷🏽‍♂️
    # for i in shoppingList['quantity']:
    #     itemValue = shoppingList['quantity'][i]*shoppingList['price'][i]
    #     totalValue += itemValue
    
    # totalValue = sum(shoppingList['price'])
    return totalValue

# ✅ create a function that clears the shopping list 
def clearList():
    global shoppingList
    shoppingList = []
    print('🗑 All of your secret groceries have been deleted 🥷')
    time.sleep(dialogWaitingTime)
    menu()

# ✅ create a function that checks if a certain item is already on the list. 
def findProduct(desiredProduct):
    if desiredProduct in shoppingList['productname']:
        print(desiredProduct, 'is already there 😎')
        time.sleep(dialogWaitingTime)
        menu()
    elif desiredProduct not in shoppingList['productname']:
        print(desiredProduct, 'is NOT here yet 🙀. ')
        if input('Shall I add it to the list? [y/n]') == 'y':
            quantity = int(input('2️⃣ Input quantity 👉 '))
            price = int(input('3️⃣ Input Price 👉 '))
            addProduct(desiredProduct, quantity, price)
        else:
            menu()

# ✅ create a function that changes the quantity of an existing product on the list

def changeQty():
  indexNr = 1
  for i in shoppingList['productname']:
      print(indexNr,':', i)
      indexNr += 1

  desiredProduct = int(input('🔎 Which product do you want to change the qty of? 👉'))
  currentQty = shoppingList['quantity'][desiredProduct-1]
  selectedProd = shoppingList['productname'][desiredProduct-1]
  print('The current quantity of', selectedProd , 'is', currentQty)
  newQty = input('New amount 👉 ')
  shoppingList['quantity'][desiredProduct-1] = newQty
  print('✅ Amount of', selectedProd , 'changed to', newQty)
  time.sleep(dialogWaitingTime)
  menu()
      


def menu():
    print('Welcome to your shopping list! ✏️')
    
    for menuItem in menuItems:
        print(menuItem)
    
    menuItem = int(input('Your selection: '))

    if menuItem == 1:
        productname = input('1️⃣ Input product 👉 ')
        quantity = int(input('2️⃣ Input quantity 👉 '))
        price = int(input('3️⃣ Input Price 👉 '))
        addProduct(productname, quantity, price)
        # if (input('Add another one? [y/n]') == 'y'):
        menu()
    if menuItem == 2:
        print(shoppingList)
        menu()
        # print('Test')
    if menuItem == 3:
        print('The total grocery value is ₿', calcTotalValue())
        menu()
        
    if menuItem == 4:
        desiredProduct = input('🔎 Which product are you looking for? 👉')
        findProduct(desiredProduct)
    
    if menuItem == 5:
        changeQty()
        
    if menuItem == 10:
        clearList()
        menu()
        # print('Test')

        
menu()
    








