from manimlib import *

class st(Scene):
	def construct(self):
		tex = Tex(r'\int_a^b f(x) dx').scale(3)
		self.add(tex)