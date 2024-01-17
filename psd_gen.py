import random
char_set="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$%^&*_"
n=int(input("enter the password length you want: "))
password=""
for i in range(0,n):
    password+=random.choice(char_set)
print(f"password: {password}")