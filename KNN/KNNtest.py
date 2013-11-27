#coding=utf-8
import unittest 
from KNN import *

class KNNTestCase(unittest.TestCase):
	
	def testFileToMatrix(self):
		mat,label=fileToMatrix("datingTestSet.txt")
		print mat
		print label
		return
	
	def testClassify0(self):
		group, label = createDataSet()
		self.assertEqual(classify0([0, 0], group, label, 3),"B")
		return
	
	def testAutoNorm(self):
		mat,label=fileToMatrix("datingTestSet.txt")
		norm,ranges,minVals=autoNorm(mat)
		print norm
		print ranges
		print minVals
		
	def testErrorRateTest(self):
		errorRate=errorRateTest(0.1,"datingTestSet.txt",3)
		print "The error rate is: %f" % (errorRate)

if __name__ == "__main__":
	unittest.main()
