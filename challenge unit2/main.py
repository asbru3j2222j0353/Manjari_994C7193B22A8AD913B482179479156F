# Define the base class Player
class player:
  def play(self):
    print("The player is playing cricket.")

# Define the Derived class batsman
class Batsman(player):
    def play(self):
      print(" The Batsman is batting. ")

# Define the Derived class bowler
class Bowler(player):
  def play(self):
    print(" The bowler is bowling. ")
    
# Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

#call the play method for each object
batsman.play()
bowler.play()
        