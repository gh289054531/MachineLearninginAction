#coding=utf-8
import unittest 
from KNN import *
from DatingClassify import *

class DatingClassifyTestCase(unittest.TestCase):
    def testShowScatter(self):
        mat,label=fileToMatrix("datingTestSet.txt")
        showScatter(mat,label)
        
    def testClassifyPerson(self):
        testPersonDate=[10,10000,0.5]
        classifyPerson("datingTestSet.txt",testPersonDate,3)

if __name__ == "__main__":
    unittest.main()