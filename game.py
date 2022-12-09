import adafruit_nunchuk
from food import Food
from player import Player

class Game:

    def __init__(self):
        self.foods = []
        self.players: list[Player] = []

        for i in range(5):
            self.foods.append(Food())

    def add_player(self, nunchuck: adafruit_nunchuk.Nunchuk):
        self.players.append(Player(nunchuck))

    def tick(self):
        for player in self.players:
            player.tick(self.foods)
