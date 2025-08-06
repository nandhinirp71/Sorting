# Time Complexity: O(n^2)
# Space Complexity: O(1)

a = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

def bubbleSort(a):
  n = len(a)
  flag = True
  while flag:
    flag = False
    for i in range(1, n):
      if  a[i-1] > a[i]:
        a[i-1], a[i] = a[i], a[i-1]
        flag = True

  return a

bubbleSort(a)
