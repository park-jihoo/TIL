---
id: e5b41b7e-ffb1-4b7e-8eeb-7bdce31026ca
title: COMPUTING1 FINAL
created_time: 2021-07-13T00:24:00.000Z
last_edited_time: 2023-10-07T16:40:00.000Z
cover_image: https://www.notion.so/images/page-cover/solid_beige.png
icon_emoji: 🧞
하위 항목: []
subclass: 2022_Fall
class: Coursework
작성일시: 2021-07-13T00:24:00.000Z
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/solid_beige.png

---

# Strongly Connected Components

*   Strongly connected components of a directed graph G = (V,E) means a maximal set of vertice C \subseteq Vsuch that for every pair of vertices u, v \in C both u \rarr v and v \rarr u

*   The transposed graph contains the edges of graph G with their directions reversed. They have exactly the same, strongly connected components. \Theta(V+E)

*   How to get Strongly Connected components

    *   Call DFS(G) to compute finish times u.f for each vertex u

    *   Create G^\top

    *   Call DFS(G^\top), but in the main loop of DFS, consider the vertices in order of decreasing u.f calculated in 1

    *   Output the vertices of each tree in the depth-first forest formed in line 3 as separate SCCs.

*   Let C and C' be distinct strongly connected components in direct graph G = (V, E) and supose that f(C) > f(C') then E^\top contains no edge (v,u) such that u \in C' and v \in C

***

# Heaps

*   Binary trees are structures defined by a finite set of nodes that contain either no nodes or left and right subtrees.

*   Full binary tree’s node is either a leaf or has degree 2. Complete binary tree is a binary tree in which all leaves have the same depth

*   Heaps: An array object that we can view as a nearly complete binary tree

*   Root is A\[1], parent(i) returns \lfloor \frac {i}{2} \rfloor, left(i) returns 2i, right(i) returns 2i+1

*   Max heap: maximum element is stored at the root, min heap은 그 반대

*   MAX-HEAPIFY lets the value float down the max heap so that subtree obeys max heap property T(n) \leq T(\frac{2n}{3}) + \Theta(1)이므로 T(n) = O(\log n)

*   BUILD-MAX-HEAP: calling MAX-HEAPIFY from the bottom-up manner 즉 i = \lfloor n/2 \rfloor에서 시작해 1까지 내려감. Cost는 O(n)

*   Heapsort: Binary Tree를 heap으로 바꾸어 주는 것으로, A\[1]부터 하나하나 A\[n]과 바꿔나간 후 MAX-HEAPIFY시켜줌

*   Priority queues: queue 같은 data structure이긴 한데 Maximum, extract\_max와 같은 것들은 heap에서 쓰던 것들

***

# Binary Search Trees

*   Inorder(root-left-right), Preorder(root-left-right), Postorder(left-right-root)

*   How to find the successor of the Binary Tree? The Successor of node is the next node visited in an inorder traversal.  If right subtree of node is empty then successor is the lowest ancestor whose left child is also an ancestor

*   Deletion of binary Tree

    *   If z has no children, simply remove if

    *   If z has only one children, elevate that child to z’s position

    *   If z has two children, find successor y and move y to take z’s position in the tree

    ```mermaid
    graph TD
    Q((Q)) --> Z((Z))
    Z --> L((L))
    Z --> R((R))
    R --> Y((Y))
    Y --> NIL
    Y --> X((X))
    ```

    ```mermaid
    graph TD
    Q((Q)) --> Y((Y))
    Y --> L((L))
    Y --> R((R))
    R --> X((X))
    ```

*   Search, insert, delete시의 complexity : O(n)

***

# Red Black Trees

*   The worst case of BST: building BST by inserting in the order, then height h = O(n)이 되어 worst case가 됨. Height에 제약을 걸기 위해 등장한 것이 Red-Black Tree

*   Rotation: maintaining the BST prpoerty by rotations O(1)

    ```mermaid
    graph TD
    y((y)) --> x((x))
    y --> green{green}
    x --> blue{blue}
    x --> red{red}
    style green fill:lightgreen,color:white
    style blue fill:skyblue,color:white
    style red fill:#f88,color:white
    ```

    ```mermaid
    graph TD
    x((x)) --> blue{blue}
    x --> y((Y))
    y --> red{red}
    y --> green{green}
    style green fill:lightgreen,color:white
    style blue fill:skyblue,color:white
    style red fill:#f88,color:white
    ```

