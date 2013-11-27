# coding=utf-8
from numpy import *
import matplotlib
import matplotlib.pyplot as plt

#only use for test
def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def fileToMatrix(filename):
    f = open(filename)
    lines = f.readlines()
    f.close()
    rowNum = len(lines)
    mat = zeros([rowNum, 3])
    labels = []
    index = 0
    for line in lines:
        line = line.strip()
        listFromLine = line.split("\t")
        mat[index, :] = listFromLine[0:3]
        label = listFromLine[-1]
        labelInt = 0
        if label == "didntLike":
            labelInt = 1
        elif label == "smallDoses":
            labelInt = 2
        elif label == "largeDoses":
            labelInt = 3
        else:
            print "类别有错误数据"
        labels.append(labelInt)
        index += 1
    return mat, labels
        

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        votelabel = labels[sortedDistIndicies[i]]
        classCount[votelabel] = classCount.get(votelabel, 0) + 1
    sortedClassCount = sorted(classCount.iteritems(), key=lambda d:d[1], reverse=True)
    return sortedClassCount[0][0]

def autoNorm(mat):
    minVals = mat.min(0)
    maxVals = mat.max(0)
    ranges = maxVals - minVals
    # norm=zeros(shape(mat))
    m = shape(mat)[0]
    norm = mat - tile(minVals, (m, 1))
    norm = norm / tile(ranges, (m, 1))
    return norm, ranges, minVals

def errorRateTest(testSetPercent, filename, k):
    mat, label = fileToMatrix(filename)
    norm, ranges, minVals = autoNorm(mat)
    m = shape(norm)[0]
    errorCount = 0
    testSetNum = int(m * testSetPercent)
    for i in range(testSetNum):
        result = classify0(norm[i, :], norm[testSetNum:, :], label[testSetNum:], k)
        if result != label[i]:
            errorCount += 1
    return errorCount / float(testSetNum)
