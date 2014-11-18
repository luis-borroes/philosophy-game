import pygame, button

class About(object):

	def __init__(self, parent):
		self.parent = parent
		self.parent.currentMenu = "about"
		self.parent.menuObj = self

		self.aboutText = [u"Vers\u00E3o 0.1",
						  "",
						  u"Programa\u00E7\u00E3o por: Lu\u00EDs Borr\u00F5es",
						  "",
						  "Silogismos e regras por:",
						  u"Lu\u00EDs Borr\u00F5es",
						  "Daniel Oliveira",
						  "Pedro Catarino",
						  "Xide Zhu",
						  "",
						  "Feito com Python 2.7 e Pygame"]

		button.Button.group = []

		button.Button("text", self.parent.mediumFont, self.aboutText, (0, 50), self.parent.resolution, None, True, 1000)
		button.Button("big", self.parent.mediumFont, "Voltar", (0, 610), self.parent.resolution, lambda: self.parent.mainMenu())
