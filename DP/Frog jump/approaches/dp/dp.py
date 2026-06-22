# Problem: Frog jump
# Approach: DP
# Language: python3
# Time: O(n)
# Space: O(n)

from os import *
from sys import *
from collections import *
from math import *

from typing import *

  
def frogJump(n: int, heights: List[int]) -> int:
    dp=[0]*n
    dp[n-1]=0
    dp[n-2]=abs(heights[n-1]-heights[n-2])
    for i in range(n-3,-1,-1):
        dp[i]=min(abs(heights[i]-heights[i+1]) + dp[i+1],abs(heights[i]-heights[i+2])+dp[i+2])
    return dp[0]

    
