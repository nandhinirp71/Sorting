def bubbleSort(arr):
  # Time Complexity: O(n^2)
  # Space Complexity: O(1)
  n = len(arr)
  flag = True
  while flag:
    flag = False
    for i in range(1, n):
      if  arr[i-1] > arr[i]:
        arr[i-1], arr[i] = arr[i], arr[i-1]
        flag = True

  return arr

def insertionSort(arr):
  # Time Complexity: O(n^2)
  # Space Complexity: O(1)
  n = len(arr)
  for i in (1, n):
    for j in (1, 0, -1):
      if arr[j} < arr[j-1]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
      else:
        break
  return arr      

def selectionSort(arr):
  # Time Complexity: O(n^2)
  # Space Complexity: O(1)
  n = len(arr)
  for i in range(1, n):
    min_index = i
    for j in range(i+1, n):
      if arr[j] < arr[min_index]:
        min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
  return arr
      

a = [-5, 3, 2, 1, -3, -3, 7, 2, 2]
bubbleSort(a)
insertionSort(a)



