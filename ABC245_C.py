import io
import sys

_INPUT = """\
6
5 4
9 8 3 7 2
1 6 2 9 5
4 90
1 1 1 100
1 2 3 100
4 1000000000
1 1 1000000000 1000000000
1 1000000000 1 1000000000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  ans=set([A[0],B[0]])
  for i in range(N-1):
    tmp=set()
    for j in ans:
      if abs(A[i+1]-j)<=K: tmp.add(A[i+1])
      if abs(B[i+1]-j)<=K: tmp.add(B[i+1])
    ans=tmp
  if len(ans)>0: print('Yes')
  else: print('No')