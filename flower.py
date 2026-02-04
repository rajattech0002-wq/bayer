import turtle

def draw_petal(turtle_obj, radius, angle):
    """Draw a single petal"""
    for _ in range(2):
        turtle_obj.circle(radius, angle)
        turtle_obj.left(180 - angle)

def draw_flower():
    """Create and display a flower using turtle graphics"""
    # Setup the screen
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("white")
    
    # Create turtle object
    flower_turtle = turtle.Turtle()
    flower_turtle.speed(0)
    flower_turtle.pensize(2)
    
    # Draw stem
    flower_turtle.pencolor("green")
    flower_turtle.penup()
    flower_turtle.goto(0, -200)
    flower_turtle.pendown()
    flower_turtle.goto(0, 50)
    
    # Draw petals
    petal_colors = ["red", "orange", "yellow", "pink", "purple"]
    flower_turtle.penup()
    flower_turtle.goto(0, 50)
    flower_turtle.pendown()
    
    for i in range(5):
        flower_turtle.pencolor(petal_colors[i])
        draw_petal(flower_turtle, 50, 60)
        flower_turtle.penup()
        flower_turtle.goto(0, 50)
        flower_turtle.pendown()
        flower_turtle.left(72)  # 360 / 5 petals
    
    # Draw center (flower core)
    flower_turtle.pencolor("yellow")
    flower_turtle.penup()
    flower_turtle.goto(0, 50)
    flower_turtle.pendown()
    flower_turtle.begin_fill()
    flower_turtle.circle(15)
    flower_turtle.end_fill()
    
    flower_turtle.hideturtle()
    screen.mainloop()

if __name__ == "__main__":
    draw_flower()
