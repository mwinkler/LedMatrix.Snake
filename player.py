from snake import Snake
from controller import Controller
from food import Food

class Player:
    
    def __init__(self, number: int, food: Food):
        self.number = number
        self.food = food
        self.snake = Snake()
        self.controller = Controller()

    def tick(self):
        self.controller.tick()
        self.snake.tick(self.controller, self.food)

        if (self.snake.collision):
            self.snake.reset()