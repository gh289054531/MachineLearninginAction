# coding=utf-8
import unittest 
from ID3 import *

class ID3TestCase(unittest.TestCase):
    def testCalEntropy(self):
        dataSet,labels = createdataSet()
        print calEntropy(dataSet)
    
    def testSplitDataSet(self):
        dataSet,labels = createdataSet()
        print splitDataSet(dataSet, 0, 1)
        print splitDataSet(dataSet, 0, 0)
        
    def testChooseBestFeatureToSplit(self):
        dataSet ,labels= createdataSet()
        print chooseBestFeatureToSplit(dataSet)
    
    def testCreateTree(self):
        dataSet ,labels= createdataSet()
        print createTree(dataSet,labels)
        

if __name__ == "__main__":
    unittest.main()
