import numpy as np
import matplotlib.pyplot as plt 
import keyboard
from random import seed
from random import randint
import matplotlib as mpl

class Snake:
    def __init__(self):
        self.x=25
        self.y=25
        self.positions = list()
        self.positions.append([self.x,self.y-2])
        self.positions.append([self.x,self.y-1])
        self.positions.append([self.x,self.y])
        self.game_over = False
        
  
    def move(self, action):   #1 = up 2= down 3=left 4=right

        if (action==1):
            self.y=self.y+1
            self.positions.append([self.x,self.y])
        if(action==2):
            self.y=self.y-1
            self.positions.append([self.x,self.y])
        if(action==3):
            self.x=self.x-1
            self.positions.append([self.x,self.y])
        if(action==4):          
            self.x=self.x+1
            self.positions.append([self.x,self.y])
        if(self.y>100 or self.y<0 or self.x>100 or self.x<0):
            self.game_over= True
   
   
    def checkFood(self, apple_pos_x, apple_pos_y):
        if(self.x == apple_pos_x and self.y == apple_pos_y):           
            
            return 1
        else: 
            self.positions.pop(0)
            return 0
    
    def checkLife(self):
        if(self.y>50 or self.y<0 or self.x>50 or self.x<0):
            return 1
        for i in range(len(positions)-2):
            if(positions[len(positions)-1][0]==positions[i][0] and positions[len(positions)-1][1]==positions[i][1]):
                return 1
        if(positions[len(positions)-1][0]==positions[len(positions)-2][0] and positions[len(positions)-1][1]==positions[len(positions)-2][1]):
                return 2  


    

def spawn_apple_x(positions):
    correct_positions = True
    apple_pos_x = 30
  
    while(correct_positions): 
        apple_pos_x = randint(0, 50)
        for i in range(len(positions)):
            if(positions[i][0]!=apple_pos_x):
                return apple_pos_x
                correct_positions=False
            


def spawn_apple_y(positions):
    correct_positions = True
    apple_pos_y = 20
  
    while(correct_positions): 
        apple_pos_y = randint(0, 50)
        for i in range(len(positions)):
            if(positions[i][1]!=apple_pos_y):
                
                return apple_pos_y
                correct_positions=False
            


def init_plot():
    plt.figure()
    plt.xlim(0,50)
    plt.ylim(0,50)
    plt.title("snake")
    plt.rcParams['axes.facecolor'] = 'b'
    plt.close()

    

def plot_grid(positions,apple_pos_x,apple_pos_y):
    score = len(positions)-3
    
    mpl.rcParams['toolbar'] = 'None'
    fig = plt.figure()
    fig.patch.set_facecolor('black')
    plt.clf()
     
    
            
    plt.xlim(0,50)
    plt.ylim(0,50)
   
    plt.rcParams['text.color'] = 'white'

    plt.title("Snake "+"score : "+str(score))
    plt.axis('off')
    
    
    
    plt.scatter(apple_pos_x,apple_pos_y)
    for i in range(len(positions)):
        plt.scatter(positions[i][0], positions[i][1])
      
   
    plt.draw()
    plt.pause(0.01)
    plt.close()

def keyListener():
   
    if keyboard.is_pressed(keyboard.KEY_UP):
        return 1
    
    if keyboard.is_pressed(keyboard.KEY_DOWN):
        return 2
    
    if keyboard.is_pressed('left'):
        return 3

    if keyboard.is_pressed('right'):
        return 4
    return 0


if __name__ == "__main__":
    init_plot()
    snake = Snake()
    action = 1
    game_over = False
    positions = snake.positions
    apple_pos_x = spawn_apple_x(positions)
    apple_pos_y = spawn_apple_y(positions)
    while(not game_over):
        temp_action = keyListener()
        if (temp_action != 0):
            action1= keyListener()
            action = temp_action  
        life = snake.checkLife() 
        snake.move(action)

        positions = snake.positions
        food = snake.checkFood(apple_pos_x, apple_pos_y)
        if(food==1):
                apple_pos_x = spawn_apple_x(positions)
                apple_pos_y = spawn_apple_y(positions)
        if(life==1):
            
            break
        

        plot_grid(positions,apple_pos_x,apple_pos_y)

