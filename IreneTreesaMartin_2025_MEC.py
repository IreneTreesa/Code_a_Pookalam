import turtle
import math

import time
time.sleep(5)

t= turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)


def circle(r,c):
    
    t.penup()
    t.goto(0,-r)
    t.pendown()
    t.begin_fill()
    t.color(c)
    t.circle(r)
    t.end_fill()
    
    

def squares(r,c): 
    
    s = r * math.sqrt(2) #required len of side
    t.hideturtle()
    
    
    
# Draw normal square
    t.penup()
    t.goto(-s/2, s/2)  # top-left of square
    t.setheading(0)    #turn right
    t.color(c)
    t.begin_fill()
    t.pendown()
    
    
    
    for _ in range(4): #drawing sq
        t.forward(s)
        t.right(90)
    t.end_fill()

# Draw tilted square
    s=r*(2**0.5) #req side
    t.penup()
    t.goto(0,-r)
    t.color(c)
    t.begin_fill()
    t.pendown()
    
    t.setheading(180) #left
    t.right(45)
    
    for _ in range(4): # draw sq
        
        t.forward(s)
        t.right(90)
    t.end_fill()
    t.penup()
    t.home()
    


def ring_of_circles(r1,r2,c): #r1-rad(big circle), r2-rad(small circle)
         
    t.home()
       
    circum=2*math.pi*r1  #circum(big circle)
    num_circles=int(circum/(2*r2)) #no. of s.circles needed
    
    
    for i in range(num_circles):
        t.penup()
        t.forward(r1)    # move outward from center
        t.pendown()
        t.begin_fill()
        t.color(c)
        t.circle(r2)
        t.end_fill()
        t.penup()
        t.backward(r1)   # go back to center
        t.right(360 / num_circles)  # turn for next 
        


def petals(r,c):
    
    for i in range(8):  # 8 petals
        angle = i * 45 +8  # spaces between squares
        t.penup()
        t.home()
        t.right(angle)
        t.pendown()

        # draw petal as two arcs
        t.begin_fill()
        t.color(c)
        for _ in range(2):
            t.circle(r, 60)  
            t.left(120)
        t.end_fill()

def petals1(r,c):
    for i in range(8):  # 8 petals
        angle = i * 45+ 30  # spaces between squares
        t.penup()
        t.home()
        t.right(angle)
        #t.forward(r)
        t.pendown()

        # draw petal as two arcs
        t.begin_fill()
        t.color(c)
        for _ in range(2):
            t.circle(r, 60)  
            t.left(120)
        t.end_fill()
        
    
    t.home()

def text():
    t.penup()
    t.goto(0,330)
    t.color('gold')
    t.write('Happy Onam !', align= 'center',font=('Lucida Handwriting',32,'bold'))
    t.goto(0,-360)
    t.write('Created by Irene Treesa Martin',align='center',font=('Segoe Script',18,'normal'))
    


     
ring_of_circles(300,25,'ivory1') 
circle(300,'SpringGreen4')
ring_of_circles(270,15,'DarkGoldenrod1')
circle(270,'DarkRed')

petals(270,'LightGoldenrod1')
squares(270,'red1')
petals1(270,'orange')

ring_of_circles(170,10,'LightGoldenrod1')
circle(170,'SpringGreen4')

squares(170,'orange') 
petals1(170,'OrangeRed') 


circle(100,'DarkRed')
squares(100,'LightGoldenrod1') 
petals1(100,'red')

ring_of_circles(40,10,'ivory1')
circle(40,'SpringGreen4')

ring_of_circles(20,5,'red')
squares(20,'gold')

text()

t.hideturtle()
turtle.done()

