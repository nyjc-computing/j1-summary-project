class Game:
  def __init__(self):
      self.player = None
      self.rooms = []
      self.now = 0

  def setup(self):
      self.player = Player()
      self.rooms.append(Bedroom())

  def isover(self):
      return self.player.isdead()