*   Red-black properties

    *   Every node is either red or black

    *   The root is black

    *   Every leaf(NIL) is black

    *   If a node is red then both its childrens are black

    *   For each node, all simple paths from the node to descendent leaves contain the same number of black nodes

*   Black-height bh(x) of node is the number of black nodes on the path from x to an external node

*   A red black tree with n internal nodes has height at most 2 \log (n+1), and time complexity의 maximal이 O(\log n)으로 계산됨

*   Insertion: inserting node z and check if node is consecutive red node. We try recoloring first, then go for a rotation

    ```python
    def insert(T, z):
    	x = T.root # node being compared with z
    	y = T.nil # parent of z
    	while not x == T.nil: # descend until reachiing the centinel
    		y = x
    		if z.key < x.key:
    			x = x.left
    		else:
    			x = x.right
    	z.p = y # insert z with parent y
    	if y == T.nil:
    		T.root = z #tree was empty
    	elif z.key < y.key:
    		y.left = z
    	else:
    		y.right = z
    	z.left =T.nil #both of z's children are centinel
    	z.right = T.nil
    	z.color = RED #new node will start at red
    	insertfixup(T, z) #correct violation
    ```

    *   InsertFixup

        *   Red uncle y: recolor, move z to the grandparent, fix it again with the new

            Graph

                  ```mermaid
                  graph TD
                  b1((15))
                  b1-->r1((5))
                  b1-->r2((17))
                  r1-->r3((3))
                  r1-->green
                  r3-->blue
                  r3-->yellow
                  r2-->red
                  r2-->black
                  style green fill:lightgreen,color:white
                  style blue fill:skyblue,color:white
                  style red fill:#f88,color:white
                  style black fill:black,color:white
                  style yellow fill:lightyellow
                  style b1 fill:black,color:white
                  style r1 fill:red,color:white
                  style r2 fill:red,color:white
                  style r3 fill:red,color:white
                  
                  ```
                  
                  ```mermaid
                  graph TD
                  r1((15))
                  r1-->b1((5))
                  r1-->b2((17))
                  b1-->r2((3))
                  b1-->green
                  r2-->blue
                  r2-->yellow
                  b2-->red
                  b2-->black
                  style green fill:lightgreen,color:white
                  style blue fill:skyblue,color:white
                  style red fill:#f88,color:white
                  style black fill:black,color:white
                  style yellow fill:lightyellow
                  style b1 fill:black,color:white
                  style r1 fill:red,color:white
                  style r2 fill:red,color:white
                  style b2 fill:black,color:white
                  
                  ```

        *   Black uncle y and z is a right child: left rotate around the parent

            Graph

            ````
              ```mermaid
              graph TD
              b1((15))
              b1-->r1((5))
              b1-->r2((17))
              r1-->green
              r1-->r3((6))
              r3-->blue
              r3-->yellow
              r2-->red
              r2-->black
              style green fill:lightgreen,color:white
              style blue fill:skyblue,color:white
              style red fill:#f88,color:white
              style black fill:black,color:white
              style yellow fill:lightyellow
              style b1 fill:black,color:white
              style r1 fill:red,color:white
              style r2 fill:red,color:white
              style r3 fill:red,color:white
              
              ```
              
              
              
              ```mermaid
              graph TD
              b1((15))
              b1-->r1((6))
              b1-->b2((17))
              r1-->r2((5))
              r2-->green
              r2-->blue
              r1-->yellow
              b2-->red
              b2-->black
              style green fill:lightgreen,color:white
              style blue fill:skyblue,color:white
              style red fill:#f88,color:white
              style black fill:black,color:white
              style yellow fill:lightyellow
              style b1 fill:black,color:white
              style r1 fill:red,color:white
              style r2 fill:red,color:white
              style b2 fill:black,color:white
              
              ```
              
            ````

        *   Black uncle y and z is a left child: right rotate around the grandparent and recolor

            Graph

                  ```mermaid
                  graph TD
                  b1((15))
                  b1-->r1((6))
                  b1-->b2((17))
                  r1-->r2((5))
                  r2-->green
                  r2-->blue
                  r1-->yellow
                  b2-->red
                  b2-->black
                  style green fill:lightgreen,color:white
                  style blue fill:skyblue,color:white
                  style red fill:#f88,color:white
                  style black fill:black,color:white
                  style yellow fill:lightyellow
                  style b1 fill:black,color:white
                  style r1 fill:red,color:white
                  style r2 fill:red,color:white
                  style b2 fill:black,color:white
                  
                  ```
                  
                  
                  
                  ```mermaid
                  graph TD
                  b1((6))
                  b1-->r1((5))
                  b1-->r2((15))
                  r1-->green
                  r1-->blue
                  r2-->yellow
                  r2-->b2((17))
                  b2-->red
                  b2-->black
                  style green fill:lightgreen,color:white
                  style blue fill:skyblue,color:white
                  style red fill:#f88,color:white
                  style black fill:black,color:white
                  style yellow fill:lightyellow
                  style b1 fill:black,color:white
                  style r1 fill:red,color:white
                  style r2 fill:red,color:white
                  style b2 fill:black,color:white
                  
                  ```

    *   Complexity: RB-Insert O(\log n), RB-Insertfixup O(\log n), sum O(\log n)

