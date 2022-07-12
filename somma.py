from manimlib import *

class st(Scene):
	def construct(self):
		tex = Tex(r'\sum_{a}^{b}{ x_i}').scale(3)
		self.add(tex)