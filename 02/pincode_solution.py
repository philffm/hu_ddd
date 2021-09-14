pincode = 13378

# create a for-loop with a range of 99999
# print each number
# if the number matches pincode print "Cracked the code"
# use exit() to stop the loop

for i in range(99999):
  print(i)
  if i == pincode:
    print("cracked the code")    
    exit()