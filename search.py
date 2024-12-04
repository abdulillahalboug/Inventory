def search():
    while True:
      
        with open("Book_inventory", "r") as f:
            inventory = [line.strip().split(", ") for line in f] #makes a list for comapring later

       
        found = False
        find = input("What book do you want to search for?\nEnter the ID or Name: ").strip()

        
        for book in inventory:
            
            if find == book[0] or find == book[1]: #compares the list
                print(f"Book found: ID = {book[0]}, Name = {book[1]}, Description = {book[2]}, inventory = {book[3]}") #prits out detials if correct 
                found = True
                break

        if not found:
            print("Book not found. Please try again.")

        
        while True:
            leave = input("Do you want to keep searching? (Y)es or (N)o: ").strip().lower() #loop to tey again
            if leave == "y":
                break  
            elif leave == "n":
                print("Exiting the search.")
                return  
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
if __name__ == "__main__":
    search()