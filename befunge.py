#!/usr/bin/python
import pygame
import re
import random
import sys
from math import floor
import six
import inputbox


class Field(object):
	def __init__(self, code):
		super(Field, self).__init__()
		self.Y = len(code)
		self.X = max([len(code[l]) for l in range(self.Y)])
		self.code = []
		for c in code:
			if self.X > len(c):
				c += " "*(self.X-len(c))
			self.code.append(list(c))
		self.direction = (1, 0)
		self.xy = (0, 0)
		self.read = False

	def step(self):
		self.xy = ((self.xy[0] + self.direction[0]) % self.X,
					(self.xy[1] + self.direction[1]) % self.Y)

	def change_direction(self, newdir):
		if newdir == "up":
			self.direction = (0, -1)
		elif newdir == "down":
			self.direction = (0, 1)
		elif newdir == "left":
			self.direction = (-1, 0)
		elif newdir == "right":
			self.direction = (1, 0)
		else:
			print("Invalid direction input")

	def stop(self):
		self.direction = (0, 0)

	def print_field(self, font):
		for c in self.code:
			print("".join(c))

	def current_char(self):
		return self.code[self.xy[1] % self.Y][self.xy[0] % self.X]

	def read_unichr(self, bl):
		self.read = bl

	def get_char(self, xget, yget):
		return self.code[yget % self.Y][xget % self.X]

	def put_char(self, yput, xput, v):
		self.code[yput % self.Y][xput % self.X] = chhr(v)


def pop(stack):
	return 0 if not stack else stack.pop()


def chhr(tal):
	if tal <= 0:
		return " "
	else:
		return six.unichr(tal)


def render_code(code):
	codefont = pygame.font.Font("./font/Inconsolata.otf", 24)
	for y, c in enumerate(code):
			for x, char in enumerate(c):
				if char in "0123456789":
					charcolor = (152, 152, 152)
				elif char in "+-*/%!`":
					charcolor = (255, 136, 136)
				elif char in "><^v?_|#@":
					charcolor = (136, 255, 136)
				elif char in ":\\$":
					charcolor = (255, 255, 136)
				elif char in ".,&~":
					charcolor = (136, 255, 255)
				elif char in "\"":
					charcolor = (255, 136, 255)
				elif char in "pg":
					charcolor = (136, 136, 255)
				else:
					charcolor = (206, 206, 206)
				codechar = codefont.render(char, 1, charcolor)
				background.blit(codechar, (charwidth*x, charheight*y))


global stack
global operations
global the_field
global background
global screen
global charwidth
global charheight
global bgcolor
global stackoutputcolor
stack = []
with open(sys.argv[1], "r") as c:
	codelist = c.read().splitlines()
the_field = Field(codelist)
ops = {"+": lambda x1, x2: stack.append(x1 + x2),
		"-": lambda x1, x2: stack.append(x2 - x1),
		"*": lambda x1, x2: stack.append(x1 * x2),
		"/": lambda x1, x2: stack.append(int(floor(float(x2)/float(x1)))),
		"%": lambda x1, x2: stack.append(x2 % x1),
		"`": lambda x1, x2: stack.append(1) if x2 > x1 else stack.append(0),
		"\\": lambda x1, x2: stack.extend([x1, x2]),
		"g": lambda x1, x2: stack.append(ord(the_field.get_char(x2, x1)))}
charwidth = 12
charheight = 28
screenheight = the_field.Y*charheight+180
screenwidth = max(the_field.X*charwidth+200, 320)
screen = pygame.display.set_mode((screenwidth, screenheight))
background = pygame.Surface(screen.get_size()).convert()
bgcolor = (52, 52, 52)
stackoutputcolor = (230, 200, 70)


