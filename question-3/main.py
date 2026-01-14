import turtle

def get_valid_inputs():
    """
    Get and validate user inputs.
    """
    try:
        sides = int(input("Enter the number of sides: "))
        length = float(input("Enter the side length: "))
        depth = int(input("Enter the recursion depth: "))
    except ValueError:
        print("Invalid input: Please enter numbers only.")
        return None

    if sides < 3:
        print("Number of sides must be at least 3.")
        return None
    if length <= 0:
        print("Side length must be greater than 0.")
        return None
    if depth < 0:
        print("Recursion depth must be 0 or greater.")
        return None
    if depth > 6:
        print("Warning: Depth > 6 may be slow.")

    return sides, length, depth


def draw_recursive_edge(t, length, depth):
    """
    Draw a single edge using recursive inward indentation.
    """
    # Draws a straight line
    if depth == 0:
        t.forward(length)
    else:
        # Divides the edge into three equal segments
        segment_length = length / 3
        
        # And draws the first segment
        draw_recursive_edge(t, segment_length, depth - 1)
        
        # Create the inward indentation
        t.right(60)
        draw_recursive_edge(t, segment_length, depth - 1)
        
        t.left(120)
        draw_recursive_edge(t, segment_length, depth - 1)
        
        t.right(60)
        
        # And draws the final segment
        draw_recursive_edge(t, segment_length, depth - 1)

def main():
    sides,length,depth =get_valid_inputs()

    # Setting up the turtle screen
    screen = turtle.Screen()
    screen.title("HIT137 Assignment 2 - Q3 Recursive Pattern")
    screen.bgcolor("white")
    
    # Creating it's pen, speed and color
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.color("black")
    # Roughly centers the drawing
    t.penup()
    t.goto(-length / 2, length / 2)
    t.pendown()
    
    # Calculating external angle
    exterior_angle = 360 / sides
    
    # Drawing each edge using recursion
    for _ in range(sides):
        draw_recursive_edge(t, length, depth)
        t.right(exterior_angle)

    print("Successfully drew the pattern.")
    screen.exitonclick()


if __name__ == "__main__":
    main()