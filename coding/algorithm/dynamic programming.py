'''
Dynamic Programming: As we know DP is all about using calculated results to formulate the final result.
 find a relation between previous states to reach the current state.
 Properties:
 1) Overlapping Subproblems
 2) Optimal Substructure

    Steps to solve a DP:
    1) Identify if it is a DP problem
    2) Decide a state expression with least parameters
    3) Formulate state relationship    
    4) Do tabulation (or add memoization)
'''

# Example of dynamic programming
# Given 3 numbers {1, 3, 5}, we need to tell
# the total number of ways we can form a number 'N' 
# using the sum of the given three numbers.
# (allowing repetitions and different arrangements).

# Total number of ways to form 6 is: 5
# 1+1+1+1+1+1
# 1+1+1+3
# 3+3
# 1+5
# 5+1

# State(n) = State(n-1) + State(n-3) + State(n-5)

# this function returns the number of  
# arrangements to form 'n'  

# memoization
def solve(n, dp=[]):

  if dp==[]:
    dp = [-1]*(n+1)
  # base case 
  if (n < 1):   
      return 0
  if (n == 1):   
      return 1
  
  # checking if already calculated 
  if (dp[n]!=-1):
      return dp[n]
  
  # storing the result and returning 
  dp[n] = solve(n-1, dp) + solve(n-3, dp) + solve(n-5, dp)
  print(dp)

  return dp[n]

print(solve(6))

# tabulation
def solve2(n): 

  dp = [-1]*(n+1)

  dp[0] =0
  dp[1] = 1

  for i in range(2,n+1):

      if i>5:
        dp[i] = dp[i-1] + dp[i-3] + dp[i-5]
      elif i>3:
        dp[i] = dp[i-1] + dp[i-3]
      else: 
        dp[i] = dp[i-1]

  return dp[n]

print(solve2(6))


'''
DP-3 Longest Increasing Subsequence
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest
subsequence of a given sequence such that all elements of the subsequence are sorted
in increasing order. For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80}
is 6 and LIS is {10, 22, 33, 50, 60, 80}.
Solution:
Optimal Substructure: Let arr[0..n-1] be the input array and L(i) be the length of the LIS ending at index i such that arr[i] is the last element of the LIS.

Then, L(i) can be recursively written as:

L(i) = 1 + max( L(j) ) where 0 < j < i and arr[j] < arr[i]; or
L(i) = 1, if no such j exists.
To find the LIS for a given array, we need to return max(L(i)) where 0 < i < n.
'''

def cal_lis(ls):

    maxcnt = []
    for i, e in enumerate(ls):

        temp_max = 1
        for j in range(i):
            if ls[j] < e and  temp_max < (maxcnt[j] + 1 ):
                temp_max = maxcnt[j] + 1
        maxcnt.append(temp_max)

    print(maxcnt)
    return max(maxcnt)

l = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(cal_lis(l))

# DP-4
# Longest Common Subsequence | DP-4
# LCS Problem Statement: Given two sequences, find the length of longest 
# subsequence present in both of them. A subsequence is a sequence that appears in 
# the same relative order, but not necessarily contiguous. 
# It is a classic computer science problem, the basis of diff (a file comparison program that outputs the differences between two files), and has applications in bioinformatics.

# Examples:
# LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
# LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

s1 = "thisisatest"
s2 = "testing123testing"

# dynamic programming: recursion
def lcs1(s1, s2, m, n):

    if m<0 or n<0:
        return 0

    if s1[m] == s2[n]:

        return 1 + lcs1(s1,s2,m-1,n-1)
    else:
        return max(lcs1(s1,s2,m,n-1), lcs1(s1,s2,m-1,n))

#print(lcs1(s1,s2,len(s1)-1,len(s2)-1))
# 1.4s

# dynamic programming with memoization
def lcs2(s1, s2, state, m, n):

    if state is None:
        state = [[None]* (len(s1)+1)] * (len(s2)+1)

    if m<0 or n<0:
        return 0

    if s1[m] == s2[n]:

        if state[n-1][m-1] is None:
            state[n-1][m-1] = lcs1(s1,s2,m-1,n-1)

        return 1 + state[n-1][m-1]
    else:
        state[n][m] = max(lcs1(s1,s2,m,n-1), lcs1(s1,s2,m-1,n))
        return state[n][m]

#print(lcs2(s1,s2,None, len(s1)-1,len(s2)-1))
# 1.3s

# dynamic programming with Tabulation
def lcs3(s1, s2):

    m = len(s1)
    n = len(s2)
    
    # state[i][j] = lcs(s1[0:i-1], s2[0:j-1])
    # state[m][n] = lcs(s1[0:m-1], s2[0:n-1])
    state = [[None]* (n+1)] * (m+1)

    for i in range(m+1):
        for j in range(n+1):
            if i ==0 or j ==0:
                state[i][j] = 0 
            elif s1[i-1] == s2[j-1]:
                state[i][j] = 1 + state[i-1][j-1]
            else:
                state[i][j] = max(state[i][j-1], state[i-1][j])

    return state[m][n]

print(lcs3(s1,s2))
#0.1s
