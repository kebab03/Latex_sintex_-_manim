from manimlib import *

class st(Scene):
	def construct(self):
		tex = Tex(r'\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}').scale(3).shift(2 * DOWN)
		tex1 = Tex(r"\sum_{k=1}^\infty {1 \over k^2} = {\pi^2 \over 6}").scale(3).shift(2 * UP)
		self.add(tex,tex1)