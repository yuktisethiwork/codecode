# Problem: Frog jump
# Approach: Approach 1
# Language: python3
# Time: O(n)
# Space: O(1)

from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    dp=[0]*n
    prev=0
    curr=abs(heights[n-1]-heights[n-2])
    for i in range(n-3,-1,-1):
        curr, prev=min(abs(heights[i]-heights[i+1]) + curr,abs(heights[i]-heights[i+2])+prev), curr
    return curr
