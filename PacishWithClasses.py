import time
# import threading
import random

gameOn = True
querriedMessages = []
score = 0

class Coin:

	def __init__(self, xPos, yPos):
		self.type = "coin"
		self.xPos = xPos
		self.yPos = yPos

	def move(self, frame):
		self.xPos = 0 #random number, frame for max and min values
		self.yPos = 0 #random number

	def hitCheck(self, pacman, system):
		if system.isContact(pacman, self):
			self.move(frame)
			score = score + 100

class Ghost:

	def __init__(self, xPos, yPos):
		self.type = "ghost"
		self.xPos = xPos
		self.yPos = yPos

	def moveUp():
		self.yPos = self.yPos - 1

	def moveDown():
		self.yPos = self.yPos + 1

	def moveLeft():
		self.xPos = self.xPos - 1

	def moveRight():
		self.xPos = self.xPos + 1

	def chooseDirection(self, pacman):
		xDif = pacman.xPos - self.xPos
		yDif = pacman.yPos - self.yPos
		if abs(xDif) 

	def hitCheck(self, pacman, system):
		if system.isContact(pacman, self):
			outPutMessage = "You hit a wall and died"
			system.queryMessage(outPutMessage)
			gameOn = False

class Pacman:

	def __init__(self, xPos, yPos, direction):
		self.type = "pacman"
		self.xPos = xPos
		self.yPos = yPos
		self.xPosOld = xPos
		self.yPosOld = yPos
		self.direction = direction

	def moveUp():
		self.yPosOld = self.yPos
		self.yPos = self.yPos - 1

	def moveDown():
		self.yPosOld = self.yPos
		self.yPos = self.yPos + 1

	def moveLeft():
		self.xPosOld = self.xPos
		self.xPos = self.xPos - 1

	def moveRight():
		self.xPosOld = self.xPos
		self.xPos = self.xPos + 1

	def input():
		#choose direction and then call one of move methods, if there is not a new command, just do the direction
		print("yos")

class System:

	def __init__(self, wallHitRule, guardModeRule): #, prefferedFPS):
		self.type = "system"
		self.wallHitRule = wallHitRule
		self.guardModeRule = guardModeRule

	def inbounds(self, pacman, frame): #or can do isInbounds and return false
		global gameOn

		if self.wallHitRule:
			outPutMessage = "You hit a wall and died"
			if pacman.xPos <= frame.minWallX:
				gameOn = False
				self.queryMessage(outPutMessage)
			elif pacman.xPos >= frame.maxWallX:
				gameOn = False
				self.queryMessage(outPutMessage)
			elif pacman.yPos <= frame.minWallY:
				gameOn = False
				self.queryMessage(outPutMessage)
			elif pacman.yPos >= frame.maxWallY:
				gameOn = False
				self.queryMessage(outPutMessage)

		else:
			outPutMessage = "You can't go out of bounds!"
			if pacman.xPos <= frame.minWallX:
				pacman.xPos = pacman.xPosOld
				self.queryMessage(outPutMessage)
			elif pacman.xPos >= frame.maxWallX:
				pacman.xPos = pacman.xPosOld
				queryMessage(outPutMessage)
			elif pacman.yPos <= frame.minWallY:
				pacman.yPos = pacman.yPosOld
				queryMessage(outPutMessage)
			elif pacman.yPos >= frame.maxWallY:
				pacman.yPos = pacman.yPosOld
				queryMessage(outPutMessage)

	def isContact(self, objectOne, objectTwo):
		if objectOne.xPos == objectTwo.xPos and objectOne.yPos == objectTwo.yPos:
			return True
		else:
			return False

	def queryMessage(self, message):
		global querriedMessages

		querriedMessages.append(message)

	def printQuery(self):
		global querriedMessages

		for counte in range(0, len(querriedMessages)):
			print(querriedMessages[counte])

		querriedMessages = []



class Frame:
	def __init__(self, minWallX, maxWallX, minWallY, maxWallY):
		self.type = "frame"
		self.minWallX = minWallX
		self.maxWallX = maxWallX
		self.minWallY = minWallY
		self.maxWallY = maxWallY
		#for draw method
		self.drawComponets = []

	def addDrawComponet(self, object):
		self.drawComponets.append(object)

	def drawFrame(self):
		for yRow in range(self.minWallY, self.maxWallY + 1):
			for xRow in range(self.minWallX, self.maxWallX + 1):

				if self.minWallX == xRow:
					print("#", end = "")
				elif self.maxWallX == xRow:
					print("#", end = "")
				elif self.minWallY == yRow:
					print("#", end = "")
				elif self.maxWallY == yRow:
					print("#", end = "")
				else:

					didDrawObject = False
					for componet in range(len(self.drawComponets)):
						if self.drawComponets[componet].xPos == xRow and self.drawComponets[componet].yPos == yRow:
							if self.drawComponets[componet].type == "pacman":
								print("O", end = "")
								didDrawObject = True
							elif self.drawComponet[componet].type == "ghost":
								print("X", end = "")
								didDrawObject = True
							elif self.drawComponet[componet].type == "coin":
								print("C", end = "")
								didDrawObject = True
							else:
								print("?", end == "")
								didDrawObject = True
					if didDrawObject == False:
						print(" ", end = "")


			print("")

frameMain = Frame(0, 20, 0, 10)
pacmanMain = Pacman(10, 5, "up")
frameMain.addDrawComponet(pacmanMain)
frameMain.drawFrame()



holdEnd = input("GAMEOVER")
#at bottom of draw function, call printQuery
#create system object before other object
