# Weekly Assignment 04
# Student name: 1690236
# Student numner: Phil Wornath


import pandas as pd

import os


#In this exercise, we're going to create a program that allows us do 
#cross-cultural cinematic research. A tool that prints the percentage of movie
#descriptions containing a certain word (scraped from Wikipedia),
#for different cultures. First we will practice a little with Pandas.
#Then, follow the steps to create the program.

#As a challenge, you can also ignore these steps and code it without help.

#1. First, download the movie_plots.csv file from Canvas and open it

csv_location = os.path.relpath('./datasets/movie_plots.csv')
df = pd.read_csv(csv_location) 
df2 = []

 
def dummy():
    print("Hello")

   

f02 = "2. Let's inspect the data. Display the first rows and get the summary (.info)"
def two():
    print(df.info)


f03 = "3. Print out the number of movies for each Origin/Ethnicity"
def three():
    selection = df['Origin/Ethnicity'].value_counts()
    print(selection)


f04 = "4. Subsetting: select only the rows with Bollywood movies"
def four():
    selection = df.loc[df['Plot'].str.contains('bollywood', case = False)]
    print(selection)

f05 = "5. Subsetting: select only the rows with Turkish movies released after 2000"
def five():
    selection = df.loc[(df['Origin/Ethnicity'].str.contains('Turkish', case = False)) & (df['Release Year']>=2000)]
    print(selection)


f06 = "6. Subsetting: create a new df with only Title, Release Year, Origin/Ethnicity, Plot"
#Use this new df for the rest of the analysis
def six():
    global df2
    df2 = df.loc[df['Release Year'],['Title','Origin/Ethnicity', 'Plot']]
    print(df2)

f07 = "7. Change the column names to Title, Year, Origin, Plot"
def seven():
    global df2
    df2 = df2.rename(columns = {'Origin/Ethnicity':'Origin'})
    print(df2)


f08 = '8. Create a new column "kimono" that is True if the Plot contains the word "kimono"'
#and false if not (tip: find a suitable string method).
#Tip: use Pandas .astype(int) to convert the resulting Boolean in 0 or 1.
def eight():
    selection = df.loc[(df['Origin/Ethnicity'].str.contains('Turkish', case = False)) & (df['Release Year']>=2000)]
    print(selection)


f09 = '9. Using your new column, pd.groupby() and another Pandas function, count the number of movies'
#with "kimono" in the plot, for the different origins.
def nine():
    selection = 0
    print(selection)

f10 = '10. Using your earlier code, create a function add_word_present() with one argument (word)'
def ten():

    selection = 0
    print(selection)

def add_word_present(word):
    print("I shouldn't be doing this at 11pm 😶‍🌫️ - will have a look tomorrow")


#11. Write another function compare_origins() with one argument (word), that:
#1. adds a column to your data frame (simply call your earlier function)
#2. prints the proportion of movies for different origins containing that word   

# def compare_origins(word):

# f11 = '11. adds a column to your data frame / prints the proportion of movies'
# def eleven():
#     selection = 0
#     print(selection)
    
# f12 = '12. Using your earlier code, create a function add_word_present() with one argument (word)'
# def twelve():
#     selection = 0
#     print(selection)
    


#that adds a column df[word] with a 1 if the word occurs in the plot,
#and 0 if not.
#Extra challenge: make sure that it's not counted if it's inside another word.


#12. We need one more tweak: to really compare different cultures,
#we need to account for the fact that the total number of movies is not the same.
#Write another, better function that calculates a percentage rather than a count.
#If you need a hint, see line 75.
#Also sort the result so that the percentage is descending.
#Finally, make it user-friendly: print the word and what the numbers mean


#You're done! Try out your function and paste your most interesting result
#as a comment
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Hint: note that df.groupby(["Origin"])[word].count() will get you the
# number of movies, grouped by origin.




menu_items = ['👋 Main menu - what do we want to do?',f02, f03, f04, f05, f06, f07, f08, f09, f10]

def menu():
    for item in menu_items:
        print(item)
    menu_select = int(input("Select option 👉"))
    if menu_select == 2:
        two()
        menu()
    if menu_select == 3:
        three()
        menu()
    if menu_select == 4:
        four()
        menu()
    if menu_select == 5:
        five()
        menu()
    if menu_select == 6:
        six()
        menu()
    if menu_select == 7:
        seven()
        menu()
    if menu_select == 8:
        eight()
        menu()
    if menu_select == 9:
        nine()
        menu()
    if menu_select == 10:
        ten()
        menu()
    # if menu_select == 11:
    #     eleven()
    # if menu_select == 12:
    #     twelve()


def init():
    menu()

init()
