def display():

    with open("Book_inventory", "r") as f:
            inventory = [line.strip().split(", ") for line in f] #makes list

            for book in inventory:
                  print(f"ID = {book[0]}, Name = {book[1]}, Description = {book[2]}, inventory = {book[3]},\n") #displays whats in the list

    print("All books has been displayed")

            

if __name__ == "__main__":

    display()
    