import pygame

class Utils(object):

	def __init__(self):
		pass

	def boxText(self, text, width, font):
		lines = []
		lineCount = 0

		for line in text:
			newLine = u""

			for word in line.split():
				size = font.size(newLine + word)

				if size[0] > width:
					lines.append(newLine.strip())
					lineCount += 1
					newLine = u""

				newLine += word + " "

			lines.append(newLine.strip())
			lineCount += 1

		surface = pygame.Surface((width, (size[1] + 5) * lineCount), pygame.SRCALPHA | pygame.HWSURFACE)

		for i in xrange(lineCount):
			surface.blit(font.render(lines[i], 1, (0, 0, 0)), (surface.get_width() * 0.5 - font.size(lines[i])[0] * 0.5, (size[1] + 5) * i))

		return surface
