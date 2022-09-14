from turtle import Turtle

class StateLabel(Turtle):
    
    def __init__(self):

        super().__init__()

        self.hideturtle()
        self.penup()


    def write_and_locate(self, x, y, answer):

       
        self.goto(x, y)
        self.write(f"{answer}", align = 'center', font = ('Arial', 8, 'normal'))
        
