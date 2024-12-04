def delete_book():
    file_name = "Book_inventory"

    target = input("Enter the name or ID of the book to delete: ")

    with open(file_name, "r") as file:
        lines = file.readlines()

    filtered_lines = []
    for line in lines:
        fields = line.strip().split(", ")  #makes a list to comapre later

     
        if not (len(fields) > 1 and (fields[0] == target or fields[1] == target)): 
            filtered_lines.append(line)

    with open(file_name, "w") as file:
        for new_id, line in enumerate(filtered_lines, start=1): #keeps track on the ID and appends the new list after deleting
            fields = line.strip().split(", ")
            fields[0] = str(new_id)  
            file.write(", ".join(fields) + "\n")

    print(f"Book with name or ID '{target}' has been deleted (if it existed).")


if __name__ == "__main__":
    delete_book()
