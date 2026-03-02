#Algorithm class
'''
1. Greedy Algorithm
2. Divide and Conquer: 
3. Dynamic Programming: find repeating/overlapping subproblem and build state relationship and work on optimization

Tip: 
# starting with examples and do not solve in your head
# Make time vs space tradeoff (hash table/hash set)
# Base case and build recursively
# try different data structure: counter
# Sort the data first if necessary
# test by examples including edge cases
# using two pointer to iterate array/list with one pass
# Sort array/list before iteration
# Use hashmap to speed up lookup values
# use list as stack: ls.append() and ls.pop()
# use list as queue: ls.append() and ls.pop(0) 

'''

# Binary Search value in a sorted list using loop
def bsearch(ls, val):

	start_idx = 0 
	end_idx = len(ls) -1

	while start_idx <= end_idx:

		mid_idx = (start_idx+end_idx)//2

		if val == ls[mid_idx]:
			return mid_idx
		
		if val > ls[mid_idx]:
			start_idx = mid_idx + 1
		else:
			end_idx = mid_idx -1

	if start_idx > end_idx:
		return None

# Binary Search using recursive
def bsearch(ls, val, start_idx=None, end_idx=None):

	if start_idx is None:
		start_idx = 0 
		end_idx = len(ls) -1

	if start_idx > end_idx:
		return None
	else:
		mid_idx = (start_idx+end_idx)//2

	if val == ls[mid_idx]:
		return mid_idx
	
	if val > ls[mid_idx]:
		return bsearch(ls, val, mid_idx + 1, end_idx)
	else:
		return bsearch(ls, val, start_idx, mid_idx - 1)

# backtracking
def permute(list, s):
    if list == 1:
        return s
    else:
        return [ y + x
                 for y in permute(1, s)
                 for x in permute(list - 1, s)
                 ]

print(permute(1, ["a","b","c"]))
print(permute(2, ["a","b","c"]))

# result:
# ['a', 'b', 'c']
# ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']

# Traversal
'''
Traversal is a process to visit all the nodes of a tree and may print their values too
In-order Traversal: left -> root -> right
Pre-order Traversal: root -> left ->right
Post-order Traversal: left -> right -> root
'''
# In-order Traversal
class TreeNode:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
	
	# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # calculate max depth of tree with recursion
    def GetMaxDepthBottomup(self):

        depth_left = self.left.GetMaxDepth() if self.left else 0
        depth_right = self.right.GetMaxDepth() if self.right else 0

        return max(depth_left, depth_right) + 1

    # calculate max depth of tree with level order Traversal
    def GetMaxDepthTopdown(self):

        depth, level = 1, [self]

        while level:
            level = [child for node in level for child in (node.left, node.right) if child]
            if len(level) > 0:
                depth +=1

        return depth

    # Remove nodes on root to leaf paths of length < K
    def RemoveShortPathNodes(self, k, level=1):

        if not self.left and not self.right and level <k:

            return None

        if self.left:
            self.left = self.left.RemoveShortPathNodes(k, level+1)

        if self.right:
            self.right = self.right.RemoveShortPathNodes(k, level+1)


	# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

	# Inorder traversal
	# Left -> Root -> Right
    def InorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

	# Preorder traversal
	# Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

	# Postorder traversal
	# Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

#Sorting
'''
Bubble Sort - O(n^2)
Insertion Sort - O(n^2)
Shell Sort  - O(n^2)
Selection Sort - O(n^2)
Merge Sort - O(nlogn), need O(n) space
Heap Sort - O(nlogn)
Quick Sort -O(nlogn), worst case: O(n^2)
Radix Sort - O(nk) - k is max number of digits
Bucket sort - O(n) - only useful when input is uniformly distributed over a range
Counting sort -  O(n+k) time when elements are in range from 1 to k.

'''      
#Bubble Sort 冒泡法 O(n^2)
# It is a comparison-based algorithm in which each pair of adjacent elements is compared and the elements are 
# swapped if they are not in order.
# Keep moving max element to the end of list

def bubblesort(list):

	# for each outer loop, the largest number from [0, iter_num] are moved the top 
	for iter_num in range(len(list)-1,0,-1): #range(start, stop, step)
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                #swap
                list[idx], list[idx+1] = list[idx+1], list[idx]


list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)


# Merge Sort - O(nlogn)
# Merge sort first divides the array into equal halves and then combines them in a sorted manner.
# This is done recurively and sorting from bottom up

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
	# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.pop(0)
        else:
            res.append(right_half[0])
            right_half.pop(0)
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

