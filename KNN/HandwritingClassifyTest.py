# coding=utf-8
import unittest 
from KNN import *
from HandwritingClassify import *

class HandwritingClassifyTestCase(unittest.TestCase):
    def testImgToVectorTest(self):
        print imgToVector("trainingDigits/0_0.txt")
    
    def testErrorRateTest(self):
        print "Error rate is: %f" % (errorRateTest("trainingDigits", "testDigits", 3))
    
    def testClassifyHandwriting(self):
        print classifyHandwriting("testDigits/0_0.txt", "trainingDigits", 3)


if __name__ == "__main__":
    unittest.main()
