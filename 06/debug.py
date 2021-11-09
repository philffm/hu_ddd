import pandas as pd

# 1
# Not such a file or directory
# Opened VS code console in that folder
df = pd.read_csv("imdb.csv") #read in the datafile

# df["metascore"] = df["metascore"] / 10 #put the scores on the same scale 
df["Metascore"] = df["Metascore"] / 10 #put the scores on the same scale  
# Wrong naming
df["average"] = df["Metascore"] + df["imdbVotes"] / 2 #take the average of the scores
# test = df["Metascore"] + df["imdbVotes"] / 2 #take the average of the scores
# print(test)