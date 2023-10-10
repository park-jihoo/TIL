---
id: 4ffcbbdd-3d96-4cb4-8ef1-56e0344af2cc
title: Computing and Programming
created_time: 2023-08-07T06:46:00.000Z
last_edited_time: 2023-09-09T03:23:00.000Z
하위 항목: []
subclass: 2023_QE
class: Coursework
작성일시: 2023-08-07T06:46:00.000Z
상위 항목: []

---

# Python Programming Basics

    - Types: Every value in python has particular type(int, float)

    - Call expressions: an expression that calls a function

    - Values do not have any meaning, so now we want to name them as **Variable**

    - You can create a new variable by naming and assigning it a value

    - String type is a type to represent text values

    - Type **bool** has only two values True or False

    - Class: another type of **object** that has variables and functions similar to module

    - Object Oriented Programming

    	- Encapsulation: Contain related information in an object

    	- Abstraction: Expose only high level interfaces to the outside world

    	- Inheritance: Child classes inherit data and behaviors from parent class

    	- Polymorphism: A single method acts in a different way depending on objects

# Recursion, Search and Sorting algorithms

    ## Search

    	### Linear Search

    		- Search from the first item to the last item sequentially

    			```python
    			def linear_search(L, value):
    				for i in range(len(L)):
    					if L[i] == value:
    						return i
    				return -1
    			```

    		- Time complexity: Linearly Increasing

    	### Binary Search

    		- One evaluation removes **half** of candidate entries

    			```python
    			def binary_search(L, v):
    				start, end = 0, len(L)-1
    				while start != end + 1:
    					mid = (start + end) // 2
    					if L[mid] < v:
    						start = mid + 1
    					else:
    						end = mid - 1
    				if start < len(L) and L[start] == v:
    					return start
    				else:
    					return -1
    			```

    		- Time complexity: proportional to log 2

    ## Sort

    	### Selection Sort

    		- Find the minimum value of the unsorted list and swap it with the leftmost entry

    			```python
    			def selection_sort(L):
    				for i in range(len(L)):
    					smallest = i
    						for j in range(i+1, len(L)):
    							if L[j]<L[smallest]:
    								smallest = j
    					L[i], L[smallest] = L[smallest], L[i]
    			```

    		- Time complexity O(n^2)

    	### Insertion Sort

    		- Insert the leftmost item of the unsorted list to the proper location of the sorted list

    			```python
    			def insertion_sort(L):
    				for i in range(1, len(L)):
    					for j in range(i, 0, -1):
    						if L[j-1]>L[j]:
    							L[j-1],L[j]=L[j],L[j-1]
    						else:
    							break
    			```

    		- Time complexity O(n^2)

    	### Merge Sort

    		- Idea

    			- Divide the whole list into two sub-lists

    			- Sort the left sublist and the right sublist separately

    			- Merge the two sorted sublist in sorted way

    			```python
    			def merge(L, first, mid, last):
    				k = first
    				sub1 = L[first:mid+1]
    				sub2 = L[mid+1:last+1]
    				i=j=0
    				while i < len(sub1) and j < len(sub2):
    					if sub1[i] <= sub2[j]:
    						L[k] = sub1[i]
    						i += 1
    					else:
    						L[k] = sub2[j]
    						j += 1
    					k += 1
    			```

    		- Time complexity O(n\log n)

    ## Recursion

    	- Function that calls itself during execution

    	- Recursion can happen when solving a problem includes solving subproblems having the same structure

# Linked Lists

    - Create nodes and link them.

    - Single linked lists: a linked lists whose node has a single link

    	- Every node can be access through the **first** node

    	- addFirst(), getFirst()

    	- To get size, navigate whole list which is inefficient

    	- Add special variable that caches the size information

    - Sentinel Node: Dummy node which is alternative of first node

    	- Sentinel is never None

    	- Sentinel.next is the real first node

    	- Then, appending with sentinel doesn’t make any special case

