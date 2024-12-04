from login import log_in
from add_books import add
from search import search
from delete import delete_book
from Display_list import display
from Update_inventory import update
from illustration import draw

def main():
    
    if log_in():
        while True:
            user = input("(A)dd\n(S)earch:\n(D)elete\n(L)ist_of_books\n(U)pdate\n(I)llustrate\n(E)xit ").capitalize()
            if user == "A":
                add()
            elif user == "S":
                search()
            
            elif user == "D":
                delete_book()

            elif user == "L":
                display()
            elif user == "U":
                update()
            elif user == "I":
                draw()


                
            elif user == "E":
                break
    
    else:
        print("Login failed. Exiting...")

main()
