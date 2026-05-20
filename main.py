import random
available_choices = ['r', 'p', 's']
class Player:
    def __init__(self, score):
        self.score = score

class Computer(Player):
    def __init__(self, score):
        super().__init__(score)
    def move(self):
        return random.choice(available_choices)

class User(Player):
    def __init__(self, score):
        super().__init__(score)
    def move(self):
        available_choices = ['r', 'p', 's']
        choice = input("Rock, paper or scissors [r/p/s]? ").lower()
        while choice not in available_choices:
            choice = input("Invalid choice. Please enter 'r', 'p', or 's'.")
        return choice


class Game:
    OUTCOMES = {('s', 's'): 0, ('p', 'p'): 0, ('r', 'r'): 0, # tie
                ('r', 'p'): -1, ('p', 's'): -1, ('s', 'r'): -1, # human player loses
                ('p', 'r'): 1, ('s', 'p'): 1, ('r', 's'): 1} # human player wins

    def __init__(self, rounds):
        self.rounds = rounds
        self.player1 = User(score=0)
        self.player2 = Computer(score=0)


    def play(self):
        for i in range(self.rounds):
            self.playround()
        self.final_result()

    def playround(self):
        human_choice = self.player1.move()
        computer_choice = self.player2.move()
        outcome = self.OUTCOMES[(human_choice, computer_choice)]
        self.round_result(outcome)

    def round_result(self,outcome):
        if outcome == 0:
            print('ROUND IS DRAW!!')
        elif outcome == -1:
            print ('COMPUTER WINS ROUND!!')
            self.player2.score += 1
        else:
            print ('USER WINS ROUND!!')
            self.player1.score += 1
    def final_result(self):
        print(f'Final Score: User {self.player1.score} - Computer {self.player2.score}')
        if self.player1.score > self.player2.score:
            print('USER WINS THE GAME!!')
        elif self.player1.score < self.player2.score:
            print('COMPUTER WINS THE GAME!!')
        else:
            print('THE GAME IS A DRAW!!')
           


print('--- Rock Paper Scissors Game ---')
while True:   
    rounds = input('How many rounds would you like to play?')
    if rounds.isnumeric():
        g = Game(int(rounds))
        g.play()
        break
    else:
        print('Invalid choice')