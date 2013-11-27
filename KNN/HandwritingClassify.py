from KNN import *
from os import listdir

# Convert 32*32 image to 1*1024 vector
def imgToVector(filename):
    returnVec = zeros((1, 1024))
    f = open(filename)
    for i in range(32):
        line = f.readline()
        for j in range(32):
            returnVec[0][i * 32 + j] = int(line[j])
    return returnVec

def errorRateTest(trainingDir, testDir, k):
    labels = []
    trainingFileList = listdir(trainingDir)
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fname = trainingFileList[i]
        label = int(fname.split("_")[0])
        labels.append(label)
        trainingMat[i, :] = imgToVector(trainingDir + "/" + fname)
    errorCount = 0
    testFileList = listdir(testDir)
    n = len(testFileList)
    for i in range(n):
        fname = testFileList[i]
        realLabel = int(fname.split("_")[0])
        KNNLabel = classify0(imgToVector(testDir + "/" + fname), trainingMat, labels, k)
        if realLabel != KNNLabel:
            errorCount += 1
    return errorCount / float(n)
        
def classifyHandwriting(fileToClassify, trainingDir, k):
    labels = []
    trainingFileList = listdir(trainingDir)
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fname = trainingFileList[i]
        label = int(fname.split("_")[0])
        labels.append(label)
        trainingMat[i, :] = imgToVector(trainingDir + "/" + fname)
    return classify0(imgToVector(fileToClassify), trainingMat, labels, k)
