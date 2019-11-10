"""
ABC is a right triangle with the angle a(ABC) = 90 deg.
M is the mid point on the hypotenuse of line l(AC).
Given the lengths of AB and BC, find a(MBC) in degrees.

Input Format:
Length of AB
Length of BC

Output:
Angle of a(MBC) in degrees, rounded to nearest integer.
"""

from math import sqrt, degrees, acos

# MBC = arccos((MB^2 + BC^2 - MC^2) / 2(MB)(BC)) **results in radians**
# solve for each component in equation, then convert to degrees

# Get input
AB = float(input())
BC = float(input())

# Solve for AC & MC (MC = AC / 2) (only need MC)
# Pythagorean Theorm applies to original right triangle ABC to give AC
AC = sqrt((AB**2) + (BC**2))
MC = AC / 2

# need to know cos(a(BCA)) which is <adjacent / hypotenuse>.  Define as 'beta'
beta = BC / AC

# Solve for MB
# MB^2 = MC^2 + BC^2 - 2(MC)(BC)cos(beta)
MB = sqrt((MC**2) + (BC**2) - (2 * MC * BC * beta))

# Calculate a(MBC)
MBC = degrees(acos((MB**2 + BC**2 - MC**2) / (2 * MB * BC)))

# Use unicode designation to include degree symbol (required in output).
print(str(round(MBC)) + "\u00b0")
