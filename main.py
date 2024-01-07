class Game:
    player_track = None
    player_score_dict = {}

    def __init__(self, dicti, number):
        self.player_track = dicti
        self.number = number
        self.rounds = 10

    def start(self):
        rounds_no = 0
        while rounds_no < 10:
            for player in self.player_track.keys():
                rolls = 2
                chances = 2
                standing_pins = 10
                while chances > 0:
                    hit = self.hitpins(standing_pins)
                    standing_pins = standing_pins - hit
                    chances -= 1
                    if standing_pins != 0:
                        ''' Normal case '''
                        self.add_score(player, hit, rounds_no)

                    elif standing_pins == 0 and chances > 1:
                        '''strike case'''
                        self.add_score(player, hit + 10, rounds_no)
                        chances -= 1

                    elif standing_pins == 0 and chances == 0:
                        self.add_score(player, hit + 5, rounds_no)

                print(f"Score after round {rounds_no + 1} - {player} - {self.getscore(player)}")
            rounds_no += 1
        return self.get_winner()

    def get_winner(self):
        maxi = -999
        for obj in self.player_score_dict:
            if sum(self.player_score_dict[obj]) > maxi:
                winning_id = obj
                winning_score = sum(self.player_score_dict[obj])
                maxi = sum(self.player_score_dict[obj])
            return self.player_track[winning_id], maxi

    def add_score(self, player, score, rounds_no):
        if player not in self.player_score_dict:
            self.player_score_dict[player] = [score]
        else:
            self.player_score_dict[player].append(score)
        return

    def getscore(self, player):
        return sum(self.player_score_dict[player])

    def hitpins(self, total_pins):
        # return 5
        import random
        return random.randrange(0, total_pins + 1)
if __name__ == "__main__":
  '''calling class method for execution'''
  '''Registering Player based upon the details being provided'''
  # n = int(input("Enter the number of players playing the game "))
  # dicti = {}
  # ''' Number of players '''
  # for player in range(n):
  #   Jersey_no = int(input("Input your lucky number "))
  #   players_name = input("Your go to name ")
  #   import random
  #   user_id = random.randrange(1,n+1)
  #   dicti[user_id] = {"Jersey_no ": Jersey_no, "Name": players_name}

  # start_game = input("Do you want to start the game? ")
  dicti = {1:{"Jersey_no ": 34, "Name": "Nik"}, 2:{"Jersey_no ": 45, "Name": "Ro"}}
  if 'yes' == 'yes':
    obj = Game(dicti, 2)
    print(obj.start())



