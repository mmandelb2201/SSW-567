import unittest

def Classify_triangle(a, b, c):
    if not isTriangle(a, b, c):
        return "not a triangle"
    elif isRight(a, b, c):
        return "right"
    elif a == b and b == c:
        return "equilateral"
    elif (a == b and b != c) or (a == c and b != c) or (b == c and b != a):
        return "isosceles"
    else:
        return "scalene"

def isTriangle(a, b, c):
    if (a + b) < c:
        return False
    elif (a + c) < b:
        return False
    elif (b + c) < a:
        return False
    else:
        return True
    
def isRight(a, b, c):
    if (a**2 + b**2) == c**2:
        return True
    elif (b**2 + c**2) == a**2:
        return True
    elif (a**2 + c**2) == b**2:
        return True
    else:
        return False


def runClassifyTriangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('Classify_triangle(',a, ',', b, ',', c, ')=', Classify_triangle(a,b,c),sep="")

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    # with 'test'.  Each function may include multiple tests
    def testEquilateral(self): # test invalid inputs
        # your tests go here.  Include as many tests as you'd like
        self.assertEqual(Classify_triangle(1,1,1),'equilateral','1,1,1 should be equilateral')
        self.assertNotEqual(Classify_triangle(10,10,10),'isosceles','Should be equilateral') 

    def testIsosceles(self):
        self.assertEqual(Classify_triangle(1, 2, 1), 'isosceles', '1, 2, 1 should be isosceles')
        self.assertNotEqual(Classify_triangle(2, 2, 20), 'equilateral', 'should be isosceles')

    def testScalene(self):
        self.assertEqual(Classify_triangle(1, 2, 3), 'scalene', '1, 2, 3 should be scalene')
        self.assertNotEqual(Classify_triangle(64, 55, 99), 'equilateral', 'should be scalene')

    def testRight(self):
        self.assertEqual(Classify_triangle(3, 4, 5), 'right', '3, 4, 5 should be right')
        self.assertNotEqual(Classify_triangle(5, 12, 13), 'scalene', 'should be right') 

    def testIsTriange(self):
        self.assertEqual(Classify_triangle(3000, 4, 5), 'not a triangle', '3000, 4, 5 should be not a triangle')
        self.assertNotEqual(Classify_triangle(7, 24, 25), 'not a triangle', 'should be right')       

if __name__ == '__main__':
    # examples of running the code
    runClassifyTriangle(1,2,3)
    runClassifyTriangle(15, 20, 25)
    runClassifyTriangle(3000, 4, 5)
    
    unittest.main(exit=False) # this runs all of the tests - use this line if running from Spyder
    #unittest.main(exit=True) # this runs all of the tests - use this line if running from the command line
    