from snake import Snake
from controller import Controller
from food import Food

class Player:
    
    def __init__(self, index: int, food: Food):
        self.index = index
        self.food = food
        self.snake = Snake()
        self.controller = Controller(index)

    def tick(self):
        self.controller.tick()
        self.snake.tick(self.controller, self.food)

        if (self.snake.collision):
            self.snake.reset()