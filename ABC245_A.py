import io
import sys

_INPUT = """\
6
7 0 6 30
7 30 7 30
0 0 23 59
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  A,B,C,D=map(int,input().split())
  if A*60+B<=C*60+D: print('Takahashi')
  else: print('Aoki')