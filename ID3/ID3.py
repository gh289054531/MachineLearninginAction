# coding=utf-8
from math import log

def createdataSet():
    dataSet = [[1, 1, 'yes'],
             [1, 1, 'yes'],
             [1, 0, 'no'],
             [0, 1, 'no'],
             [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels

# 计算数据集的熵
def calEntropy(dataSet):
    size = len(dataSet)
    p = {}
    for data in dataSet:
        if p.has_key(data[-1]) == False:
            p[data[-1]] = 0;
        p[data[-1]] += 1
    entropy = 0.0
    for key in p:
        prob = float(p[key]) / size
        entropy -= prob * log(prob, 2)
    return entropy

# 提取按照targetFeatureValue划分出来的子数据集
def splitDataSet(dataSet, featureIndex, targetFeatureValue):
    retDataSet = []
    for data in dataSet:
        if data[featureIndex] == targetFeatureValue:
            left = data[:featureIndex]
            right = data[featureIndex + 1:]
            left.extend(right)
            retDataSet.append(left)
    return retDataSet

# 选择基于哪个特征进行划分
def chooseBestFeatureToSplit(dataSet):
    baseEntropy = calEntropy(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    featureLen = len(dataSet[0]) - 1
    for i in range(featureLen):
        featureList = [f[i] for f in dataSet]
        featureSet = set(featureList)
        curEntropy = 0.0
        for targetFeatureValue in featureSet:
            subDataSet = splitDataSet(dataSet, i, targetFeatureValue)
            prob = float(len(subDataSet)) / len(dataSet)
            curEntropy += prob * calEntropy(subDataSet)
        infoGain = baseEntropy - curEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

# 如果生成树时已经遍历了所有特征，但是最后仍然有多种分类，那么哪个类出现次数多就返回哪个类
def majorityCount(classList):
    classCount = {}
    for c in classList:
        if classCount.has_key(c) == False:
            classCount[c] = 0
        classCount[c] += 1
    sortedClassCount = sorted(classCount.iteritems(), lambda x:x[1], reverse=True)
    return sortedClassCount[0][0]

# 递归生成ID3决策树
def createTree(dataSet, labels):
    classList = [f[-1] for f in dataSet]
    #如果只有一个类
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    #如果不止一个类但是所有的特征都被访问过了
    if len(dataSet[0]) == 1:
        return majorityCount(classList)
    bestFeatureIndex = chooseBestFeatureToSplit(dataSet)
    bestFeatureLabel = labels[bestFeatureIndex]
    ID3Tree = {bestFeatureLabel:{}}
    del(labels[bestFeatureIndex])
    featureList = [f[bestFeatureIndex] for f in dataSet]
    featureSet = set(featureList)
    for targetFeatureValue in featureSet:
        subLabels = labels[:]
        ID3Tree[bestFeatureLabel][targetFeatureValue] = createTree(splitDataSet(dataSet, bestFeatureIndex, targetFeatureValue), subLabels)
    return ID3Tree
