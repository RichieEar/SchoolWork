import turtle

def face():
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    t3 = turtle.Turtle()
    t4 = turtle.Turtle()
    t5 = turtle.Turtle()
    t6 = turtle.Turtle()

    def eyes(turtle, color, size, x, y):
        turtle.shape("turtle")
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x,y)
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()
        turtle.pendown()

    def draw_eyes_outline(turtle, size, x, y):
        turtle.shape("turtle")
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.circle(size)

    def nose(turtle, color, size, x, y):
        turtle.shape("turtle")
        turtle.penup()
        turtle.color(color)
        turtle.fillcolor(color)
        turtle.goto(x,y)
        turtle.begin_fill()
        turtle.circle(size)
        turtle.end_fill()
        turtle.pendown()

    def mouth(turtle, size, angle, x, y):
        turtle.shape("turtle")
        turtle.right(90)
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.circle(size, angle)

    '''def face(turtle, color, size, angle, x, y):
        eye(turtle, color, size, x, y)
        turtle.penup()
        turtle.bk(200)
        eye(turtle, color, size, x, y)'''
        
 
    eyes(t1, 'red', 50, 100, 100)
    draw_eyes_outline(t2, 50, 100, 100)
    eyes(t3, 'blue', 50, -100, 100)
    nose(t4, 'red', 25, 0, 0)
    draw_eyes_outline(t5, 25, 0, 0)
    mouth(t6, 100, 180, -100, -10)

face()
