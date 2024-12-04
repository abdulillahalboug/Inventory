def update():
    while True:
        file_name = "Book_inventory"
        
        while True:  #checks to see what you want to change
            change = name()
            text = ""
            fix = ""
            if change == "Q":
                text = "Quantity"
                fix =3
                break
            elif change == "D":
                fix = 2
                text = "Description"
                break
            elif change == "N":
                text = "Name"
                fix = 1
                break
            else:
                print(f"{change} is invalid")


            

        with open(file_name, "r") as f:

            inventory = [line.strip().split(", ") for line in f] #makes list
            while True:
                target = input(f"\nEnter the name or ID of the book to change the {text}: ").strip().lower()
                found = False  

                for line in inventory:
                    if line[0].strip() == target or line[1].strip().lower() == target: #compares
                        print(f"Match found: ID = {line[0]}, Name = {line[1]}, Description = {line[2]}, inventory = {line[3]},\n")
                        found = True
                        break  
                
                if found:
                    break 

                leave = input("There's no such item.\nPress (L) to leave or any other key to try again: ").capitalize() #in case its not there or you wrote it wrong
                if leave == "L":
                    break
            
            


            num = input(f"Enter to the change {text} ") #depening on what you change its going to change the varuiable you picked at the beginning
            n = 0


            for line in inventory:
                if line[0] == str(target) or line[1].strip().lower() == target.strip().lower(): #compares then updates the new varuible
                    inventory[n][fix] = num
                    print("Book updated successfully!")
                n += 1

        with open(file_name, "w") as fx:
            for items in inventory:
                fx.write(", ".join(items) + "\n") #writes everthing back 
        while True:
            done = input("are you done? (Y)es or (N)o: ").capitalize()

            if done == "N":
                print("\n")
                break
            elif done == "Y":
                return
            else:
                print("click yes or no") #checks if you want to continue or not

def name():
    change = input("What do you want to change?\n(Q)uantity, (D)escription, or (N)ame: ").capitalize()
    return change
if __name__ == "__main__":
    update()
