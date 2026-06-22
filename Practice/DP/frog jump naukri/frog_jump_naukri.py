# Practice: frog jump naukri
# Language: python3
# Date: 22/06/2026

from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    dp=[-1]*n
    def f(i):
        if dp[i]!=-1:
            return dp[i]
        if i==n-1:
            dp[n-1]=0
            return 0
        if i==n-2:
            dp[n-2]=abs(heights[n-1]-heights[n-2])
            return dp[i]
        dp[i]=min(abs(heights[i]-heights[i+1]) + f(i+1),abs(heights[i]-heights[i+2])+f(i+2))
        return dp[i]
    f(0)
    return dp[0]

    
