import pygame, utils
util = utils.Utils()

class Button(object):
	group = []
	imgBig = pygame.image.load("assets/menuBig.png")
	imgValid = pygame.image.load("assets/menuValid.png")
	imgInvalid = pygame.image.load("assets/menuInvalid.png")
	_convertTrigger = False

	def __init__(self, bType, font, text, pos, resolution, callback = None, box = False, boxWidth = 400):
		self.font = font
		self.box = box
		self.boxWidth = boxWidth

		if not Button._convertTrigger:
			Button.imgBig = Button.imgBig.convert_alpha()
			Button.imgValid = Button.imgValid.convert_alpha()
			Button.imgInvalid = Button.imgInvalid.convert_alpha()
			Button._convertTrigger = True

		if bType == "text":
			img = None
		elif bType == "big":
			img = Button.imgBig
		elif bType == "valid":
			img = Button.imgValid
		elif bType == "invalid":
			img = Button.imgInvalid

		if img:
			self.position = pygame.rect.Rect((resolution[0] * 0.5 - img.get_width() * 0.5 + pos[0], pos[1]), img.get_size())
			self.callback = callback

			self.img = img
			self.overlay = pygame.Surface(img.get_size(), pygame.SRCALPHA | pygame.HWSURFACE)
			self.overlay.fill((255, 255, 255, 60))
			self.overlay.convert_alpha()
			self.setText(text)

		else:
			self.img = None
			self.setText(text)
			self.position = pygame.rect.Rect((resolution[0] * 0.5 - self.textSize[0] * 0.5 + pos[0], pos[1]), self.textSize)
			self.callback = None

		Button.group.append(self)

	def updateAndDraw(self, screen, mPos, trigger):
		if self.img:
			screen.blit(self.img, self.position.topleft)

		screen.blit(self.text, (self.position.centerx - self.textSize[0] * 0.5, self.position.centery - self.textSize[1] * 0.5))

		if mPos[0] in xrange(self.position.left, self.position.right) and mPos[1] in xrange(self.position.top, self.position.bottom) and self.img and self.callback:
			screen.blit(self.overlay, self.position.topleft)

			if trigger:
				self.callback()

	def setText(self, text):
		self.rawText = text

		if self.box:
			self.text = util.boxText(text, self.boxWidth if not self.img else self.img.get_width(), self.font)
		else:
			self.text = self.font.render(text, 1, (0, 0, 0))

		self.textSize = self.text.get_size()
