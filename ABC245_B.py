import io
import sys

_INPUT = """\
6
8
0 3 2 6 2 1 0 0
3
2000 2000 2000
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  A=set(list(map(int,input().split())))
  for i in range(2001):
    if i not in A:
      print(i)
      break