import pygame, random, codecs

class Silogism(object):

	def __init__(self):
		self.silogisms = []
		self.file = codecs.open("assets/silogisms.txt", "r", "utf-8")

		lines = self.file.readlines()
		currentArg = []
		arg = []
		rules = []
		state = False # false is getting arg, true is getting rules

		for line in lines:
			if not state:
				if len(line) < 3:
					currentArg.append(arg)
					arg = []
					state = True
					continue

				arg.append(u"\u2022 " + line)

			if state:
				if len(line) < 3:
					currentArg.append(rules)
					self.silogisms.append(currentArg)
					rules = []
					currentArg = []
					state = False
					continue

				rules.append(u"\u2022 " + line)


		self.file.close()

	def getSilogism(self):
		return random.choice(self.silogisms)
