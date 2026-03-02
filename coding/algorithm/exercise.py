def clockangle(hour, min):

	angle = abs(hour*5 - min) /60*360
	return angle

# create all sub sets for a given set
# Algorithm: recursive
def powerset(s:set) -> list:

	ps = []
	if len(s) == 0:
		ps = [{}]
	else:
		ls = list(s)
		for item in powerset(set(ls[1:])):
			ps.append(item)
			if item == {}:
				ps.append({ls[0]})
			else:
				ps.append(item.union({ls[0]}))

	return ps

# powerful solution for above problem
# bit operation
def powerset(s):
	x = len(s)
	for i in range(1 << x):
		print ([s[j] for j in range(x) if (i & (1 << j))])


# sort k linked lists of integers

# Definition for singly-linked list.
from heapq import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# use heap to store sorting and pop mins
# complexity: O(N log k)
def mergeKLists(lists) -> ListNode:
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    head = point = ListNode(0)
    q = []
    for k, l in enumerate(lists):
        if l:
            heappush(q, (l.val, k))

    while len(q)>0:
        val, k = heappop(q)
        point.next = lists[k]
        point = point.next
        lists[k] = lists[k].next
        if lists[k]:
            heappush(q, (lists[k].val, k))
            
    return head.next


sl1 = ListNode(1)
sl1.next = ListNode(4)
sl1.next.next = ListNode(5)

sl2 = ListNode(1)
sl2.next = ListNode(3)
sl2.next.next = ListNode(5)

sl3 = ListNode(2)
sl3.next = ListNode(6)

lists = [sl1, sl2, sl3]