def run_code():
	global the_field
	global stack

	def initiate_new_run():
		render_code(the_field.code)
		screen.blit(background, (0, 0))
		screen.blit(stacksurf, (0, screenheight-180))
		screen.blit(outsurf, (int(float(screenwidth)/2.0), screenheight-180))
		screen.blit(cursor, (the_field.xy[0]*charwidth, the_field.xy[1]*charheight))
		pygame.display.flip()
	stackcharheight = 16
	stackcharwidth = 10
	paused = False
	step1 = False
	reset = False
	pygame.display.set_caption("Befunge-93 Interpreter")
	cursor = pygame.Surface((charwidth, charheight), pygame.SRCALPHA)
	stacksurf = pygame.Surface((screenwidth, 180), pygame.SRCALPHA)
	outsurf = pygame.Surface((int(float(screenwidth)/2.0), 180), pygame.SRCALPHA)
	background.fill(bgcolor)
	outsurf.fill((0, 0, 0, 100))
	stacksurf.fill((0, 0, 0, 100))
	cursor.fill((255, 255, 255, 130))
	stackfont = pygame.font.Font("./font/Inconsolata.otf", 18)
	outcount = 0
	outline = 0
	instring = ""
	# Event loop
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					paused = not paused
				elif event.key == pygame.K_RIGHT:
					step1 = not step1
					paused = False
				elif event.key == pygame.K_ESCAPE:
					return
				elif event.key == pygame.K_r:
					reset = True
		if paused:
			continue
		if step1:
			paused = True
			step1 = False
		if reset:
			reset = False
			break
		initiate_new_run()
		screen.blit(background, (0, 0))
		background.fill(bgcolor)
		screen.blit(stacksurf, (0, screenheight-180))
		screen.blit(outsurf, (int(float(screenwidth)/2.0), screenheight-180))
		stacksurf.fill((0, 0, 0, 100))
		screen.blit(cursor, (the_field.xy[0]*charwidth, the_field.xy[1]*charheight))
		if not the_field.read:
			if the_field.current_char() == ">":
				the_field.change_direction("right")
			elif the_field.current_char() == "v":
				the_field.change_direction("down")
			elif the_field.current_char() == "<":
				the_field.change_direction("left")
			elif the_field.current_char() == "^":
				the_field.change_direction("up")
			elif the_field.current_char() == "?":
				the_field.change_direction(random.choice(["right", "down", "up", "left"]))
			elif the_field.current_char() == "@":
				the_field.stop()
			elif re.match("[0-9]", the_field.current_char()):
				stack.append(int(the_field.current_char()))
			elif the_field.current_char() in ops:
				ops[the_field.current_char()](pop(stack), pop(stack))
			elif the_field.current_char() == "!":
				stack.append(1 if pop(stack) == 0 else 0)
			elif the_field.current_char() == "$":
				pop(stack)
			elif the_field.current_char() == "_":
				the_field.change_direction("right") if pop(stack) == 0 else the_field.change_direction("left")
			elif the_field.current_char() == "|":
				the_field.change_direction("down") if pop(stack) == 0 else the_field.change_direction("up")
			elif the_field.current_char() == ".":
				outint = str(pop(stack))
				out = stackfont.render(outint, 1, stackoutputcolor)
				outsurf.blit(out, (stackcharwidth*outcount, stackcharheight*outline))
				outcount += len(outint)
			elif the_field.current_char() == ",":
				outtext = chhr(pop(stack))
				if outtext == "\n":
					outline += 1
					outcount = -1
					out = stackfont.render("", 1, stackoutputcolor)
				else:
					out = stackfont.render(outtext, 1, stackoutputcolor)
				outsurf.blit(out, (stackcharwidth*outcount, stackcharheight*outline))
				outcount += len(outtext)
			elif the_field.current_char() == ":":
				stack.extend([pop(stack)]*2)
			elif the_field.current_char() == "#":
				the_field.step()
			elif the_field.current_char() == "\"":
				the_field.read_unichr(True)
			elif the_field.current_char() == "p":
				the_field.put_char(pop(stack), pop(stack), pop(stack))
			elif the_field.current_char() == "&":
				try:
					stack.append(int(inputbox.ask(screen, "Put a number in the stack")))
				except Exception:
					continue
			elif the_field.current_char() == "~":
				if not instring:
					instring = list(inputbox.ask(screen, "Put a string to the stack"))
					instring.append(-1)
					instring = instring[::-1]
					stack.append(ord(instring.pop()))
				else:
					if instring[len(instring)-1] == -1:
						stack.append(int(instring.pop()))
					else:
						stack.append(ord(instring.pop()))
		elif the_field.current_char() == "\"":
			the_field.read_unichr(False)
		else:
			stack.append(ord(the_field.current_char()))
		the_field.step()
		# Print stack
		for x, s in enumerate(stack[::-1]):
			try:
				stackstack = stackfont.render("%d. %d [%s] (%s)" %
											(x+1, s, hex(s), chhr(s)), 1, stackoutputcolor)
			except Exception:
				stackstack = stackfont.render("%d. %d (%s)" %
											(x+1, s, chhr(s)), 1, stackoutputcolor)
			stacksurf.blit(stackstack, (0, stackcharheight*x))
		try:
			pygame.time.wait(int(sys.argv[2]))
		except Exception:
			pygame.time.wait(50)
	with open(sys.argv[1], "r") as c:
		codelist = c.read().splitlines()
	the_field = Field(codelist)
	stack = []
	run_code()


if __name__ == '__main__':
	pygame.init()
	run_code()
	pygame.quit()
