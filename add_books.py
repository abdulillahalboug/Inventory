def add():
    while True:
        book = input("What is the name of the book? ")
        while book == "":
            book = input("You need to enter a book: ") #checks to see if you typed anything

        description = input("What is the description? ")
        while description == "":
            description = input("You need to enter a description: ")

        amount = input("How many books? ")
        while amount == "": #checks to see if you typed anything
            amount = input("You need to enter an amount: ")

       
        with open("Book_inventory", "r") as f:
            n = sum(1 for line in f)  
            store_information = f"{n + 1}, {book}, {description}, {amount}\n"  #Adds the details you worte including keeping up with what ID it is

        
        with open("Book_inventory", "a") as f:
            f.write(store_information)

        print(f"Book '{book}' added successfully!")

      
        while True:
            choice = input("Do you want to add another book? (Y)es or (N)o: ").lower() #checks to see if you want to add or exit
            if choice == "y":
                break  
            elif choice == "n":
                print("Exiting the add function.")
                return  
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


if __name__ == "__main__":
    add()
