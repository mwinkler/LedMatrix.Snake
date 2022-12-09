import adafruit_nunchuk
from snake import Snake
from controller import Controller
from food import Food

class Player:
    
    def __init__(self, nunchuck: adafruit_nunchuk.Nunchuk, food: Food):
        self.food = food
        self.snake = Snake()
        self.controller = Controller(nunchuck)

    def tick(self):
        self.controller.tick()
        self.snake.tick(self.controller, self.food)

        if (self.snake.collision):
            self.snake.reset()