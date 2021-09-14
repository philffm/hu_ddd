# go to https://peppergeek.com/hot-sauce-scoville-scale/
# create a dictionary based on the data you see on the page

sauces = [
  {"brand": "Frank’s RedHot Sauce", "shu": 450},
  {"brand": "Tabasco Hot Sauce", "shu": 2500},
  {"brand": "Cholula Hot Sauce", "shu": 3600},
  {"brand": "Dawson’s Original Hot Sauce", "shu": 82000},
  {"brand": "Da Bomb Beyond Insanity", "shu": 135000},
  {"brand": "Dingo Widow Maker", "shu": 682000},
  {"brand": "Dragon In The Clouds", "shu": 1000000},
  {"brand": "Mad Dog 357 Gold Edition", "shu": 1000000},
  {"brand": "The Last Dab Triple X", "shu": 2000000},
  {"brand": "Satan’s Blood", "shu": 800000},
  {"brand": "Mad Dog 357 Plutonium No.9", "shu": 9000000},

]

# print the list of sauces as follows:
# 1 Frank’s RedHot Sauce 450 SHU
# 2 Tabasco Hot Sauce 2500 SHU
# 3 ...
# let the number be published dynamically

i = 1
for sauce in sauces:
  name = sauce["brand"]
  shu = sauce["shu"]
  print(i,name,shu)
  i = i + 1

# print the list of sauces with a SHU of 1000000 or higher
for sauce in sauces:
  name = sauce["brand"]
  shu = sauce["shu"]
  if shu >= 1000000:
    print(name,shu)