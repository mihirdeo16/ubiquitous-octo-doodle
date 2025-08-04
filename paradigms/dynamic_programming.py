
__license__ = "Apache-2.0"
__version__ = "0.1.0"
__maintainer__ = "Mihir Deo"

""""
A problem where you have overlapping sub-problems, one can use DP.
It is way to cache these solutions of sub-problem as use them to optimize main problem speed.

A dynamic programming can problem can be seen in two approaches:
1. Top Down: memorization, you start at nth position and go down using recursive call to meet/hit base condition. Along the way we do caching.
2. Bottom UP: tabulation, you track/mark sub-problem solution (base condition) as you go up/end of the problem. 
3. Bottom UP + Cache using prev,curr temp variables to put M - O(n)

Playlist: 
1. https://www.youtube.com/playlist?list=PLKYEe2WisBTFw-XWc-kwS3dkQeeSmvpg5
2. https://docs.google.com/spreadsheets/d/1pEzcVLdj7T4fv5mrNhsOvffBnsUH07GZk7c2jD-adE0/edit?gid=0#gid=0
3. https://www.youtube.com/watch?v=mBNrRy2_hVs&t=1103s

TODO:
+ Coin Change
+ Jump Game
+ Longest Common Subsequence
"""
from math import cos
from typing import List, Dict, Any, Tuple, Union

def fib_dyna(n):
    """
    Implement Fibonacci series problem: given position find it's fibonacci number.
    """
    ##########
    # Top Down: memorization solution
    ##########
    def fib_t(n,memo={}):
        if n in memo:
            return memo[n]
        memo[n] = fib_t(n-1,memo) + fib_t(n-2,memo)
        return memo[n]
    memo = {0:1,1:1}
    fib_t(n,memo)

    ##########
    # Bottom UP : tabulation solution
    ##########   
    def fib_b(n):
        if n < 3:
            return 1
        dp = [None] *n
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
    
    ##########
    # Bottom UP : tabulation solution 
    # M - O(n)
    ##########   
    def fib_b_1(n):
        if n < 3:
            return 1
        prev = 1
        curr = 1
        for i in range(2,n):
            prev, curr = curr, prev+ curr
        
        return curr
    
def climbing_stairs(n):
    """
    Implement Climbing stair problem: Given stair number find how many ways one can reach there.
    """
    ##########
    # Top Down: memorization solution
    ##########
    def climb_stair_t(n,memo={}):
        if n in memo:
            return memo[n]
        memo[n] = climb_stair_t(n-1,memo) + climb_stair_t(n-2,memo)
        return memo[n]
    
    climb_stair_t(n,memo={1:1,2:2})

    ##########
    # Bottom UP : tabulation solution
    ##########
    def climb_stair_b(n):
        if n == 1:
            return 1
        if n== 2:
            return 2
        dp = [None]*n
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
    

def minimum_cost_climb_stairs(cost:List[int]):
    """
    Implement Min Cost Climbing Stairs: Given cost array of stairs, calculate minimum cost it will take to end.
    One can take either 1 or 2 step at given point. And you can either start at index 0 or 1.
    Logic: Bottom UP: tabulation solution
        So at every step, you do look at either you would have came from 1st or 2nd stairs. 
        And the optimal cost of reaching there is minimum of 1st and 2nd, stairs. Secondly, we can keep track of stair as the stack up using DP.

    T - O(n)
    M - O(n)
    """
    ##########
    # Top Down: memorization solution
    ##########
    def min_cost(i,memo={}):
        if i in memo:
            return memo[i]
        else:
            one_step = cost[i-1] + min_cost(i-1)
            two_step = cost[i-2] + min_cost(i-2)

            memo[i] = min(one_step,two_step)

            return memo[i]
    n = len(cost)
    min_cost(n,memo={0:0,1:0})

    ##########
    # Bottom UP : tabulation solution
    ##########
    dp = [0] * (len(cost)+1)

    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2,len(cost)):
        dp[i] =  min(dp[i-1],dp[i-2])
        
    return dp[-1]

    ##########
    # Bottom UP : tabulation solution (Initial Position)
    ##########
    dp = [0] * (len(cost))

    dp[0] = cost[0]
    dp[1] = cost[1]

    for i in range(2,len(cost)):
        dp[i] =  cost[i] + min(dp[i-1],dp[i-2])
        
    return min(dp[-1],dp[-2])


    ##########
    # Bottom UP : Cache solution
    ##########

    prev = 0
    curr = 0
    for i in range(2,len(cost)):
        curr =  min(cost[i-2]+prev,curr+cost[i-1])
        prev = curr
        
    return curr


