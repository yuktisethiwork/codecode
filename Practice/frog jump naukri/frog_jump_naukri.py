# Practice: frog jump naukri
# Language: python3
# Date: 22/06/2026

from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    dp=[0]*n
    def f(i):
        if i==n-1:
            return 0
        if i==n-2:
            return abs(heights[n-1]-heights[n-2])
        return min(abs(heights[i]-heights[i+1]) + f(i+1),abs(heights[i]-heights[i+2])+f(i+2))
    return f(0)
