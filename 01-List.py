# Write a function to calculate distance between two coordinates
from math import *

a = int(input('Please enter X1: '))
b = int(input('Please enter Y1: '))
c = int(input('Please enter X2: '))
d = int(input('Please enter Y2: '))

def square(num):
  return num * num

def calculate_distance(x1, y1, x2, y2):
  sum_of_squares = square(x2 - x1) + square(y2 - y1)
  distance = sqrt(sum_of_squares)
  return distance

result = calculate_distance(a, b, c, d)
print(f'The distance between ({a}, {b}) and ({c}, {d}) is {result}')
