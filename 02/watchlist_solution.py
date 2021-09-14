# tip: check https://www.askpython.com/python/list/python-list for some basic operators

watch_list = []

# add 5 YouTube video titles to the watch list
watch_list.append("video 1")
watch_list.append("video 2")
watch_list.append("video 3")
watch_list.append("video 4")
watch_list.append("video 5")

# print the first video with "now playing: xxx" and the second video with "next video xxx"
print('Now playing:',watch_list[0]," Next video:",watch_list[1])

# print the 5 YouTube videos (for-loop)
for video in watch_list:
  print(video)

# change the 3rd video with another video
watch_list[2] = "New video"

# print the number of videos in the list
watch_list_length = len(watch_list)
print("Total videos in list:",watch_list_length)

# delete the last video (dynamically)
watch_list.pop()

# print the number of videos in the list
watch_list_length = len(watch_list)
print("Total videos in list:", watch_list_length)

# clear the list
watch_list.clear()

# print the number of videos in the list
watch_list_length = len(watch_list)
print("Total videos in list:",watch_list_length)