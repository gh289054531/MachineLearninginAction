#coding=utf-8
from KNN import *
import matplotlib
import matplotlib.pyplot as plt

def showScatter(mat, labels):
    didntLikeX = []
    didntLikeY = []
    smallDosesX = []
    smallDosesY = []
    largeDosesX = []
    largeDosesY = []
    m = shape(mat)[0]
    for i in range(m):
        if labels[i] == 1:
            didntLikeX.append(mat[i][1])
            didntLikeY.append(mat[i][2])
        if labels[i] == 2:
            smallDosesX.append(mat[i][1])
            smallDosesY.append(mat[i][2])
        if labels[i] == 3:
            largeDosesX.append(mat[i][1])
            largeDosesY.append(mat[i][2])    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    s1 = ax.scatter(didntLikeX, didntLikeY, s=20, c='red')
    s2 = ax.scatter(smallDosesX, smallDosesY, s=30, c='green')
    s3 = ax.scatter(largeDosesX, largeDosesY, s=50, c='blue')
    plt.xlabel("Percentage of Time Spent Playing Video Games")
    plt.ylabel("Liters of Ice Cream Consumed Per Week")
    plt.legend([s1, s2, s3], ["didntLike", "smallDoses", "largeDoses"], loc=1)
    plt.show()
    return

def classifyPerson(filename, personData,k):
    resultList = ["didnt like", "small dose", 'large dose']
    mat, labels = fileToMatrix(filename)
    norm, ranges, minVals = autoNorm(mat)
    normPersonData = (array(personData) - minVals) / ranges
    classifyResult = classify0(normPersonData, norm, labels, k)
    print resultList[classifyResult - 1]