# Binary Search Trees

    ## Rooted Binary Tree

    	- Rooted tree: there is only one root node

    	- Every node has one parent

    	- A node without a child is leaf

    	- Rooted binary tree: each node has at most 2 children nodes

    ## Binary Search Trees

    	- A binary search tree is a rooted binary tree that has 2 properties

    	- For every node x,

    		- x’s value is unique in the whole tree

    		- Every node y in the left subtree of node x has value less then x’s value

    		- Every node z in the right subtree of the node x has value greater than x’s value

    	### Search

    	```python
    	class BST():
    		def __searchHelp(self, curNode: TreeNode, x: int) -> TreeNode:
    			if not curNode:
    				return None
    			if x == curNode.val:
    				return curNode
    			elif x < curNode.val:
    				return self.__searchHelp(curNode.left, x)
    			else:
    				return self.__searchHelp(curNode.right, x)
    		def search(self, x: int) -> TreeNode:
    			return self.__searchHelp(self.root, x)
    	```

    	### Insert

    	```python
    	class BST():
    		def __insertHelp(self, curNode: TreeNode, x: int) -> TreeNode:
    			if not curNode:
    				return TreeNode(x)
    			if x < curNode.val:
    				curNode.left = self.__insertHelp(curNode.left, x)
    			elif x > curNode.val:
    				curNode.right = self.__insertHelp(curNode.right, x)
    			return curNode
    		def insert(self, x: int) -> None:
    			self.root = self.__insertHelp(self.root, x)
    	```

    	### Delete

    	- Delete a leaf node: search the node and simply cut parent’s link

    	- Delete node with one child: search the node and cut parent’s link. Move the child node to where the target node was

    	- Delete node with two children: search the node using its key value and delete either of two:

    		- The rightmost node in the left subtree

    		- The leftmost node in the right subtree

    		and place its copy at the target node’s location

# Trees and Graphs

    ## Trees

    	- A tree comprises a set of nodes that are connected to each other

    	- There is only one path between two nodes in a tree

    	### Breadth-First Traversal

    	- Visit nodes from left to right, and from top to bottom

    		```python
    		class Tree():
    			def visit(self, node: TreeNode):
    				print(node.val)
    			def BFT(self):
    				if self.root == None:
    					return
    				q = [self.root]
    				while q:
    					curNode = q.pop(0)
    					self.visit(curNode)
    					for childNode in curNode.child:
    						if childNode:
    							q.append(childNode)
    		```

    	- Use doubly-linked list(deque) to make them faster!

    	### Depth-First Traversal

    	- Three types: preorder, inorder, postorder

    	- Preorder: visit a node before traversing its children from left to right

    		```python
    		class Tree():
    			def visit(self, node: TreeNode):
    				print(node.val)
    			def __DFT_preorderHelp(self, curNode: TreeNode):
    				if curNode == None:
    					return
    				self.visit(curNode)
    				for childNode in curNode.child:
    					self.__DFT_preorderHelp(childNode)
    			def DFT_preorder(self): 
    				self.__DFT_preorderHelp(self.root)
    		```

    	- Inorder: traverse a node’s children from left to right and visit the node in the middle

    		```python
    		class Tree():
    			def visit(self, node: TreeNode):
    				print(node.val)
    			def __DFT_inorderHelp(self, curNode: TreeNode):
    				if curNode == None:
    					return
    				for i in range(len(curNode.child)): 
    					if i == 1:
    						self.visit(curNode) 
    					self.__DFT_inorderHelp(curNode.child[i])
    			def DFT_inorder(self): 
    				self.__DFT_inorderHelp(self.root)
    		```

    	- Postorder: Visit a node after traversing its children from left to right

    		```python
    		class Tree():
    			def visit(self, node: TreeNode):
    				print(node.val)
    			def __DFT_postorderHelp(self, curNode: TreeNode): 
    				if curNode == None:
    					return
    				for i in range(len(curNode.child)):
    					self.__DFT_postorderHelp(curNode.child[i]) 
    					self.visit(curNode)
    			def DFT_postorder(self): 
    				self.__DFT_postorderHelp(self.root)
    		```

    ## Graphs

    	- A graph comprises a set of nodes and a set of edges, each of which connects two nodes

    	- A simple graph is a graph that doesn’t have loop or parallel edge

    	- Vertex is a node, and edge is a pair of vertices.

    	- Two vertices which have an edge between are adjacent

    	- A path is a sequence of vertices connected by edges

    	- A path with unique vertices is a simple path

    	- A cycle is a path where the first and last vertices are same

    	### DFS - Preorder

    	```python
    	class undi_graph():
    		def __DFTHelp(self, visited: list, v: int) -> None:
    			if not visited[v]:
    				visited[v] = True
    				print(v)
    				for w in self.neighbor[v]:
    					self.__DFTHelp(visited, w)
    	
    		def DFT(self) -> None:
    			if self.V:
    				visited = {}
    				for v in self.V:
    					visited[v] = False
    				for v in self.V:
    					self.__DFTHelp(visited, v)
    	```

    	- We should mark the nodes we already visited to handle cycles

    	- When you want to know if two vertices are connected

    	- When you want to know if all vertices in a graph are connected

    	- When you want to know how many disjoint islands are in a graph

    	- When you want to know if a graph has a cycle

