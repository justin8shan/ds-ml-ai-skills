# command line input:
# use input function
do= input(‘What would you like to do?’).split()

# use arg


#list
'''
Allow heterogeneous data element: which is less efficient than array
The items in list are stored next to each other in memory
time complexity: O(n)
'''
ls = [1,2,3]
ls.append([4]) # add element [1,2,3,[4]]
ls.pop(index=-1) # default pop last element 
ls.pop() # pop last element like stack
ls.pop(0) # pop first element like queue
ls.remove(value) # del ls[0]
ls.sort(reverse=False) # False is Asc, True is Desc
sorted(ls) # sort list by don't modify original
ls.reverse() # another way: l[::-1] which doesn't modify orignial
ls.copy()
ls.clear()
ls.count('a') # count occurences of input element 
ls.extend([4,5]) # merge list [1,2,3,4,5], equivilent to ls + [4, 5]
len(ls)

# dict: hash map
d = {'Python': 2, 'Java': 1, "C": 3}
len(d)
d.popitem() # pop last item from dictionary
d.keys() # return list of keys
d.values() # list of values
d.items() # list of pairs in tuple
d.clear()

# to remove element
del d['C'] or d.pop('C',default)
del d

#sort dictionary by values
sorted(d.items(), key = lambda x: x[1]) # output is : [('Java', 1), ('Python', 2), ('C', 3)]


{**d1, **d2} # merge dictionary
d1.update(d2) # add d2 to d1
d1.copy().update(d2)

# tuple
t = (1, 2, 3, 'edureka') # non mutable comparing to list
t1 + t2 # merge tuple

# set: unordered unique collection
# set is implemented as hash set in python

v in s: O(1)

s =set() # empty set
s = {1, 2, 3}
s2 = {3, 4, 5, 6}
s.add(4)
s.union(s2) or s|s2 # {1,2,3,4,5,6}
s.intersection(2) or s&s2 # {3,4}
s.difference(s2) or s-s2 # {1,2}
s.symmetric_difference(s2) or s^s2 # {1,2,5,6	}

# Counter - dict subclass
from collections import Counter, defaultdict

c = Counter(['foo','boo']) # return {"foo":1, "boo":1}

c = Counter()
ids = [1,1,1,2,3,2]
for id in ids:
    c[id] +=1

# sorting counters
c.most_common()

# dictonary with key -value list pair
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list) # build a empty dictionary with values default as empty list. This is to save effort to initialize list when adding new key
for k, v in s:
    d[k].append(v) 

sorted(d.items()) # return [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]



#array
'''
Array is a data structure used to store homogeneous elements at contiguous locations. Size of an array must be provided before storing data.
complexity: 

Let size of array be n.
Accessing Time: O(1) [This is possible because elements
                       are stored at contiguous locations]   
Search Time:   O(n) for Sequential Search: 
               O(log n) for Binary Search [If Array is sorted]
Insertion Time: O(n) [The worst case occurs when insertion 
                     happens at the Beginning of an array and 
                     requires shifting all of the elements]
Deletion Time: O(n) [The worst case occurs when deletion 
                     happens at the Beginning of an array and 
                     requires shifting all of the elements]
'''
import array

arr = array.array('i',[1,2,3]) # i for integer type
arr[index] # access like list
arr.append(4)
arr.pop(index=-1) # default -1
arr.remove(4)
arr.count(4)
arr.reverse()
arr.insert(index,value)
arr1 + arr2

sorted(arr,reverse = True)

for a in arr: 
	print(a)

