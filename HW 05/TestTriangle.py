# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    #Test Invalid Input
    def testInvalidInput(self):
        self.assertEqual(classify_triangle(199, 203, 2), 'InvalidInput', '200, 203, 2 is not a valid triangle')
        self.assertEqual(classify_triangle(-2, 4, 5), 'InvalidInput', 'Arguments less than 0 are not valid traingles')

    #Test all inputs are numbers
    def testInputsAreNumbers(self):
        self.assertEqual(classify_triangle("dog", 2, 4), 'InvalidInput', 'dog is not a number')

    #Test not a triangle detection
    def testNotATriangle(self):
        self.assertEqual(classify_triangle(199, 1, 1), 'NotATriangle', 'You cannot make a triangle with 199, 1, and 1')

    # test right triangle
    def testRightTriangle(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testNotRightTriangle(self): 
        self.assertNotEqual(classify_triangle(6,3,4),'Right','6,3,4 is not a Right triangle')

    # test equilateral triangle
    def testEquilateralTriangle(self): 
        self.assertEqual(classify_triangle(3,3, 3),'Equilateral','3,3,3 is a Equilateral triangle')

    def testNotEquilateralTriangle(self): 
        self.assertNotEqual(classify_triangle(8,7,4),'Equilateral','8,7,4 is not a Equilateral triangle')
        
    # test Scalene triangle
    def testScaleneTriangle(self): 
        self.assertEqual(classify_triangle(10, 9, 6),'Scalene','10, 9, 6 is a Scalene triangle')

    def testNotScaleneTriangle(self): 
        self.assertNotEqual(classify_triangle(9, 9, 9),'Scalene','9, 9, 9 is not a Scalene triangle')
    
    # test Isoceles triangle
    def testIsocelesTriangle(self): 
        self.assertEqual(classify_triangle(10, 10, 6),'Isoceles','10, 10, 6 is a Isoceles triangle')

    def testNotScaleneTriangle(self): 
        self.assertNotEqual(classify_triangle(14, 18, 9),'Isoceles','14, 18, 9 is not a Isoceles triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