def rob(nums: List[int]):
    """
    Implement House Robber: You can't rob adjacent houses else you will alert police, calculate maximum money you can rob.
    Logic: Bottom UP : tabulation solution
        We can start from beginning of street, and calculate total cost we would have along way, keep in condition that we would not rob adjacent houses. So at every house we can do either rob it or leave it, based on prev house is great.
    T - O(n)
    M - O(n)

    """
    ##########
    # Bottom UP : tabulation solution
    ##########
    dp = [0]*len(nums)

    dp[0] = nums[0]
    dp[1] = max(nums[1],nums[0])

    for i in range(2,len(nums)):
        dp[i] = max(nums[i]+dp[i-2],dp[i-1])
    return dp[-1]

    ##########
    # Top Down: memorization solution
    ##########
    def helper(i,memo={}):
        if i in memo:
            return memo[i]
        else:

            rob_true = nums[i] + helper(i-2,memo)
            rob_skip = helper(i-1,memo)

            memo[i] = max(rob_true,rob_skip)
            return memo[i]

    memo= {0:nums[0],1:max(nums[0],nums[1])}



def unique_path(cols:int,rows:int)->int:
    """
    Implement Unique Path: Find ways to reach destination, given robot can move either right or down. Given robot start at, (0,0) and reach (m-1,n-1)
    Logic: Bottom UP DO: tabulation solution
        So if we do look up at position as sum of its path from UP and LEFT we can do compounding effect to track the DP.
        We can create table of mXn check its UP & LEFT loc. 
    """
    ##########
    # Bottom UP : tabulation solution
    # T - O(row X col)
    # M - O(row X col)
    ##########
    dp = [[0]*cols for _ in range(rows)]

    # make 1st rows as 1s.
    for c in range(cols):
        dp[0][c]=1
    
    # make 1st cols as 1s.
    for r in range(rows):
        dp[r][0]=1

    # Iterate on all rows X col
    for r in range(rows):
        for c in range(cols):

            up = 0 if (r-1) < 0 else dp[r][c-1]

            left = 0 if (c-1) < 0 else dp[r-1][c]

            dp[r][c] = up + left
    
    # return dp[-1][-1]

    ##########
    # Top Down: memorization solution
    ##########

    def path(r,c,memo):
        if memo[(r,c)]:
            return memo[(r,c)]
        if r < 0 or c < 0:
            return 0
        up = path(r-1,c,memo)
        left = path(r,c-1,memo)
        memo[(r,c)] = up + left
        return memo[(r,c)]
    
    memo = {(0,0):1}
    res = path(rows-1,cols-1,memo)
    
    return res


def max_sub_array(nums:List)->int:
    """
    Implement Maximum sub array: Find the subarray with largest sum and return sum.
    Logic; Bottom UP : tabulation solution
        At any point in array of index "i" we can ask should we consider as interim element or start of array? Condition can be, if we consider so far sum adding element is bigger or element itself is bigger. If sum is bigger then make sense to call this element as interim element else consider this as start. Also for start, consider max between, zero and number.
        Edge case; if nums array is of 1 or less.     
    """

    ##########
    # Bottom UP : tabulation solution
    # T - O(n)
    # M - O(n)
    ##########
    n = len(nums)
    if n <2:
        return nums[0]
    
    dp = [0]*n
    dp[0] = max(nums[0],0)

    for i in range(1,n):
        dp[i] = max(nums[i],dp[i-1]+nums[i])
    
    return max(dp)

    ##########
    # Bottom UP : tabulation solution
    # T - O(n)
    # M - O(1)
    ##########
    n = len(nums)
    if n <2:
        return nums[0]
    
    max_sum = float('-inf')
    curr_sum = max(nums[0],0)

    for i in range(1,n):
        curr_sum = curr_sum+nums[i]
        max_sum = max(max_sum,curr_sum+nums[i])

        if curr_sum < 0:
            curr_sum = 0
    
    return max_sum



def longest_incr_subsqu(nums:List[int])-> int:
    """
    Implement Longest Increasing Subsequence; Given array of integers return length of longest increasing subsequence.
    Logic: Bottom UP : tabulation solution
        We start with smallest sub-problem as build up, for given point we do look at of relative sub-array, to see how large a increasing subsequence we can form. So T - O(n^2), and save in DP memory, M - O(n)
    """
    n = len(nums)
    if n < 2:
        return n
    dp = [1] * n

    for i in range(1,n):
        for j in range(i):
           if nums[i] > nums[j]:
               dp[i] = max(dp[i],dp[j]+1)

    return max(dp)


def main():
    """
    Main function to run the project.
    """
    pass    
    # Add your code here


if __name__=="__main__":
    main()