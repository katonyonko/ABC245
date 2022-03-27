import io
import sys

_INPUT = """\
6
5 5
1 2
2 3
3 4
4 2
4 5
3 2
1 2
2 1
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,M=map(int,input().split())
  G=[set() for _ in range(N)]
  IG=[set() for _ in range(N)]
  for i in range(M):
    U,V=map(int,input().split())
    U-=1; V-=1
    G[U].add(V)
    IG[V].add(U)
  s=[]
  ans=set()
  for i in range(N):
    if len(G[i])==0: s.append(i)
  while s:
    x=s.pop()
    ans.add(x)
    for v in IG[x]:
      G[v].remove(x)
      if len(G[v])==0:
        s.append(v)
  print(N-len(ans))