*   Deletion: BST Deletion처럼 하되, 움직이는 node의 original color이 BLACK이면 문제가 생김

    ```python
    def rb_transplant(T,u,v):
    	if u.p == T.nil:
    		T.root = v
    	elif u == u.p.left:
    		u.p.left = v
    	else:
    		u.p.right = v
    	v.p = u.p

    def rb_delete(T. z):
    	y = z
    	y_origin = y.color
    	if z.left == T.nil:
    		x=z.right
    		rb_transplant(T,z,z.right)
    	elif z.right == T.nil
    		x=z.left
    		rb_transplant(T,z,z.left)
    	else:
    		y= tree_minimum(z.right) #successor
    		y_origin = y.color
    		x = y.right
    	if not y== z.right
    		rb_transplant(T,y,y.right)
    		y.right=z.right
    		y.right.p=y
    	else:
    		x.p = y
    		rb_transplant(T,z,y)
    		y.left=z.left
    		y.left.p=y
    		y.color=z.color
    	if y_origin == BLACK:
    		rb_delete_fixup(T. x)
    ```

    *   DeleteFixUp

        *   The sibling w of x is RED: left rotate around x.p and recolor, then new sibling is BLACK

            Graph

                  ```mermaid
                  graph TD
                  B((B))
                  B-->A((A))
                  B-->D((D))
                  D-->C((C))
                  D-->E((E))
                  C-->purple
                  C-->green
                  A-->blue
                  A-->yellow
                  E-->red
                  E-->black
                  style green fill:lightgreen,color:white
                  style blue fill:skyblue,color:white
                  style red fill:#f88,color:white
                  style black fill:black,color:white
                  style yellow fill:lightyellow
                  style purple fill:purple,color:white
                  style A fill:black,color:white
                  style B fill:black,color:white
                  style C fill:black,color:white
                  style D fill:red,color:white
                  style E fill:black,color:white
                  
                  ```
                  
                  ```mermaid
                  graph TD
                  D((D))
                  D-->B((B))
                  D-->E((E))
                  B-->A((A))
                  B-->C((C))
                  C-->purple
                  C-->green
                  A-->blue
                  A-->yellow
                  E-->red
                  E-->black
                  style green fill:lightgreen,color:white
                  style blue fill:skyblue,color:white
                  style red fill:#f88,color:white
                  style black fill:black,color:white
                  style yellow fill:lightyellow
                  style purple fill:purple,color:white
                  style A fill:black,color:white
                  style D fill:black,color:white
                  style C fill:black,color:white
                  style B fill:red,color:white
                  style E fill:black,color:white
                  
                  ```

        *   The sibling w of x is BLACK with two BLACK children: recolor and move x to B and fix it again(여기서만 반복됨)

            Graph

                  ```mermaid
                  graph TD
                  B((B))
                  B-->A((A))
                  B-->D((D))
                  D-->C((C))
                  D-->E((E))
                  C-->purple
                  C-->green
                  A-->blue
                  A-->yellow
                  E-->red
                  E-->black
                  style green fill:lightgreen,color:white
                  style blue fill:skyblue,color:white
                  style red fill:#f88,color:white
                  style black fill:black,color:white
                  style yellow fill:lightyellow
                  style purple fill:purple,color:white
                  style A fill:black,color:white
                  style B fill:grey,color:white
                  style C fill:black,color:white
                  style D fill:black,color:white
                  style E fill:black,color:white
                  
                  ```
                  
                  ```mermaid
                  graph TD
                  B((B))
                  B-->D((D))
                  D-->C((C))
                  D-->E((E))
                  B-->A((A))
                  C-->purple
                  C-->green
                  A-->blue
                  A-->yellow
                  E-->red
                  E-->black
                  style green fill:lightgreen,color:white
                  style blue fill:skyblue,color:white
                  style red fill:#f88,color:white
                  style black fill:black,color:white
                  style yellow fill:lightyellow
                  style purple fill:purple,color:white
                  style A fill:black,color:white
                  style D fill:red,color:white
                  style C fill:black,color:white
                  style B fill:grey,color:white
                  style E fill:black,color:white
                  
                  ```

        *   The sibling w of x is BLACK with w’s RED left child, BLACK right child

            Graph

                  ```mermaid
                  graph TD
                  B((B))
                  B-->D((D))
                  D-->C((C))
                  D-->E((E))
                  B-->A((A))
                  C-->purple
                  C-->green
                  A-->blue
                  A-->yellow
                  E-->red
                  E-->black
                  style green fill:lightgreen,color:white
                  style blue fill:skyblue,color:white
                  style red fill:#f88,color:white
                  style black fill:black,color:white
                  style yellow fill:lightyellow
                  style purple fill:purple,color:white
                  style A fill:black,color:white
                  style D fill:red,color:white
                  style C fill:black,color:white
                  style B fill:grey,color:white
                  style E fill:black,color:white
                  
                  ```
                  
                  
                  
                  ```mermaid
                  graph TD
                  B((B))
                  B-->A((A))
                  B-->C((C))
                  C-->purple
                  C-->D((D))
                  D-->green
                  D-->E((E))
                  A-->blue
                  A-->yellow
                  E-->red
                  E-->black
                  style green fill:lightgreen,color:white
                  style blue fill:skyblue,color:white
                  style red fill:#f88,color:white
                  style black fill:black,color:white
                  style yellow fill:lightyellow
                  style purple fill:purple,color:white
                  style A fill:black,color:white
                  style D fill:red,color:white
                  style C fill:black,color:white
                  style B fill:grey,color:white
                  style E fill:black,color:white
                  
                  ```

        *   The sibling w of x is BLACK with RED right child

            Graph

                  ```mermaid
                  graph TD
                  B((B))
                  B-->A((A))
                  B-->D((D))
                  D-->C((C))
                  D-->E((E))
                  C-->purple
                  C-->green
                  A-->blue
                  A-->yellow
                  E-->red
                  E-->black
                  style green fill:lightgreen,color:white
                  style blue fill:skyblue,color:white
                  style red fill:#f88,color:white
                  style black fill:black,color:white
                  style yellow fill:lightyellow
                  style purple fill:purple,color:white
                  style A fill:black,color:white
                  style B fill:grey,color:white
                  style C fill:black,color:white
                  style D fill:black,color:white
                  style E fill:red,color:white
                  
                  ```
                  
                  ```mermaid
                  graph TD
                  D((D))
                  D-->B((B))
                  B-->A((A))
                  B-->C((C))
                  D-->E((E))
                  C-->purple
                  C-->green
                  A-->blue
                  A-->yellow
                  E-->red
                  E-->black
                  style green fill:lightgreen,color:white
                  style blue fill:skyblue,color:white
                  style red fill:#f88,color:white
                  style black fill:black,color:white
                  style yellow fill:lightyellow
                  style purple fill:purple,color:white
                  style A fill:black,color:white
                  style B fill:black,color:white
                  style C fill:grey,color:white
                  style D fill:grey,color:white
                  style E fill:black,color:white
                  
                  ```