unsorted_list = [64, 34, 25, 12, 22, 11, 90]

print(merge_sort(unsorted_list))

# Insertion Sort - O(n^2)
# Assume first i elements are sorted, insert i+1 element to the sorted list
# compare the first two elements and sort them. Then we pick the third element and find its proper position 
# among the previous two sorted elements. 

def insertion_sort(InputList):

    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
		
		# Compare the current element with previous element one by one		
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1

        # find position j    
        InputList[j+1] = nxt_element

list = [19,2,31,45,30,11,121,27]
insertion_sort(list)
print(list)

# Shell Sort 希尔排序法 O(n^2)
# Shell Sort involves sorting elements which are away from each other. We sort a large sublist of a given list 
# and go on reducing the size of the list until all elements are sorted. The below program finds the gap by 
# equating it to half of the length of the list size and then starts sorting all elements in it. Then we keep 
# resetting the gap until the entire list is sorted.
# a. 将数组切割一半成:2*(n/2)
# b. 对数组的列进行插入法排序
# c. 再将数组切割一半成：4*(n/4)，对每列重复插入法排序,直到 行向量变成列向量，完成最后一次排序

def shellSort(input_list):
    
    gap = len(input_list) // 2
    while gap > 0:


        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
		
			# Sort the sub list for this gap with insertion sort
            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp

		# Reduce the gap for the next element

        gap = gap//2

list = [19,2,31,45,30,11,121,27]

shellSort(list)
print(list)

# Selection Sort：选择排序法 - O(n^2)
# start by finding the minimum value in a given list and move it to a sorted list
# similar to bubble sort
def selection_sort(input_list):

    for idx in range(len(input_list)):

        min_idx = idx
        # selected min value and placed in list[idx]
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
		# Swap the minimum value with the compared value

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


l = [19,2,31,45,30,11,121,27]
selection_sort(l)
print(l)


# Heap Sort - O(nlogn)
'''
1. Build a max heap from the input data.
2. At this point, the largest item is stored at the root of the heap. Swap it with the last item of the heap 
   followed by reducing the size of heap by 1. Finally, Reheapify the root of tree
3. Repeat above steps while size of heap is greater than 1.
'''

def heapify(arr, n, i): 
'''
    move largest value to current root - arr[i] 
'''
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
  
    # move largest element to last index and reheapify the root
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
  
# Driver code to test above 
arr = [ 12, 11, 13, 5, 6, 7] 
heapSort(arr) 
n = len(arr) 
print ("Sorted array is") 
for i in range(n): 
    print ("%d" %arr[i]), 

# Quick Sort
'''
Divide and Conquer algorithm. It picks an element as pivot and partitions the given array around the picked pivot. 
There are many different versions of quickSort that pick pivot in different ways.

Always pick first element as pivot.
Always pick last element as pivot (implemented below)
Pick a random element as pivot.
Pick median as pivot.
The key process in quickSort is partition(). Target of partitions is, given an array and an element x of array as pivot, 
put x at its correct position in sorted array and put all smaller elements (smaller than x) before x, and put all greater
elements (greater than x) after x. All this should be done in linear time.
'''

# move pivot value to correct position
# all value smaller than pivot are placed right of pivot 
# all value larger than pivot are placed left of pivot

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    # compare all elements with pivot and put smaller value to the front of list
    for j in range(low , high): 
        if   arr[j] < pivot: 
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  
# The main function that implements QuickSort 
# arr[] --> Array to be sorted, 
# low  --> Starting index, 
# high  --> Ending index 
  
# Function to do Quick sort 
def quickSort(arr,low,high): 
    if low < high: 
  
        # pi is partitioning index, arr[pi] is now 
        # at right place 
        pi = partition(arr,low,high) 
  
        # Separately sort elements before 
        # partition and after partition 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 

# Bucket Sort - O(n)
'''
Algorithm: create N buckets and put each element in corresponding bucket. 
within each bucket, do insertion sort,  then merge all buckets. This is useful when 
input is uniformly distributed over a range

BucketSort(arr[], n)
1) Create n empty buckets (Or lists).
2) Do following for every array element arr[i].
    a) Insert arr[i] into bucket[n*array[i]]
3) Sort individual buckets using insertion sort.
4) Concatenate all sorted buckets.
'''
def insertionSort(b): 
    for i in range(1, len(b)): 
        up = b[i] 
        j = i - 1
        while j >=0 and b[j] > up:  
            b[j + 1] = b[j] 
            j -= 1
        b[j + 1] = up      
    return b      
              
