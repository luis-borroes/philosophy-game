import pygame, sys, button, game, silogism, about

class Menu(object):

	def __init__(self, screen, clock, fps, resolution):
		self.screen = screen
		self.clock = clock
		self.fps = fps
		self.resolution = resolution
		self.halfResolution = (self.resolution[0] * 0.5, self.resolution[1] * 0.5)
		self.silogism = silogism.Silogism()

		self.running = True

		self.mediumFont = pygame.font.Font("assets/fonts/OpenSans-Semibold.ttf", 30)
		self.bigFont = pygame.font.Font("assets/fonts/OpenSans-Semibold.ttf", 72)

		self.currentMenu = ""

		self.mainMenu()

		while self.running:
			dt = self.clock.tick(self.fps)

			mouseTrigger = False

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.leave()

				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						if self.currentMenu == "main":
							self.leave()
						else:
							self.mainMenu()

				if event.type == pygame.MOUSEBUTTONUP:
					if event.button == 1:
						mouseTrigger = True

			self.screen.fill((34, 167, 240))

			mPos = pygame.mouse.get_pos()

			for butt in button.Button.group:
				butt.updateAndDraw(self.screen, mPos, mouseTrigger)

			pygame.display.flip()

	def mainMenu(self):
		self.currentMenu = "main"

		button.Button.group = []

		button.Button("text", self.bigFont, "Silogismos", (0, 150), self.resolution)
		button.Button("text", self.mediumFont, "Tenta verificar a validade destes silogismos!", (0, 300), self.resolution)

		button.Button("big", self.mediumFont, u"Come\u00E7ar", (0, 390), self.resolution, lambda: game.Game(self))
		button.Button("big", self.mediumFont, "Sobre", (0, 475), self.resolution, lambda: about.About(self))

	def leave(self):
		self.running = False
		pygame.quit()
		sys.exit(0)
