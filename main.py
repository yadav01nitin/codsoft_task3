import random

lower="abcdefghijklmnopqrstuvwxyz"
upper=lower.upper()
numbers="0123456789"
symbols="~`!@#$%^&*()_+{}|:<>?,./;'"
all=(lower+upper+numbers+symbols)

length=int(input("Enter the length of the password: "))
password=""

for i in range(length):
 password+=random.choice(all)

print("Your new password is: ",password)