***

# Minimum Spanning Tree

    - MST of an undirected, connected weighted graph is a spanning tree of minimun weight. Total weight is T, w(T) = \sum_{(u,v) \in T}w(u,v) 

    - An edge (u, v) is a safe edge for A, if A \cup {\lbrace (u,v) \rbrace} is also a subset of MST

    - A **cut** (S, V-S) of G is a partition of V, an edge (u, v) \in E **crosses** the cut  (S, V-S) if one of its endpoints is in S, and the other is in V-S

    - A cut **respects** a set of edges A if no edge in A crosses the cut

    - Prim’s algorithm: start by picking any vertex r to be the root of the tree, while the tree doesn’t contain all vertices in the graph, find a light edge leaving the tree and add it to the tree O((E+V)\log V)

    	Graph implementation

    		```mermaid
    		graph LR
    		a((a))---|4|b((b))
    		a---|8|h((h))
    		b---|8|c((c))
    		h---|7|i
    		i((i))---|2|c
    		i---|6|g((g))
    		b---|11|h
    		h---|1|g
    		c---|7|d((d))
    		g---|2|f((f))
    		c---|4|f
    		d---|14|f
    		d---|9|e((e))
    		f---|10|e
    		```

    		```mermaid
    		graph LR
    		a((a))===|4|b((b))
    		a===|8|h((h))
    		i((i))===|2|c((c))
    		h===|1|g((g))
    		c===|7|d((d))
    		g===|2|f((f))
    		c===|4|f
    		d===|9|e((e))
    		
    		```

    	Code implementation

    		```c++
    		#include<vector>
    		#include<queue>
    		struct myComp {
    		    constexpr bool operator()(
    		            edge const &a,
    		            edge const &b)
    		    const noexcept {
    		        return a.weight > b.weight;
    		    }
    		};
    		
    		vector<edge> prim(vector<edge> adj, int first, int V) {
    		    vector<edge> mst;
    		    vector<bool> visited(V, false);
    		    priority_queue<edge, vector<edge>, myComp> pq;
    		    pq.push(edge(first, first, 0));
    		    vector<int> key(V, INT16_MAX);
    		    key[first] = 0;
    		    while (!pq.empty()) {
    		        edge now = pq.top();
    		        pq.pop();
    		        if (visited[now.end])
    		            continue;
    		        visited[now.end] = true;
    		        for (auto ed: adj) {
    		            int v = ed.end;
    		            int w = ed.weight;
    		            if (!visited[v] && key[v] > w) {
    		                remove(mst.begin(), mst.end(), ed);
    		                key[v] = w;
    		                ed.weight = w;
    		                pq.push(ed);
    		                mst.push_back(ed);
    		            }
    		        }
    		    }
    		    return mst;
    		}
    		```

    - Kruskal’s algorithm: arrange edges in ascending order of weights, then add the next edge to T unless doing so would create a cycle

    	Graph implementation

    		```mermaid
    		graph LR
    		a((a))---|4|b((b))
    		a---|8|h((h))
    		b---|8|c((c))
    		h---|7|i
    		i((i))---|2|c
    		i---|6|g((g))
    		b---|11|h
    		h---|1|g
    		c---|7|d((d))
    		g---|2|f((f))
    		c---|4|f
    		d---|14|f
    		d---|9|e((e))
    		f---|10|e
    		```

    		```mermaid
    		graph LR
    		a((a))===|4|b((b))
    		a===|8|h((h))
    		i((i))===|2|c((c))
    		h===|1|g
    		c===|7|d((d))
    		g===|2|f((f))
    		c===|4|f
    		d===|9|e((e))
    		```

    	Code implementation

    		```c++
    		#include<vector>
    		#include<queue>
    		struct myComp {
    		    constexpr bool operator()(
    		            edge const &a,
    		            edge const &b)
    		    const noexcept {
    		        return a.weight > b.weight;
    		    }
    		};
    		
    		vector<edge> Kruskal(vector<edge> adj, int V) {
    		    vector<edge> mst;
    		    vector<bool> visited(V, false);
    		    priority_queue<edge, vector<edge>, myComp> pq(adj.begin(), adj.end());
    		    while (!pq.empty()) {
    		        edge smallest = pq.top();
    		        pq.pop();
    		        if (visited[smallest.start] && visited[smallest.end])
    		            continue;
    		        else {
    		            visited[smallest.start] = true;
    		            visited[smallest.end] = true;
    		            mst.push_back(smallest);
    		        }
    		    }
    		    return mst;
    		}
    		```

    - Disjoint set operations: disjoint set data structure maintains a collection of disjoint dynamic sets. This makes Kruskal’s algorithm total of O(E \log V)