def bucketSort(x): 
    arr = [] 
    slot_num = 10 # 10 means 10 slots, each 
                  # slot's size is 0.1 
    for i in range(slot_num): 
        arr.append([]) 
          
    # Put array elements in different buckets  
    for j in x: 
        index_b = int(slot_num * j)  
        arr[index_b].append(j) 
      
    # Sort individual buckets  
    for i in range(slot_num): 
        arr[i] = insertionSort(arr[i]) 
          
    # concatenate the result 
    k = 0
    for i in range(slot_num): 
        for j in range(len(arr[i])): 
            x[k] = arr[i][j] 
            k += 1
    return x 
  
# Driver Code 
x = [0.897, 0.565, 0.656, 
     0.1234, 0.665, 0.3434]  
print("Sorted Array is") 
print(bucketSort(x)) 

# Counting Sort- O(n+k): similar to bucket sort
# The main function that sort the given string arr[] in  
# alphabetical order 
def countSort(arr): 
    # Create a count array to store count of inidividul 
    # characters and initialize count array as 0 
    count = [0 for i in range(256)] 
  
    # For storing the resulting answer since the  
    # string is immutable 
    ans = ["" for _ in arr] 
  
    # Store count of each character 
    for i in arr: 
        count[ord(i)] += 1
  

    start = 0
    for i in range(256): 
        for j in range(count[i]):
            ans[start+j] = chr(i)
        start += count[i]
    return ans  
  
# Driver program to test above function 
arr = "geeksforgeeks"
ans = countSort(arr) 
print ("Sorted character array is {}".format("".join(ans))) 

