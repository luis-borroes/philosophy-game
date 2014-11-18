#!/usr/bin/env python

import pygame, menu, os

class Main(object):

	def __init__(self):
		clock = pygame.time.Clock()
		fps = 120
		resolution = (1280, 720)

		icon = pygame.image.load("assets/icon.png")
		pygame.display.set_icon(icon)
		pygame.display.set_caption("Silogismos", "Silogismos")

		screen = pygame.display.set_mode(resolution)

		objMenu = menu.Menu(screen, clock, fps, resolution)

if __name__ == "__main__":
	os.environ["SDL_VIDEO_CENTERED"] = "1"
	pygame.init()
	Main()
