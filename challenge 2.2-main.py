"""
implement a class called player that represent a cricket player the player class should have a
method called paly() which prints"the player is playing cricket drive two classes batsman and
bowler from the player classes override the play () method in each drive class to print"the batsman
is batting"and"the bowler is bowling", respectively write ya program to create object of both the
batsman and classes and call play () method for each object 
"""


#define the base class player 
class player:
 def play(self):
  print("the player is          playing cricket.")

#defender drived class batsman 
class Batsman(player):
 def play(self):
  print("the batsman is           batting.")
#define the drived class Bowler
class Bowler (player):
  def play(self):
   print ("the Bowler is            bowling.")

#create a object of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()
#call the play() method for ecah object
batsman.play()
bowler.play()