#linked list
'''
store elements in separate object
including singly linked list, Doubly linked list, Circular linked list

complexity:
Accessing time of an element : O(n)
Search time of an element : O(n)
Insertion of an Element : O(1) [If we are at the position 
                                where we have to insert 
                                an element] 
Deletion of an Element : O(1) [If we know address of node
                               previous the node to be 
                               deleted] 

'''
# Python has no linked list shipped with standard library
# 
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def print_list(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    def add_head(self,newdata):
        NewNode = Node(newdata)
        NewNode.nextval = self.headval
        self.headval = NewNode

    def add_tail(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return

        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

    def insert(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode   

    def remove(self, Removekey):

        if (self.headval == None):
            return        

        current_node = self.head
        prev_node = None
        while ( current_node is not None):
            if current_node.dataval == Removekey:
                break
            prev_node = current_node
            current_node = current_node.next

        if prev_node and current_node:
        	# found and not head
        	prev_node.next = current_node.next

        elif prev_node is None:
        	# head node found
        	self.headval = current_node.next

# stack: LIFO 
'''
complexity: 

Insertion : O(1)
Deletion :  O(1)
Access Time : O(n) [Worst Case]
Insertion and Deletion are allowed on one end. 
'''

# Implemenation using deque module
from collections import deque

stack = deque()

stack.append(value)
stack.pop()

# Implemenation using queue module
from queue import LifoQueue 
stack = LifoQueue(maxsize = 3) 
stack.qsize()
stack.put('a')
stack.get()

# queue: FIFO
'''
complexity:
Insertion : O(1)
Deletion  : O(1)
Access Time : O(n) [Worst Case]
'''
# Implemenation using deque module
from collections import deque

queue = deque()
queue = deque([1,2,4,8])

queue.append(value)
queue.popleft()
# Implemenation using queue module
from queue import Queue 

q = Queue(maxsize = 3) 
q.put('3')
q.get()

# priority queue: pop minimum value from the queue
# similar to min heap
from queue import PriorityQueue

q = PriorityQueue(maxsize = 10)
q.put((3, 'abc'))
q.put((1, 'ddd'))
q.get() # pop (1, 'ddd')

# Binary tree
'''
The maximum number of nodes with ‘l’ levels = 2**l-1. 
Maximum number of nodes = 2**(h + 1) – 1.
Minimum possible height =  ceil(Log2(n+1)) - 1  
Time Complexity of Tree Traversal: O(n)
'''

# Binary Search Tree is special Binary tree
'''
The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.
Search :  O(h)
Insertion : O(h)
Deletion : O(h)
Extra Space : O(n) for pointers

h: Height of BST
n: Number of nodes in BST

If Binary Search Tree is Height Balanced, 
then h = O(Log n) 

BST provide moderate access/search (quicker than Linked List and slower than arrays).
BST provide moderate insertion/deletion (quicker than Arrays and slower than Linked Lists).

Examples : Its main use is in search application where data is constantly entering/leaving and data needs to printed in sorted order.

Balanced tree: usually mean height balanced tree: 
1) Left subtree of T is balanced
2) Right subtree of T is balanced
3) The difference between heights of left subtree and right subtree is not more than 1. 

AVL tree is a self-balancing Binary Search Tree (BST) where the difference between heights of left and right subtrees cannot 
be more than one for all nodes.

Comparison with Red Black Tree
The AVL tree and other self-balancing search trees like Red Black are useful to get all basic operations done in O(log n) time. 
The AVL trees are more balanced compared to Red-Black Trees, but they may cause more rotations during insertion and deletion. 
So if your application involves many frequent insertions and deletions, then Red Black trees should be preferred. And if the 
insertions and deletions are less frequent and search is the more frequent operation, then AVL tree should be preferred over Red Black Tree.

Red-Black Tree is a self-balancing Binary Search Tree (BST) where every node follows following rules.
1) Every node has a color either red or black.
2) Root of tree is always black.
3) There are no two adjacent red nodes (A red node cannot have a red parent or red child).
4) Every path from a node (including root) to any of its descendant NULL node has the same number of black nodes.

'''

class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

	# Insert method to create nodes
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
            	print(str(data) + ' is already there')
        else:
            self.data = data

	# findval method to compare the value with nodes
    def findval(self, lkpval):

        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"

            self.left.findval(lkpval)
            
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            self.right.findval(lkpval)
            
        else:
            print(f'{self.data} is found')


	# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        elif self.right:
        	print('None')

        print(self.data)

        if self.right:
            self.right.PrintTree()
        elif self.left:
        	print('None')

# Heap is a special type of tree
'''
Heap is a special data structure and it cannot be used for searching of a particular element.

Max Heap or Min Heap
Max-Heap: In a Max-Heap the key present at the root node must be greatest among the keys present at all of it’s children. 
The same property must be recursively true for all sub-trees in that Binary Tree.
Min-Heap: In a Min-Heap the key present at the root node must be minimum among the keys present at all of it’s children. 
The same property must be recursively true for all sub-trees in that Binary Tree.
Complexity
Get Minimum in Min Heap: O(1) [Or Get Max in Max Heap]
Extract k Minimum Min Heap: O(Log n) [Or Extract k Max in Max Heap]
Decrease Key in Min Heap: O(Log n)  [Or Decrease Key in Max Heap]
Insert: O(Log n) 
Delete: O(Log n)
Heapify: O(Log n)

A Min Heap is a Complete Binary Tree. A Min heap is typically represented as an array. The root element will be at Arr[0]. 
For any ith node, i.e., Arr[i]:
Arr[(i -1) // 2] returns its parent node.
Arr[(2 * i) + 1] returns its left child node.
Arr[(2 * i) + 2] returns its right child node.
'''
# Min Heap implementation
import sys 
  
class MinHeap: 
  
    def __init__(self, maxsize): 
        self.maxsize = maxsize 
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1) 
        self.Heap[0] = -1 * sys.maxsize 
        self.FRONT = 1
  
    # Function to return the position of 
    # parent for the node currently 
    # at pos 
    def parent(self, pos): 
        return pos//2
  
    # Function to return the position of 
    # the left child for the node currently 
    # at pos 
    def leftChild(self, pos): 
        return 2 * pos 
  
    # Function to return the position of 
    # the right child for the node currently 
    # at pos 
    def rightChild(self, pos): 
        return (2 * pos) + 1
  
    # Function that returns true if the passed 
    # node is a leaf node 
    def isLeaf(self, pos): 
        if pos > (self.size//2) and pos <= self.size: 
            return True
        return False
  
    # Function to swap two nodes of the heap 
    def swap(self, fpos, spos): 
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 
  
    # Function to heapify the node at pos 
    def minHeapify(self, pos): 
  
        # If the node is a non-leaf node and greater 
        # than any of its child 
        if not self.isLeaf(pos): 
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]): 
  
                # Swap with the left child and heapify 
                # the left child 
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
                    self.swap(pos, self.leftChild(pos)) 
                    self.minHeapify(self.leftChild(pos)) 
  
                # Swap with the right child and heapify 
                # the right child 
                else: 
                    self.swap(pos, self.rightChild(pos)) 
                    self.minHeapify(self.rightChild(pos)) 
  
    # Function to insert a node into the heap: add to the end of heap and move up
    def insert(self, element): 

        if self.size >= self.maxsize : 
            return
        self.size+= 1
        self.Heap[self.size] = element 
  
        current = self.size 
  
        while self.Heap[current] < self.Heap[self.parent(current)]: 
            self.swap(current, self.parent(current)) 
            current = self.parent(current) 
  
    # Function to print the contents of the heap 
    def Print(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1])) 
  
    # Function to build the min heap from bottom-up starting from last parent node 
    def minHeap(self): 
  
        for pos in range(self.size//2, 0, -1): 
            self.minHeapify(pos) 
  
    # Function to remove and return the minimum 
    # element from the heap 
    def remove(self): 
  
        popped = self.Heap[self.FRONT] 
        self.Heap[self.FRONT] = self.Heap[self.size] 
        self.size-= 1
        self.minHeapify(self.FRONT) 
        return popped 


# Create minHeap with built-in library named heapq
import heapq

h = [21,1,45,78,3,5]
heapq.heapify(h) #convert list to heap
heapq.heappush(h,8) #push new element to heap
heapq.heappop(h) #
heapq.heapreplace(h,10) # remove smallest and add new value

# Heap elements can be tuples as long as first element is comparable, if first element are repeating, 
# 2nd element should be comparable
h = []
heappush(h, (5, 'write code'))
heappush(h, (7, 'release product'))
heappush(h, (1, 'write spec'))
heappush(h, (3, 'create tests'))
heappop(h)

# Hashing
'''
Hashing function: A function that converts a given big input key to a small practical integer value. The mapped 
integer value is used as an index in hash table. A good hash function should have following properties
1) Efficiently computable.
2) Should uniformly distribute the keys (Each table position equally likely for each key)
Complexity:
Space : O(n)
Search    : O(1) [Average]    O(n) [Worst case]
Insertion : O(1) [Average]    O(n) [Worst Case]
Deletion  : O(1) [Average]    O(n) [Worst Case]

Hashing seems better than BST for all the operations. But in hashing, elements are unordered and in BST elements 
are stored in an ordered manner. Also BST is easy to implement but hash functions can sometimes be very complex 
to generate. In BST, we can also efficiently find floor and ceil of values.

Example : Hashing can be used to remove duplicates from a set of elements. Can also be used find frequency of all items. 
For example, in web browsers, we can check visited urls using hashing. In firewalls, we can use hashing to detect spam. 
We need to hash IP addresses. Hashing can be used in any situation where want search() insert() and delete() in O(1) time.
'''
d = dict() # hashmap
d = {} # hashset

# Graph
'''
A Graph consists of a finite set of vertices(or nodes) and set of Edges which connect a pair of nodes.
Undirected Graph  vs Directed Graph
Weighted Graph  vs. Unweighted Graph

Two type of representation: Adjacency Matrix , Adjacency Linked List

Time Complexities in case of Adjacency Matrix :
Traversal :(By BFS or DFS) O(V^2)
Space : O(V^2)

Time Complexities in case of Adjacency List :
Traversal :(By BFS or DFS) O(E*logV)
Space : O(V+E)
'''
# here graph is represented with dictionary {vertice: edge}
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

# Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

    def addVertex(self, vrtx):
       if vrtx not in self.gdict:
            self.gdict[vrtx] = []


    def edges(self):
        return self.findedges()
# Find the distinct list of edges

    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename        

    def AddEdge(self, edge):
        edge = set(edge) # edge {'a', 'b'}
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]


