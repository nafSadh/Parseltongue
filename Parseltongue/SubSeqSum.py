def GetSubSeqSum(A, C) :
  '''return index of sub array that produce sum C'''
  C = int(C)
  map = dict()
  sum = 0
  map[0] = -1
  for i in range (len(A)):
    sum += int(A[i])
    if (sum-C) in map:
      return [A[j] for j in range(map[sum-C]+1,i+1)]
    map[sum]=i
  return []

import sys




def main():
  fibo(100)

if __name__ == '__main__':
  main()