***

# Single-Source Shortest Paths

    - Shortest path problems: The shortest-path weight  \delta(u,v) from u to v = \begin{cases}\min \lbrace w(p):u \xrightarrow p v  \rbrace &  \text{if there is a path} \\ \infty &\text{otherwise} \end{cases}

    > 📖 Subpaths of Shortest Paths are Shortest Paths!

    - Negative-weight edges: if it makes negative weighted cycle, then - \infty 

    - Can a Shortest path contain a cycle? Negative이면 위처럼 안 되고, positive이거나 zero여도 들어가지 않음

    - Shortest-path tree: a directed subgraph that unique simple path is shortest path

    - Bellman-Ford Algorithm: returns a boolean value whether there is a negative weight cycle

    	- Relaxation: if v.d > u.d + w(u,v) then v.d = u.d+w(u,v) and v.\pi = u

    	- Psuedo Code

    		```javascript
    		BELLMAN_FORD(G,w,s)
    			INITIALIZE_SINGLE_SOURCE(G,s)
    			for(var i=1;i<=G.V.size()-1;i++){
    				for(edge in G.E){
    					RELAX(u,v,w)
    				}
    			}
    			for(edge in G.E){
    				if (v.d > u.d + w(u,v))
    					return false;
    			}
    			return true;
    		```

    - Directed Acyclic Graph Shortest Path: topological sort를 이용해 Relaxation 진행

    - Dijkstra: running time이 bellman-ford에 비해 적음, BFS를 weight graph로 확장한 것

    	```python
    	def dijkstra(start):
    	    q = []
    	    heapq.heappush(q, (0, start))
    	    while q:
    	        d, now = heapq.heappop(q)
    	        if dist[now] < d:
    	            continue
    	        for node in graph[now]:
    	            cost = d + node[1]
    	            if dist[node[0]] > cost:
    	                dist[node[0]] = cost
    	                heapq.heappush(q, (cost, node[0]))
    	```

