import heapq
input = open("input.txt").readlines()

list1, list2 = [], []

for line in input:
    lineLocations = line.split()
    if line:
        list1.append(int(lineLocations[0]))
        list2.append(int(lineLocations[1]))

heapq.heapify(list1)
heapq.heapify(list2)

totalDistances = 0

for i in range(len(input)):
    x = heapq.heappop(list1)
    y = heapq.heappop(list2)

    totalDistances += abs(x-y)

print(totalDistances)