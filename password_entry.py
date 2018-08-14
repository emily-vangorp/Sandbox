"""Emily Van Gorp"""
MIN_LENGTH = 6
password = input("Password: ")
while len(password) < MIN_LENGTH:
    print("Too short.")
    password = input("Password: ")
for char in password:
    print('*', end='')
