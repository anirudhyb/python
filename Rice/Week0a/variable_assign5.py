## Challenge # 11
#  https://www.coursera.org/learn/interactive-python-1/supplement/McyXj/practice-exercises-for-variables-and-assignments-optional


# Compute the area of a triangle (using Heron's formula),
# given its side lengths.

###################################################
# Tests
# Student should uncomment ONLY ONE of the following at a time.

# Test 1 - Select the following lines and use ctrl+shift+k to uncomment.
x0, y0 = 0, 0
x1, y1 = 3, 4
x2, y2 = 1, 1


# Test 2 - Select the following lines and use ctrl+shift+k to uncomment.
x0, y0 = -2, 4
x1, y1 = 1, 6
x2, y2 = 2, 1


# Test 3 - Select the following lines and use ctrl+shift+k to uncomment.
x0, y0 = 10, 0
x1, y1 = 0, 0
x2, y2 = 0, 10


###################################################
# Triangle area (Heron's) formula
# Student should enter formulas on the next lines.



###################################################
# Test output
# Student should not change this code.

a = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5
b = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
c = ((x2 - x0) ** 2 + (y2 - y0) ** 2) ** 0.5

s = (a + b + c) / 2

area = (s * (s -a) * (s -b) * (s-c)) ** 0.5

print "A triangle with vertices (" + str(x0) + "," + str(y0) + "),",
print "(" + str(x1) + "," + str(y1) + "), and",
print "(" + str(x2) + "," + str(y2) + ") has an area of " + str(area) + "."


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

# Test 1 output:
#A triangle with vertices (0,0), (3,4), and (1,1) has an area of 0.5.

# Test 2 output:
#A triangle with vertices (-2,4), (1,6), and (2,1) has an area of 8.5.

# Test 3 output:
#A triangle with vertices (10,0), (0,0), and (0,10) has an area of 50.
