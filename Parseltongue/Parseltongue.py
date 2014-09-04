#!/usr/bin/python -tt
import SubSeqSum
def fibos(n):
  f0=0
  f1=1
  for i in range(n):
    temp = f0+f1
    f0=f1
    f1=temp
    print i,'=',f1
