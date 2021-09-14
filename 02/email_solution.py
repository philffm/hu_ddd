name = "Erik"
lastname = "Hekman"
domain = "http://www.hu.nl"
password = "w00t1337"

# clean up name and lastname with .lower()
# use .replace() and change http://www. with nothing
name = name.lower()
lastname = lastname.lower()
domain = domain.replace("http://www.", "")

# create a variable called email based on name, lastname, domain
email = name + "." + lastname + "@" + domain

# now that the account is "created" display the email
# ask the user for the password
# check if the password are correct, using a while-loop. If the user is correct display it if not continue to ask
password_input = input("What is the secret password? ")
while password_input != password:
  password_input = input("What is the secret password? ")

print("You are now logged in!")