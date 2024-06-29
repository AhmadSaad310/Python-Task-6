
import random
class Player:
    name=int(input('Enter your name = '))
    score=0
    def __init__(self, name):
        self.name=name
        self.score=0
    def roll_dice(self):
        score=random.randint(1,6)
        print (f'{self.name} {score}')
    def  get_score(self):
        return self.score
class ComputerPlayer(Player):
    pass
class  Game():
    def __init__(self, player_name):
       self.player=Player(player_name)
       self.computerplayer=ComputerPlayer('Machen')
    def  play_round(self):
        self.play_round=random.randint(1,6)
        self.player=self.play_round
        self.computerplayer=self.play_round
        print(f'{self.player} {self.computerplayer}')
    def  display_scores(self):
        self.get_score.append=self.display_scores
        print(f'{self.display_scores}')
    def determine_winner(self):
        if self.display_scores(Player)>self.display_scores(ComputerPlayer):
            print('You are the winner')
        else:
            print ('Sorry. You are loser')




    
    

        

        