# Create the dictionary with graph elements
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)

print(g.getVertices())


# Tries 
'''
Also known as radix tree or prefix tree
Efficient data structure for searching words in dictionaries
Search complexity: O(M), M = word (or key) length to be searched 
much faster than BST which is O(M*log N), N is number of keys in tree
The advantages of Trie are there are no collisions (like hashing) so worst case time complexity is O(n). Also, 
the most important thing is Prefix Search. With Trie, we can find all words beginning with a prefix (This is not possible with Hashing). 
The only problem with Tries is they require a lot of extra space.
Insert time : O(M) where M is the length of the string.
Search time : O(M) where M is the length of the string.
Space : O(ALPHABET_SIZE * M * N) where N is number of 
        keys in trie, ALPHABET_SIZE is 26 if we are 
        only considering upper case Latin characters.
Deletion time : O(M)

Example : The most common use of Tries is to implement dictionaries due to prefix search capability. Tries are also well suited for
implementing approximate matching algorithms, including those used in spell checking. It is also used for searching 
Contact from Mobile Contact list OR Phone Directory.
'''
# Trie implementation
class TrieNode: 
      
    # Trie node class 
    def __init__(self): 
        self.children = [None]*26 # store next TrieNode for each chacter
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self): 
      
        # Returns new trie node (initialized to NULLs) 
        return TrieNode() 
  
    def _charToIndex(self,ch): 
          
        # private helper function 
        # Converts key current character into index 
        # use only 'a' through 'z' and lower case 
          
        return ord(ch)-ord('a') 
  
  
    def insert(self,key): 
          
        # If not present, inserts key into trie 
        # If the key is prefix of trie node,  
        # just marks leaf node 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
  
            # if current character is not present 
            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index] 
  
        # mark last node as leaf 
        pCrawl.isEndOfWord = True
  
    def search(self, key): 
          
        # Search key in the trie 
        # Returns true if key presents  
        # in trie, else false 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
            index = self._charToIndex(key[level]) 
            if not pCrawl.children[index]: 
                return False
            pCrawl = pCrawl.children[index] 
  
        return pCrawl != None and pCrawl.isEndOfWord 
  
