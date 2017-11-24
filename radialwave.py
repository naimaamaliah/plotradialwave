from sympy import var
from sympy.physics.hydrogen import R_nl
def radialwave(n,l,r):
	var("r Z")
	radialwave=eval('R_nl(n,l,r,Z=1)')
	return radialwave;

def V(r):
	var('r')
	V=1/(r**2)
	return V;