***

# Dynamic Programming

    - Divide and Conquer: divide the problem into a number of subproblems that are smallere instances of the same problem then solve them recursively

    - Top-down approach: if we nened the result in na future recursive call, we can use the stored value and it’s called **memoization →** solves each subproblem just once

    - Bottom-up approach: comopute the solutions for smaller things first then the answer will be stored at r[n]

***

# All Pairs Shortest Path

    - Sparse Graph는 edge가 적어서 |E| = O(|V|)인 그래프이고 dense graph는 |E| = \Theta (V^2)인 그래프이다.

    - input의 경우는 n \times n matrix W = (w_{ij})가 이용되는데, 이들은 현재의 edge weight를 담고 있다.

    - output은 shortest path를 저장하는 L, predecessor matrix \Pi = (\pi_{ij})이다. 만약 path가 없다면 \pi_{ij} = NIL

    - If we use dijkstra for all vertices, then running time will be O(V \times (V+E) \log V)

    - If we use Bellman-Ford algorithm for all vertices, the running time will be O(V^2E)

    - Using Dynamic Programming, l_{ij}^{(0)} = \begin{cases}
       0 &\text{if } i=j \\
       \infty &\text{if } i \not = j
    \end{cases}, l_{ij}^{(r)} = \min \lbrace l_{ik}^{(r-1)} + w_{kj}: 1 \leq k \leq n \rbrace

    - SLOW-APSP: 각각의 vertex에 대해 extended-shortest path를 적용하는 것으로, 효율은 dijkstra보다 안 좋음

    - FAST-APSP by using matrix multipliication: L^{(n-1)} = L^{(0)} \odot W \odot \dotsb \odot W = L^{(0)} \odot W ^{(n-1)}이기에, matrix multiplication을 진행해 L^{2^{|\log (n-1)|}} = L ^{(n-1)}로 두면 계산 과정이 훨씬 줄어든다.

    - Floyd-Warshall Algorithm: \Theta(V^3)

    - An intermediate vertex of simple path p = \lang v_1,v_2,...,v_l \rang is any vertex of p except v_1 or v_l

    - There are 2 cases: k is not an intermediate vertex of p, k is an intermediate vertex of p

    - first case에서 d_{ij}^{(k)} = d_{ij}^{(k-1)}이고, second case에서 d_{ij}^{(k)}=d_{ik}^{(k-1)}+d_{kj}^{(k-1)}이 됨

    - 두 가지를 합치면, d_{ij}^{(k)}=\min \lbrace d_{ij}^{(k-1)}, d_{ik}^{(k-1)}+d_{kj}^{(k-1)} \rbrace이고 k가 0이면 w_{ij}이다.

    - \pi_{ij}^{(k)} = \begin {cases} \pi_{ij}^{(k)} & \text{if} \ d_{ij}^{(k-1)} > d_{ik}^{(k-1)}+d_{kj}^{(k-1)} \\ \pi_{ij}^{(k)}  & \text{if} \ d_{ij}^{(k-1)} \leq d_{ik}^{(k-1)}+d_{kj}^{(k-1)} \end{cases} 
