x = [8,5,2,6,9,3,1,4,7]

def selection_sort(numList):
   for i in range(0, len(numList), 1):
       minIndex = i
       for j in range(i+1, len(numList), 1):
           if numList[minIndex] > numList[j]:
               minIndex = j
       temp = numList[i]
       numList[i] = numList[minIndex]
       numList[minIndex] = temp
   return numList
print(selection_sort(x))