# driver function 
def main(): 
  
    # Input keys (use only 'a' through 'z' and lower case) 
    keys = ["the","a","there","anaswe","any", 
            "by","their"] 
    output = ["Not present in trie", 
              "Present in trie"] 
  
    # Trie object 
    t = Trie() 
  
    # Construct trie 
    for key in keys: 
        t.insert(key) 
  
    # Search for different keys 
    print("{} ---- {}".format("the",output[t.search("the")])) 
    print("{} ---- {}".format("these",output[t.search("these")])) 
    print("{} ---- {}".format("their",output[t.search("their")])) 
    print("{} ---- {}".format("thaw",output[t.search("thaw")])) 
  
if __name__ == '__main__': 
    main() 

# Segment Tree
'''
This data structure is usually implemented when there are a lot of queries on a set of values. These queries involve 
minimum, maximum, sum, .. etc on a input range of given set. Queries also involve updation of values in given set. 
Segment Trees are implemented using array.
Construction of segment tree : O(N)
Query : O(log N)
Update : O(log N)
Space : O(N) [Exact space = 2*N-1]
Example : It is used when we need to find Maximum/Minumum/Sum/Product of numbers in a range.

'''

# Suffix Tree

'''
Suffix Tree is mainly used to search a pattern in a text. The idea is to preprocess the text so that search operation 
can be done in time linear in terms of pattern length. The pattern searching algorithms like KMP, Z, etc take time 
proportional to text length. This is really a great improvement because length of pattern is generally much smaller than text.

Suffix Tree is compressed trie of all suffixes, so following are very abstract steps to build a suffix tree from given text.
1) Generate all suffixes of given text.
2) Consider all suffixes as individual words and build a compressed trie.
Example : Used to find find all occurrences of the pattern in string. It is also used to find the longest repeated substring 
(when text doesn’t change often), the longest common substring and the longest palindrome in a string.
'''





