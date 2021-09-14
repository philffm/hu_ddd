# create an empty list that will hold a dictionary
playlist = []

# create a function that has four parameters: title, artist, album, duration
def add(title, artist, album, duration, playing):
  song = {"title":title, "artist":artist, "album":album, "seconds":duration, "playing": playing}
  playlist.append(song)

def play(title):
  for song in playlist:
    if song["title"] == title:
      song["playing"] = True

def stop(title):
  for song in playlist:
    if song["title"] == title:
      song["playing"] = False

def length():
  seconds = 0
  for song in playlist:
    seconds = seconds + song["seconds"]
  return seconds

# create a function that adds these items to playlist
add("Teardrop", "Massive Attack", "Mezzanine", 294, False)
add("Enjoy the Ride", "Morcheeba", "Dive Deep", 244, False)

# change the value of playing to True
play("Teardrop")

# change the value of playing to False
stop("Teardrop")

# create a function that returns the sum of all the seconds in songs (use return for this function)
print(length())
