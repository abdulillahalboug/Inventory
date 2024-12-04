import turtle

def draw_hat_top():
    turtle.penup()
    turtle.goto(-25, 50) 
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("black")
    turtle.goto(0, 150)  
    turtle.goto(25, 50)  
    turtle.goto(-25, 50)  
    turtle.end_fill()
    
def draw_brim():
    turtle.penup()
    turtle.goto(-50, 50)  
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor("black")
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(10)
    turtle.end_fill()

def write_title_on_book(text):
    turtle.penup()
    turtle.goto(0, 190)  
    turtle.pendown()
    turtle.color("white")
    turtle.write(text, align="center", font=("Arial", 16, "bold"))  
    turtle.penup()


def draw_rectangle(x, y, width, height, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()


def draw_book():
   
    draw_rectangle(-100, -50, 200, 300, "brown")
   
    draw_rectangle(-120, -50, 20, 300, "darkred")

def draw_gun():
  
    turtle.penup()
    turtle.goto(-50, 0) 
    turtle.pendown()
    turtle.color("black")
    turtle.fillcolor("gray")
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(20)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-30, 50) 
    turtle.pendown()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(80)
        turtle.left(90)
        turtle.forward(15)
        turtle.left(90)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-50, 0)  
    turtle.pendown()
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(10, 180)  
    turtle.end_fill()

    
    turtle.penup()
    turtle.goto(-40, 15) 
    turtle.pendown()
    turtle.color("black")
    turtle.width(3)
    turtle.goto(-40, 5) 
    turtle.penup()


def draw_heart():
    turtle.penup()
    turtle.goto(0, 30)  
    turtle.pendown()
    turtle.color("red")
    turtle.fillcolor("red")
    turtle.begin_fill()
    
    
    turtle.left(50)
    turtle.forward(50)  
    turtle.circle(25, 180)  
    turtle.right(100)
    
    
    turtle.circle(25, 180)
    turtle.forward(50)
    
    turtle.end_fill()
    turtle.penup()


def exit_program():
    print("Returning to main program...")
    turtle.bye()  
    return  


def draw():
    while True:
       
        try:
            with open("Book_inventory", "r") as f:
                inventory = [line.strip().split(", ") for line in f]
        except FileNotFoundError:
            print("Error: 'Book_inventory' file not found.")
            return

    
        find = input("What book do you want to illustration?\nEnter the ID or Name (or press 'E' to return): ").strip()
        
        if find.lower() == "e":  
            return  

        found = False
        for book in inventory:
            if find == book[0] or find == book[1]:
                if book[2] == "magic":
                    draw_book()
                    write_title_on_book(book[1])
                    draw_brim()
                    draw_hat_top()
                    found = True
                    break
                elif book[2] == "action":
                    draw_book()
                    write_title_on_book(book[1])
                    draw_gun()
                    found = True
                    break
                elif book[2] == "romance":
                    draw_book()
                    write_title_on_book(book[1])
                    draw_heart()
                    found = True
                    break

        if not found:
            print("Book not found. Please try again.")

if __name__ == "__main__":
    turtle.listen()
    turtle.onkey(exit_program, "e")  
    draw()


"""I have three description that i can illlustrate which are
   Action
   Romance
   Magic"""