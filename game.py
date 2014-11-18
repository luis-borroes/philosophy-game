import pygame, button

class Game(object):

	def __init__(self, parent):
		self.parent = parent
		self.parent.currentMenu = "game"
		self.parent.menuObj = self

		self.silogism = self.parent.silogism.getSilogism()

		button.Button.group = []

		button.Button("text", self.parent.mediumFont, self.silogism[0], (0, 135), self.parent.resolution, None, True, 1000)
		button.Button("valid", self.parent.mediumFont, u"V\u00E1lido", (-250, 400), self.parent.resolution, lambda: EndGame(self, parent, u"\u2022 V\u00E1lido"))
		button.Button("invalid", self.parent.mediumFont, u"Inv\u00E1lido", (250, 400), self.parent.resolution, lambda: EndGame(self, parent, u"\u2022 Inv\u00E1lido"))

		button.Button("text", self.parent.mediumFont, "Prima Esc para sair", (-self.parent.halfResolution[0] + 150, self.parent.resolution[1] - 50), self.parent.resolution)

class EndGame(object):

	def __init__(self, game, parent, choice):
		self.parent = parent
		self.parent.currentMenu = "endGame"
		self.parent.menuObj = self

		button.Button.group = []

		button.Button("text", self.parent.mediumFont, game.silogism[1][1:], (0, 120), self.parent.resolution, None, True, 1000) #pass all but first element of silogism

		button.Button("text", self.parent.mediumFont, "Prima Esc para sair", (-self.parent.halfResolution[0] + 150, self.parent.resolution[1] - 50), self.parent.resolution)

		answer = game.silogism[1][0].rstrip()
		
		if choice == answer:
			button.Button("text", self.parent.bigFont, "Correto!", (0, 20), self.parent.resolution)
			button.Button("valid", self.parent.mediumFont, "Continuar", (0, 650), self.parent.resolution, lambda: Game(parent))

		else:
			button.Button("text", self.parent.bigFont, "Errado!", (0, 20), self.parent.resolution)
			button.Button("invalid", self.parent.mediumFont, "Continuar", (0, 650), self.parent.resolution, lambda: Game(parent))
