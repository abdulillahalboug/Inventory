def name_password():
    Name = input("Enter your Name: ")
    password = input("Enter your password: ") #your inputs
    return Name, password


def log():
    h = []
    

    with open("credentials.txt", "r") as f:
        for line in f:
            h.append(line.strip().split(", "))

    
    attempts = 0
    
    while attempts < 3: #checks your attempts then closes if its more then 3
       
        Name, password = name_password()

       
        user_found = False  
        

        for user in h:
            if Name == user[0]: 
                user_found = True  
                if password == user[1]:  #checks if its correct
                    print("Log in successfully")
                    return True
                else:
                    print("Password is wrong.")
                    attempts += 1
                    break

        if not user_found:  
            print("Name is wrong.")
            attempts += 1
        
        print(f"Attempt {attempts}/3\n")

    print("You are locked out due to too many failed attempts.")
    return False
 


def log_in():
    log()

def log_in():
    return log()