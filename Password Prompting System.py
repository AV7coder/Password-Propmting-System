# Password Prompting System
while True:
    password = int(input("Enter Password: "))
    if password == 123: 
        print("ACCESS GRANTED")
        break # stops printing ACCESS GRANTED once you got it right
    else:
        print("ACCESS DENIED")    
        password = int(input("Enter Password: "))