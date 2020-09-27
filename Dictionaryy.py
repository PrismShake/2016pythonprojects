from hashlib import*


user = {}
#creates an encrypted password
def hash(password):
	sha256(password.encode('utf-8')).hexdigest()
	 
	# The above will give you a hash of MYSTRING

#login function
print("New Account!")
username = input("What's your username?")
password = input(" Enter password")

user[username] = hash(password)
print(user)

print("\n\n Let's Log in")
username = input("Username?")
password = input("Password")

while user[username] != hash(password): 
	password = input("Wrong Password")
print("You're in")