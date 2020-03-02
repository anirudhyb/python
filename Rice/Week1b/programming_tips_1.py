# Programming tips

### http://www.codeskulptor.org/#examples_tips1.py

############
# This is a compilation of the examples from Week 1's Programming Tips.
# Many of these functions have errors, so this file won't run as is.
############


import math


############
# Has multiple NameErrors
def volume(side):
    return side ** 3   # sidde --> side

s = 2
print "Volume of cube with side", s, "is", volume(s), "."


############
# Has a NameError

import random

def random_dice():
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1 + die2

print "Sum of two random dice, rolled once:", random_dice()
print "Sum of two random dice, rolled again:", random_dice()
print "Sum of two random dice, rolled again:", random_dice()


############
# Has an AttributeError


import math 

def volume_sphere(radius):
    return 4.0/3.0 * math.pi * (radius ** 3) # math.Pi is error

r = 2
print "Volume of sphere of radius", r, "is", volume_sphere(r), "."


############
# Has multiple TypeErrors
def area_triangle(base, height):
    return 0.5 * base * height

b = 5
h = 2 + 2
print "Area of triangle with base", b, "and height", h, "is", area_triangle(b, h), "."


############
# Has multiple SyntaxErrors
def is_mary(x):
    if x == "Mary":
        print "Found Mary!"
    else:
        print "No Mary."

is_mary("Mary")
is_mary("Fred")


############
# Poor readability

# Indentation error --> means tab is to be used 

import math 

def area(a,b,c):
	"""
	Computes the Area of a triange, given the lengths of 3 sides
	"""
	s = (a+b+c) / 2.0
	return math.sqrt(s*(s-a)*(s-b)*(s-c))


############
# Improved readability

def area_triangle_sss(side1, side2, side3):
    """
    Returns the area of a triangle, given the lengths of
    its three sides.
    """
    
    # Use Heron's formula
    semi_perim = (side1 + side2 + side3) / 2.0
    return math.sqrt(semi_perim *
                     (semi_perim - side1) *
                     (semi_perim - side2) * 
                     (semi_perim - side3))

base = 3
height = 4
hyp = 5
print "Area of triangle with sides", base, height, hyp, "is", area_triangle_sss(base, height, hyp), "."


############
# Could use error-checking of input value
def favorites(instructor):
    """Return the favorite thing of the given instructor."""
	
    if instructor == "Joe":
    	return "games"
    elif instructor == "Scott":
    	return "ties"
    elif instructor == "John":
    	return "outdoors"
    else: 
		return "Dont Know"
		
print favorites("John")
print favorites("Jeannie")



