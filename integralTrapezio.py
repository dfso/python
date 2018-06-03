from numpy import *

class Trapezoidal(object):
	def __init__(self, a, b, x, y):
		self.a = a
		self.b = b
		self.x = x
		self.y = y
		
	def integrate(self):
		h = float(x[1] - x[0])
		s = y[0] + y[-1] + 2.0*sum(y[1:-1])
		return h * s / 2.0
        
if __name__ == '__main__':
	print "Calculando Integrais atraves do Metodo do Trapezio\n"
	a = input("valor do limite inferior: ");
	b = input("valor do limite superior: ");
	n = input("numero de subintervalos: ");
	x = linspace(a, b, n+1)
	y = 2.0*x**2 - x - 4.0
	T = Trapezoidal(a, b, x, y)
	print "Integral = %12.4f" % (T.integrate())

