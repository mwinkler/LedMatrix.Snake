from food import Food
from player import Player

class Game:

    def __init__(self):
        self.food = Food()
        self.players: list[Player] = []

    def add_player(self):
        self.players.append(Player(len(self.players), self.food))

    def tick(self):
        for player in self.players:
            player.tick()