# Hash

    ## Data Indexed Arrays

    	- A data-indexed array has all possible data as its indices

    	- Initially, all values of the array are False, meaning the array is empty

    	- When data x is added to the array, xth element becomes True

    	- In the case of english word

    		- Map each 26 english alphabets to an integer

    		- Every lower-case word can be represented as a unique integer

    	- What about integer overflow? Use hash function

    	### Data-Indexed Array with Chains

    	- Each element is initially None but becomes a linked list when an item is added

    ## Hash

    	### Hash Table

    	- A table that stores data by using a valid index that is computed as follows

    		```mermaid
    		graph LR
    		  Data --> A[Hash function]
    			A-->B[Hash value]
    			B-->C[reduction]
    			C-->D[Valid index]
    		```

    	- How can we improve our hash table to achieve O(1)?

    	### Hash Table - Resizing

    	- Increase of using a fixed M, we can increase M as N increases.

    	- The hash table’s chains now have less than 1.5 items on average

    	- Resizing a hash table with N items require O(N) time to redistribute all N items

    	### Hash Function

    	- Using a small prime number as a base is typical

# Bits, Data types, and Operations

    ## Bits(Binary Digits)

    	- Devices react to the presence or absence of voltages in electronic circuits

    	- Detection with margin: Rough detection when a computer expects 0V for absence and 2.9V for presence

    ## Data Types

    	- Boolean Types: True or False

    	- Integer representation

    		- Unsigned Integers: A data type that represents positive integers and zero

    		- Signed Integers: A data type that represents positive/negative integers and zero

    			- Use 2’s complement to represent a negative value (-X) so that X+(-X)=0 

    		- Operations: addition, subtraction(negate the subtrahend and perform addition), if overflow(operands are too big)

    	- Floating point

    		```undefined
    		N = (-1)^S\times1.fraction\times2^{exponent - 127}
    		```

    		- Floating point arithmetic is more complex than integer arithmetic

    		- Trade off between development cost and execution cost

    	- Hexagonal: a method to represent binary strings for human convenience

