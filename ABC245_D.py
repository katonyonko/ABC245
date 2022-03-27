import io
import sys

_INPUT = """\
6
1 2
2 1
12 14 8 2
1 1
100 1
10000 0 -1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  A=list(map(int,input().split()))
  C=list(map(int,input().split()))
  A=A[::-1]
  C=C[::-1]
  now=[0]*(N+M+1)
  ans=[]
  for i in range(M+1):
    tmp=(C[i]-now[i])//A[0]
    ans.append(tmp)
    for j in range(N+1):
      now[i+j]+=tmp*A[j]
  print(*ans[::-1])