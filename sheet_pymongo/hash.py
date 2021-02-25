import bcrypt

passwd = b'1234' # Enter your password for generate hash 

salt = bcrypt.gensalt() # generated salt
hashed = bcrypt.hashpw(passwd, salt) # Set hashed for store in database Hashed = salt + hash 

def show():
    print(salt)
    print(hashed)

def check():
    if bcrypt.checkpw(passwd, hashed):
        print("match")
    else:
        print("does not match")

case = int(input("case 1 : show hashed & salt \ncase 2 : check password \nInput case : "))

if(case == 1):
    show()
elif(case == 2):
    check()