# Von Neumann model and Machine Code

    ## Von Neumann model

    	- A program is contained in memory

    	- Data for the program is either contained in the memory or obtained from the input devices

    	- A program instruction and data for its execution are sent from the memory to the processing unit

    	- The program instruction is executed in the processing unit and the result is sent to the memory

    	- The program results are provided by the output devices

    	- The entire procedure is managed by the control unit

    	### Components

    	- Memory: has many locations, each of which has its address and scan/score data

    		- Register: a small amount of fast storage that the processor can quickly access

    	- Processing unit: the simplest processing unit is the ALU(arithmetic and logic unit)

    		- ALU normally process data elements of a fixed size

    		- The data elements are called “words”

    	- Input and output: devices for getting data into and out of computer memory

    	- Control Unit: It’s like the conductor of an orchestra

    		- Instruction Register + Program Counter

    ## Instruction

    	- Instruction is the most basic unit of computer processing

    	- Instruction Processing

    		```mermaid
    		graph TD
    		  A[Fetch instruction from memory] --> B[Decode instruction]
    			B --> C[Evaluate address]
    			C --> D[Fetch operands]
    			D --> E[Execute operations]
    			E --> F[Store result]
    			F --> A
    		```

    	- Fetch: load the instruction in the memory location into IR

    	- Decode: Identify the opcode - operation ID

    	- Evaluation Address: For instruction that require memory access, compute address used for access

    	- Fetch operands: obtain source operands needed to perform operation

    	- Execute: perform the operation using the source operands

    	- Store Result: Write results to destination register

# C programming basics

    - Basic C Program

    	```c
    	#include<stdio.h>
    	int main(void){
    		printf("Hello World!\n");
    		return 0;
    	}
    	```

    - C uses compiler, which is different with python(interpreter)

    - We need one more step, compiling

    - Preprocessor macros: start with # and doesn’t end with ; This is replaced by other C codes in the C preprocessor stage of compilation

    - xx.h is a header file that holds declarations useful among multiple source files

    - Comment: one-line comment(//), multi-line comment(/* */)

    - #define: used to create fixed values within a program

    ## Variables in C

    	- Compiler generates the full set of data movement operations

    	- Variable type is immutable

    	- Variable Scope

    		- Local variable: A variable is declared within a block then it’s visible until the end of the block

    		- Global variable: it’s a global variable that can be accessed anywhere in the program

    	- Initializer: Variable declaration with an initial value

    ## Operators in C

    	- Assignment or arithmetic, bitwise, logical

    	- Increment or decrement operators have subtle difference: evaluate and increment or increment and evaluate

    ## Memory in C

    	- Global variables are stored in global data  section

    	- Local variables are stored in run-time stack

    	- Another region reserved for dynamically allocated data called heap

    ## Functions in C

    	- Definition: header, any variable declared in the body is local to the function

    	- Call: the caller must transmit proper arguments. Calling is possible only when the callee is declared before

    	- Declaration(function prototype): informs the compiler about relevant properties

    	### Memory Operation

    	- Calling(Passing arguments to the function)

    	- Start Callee(Reserve stack for the function)

    	- End Callee(Return)

    	- Return to caller

    	> 📖 C uses stack to manage memory operation of a function call

    ## Pointers

    	- A pointer variable contains an address of a memory object

    	- Address operator & and indirection operator *

    	- Swapping can be operated with call by reference

    	- Null pointer: A special case pointer that points to nothing

# I/O in C

    - One Character I/O: putchar, getchar

    - Buffered I/O: keyboard input is buffered until we press Enter

    - Formatted I/O: printf, scanf(prints/scans out ASCII text embedded with values)

    ### File I/O

    - File pointer: a pointer that points to a type FILE

    - fopen() returns a file pointer to the physical file “file name”

    - fgetc, fputc, fscanf, fprintf

# Dynamic data structures in C

    ## Structures

    	- A convenient way of representing objects that are best represented by combinations of the basic data types

    	- Declaration, accessing members, memory allocation

    	- C structure enable programmers to define their own aggregate type by typedef

    ## Dynamic memory allocation

    	- Allocation: malloc function

    		- Parameter: requested memory size, returns a pointer to the reserved block or NULL when failed

    	- Deallocation: free

# Algorithm Basics