# Radix Sort
'''
The idea of Radix Sort is to do digit by digit sort starting from least significant 
digit to most significant digit. Radix sort uses counting sort as a subroutine to sort.
'''
# the digit represented by exp. 
def countingSort(arr, exp1): 
  
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]//exp1) 
        count[ (index)%10 ] += 1
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]//exp1) 
        output[ count[ (index)%10 ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
  
# Method to do Radix Sort 
def radixSort(arr): 
  
    # Find the maximum number to know number of digits 
    max1 = max(arr) 
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1/exp > 1: 
        print(exp)
        countingSort(arr,exp) 
        exp *= 10
  
# Driver code to test above 
arr = [ 170, 45, 75, 90, 802, 24, 2, 66] 
radixSort(arr) 
  
for i in range(len(arr)): 
    print(arr[i]), 
  
  
# This code is contributed by Mohit Kumra 

# Search
# Linear search - visit each item and compare one by one, inefficient
# Interpolation Search

import collections
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    # Check for the visisted and unvisited nodes
    # DFS (Depth First Traversal)
    def dfs(self, start, visited = None):
        if visited is None:
            visited = set()

        visited.add(start)
        self.marked(start)
        
        for next in self.gdict[start] - visited:
            self.dfs(next, visited)

    # BFS (Breadth First Search)    
    def bfs(self, startnode):
    # Track the visited and unvisited nodes using queue
        seen, queue = set([startnode]), collections.deque([startnode])
        while queue:
            vertex = queue.popleft()
            self.marked(vertex)
            for node in self.gdict[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)

    def marked(self, n):
        print(n)

# The graph dictionary
gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }
g = graph(gdict)
g.bfs("a")


# min steps to visit all vertices in graph


from math import inf
from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        # 1 <= graph.length <= 12
        # 0 <= graph[i].length < graph.length

        nodeCount = len(graph)
        
        # NOTE
        # We are using BFS here because it's better suited for 'shortest path'
        # types of problems. DFS solution is also viable though.

        # Thoughts:
        # 0. explore all possible paths for each number of steps from step 1 
        # 1  define initial state [0...0] and target state [1...1]
        # 1. start at each node, do BFS to try reaching all other nodes.
        # 2. Must keep track of visited nodes, else infinite loop may happen.
        # 3. But each node may have to be visited multiple times, as described in the problem
        #    statement. So we cannot be too strict in limiting searches
        # 4. We must describe the state during a search, we need:
        #    - The current node we are on
        #    - Nodes we have visited (Notice the order does not matter in this case, that's a key)

        # each search is described by (currentNode, visited)
        # same search does _not_ have to be repeated, since if re-visited with
        # the same state, it would yield the same result.
        # NOTE this does not prevent revisiting the same node again,
        # it just prevents revisiting it with the same STATE!

        # Since the input size is restricted, we can use a number to encode
        # which nodes have been visited -- the i-th bit is on iff node i has been visited

        # conceptually masks[k] indicates that only node k has been visited
        masks = [1 << i for i in range(nodeCount)]
        # used to check whether all nodes have been visited (11111...111)
        allVisited = (1 << nodeCount) - 1
        queue = deque([(i, masks[i]) for i in range(nodeCount)])
        steps = 0

        # encoded_visited in visited_states[node] if
        # (node, encoded_visited) has been pushed onto the queue
        visited_states = [{masks[i]} for i in range(nodeCount)]
        # states in visited_states will never be pushed onto queue again

        while queue:
            # number of nodes to be popped off for current steps size
            # this avoids having to store steps along with the state
            # which consumes both time and memory
            count = len(queue)
            origin_cnt = count

            while count:
                currentNode, visited = queue.popleft()
                if visited == allVisited:
                    return steps

                # start bfs from each neighbor
                for nb in graph[currentNode]:
                    new_visited = visited | masks[nb]
                    print(origin_cnt, currentNode, nb, steps+1, bin(new_visited)[2:], bin(allVisited)[2:])
                    # pre-check here to for efficiency, as each steps increment may results
                    # in huge # of nodes being added into queue
                    if new_visited == allVisited:
                        return steps + 1
                    if new_visited not in visited_states[nb]:
                        visited_states[nb].add(new_visited)
                        queue.append((nb, new_visited))

                count -= 1
            steps += 1
        # no path which explores every node
        return inf

# test cases:
g = [[1,2,3],[0],[0],[0]]
s = Solution()
s.shortestPathLength(g)


# Searches K'th element from array
'''
method 1: Quick Sort = O(nlogn)
method 2: Min Heap = O(n+klogn)
method 3: Quick Select (pick pivot and stop when pivit in K'th pos) = O(n) average
method 4: Randomized QuickSelect. - expected O(n), worst case O(n**2)
method 5: Balanced QuickSelect - worst case O(n)
'''
# Balanced QuickSelect
'''
Selecting a pivot that divides array in a balanced way (there are not very few elements on one side and many on another side). 
After the array is divided in a balanced way, we apply the same steps as used in quickSelect() to decide whether to go left or right of the pivot.
Following is complete algorithm.
kthSmallest(arr[0..n-1], k)
1) Divide arr[] into ⌈n/5⌉ groups where size of each group is 5 except possibly the last group which may have less than 5 elements.
2) Sort the above created ⌈n/5⌉ groups and find median of all groups. Create an auxiliary array ‘median[]’ and store medians of all ⌈n/5⌉ groups in this median array.
// Recursively call this method to find median of median[0..⌈n/5⌉-1]
3) medOfMed = kthSmallest(median[0..⌈n/5⌉-1], ⌈n/10⌉)
4) Partition arr[] around medOfMed and obtain its position.
pos = partition(arr, n, medOfMed)
5) If pos == k return medOfMed
6) If pos > k return kthSmallest(arr[l..pos-1], k)
7) If pos < k return kthSmallest(arr[pos+1..r], k-pos+l-1)
'''


# Pattern Searching
'''
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of 
pat[] in txt[]. You may assume that n > m.

Method 1: Naive algorithm - O(m(n-m+1))
Mehtod 2: KMP - O(n)
The KMP matching algorithm uses degenerating property (pattern having same sub-patterns appearing more than once in the pattern) 
of the pattern and improves the worst case complexity to O(n). The basic idea behind KMP’s algorithm is: whenever we detect a mismatch 
(after some matches), we already know some of the characters in the text of the next window. We take advantage of this information to 
avoid matching the characters that we know will anyway match
Method 3: 
'''



# Minimum spanning tree
'''
Spanning Tree: Given a connected and undirected graph, a spanning tree of that graph is a subgraph that is a tree and connects all 
the vertices together
Minimum Spanning Tree (MST): spanning tree with weight less than or equal to the weight of every other spanning tree. The weight 
of a spanning tree is the sum of weights given to each edge of the spanning tree.

# edges of MST: V-1

Kruskal’s algorithm: O(ElogE) or O(ElogV) (Greedy algoritm)
1. Sort all the edges in non-decreasing order of their weight.
2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
3. Repeat step#2 until there are (V-1) edges in the spanning tree.

'''


# Recursion vs Iteration
'''
Recursion:  Memory (stack) overflow and inefficient but simplicity and easy to understand in most of the cases 
So, use either iteration or recursion according to the task you want to perform. If simplicity is required and memory overflow is not a major issue 
then use recursion otherwise go with iterations.
'''

