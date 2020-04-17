import csv
import random
with open(r'C:\Users\Sunkavilli Suranya\Downloads\iris.data.txt') as csvfile:
    lines = csv.reader(csvfile)
    for row in lines:
        print(', '.join(row))
def loadDataSet(filename, split, trainingset = [], testset = []):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset) -1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
                if random.random() < split:
                    trainingset.append(dataset[x])
                else:
                    testset.append(dataset[x])                          
                    
trainingset = []
testset = []
loadDataSet(r'C:\Users\Sunkavilli Suranya\Downloads\iris.data.txt', 0.66, trainingset, testset)
print(repr(len(trainingset)));
print(repr(len(testset)))
import math
def euclidianDistance(instance1, instance2, length):
    distance = 0
    for i in range(length):
        distance += (pow(instance1[i] -instance2[i], 2))
    return math.sqrt(distance)    
  inst1 = [3,3,3,'a']
inst2 = [5,5,5,'b']
euclidianDistance(inst1, inst2, 3)
import operator
def getNeighbour(trainingset, testinstance, k):
    distance = []
    length = len(testinstance) - 1
    for x in range(len(trainingset)):
        dist = euclidianDistance(testinstance, trainingset[x], length)
        distance.append((trainingset[x], dist))
    distance.sort(key = operator.itemgetter(1))
    neighbours = []
    for x in range(k):
        neighbours.append(distance[x][0])
    return neighbours    
trainset = [[3,3,3,'a'], [4,4,4,'b']]
testinstance = [5,5,5]
k = 1
neighbour = getNeighbour(trainset, testinstance, k)
print(neighbour)
import operator
def getResponse(neighbours):
    classvotes = {}
    for x in range(len(neighbours)):
        response = neighbours[x][-1]
        if response in classvotes:
            classvotes[response] += 1
        else:
            classvotes[response] = 1
        sortedvotes = sorted(classvotes.items(), key = operator.itemgetter(1), reverse = True)
        return sortedvotes[0][0]
neighbour = [[2,2,2,'a'],[3,3,3,'a'],[4,4,4,'b']]
response = getResponse(neighbour)
print(response)
def getaccuracy(testset, predictions):
    correct = 0
    for x in range(len(testset)):
        if testset[x][-1] is predictions[x]:
            correct += 1
    return (correct/float(len(testset))) * 100

testset = [[2,2,2,'a'],[3,3,3,'a'],[4,4,4,'b']]
prediction = ['a','a','a']
accuracy = getaccuracy(testset, prediction)
print(accuracy)
def main():
    trainingset = []
    testset = []
    split = 0.67
    loadDataSet(r'C:\Users\Sunkavilli Suranya\Downloads\iris.data.txt', split, trainingset, testset)
    predictions = []
    k  = 3
    for x in range(len(testset)):
        neighbours = getNeighbour(trainingset, testset[x], k)
        result = getResponse(neighbours)
        predictions.append(result)
    accuracy = getaccuracy(testset, predictions)
    print(accuracy)
main()
