from manimlib import *

class st(Scene):
	def construct(self):
		tex = Tex(r'\frac{a}{b}').scale(3)
		self.add(tex)