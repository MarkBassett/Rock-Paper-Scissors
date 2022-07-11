import random


class Game:
    play_game = True
    shapes = ['rock', 'paper', 'scissors']
    shapes_length = 0
    shapes_mid = 0

    def __int__(self):
        self.computer_move = None
        self.player_move = None
        self.message = ''
        self.player_wins
        self.player_name = ''
        self.player_score = 0

    def computers_move(self):
        self.computer_move = random.choice(Game.shapes)

    def player_setup(self):
        self.player_name = input('Enter your name: ')
        with open('rating.txt', 'r') as f:
            scores = f.read()
        scores = scores.split()
        if self.player_name in scores:
            self.player_score = int(scores[scores.index(self.player_name) + 1])
        else:
            self.player_score = 0
        print(f'Hello, {self.player_name}')
        user_shapes = input()
        if user_shapes:
            Game.shapes = user_shapes.split(',')
        Game.shapes_length = len(Game.shapes) - 1
        Game.shapes_mid = int(Game.shapes_length / 2)
        print("Okay, let's start")

    def player_input(self):
        self.player_move = input()
        if self.player_move == '!exit':
            self.message = 'Bye!'
            Game.play_game = False
        elif self.player_move == '!rating':
            self.message = f'Yor rating: {self.player_score}'
        elif self.player_move not in Game.shapes:
            self.message = 'Invalid input'
        else:
            index = Game.shapes.index(self.player_move)
            if Game.shapes.index(self.player_move) < Game.shapes_length:
                options = Game.shapes[index - Game.shapes_length:] + Game.shapes[:index]
            else:
                options = Game.shapes[:index]
            win = options[:Game.shapes_mid]
            loose = options[Game.shapes_mid:]
            self.computers_move()
            self.winner(loose, win)

    def winner(self, loose, win):
        if self.computer_move in loose:
            self.message = f'Well done. The computer chose {self.computer_move} and failed'
            self.player_score += 100
        elif self.computer_move in win:
            self.message = f'Sorry, but the computer chose {self.computer_move}'
        else:
            self.message = f'There is a draw ({self.computer_move})'
            self.player_score += 50


play = Game()
play.player_setup()
while play.play_game:
    play.player_input()
    print(play.message)