# reverse string w/t special chars
'''
Algorithm: 
define two points (start and end) to move both toward each other and swap them if both are alphabets
'''
def reverseStr(s: str)->str:

	if s is None or len(s)==0:
		return s
	s=list(s)
	length = len(s)	
	j=length-1

	# move indexes from both end swap if both are alphabets
	for i in range(length//2-1):
		c=s[i]
		if c.isalpha():
			while not s[j].isalpha():
				j -=1

			s[i] = s[j]
			s[j] = c
			j-=1
	s=''.join(s)
	return s


# Given a string, print all possible palindromic partitions
'''
Algorithm: move a pointer along the string and check all possibitity of Palindromic by assuming 
point is the middle of Palindromic substring
'''
def getPalindromic(s:str) ->str :

	result = [] # list of all palindromic
	for i in range(len(s)):
		j=0
		prej=-1

		while prej !=j:
			prej = j
			# substr with odd # of chars
			if i-j>=0 and i+j<=len(s) -1:
				if s[i-j] == s[i+j]:
					result.append(s[i-j:i+j+1])
					cut.append([i-j,i+j+1])
					j+=1

		j=0
		prej=-1
		
		while prej !=j:
			prej = j
			# substr with even # of chars
			if i-j>=0 and i+j+1<=len(s) -1:
				if s[i-j] == s[i+j+1]:
					result.append(s[i-j:i+j+2])
					cut.append([i-j,i+j+2])
					j+=1

	return result

#Given a string, print all possible palindromic partitions
'''
Given a string, find all possible palindromic partitions of given string.
Input: nitin
Output: n i t i n
		n iti n
		nitin

'''
# print all paritions 
def isPalindromic(s:str):

	return s==s[::-1]

# recursively print all paritions by starting from simple string
def partition(s: str):
   	
   	if len(s) ==1: 
   		return [[s]]
   	else:
   		prev = partition(s[1:])
   		p=[]
   		for i in range(len(prev)):
   			p.append([s[0]] + prev[i])

   			new = s[0] + prev[i][0]
   			new2 = s[0] + ''.join(prev[i][0:2])

   			if isPalindromic(new):
   				p.append([new] + prev[i][1:])

   			if isPalindromic(new2):
   				p.append([new2] + prev[i][2:])

   	return p 

#Count triplets with sum smaller than a given value
'''
Given an array of distinct integers and a sum value. Find count of triplets with sum smaller than given sum value. Expected Time Complexity is O(n^2).
Examples:
Input : arr[] = {-2, 0, 1, 3}
        sum = 2.
Output : 2
'''

def triplet(num: list, sum:int) -> int:

	count = 0
	num.sort()

	for i in range(0,len(num)-2):
		j = i+1
		k= len(num)-1
		while (j < k):
			if num[i] + num[j] + num[k] >= sum:
				k-=1
			else:
				count += k-j
				j+=1
	return count


# Convert array into Zig-Zag fashion
'''
Given an array of DISTINCT elements, rearrange the elements of array in zig-zag fashion in O(n) time. 
The converted array should be in form a < b > c < d > e < f.
Input: arr[] = {4, 3, 7, 8, 6, 2, 1}
Output: arr[] = {3, 7, 4, 8, 2, 6, 1}

algorithm: bubble swapping
A, B, C: if A>B and A>C, then B<A>C
         if A>B and A<C, then B<C>A

'''
def zigzag(num: list) -> list:

	smaller = True
	for i in range(len(num)-1):

		if (num[i] > num[i+1] and smaller) or (not(smaller) and num[i] < num[i+1]):
			num[i], num[i+1] = num[i+1], num[i]

		smaller = not smaller

	return num


# Generate all possible sorted arrays from alternate elements of two given sorted arrays 

'''
For Example

 
A = {10, 15, 25}
B = {1, 5, 20, 30}

The resulting arrays are:
  10 20
  10 20 25 30
  10 30
  15 20
  15 20 25 30
  15 30
  25 30
Algorithm: loop each list for all possibilities. the pattern of getting next value is same from either array.
So it can be repeated with recursive function call. Below code can be further simplified based on sorted array 
input
'''

def alternate(A:list, B: list, output=[], len:int=0):

    # variable len is used to record current number of values
    # initially use list appending to store all output which cause issue of previous output affecting next output 

    if len>0 and len%2==0:
        # print
        print(output[0:len])

    if len==0:
        # initialize output with maximized length
        output=["" for i in range(7)]

    searchlist = (A if len%2==0 else B)

    for e in searchlist:
        if len==0 or e>output[len-1]:
            # initialize first value or add next value
            output[len] = e
            alternate(A,B,output, len+1)    

# Pythagorean Triplet in an array
'''
Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a^2 + b^2 = c^2.
Example:

Input: arr[] = {3, 1, 4, 6, 5}
Output: True
There is a Pythagorean triplet (3, 4, 5).

Algorithm: O(n*n)
1) sqaure all element and sort list
2) start from c(k) and loop from largest to smallest
3) set up two pointers a(i) starting from 0 and b(j) starting from k-1
4) move i or j depends on the comparison of a**a +b**b vs c**c

'''
def triplets(ls:list) -> list:

    ls = [x**2 for x in sorted(ls)]
    result=[]

    for k in range(len(ls)-1, 1, -1):

        i, j =0, k-1
        while (i<j):

            if (ls[i] + ls[j]) == ls[k]:
                result.append((ls[i]**0.5,ls[j]**0.5,ls[k]**0.5))
                i+=1
                j-=1
            elif (ls[i] + ls[j]) > ls[k]:
                j-=1
            else:
                i+=1
    return result

#         
def longestsubarray(ls:list) -> list:

    ls.sort()
    maxlength = 0
    nextstart = 0

    for i in range(len(ls)):
        if i< nextstart:
            continue
        cnt = 1
        while ((i+cnt) <=len(ls)-1) and ((ls[i+cnt] - ls[i]) == cnt) :
            cnt +=1

        maxlength = max(maxlength, cnt)
        nextstart = i+maxlength

    return maxlength       

# Find the smallest positive integer value that cannot be represented as sum of any subset of a given array
'''
Given a sorted array (sorted in non-decreasing order) of positive numbers, find the smallest positive integer 
value that cannot be represented as sum of elements of any subset of given set.
Expected time complexity is O(n).
Examples:
Input:  arr[] = {1, 3, 6, 10, 11, 15};
Output: 2

Algorithm:
1) We decide that ‘res’ is the final result: If arr[i] is greater than ‘res’, then we found the gap which is ‘res’ 
because the elements after arr[i] are also going to be greater than ‘res’.
2) if 'res' is not final result, then  'res’ is incremented after considering arr[i]: The value of ‘res’ is incremented 
by arr[i] (why? If elements from 0 to (i-1) can represent 1 to ‘res-1’, then elements from 0 to i can represent from 1 to ‘res + arr[i] – 1’ 
be adding ‘arr[i]’ to all subsets that represent 1 to ‘res’)
'''
# loop
def minPosInt(ls:list) -> list:

    min_int = 1 

    for i in range(len(ls)):
        if ls[i] > min_int:
            return min_int
        else:
            min_int+=ls[i]

    return min_int

# recursive: easy to understand, starting from 1 element
def minPosInt(ls:list) -> list:
    
    if len(ls) ==1:
        return 1 if ls[0] >1 else 2
    else:
        pm = minPosInt(ls[:-1])
        if ls[-1] > pm:
            return pm
        else:
            return pm + ls[-1]


# Stock Buy Sell to Maximize Profit
'''
The cost of a stock on each day is given in an array, find the max profit that you can make by buying and selling 
in those days. For example, if the given array is {100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned 
by buying on day 0, selling on day 3. Again buy on day 4 and sell on day 6. If the given array of prices is sorted 
in decreasing order, then profit cannot be earned at all.

'''
# Algorithm: Recursive + brute force with all possibilities
def maxProfit(ls:list) -> list:
    
    if len(ls) < 1:
        return 0
    # elif len(ls) == 2:
    #     return (ls[-1] - ls[0]) if (ls[-1] - ls[0]) > 0 else 0
    
    profit = 0

    for buy in range(len(ls)-1):

        for sell in range(buy+1, len(ls)):

            if ls[sell] > ls[buy]:
                cur_profit = (ls[sell] -ls[buy]) 
                cur_total = maxProfit(ls[0:buy]) + cur_profit + maxProfit(ls[sell+1:len(ls)])
                profit = max(profit, cur_total)

    return profit


# max difference of any two numbers from a list
# two pointer: max diff and min elment
def maxDiff(arr:list):
    
    if len(arr) < 2:
        return 0

    max_diff = arr[1] - arr[0] 
    min_element = arr[0] 
      
    for i in range(1, len(arr)): 
        if (arr[i] - min_element > max_diff): 
            max_diff = arr[i] - min_element 
      
        if (arr[i] < min_element): 
            min_element = arr[i]

    return max_diff 
      
# two pointer: max diff and max elment
def maxDiff2(arr:list):
    
    if len(arr) < 2:
        return 0

    max_diff = arr[1] - arr[0] 
    max_element = arr[-1] 
      
    for i in range(len(arr)-2,-1,-1): 
        
        max_diff = max_element -arr[i] if max_element - arr[i]> max_diff else max_diff
        max_element = arr[i] if arr[i] > max_element else max_element

    return max_diff 



# for a given list of items [1,1,1,2,3,2] after removing m items, how many unique items are left at minimum? 
# idea is to convert input from list to dictionary with counter for each element

from collections import Counter

def deleteProduct(ids, m):
    # initialize counter
    counter = Counter()
    for id in ids:
        counter[id] +=1

    print(counter)

    # sort ids for elimination
    sorted_id = sorted(counter, key = counter.get)
    
    # remove element iterating
    j=-1
    for i in range(m):
       
        while True:
            j+=1
            if j > len(sorted_id)-1:
                j=0
            id = sorted_id[j]

            if counter[id] > 0:
                break

        counter[id] -=1

    # remove zero counter IDs
    remain = [ k for k,v in counter.items() if v>0]
    
    return len(remain)


ids = [1,1,1,2,3,2]
m = 4

print(deleteProduct(ids,m))


# generate random number for given probability p = [0.1, 0.05, 0.05, 0.2, 0.4, 0.2]
# idea is to convert input from probability to cumulated probability
# p = [0.1, 0.15, 0.2, 0.4, 0.8, 1]

from random import random

def roll_dice(p:list):

    # convert p to cumulated probability
    r = random()
    output = -1

    sum_p = []
    for i,v in enumerate(p):
        if sum_p ==[]:
            sum_p.append(v)
        else:
            sum_p.append(sum_p[-1]+v)

        if sum_p[-1] >= r and output==-1:
            output = i+1

    output = 1 if output ==-1 else output

    print(sum_p ,r )

    return output

print(roll_dice([0.1, 0.05, 0.05, 0.2, 0.4, 0.2]))



# given sum to find pair from array 

def find_pair(ls, value):
    '''
    using Hash table
    time complexity: O(n)
    Space complexity: O(n)
    '''
    s = set()

    for e in ls:

        temp = value -e 
        if temp in s: 
            print(e,temp)

        s.add(e)


def find_pair2(ls, value):
    '''
    Using sorting array with two pointers
    Time complexity: O(nlogn + n)
    Space complexity: O(1)
    '''
    ls = sorted(ls)

    j = len(ls) -1
    i = 0
    while i< j:

        while ls[i] + ls[j] > value:
            j-=1

        if ls[i] + ls[j] == value and i!=j:
            print(ls[i], ls[j])

        i+=1


ls = [1,3,2,5,4,8,7]
value = 6

find_pair2(ls, value)


# find max sum of continuous subarray
# [-1, -2, 3, 1,-2,3,8,-2] => [3,1,-2, 3,8] = 13

# algorithm: dynamic programming
# Idea: when to start new subarray? only if the previous sum is less than 0.
# if previous sum > 0, add current value whether it is negative or not because subarray
# may contain negative number. compare max_sum with current temp_sum and record max_sum

def max_subarr(ls):
    
    temp_sum = ls[0]
    max_sum = ls[0]

    i=1
    while i < len(ls):

        if temp_sum < 0:
            temp_sum = ls[i]
        else:
            temp_sum +=ls[i]

        max_sum = max(temp_sum, max_sum)
        i+=1

    return max_sum

#print(max_subarr([-1, -2, 3, 1,-2,3,8,-2]))
#print(max_subarr([-1, -2, -2,-2]))


# find max sum of two continuous subarray without overlap
# [2, -1, -2, 3, 1,-2,3,8,-2] => [2] + [3,1,-2, 3,8] = 15

# algorithm: dynamic programming
# Need two subarrays: one on left, another one on right. calculate left and right maxsum of subarray
# maxsum is calcuated and recorded as above function

def max_twosubarr(ls):
    
    temp_sum = ls[0]
    max_sum = ls[0]

    i=1
    leftsum_list= [max_sum]
    while i < len(ls):

        if temp_sum < 0:
            temp_sum = ls[i]
        else:
            temp_sum +=ls[i]

        max_sum = max(temp_sum, max_sum)
        leftsum_list.append(max_sum)
        i+=1

    print(leftsum_list)
    temp_sum = ls[-1]
    max_sum = ls[-1]
    j = len(ls)-2

    total_sum = ls[0] + ls[1]

    while j>0:

        if temp_sum < 0:
            temp_sum = ls[j]
        else:
            temp_sum +=ls[j]

        max_sum = max(temp_sum, max_sum)

        total_sum = max(total_sum, max_sum + leftsum_list[j-1])

        j-=1


    return total_sum

# print(max_subarr([-1, -2, 3, 1,-2,3,8,-2]))
# print(max_twosubarr([2, -1, -2]))
print(max_twosubarr([2, -1, -2, 3, 1,-2,3,8,-2]))


# Markov chain - first order 
import numpy as np
#Current state
I = np.matrix([[0.1, 0.9]])
#Transition Matrix
T = np.matrix([[.6, 0.4],
               [.1, 0.9]])
print(I)
for i in range(100):
    I = I * T

print(I)
