---
id: 7806a722-3120-4dbe-9ae8-c9c96af16848
title: BKMS2 FINAL
created_time: 2023-06-12T02:31:00.000Z
last_edited_time: 2023-10-07T16:40:00.000Z
cover_image: https://www.notion.so/images/page-cover/rijksmuseum_vermeer_the_milkmaid.jpg
icon_emoji: 🤝
하위 항목: []
subclass: 2023_Spring
class: Coursework
작성일시: 2023-06-12T02:31:00.000Z
상위 항목: []
_thumbnail: https://www.notion.so/images/page-cover/rijksmuseum_vermeer_the_milkmaid.jpg

---

# Frequent Itemset Mining & Assocation Rules

    - A general many-to-many mapping between two kinds of things

    - **Support** : Number of baskes containing all items in I

    - **Confidence**: \frac {\textbf{support}(I\cup j)}{\textbf{support}(I)}

    - **Interest** : difference between its confidence and the fraction of baskets that contain j

    	```undefined
    	\textbf{Interest}(I \rightarrow j) = \textbf{conf}(I \rightarrow j) - \Pr[j]
    	```

    - Goal : Find all association rulses with support\geq s and confidence \geq c

    - Mining Association Rules

    	- Find all frequent itemset I

    	- Rule generation

    		- For every subset A of I, generate a reule A → I \ A

    		- Output the rules above the confidence threshold

    - Compacting the output

    	- Maximal frequent itemsets

    	- Closed itemsets

    ## Finding Frequent Itemsets

    	- Computation model

    		- The true cost of mining disk-resident data is usually the number of **disk I/O** 

    		- Association-rule algorithms read the data in passes - all baskets read in turn

    		- We measure the cost by the **number of passses** an nalgorithm makes over the data

    	- Main memory bottleneck: # of different things we can count is limited by main memory

    	- Finding Frequent pairs: pairs are common

    		- Naive Algorithm: generate \frac {n(n-1)}{2} pairs

    		- Count all pairs using matrix(4 bytes per pair)

    		- Keep a table of triples with count(only pairs with count > 0, 12 bytes per pair)

    	### A-Priori Algorithm

    		> 💡 Key Idea : **monotonicity**

    		- Read baskets and count in main meory the occurences of each individual item

    		- Read baskets again and count in main memory <u>only</u> those pairs where both elements are frequent

    		```mermaid
    		graph LR
    			subgraph Pass1
    				A(item counts)
    			end
    			subgraph pass2
    				B(Frequent items)
    				C(Counts of pairs of frequent items)	
    			end
    		A ---> B
    		```

    		- In frequent triples and more, for each k we construct to set of k tuples. 

    			- Candidate k tuples: those that might be frequent sets based on information from the pass for k -1

    			- The set of truly frequent k tuples

    	### PCY Algorithm

    		> 💡 Use idle memory to reduce memory required in pass 2 of A-priori!

    		- Pass 1 of PCY: In addition to item counts, maintain a hash table with as many buckets as fit in memory

    		```plain text
    		FOR (each basket):
    			FOR (each item in the basket):
    				add 1 to item's count
    			FOR (each pair of items):
    				hash the pair to a bucket
    				add 1 to the count for that bucket
    		```

    		- Pass 2: Only count pairs that hash to frequent buckets

    		- Between passes - replace the buckets by bit0vector, then 4 byte integers will be replaced to bits and it requires 1/32 of memory

    	- Multistage Algorithm: limit the number of candidates to be counted

    		- After pass 1 of PCY, rehash only those pairs that qualify for pass 2 of PCY

    		- On middle pass, fewer pass contribute to buckets, which leads to fewer positives

    	- Multihash: Use Several independent hash tables on the first pass

    		- Risk: Halving the number of buckets doubles the average count

    	### Frequent itemsets in ≤2 passes

    		- Random sampling: take a random sample of the market baskets and run a-priori or one of its improvements in main memory

    		- SON: Repeatedlyl read small subsets of the baskets into main memory and run an in-memory algorithm to find all frequent itemsets

# Finding Similar Items: LSH

    > 💡 Given q, find data points x_j that are within distance threshold d(q, x_j) ≤ s in O(1)

    - Distance Measures: Jaccard distance/similarity

    	```undefined
    	sim(C_1, C_2) = |C_1 \cap C_2| / |C_1 \cup C_2| \\ d(C_1, C_2) = 1 - sim(C_1, C_2)
    	```

    - 3 Essential steps for similar docs

    	- Shingling: Convert Document to sets

    	- Min-hashing: Convert Large sets to short signatures, while preserving similarity

    	- LSH: Focus on pairs of signatures likely to be from simlilar documents

    ## Shingling

    	- A k-shingle for a document is a sequence of k tokens that appears in the doc

    	- Document D_1 is a set of its k-shingles C_1 = S(D_1) and each document is a 0/1 vector in the space of k-shingles

    	- Documents that have lots of shingles in common have similar text, even if the text appears in different order

    ## MinHashing

    	- Encode sets using 0/1 vectors

    	- Interpret set intersection as bitwise AND, and set union as bitwise OR

    	- Rows are elements(shingles), columns are sets(documents)

    	- Hashing columns: find a hash function such that if similarity is high then with high probability same hash function value, and low then high probability different hash function value

    	- Min-hashing: define a hash function h_\pi(C) = \min_\pi\pi(C)

    	```undefined
    	\Pr[h_\pi(C_1) = h_\pi(C_2)] = sim(C_1, C_2)
    	```

    	- Similarity of 2 signatures is the fraction of the hash functions in which they agree

    	- sig(C)[i] = \min (\pi_i(c)) is compressed bit vector

    ## Locality Sensitive Hashing

    	> 💡 Goal: Find documents with Jaccard similarity at least s

    	- Ensure that similar columns are likely to hash to the same bucket with high probability

    	- Overview of LSH

    		- Divide matrix M into b bands of r rows

    		- **For each band**, hash its protion of each column to a hash table with k buckets(make k as large as possible)

    		- Candidate column pairs are those that hash to the same bucket for ≥1 band

    		- Tune b and r to catch most similar pairs, but few non-similar pairs

    	- (For simplicity) We assume that same bucket implies identical in that band

    	- Tradeoff: The number of b and number of rows r balances false positive / false negative

    	- Assume column C1 and C2 have similarity t

    		- Prob that all rows in band equal t^r

    		- Prob that some row in band unequal 1 - t^r

    		- Prob that no band is identical (1-t^r)^b

    		- Prob that at least 1 band identical 1-(1-t^r)^b

    - Generalizing Min-hash

    - Choosing s-curve by r and b

    - Probability that c1 and c2 are candidate pair is 1 - (1-s^r)^b

    ![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/39e0b223-1835-42aa-b402-55c900b7fe90/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20231018%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20231018T004223Z&X-Amz-Expires=3600&X-Amz-Signature=0d434e6dc12f2302d71abac5130146dd68ac05d1fbd73154a4f739e8ac807e58&X-Amz-SignedHeaders=host&x-id=GetObject)

    - b가 고정되어 있을 때, r이 커질수록 false negative 증가, false positive 감소

    - r이 고정되어 있을 떄, b가 커질수록 false positive 증가, false negative 감소

    ## LS Families

    	- A family H of hash function is said to be (d_1, d_2, p_1, p_2)-sensitive if for any x and y in s

    		- if d(x, y) \leq d_1 then probability over all h \in H that h(x) = h(y) is at least p_1

    		- if d(x, y) \geq d_2 then probability over all h \in H that h(x) = h(y) is at most p_2

    	> With LS Families we can to LSH

    - Amplifying Hash functions: AND and OR

    	- AND construction like **rows in a band**

    	- OR construction like **many bands**

    	- 합치면 결국 1 - (1-s^r)^b가 나와서 LSH

# Link Analysis, PageRank

    - How to organize Web?

    	- Human created web directories

    	- Web search

    - 2 challenges of web search

    	- Who to **trust**?

    	- What is the **best** answer to query?

    - Link Analysis algorithms’ idea: Links as votes

    - _Random surfer_ model: Start at random page and follow random outlinks repeatedly, from hatever page you are at

    - importance = the principal eigenvector of the transition matrix of the Web

    - rank for page

    ```undefined
    r_j = \sum_{i \rightarrow j} \frac {r_i}{d_i}
    ```

    - Stochastic adjacency matrix M: if i→j then M_{ji} = \frac{1}{d_i} else 0

    - Rank vector r: vector with an entry per page

    - The flow equations can be written as

    	```undefined
    	r = M \cdot r
    	```

    - We can solve this by power iteration!

    - Imagine a random walk surfer: at time t+1, the surfer follows an out-link from i uniformly at random and ends up some page j linked from i

    - If it’s stationary distribution, p(t+1) = M \cdot p(t) = p(t)

    - In undirected graph, r_i = d_i/2m

    - Two problems: Dead end, spider traps → teleport!

    - Random teleport, then equation changes like this

    	```undefined
    	r_j = \sum_{i \rightarrow j} \frac {r_i}{d_i} + (1-\beta)\frac{1}{N}
    	```

    - Google Matrix A

    	```undefined
    	A = \beta M + (1-\beta) \left[ \frac{1}{N} \right]_{N\times N}
    	```

    - Sparse Matrix Encoding: encode sparse matrix using only nonzero entries → 2|r|+|M|

    - Block-based Update Algorithm → break r_new into k blocks that fit in memory → k(|M|+|r|)+|r|

    - Block-stripe Update Algorithm → break M into stripes! Each stripe only contain destinatioin nodes in corresponding block of r new → |M| (1+\epsilon) + (k+1)|r|

    ### Topic-specific Pagerank

    	- Instead of generic popularity, we can measure popularity withun a topic.

    	- Teleport can go to topic speciific set of relevant pages

    		- Bias the random walk(topic specific set of relevant pages)

    	- Which topic ranking to use? User context

    	- Graph proximity: 일반적인 그래프 상에서의 위치

    	- Simrank: Random walks from a fixed node on k-partite graph, then teleport set S = {u}

    ### TrustRank: combating web spam

    	- First Spammer: Term spam, and google decided pagerank as a tool to measure the importance of Web pages

    	- Spam Farming: Spam farms were developed to concentrate pageRank on a single page, and there is a link structures that boost pagerank of particular page

    	```undefined
    	y = \frac {x}{1-\beta^2}+c \frac{M}{N}, c = \frac{\beta}{1+\beta}
    	```

    	- Trustrank: topic-specific pagerank with teleport set ot **trusted pages**

    		- Sample a set of seed pages from the web

    		- Use a threshold value and mark all pages below the trust threshold as spam

    		- Trust propagation: for each q \in o_p, p confers to the trust to q is  \frac{\beta t_p}{|o_p|}. This trust is additive

    	- Spam Mass = \frac {r_p - r_p ^+}{r_p}, r_p is pagerank of p, and r_p^+is pagerank of p with teleport into trusted pages only

    ### HITS

    	- Quality as an expert(hub), quality as a content(authority)

    	- Authorities are pages containing useful informations

    	- Hubs are pages that link to authorities

    	```python
    	a[0], h[0] = 1/sqrt(N), 1/sqrt(N)
    	while converge:
    		a[t+1] = sum(h[t])
    		h[t+1] = sum(a[t])
    		normalize a, h
    	```

    	- Write vector a and h as authority and hubs and adjacency matrix as A_{ij}=1 if i→j, 0 otherwise then 

    	```undefined
    	a = (A^TA)a \\ h = (AA^T)h
    	```

# Community Detection in Graphs

    > 💡 PageRank based Algorithm for finding dense clusters

    - Seed Nodes: Compute approximate Personalized Pagerank(PPR) around node s

    - Algorithm outline

    	- Pick a seed node s of interest

    	- Run PPR with teleport set {s}

    	- Sort the nodes by the decreasing PPR score

    	- Sweep overr the nodes and find **good clusters**

    - Cut

    ```undefined
    cut(A) = \sum_{i \in A, j \notin A} w_{ij}
    ```

    - Graph Partitioning Criteria: conductance

    ```undefined
    \phi (A) = \frac {|\{(i, j) \in E ; i \in A, j\notin A \}|}{\min(vol(A), 2m-vol(A))}
    ```

    - Sweep: sort nodes by decreasing ppr score and get local minima of conductance

    - Computing PPR

    	```undefined
    	r^{(t+1)} = \beta M \cdot r^{(t)} + (1 - \beta) a
    	```

    - Approximate pagerank: lazy random walk, stays in 1/2 probability and walks to random neighbor at other half

    - An \epsilon-approximate Pagerank vector for pr_\alpha(s) is a pagerank vector pr_\alpha(s-r) where the vector r is nonnegative and satisfies r(v) \leq \epsilon d(v) for every vertex v in the graph

    - Push algorithm

    	```python
    	r', q' = r, q
    	r'[u] = r[u] + (1-beta)q[u]
    	q'[u] = beta * q[u] / 2
    	for v in u->v:
    		q'[v] = q[v] + beta * q[u] / (2 * d[u])
    	return r', q'
    	```

    - Why standard cluster methods do not work?

    	- high dimensional data

    	- noisy and sparse data

    	- number of cluster is unknown

    	- cell types are hierarchically organized

    - Knn graph: directed graph with vertex set V and an edge from v to its k most similar objects in V

    - NN-descent: if K is large enough then even if we start from a arandom knn approximation we are likely to find for each object K times with radius of 

    - NN-descent: if K is large enough then even if we start from a arandom knn approximation we are likely to find for each object K times with radius of ∆/2 by exploring its neighbors’ neighbor

    	- Start with a random knn graph

    	- iteratively refine the list of nearest neighbors of each code

    	- keep doing until convergence

    - Modularaity Q

    	```undefined
    	Q(G, S) = \frac 1 {2m} \sum_{s \in S} \sum_{i\in S} \sum_{j\in S} \left( A_{ij} - \frac {k_ik_j}{2m} \right) \\Q = \frac 1{2m} \sum_{ij} \left[ A_{ij} - \frac {k_ik_j}{2m}  \right] \delta(c_i, c_j)
    	```

    	- We can identify communities by maximizing modularity

    - Louvain algorithm: greedy algorithm for community detection

    	- Modularity is optimized by allowing only local changes to node-communities memberships

    	- The identified communities are aggregated into super-nodes to build a new network

    	- Repeat until no increase of modularity is possible

    	```undefined
    	\Delta Q(i \rightarrow C) = \left[ \frac {\sum_{in} + k_{i, in}}{2m} - \left(\frac{\sum_{tot}+k_i}{2m} \right)^2\right] - \left[ \frac {\sum_{in} }{2m} - \left(\frac{\sum_{tot}}{2m} \right)^2 - \left(\frac{k_i}{2m} \right)^2\right]
    	```

# Recommender System

    - Gathering known ratings for matrix

    - Extrapolating unknown ratings from the known ones

    - Evaluating extrapolation methods

    ## Content-based

    	> 💡 Recommend items to customer x similar to previous items rated highly by x

    	- How to pick important features? TF-IDF(Term frequency * inverse doc frequency)

    	- User profile possibilities: u(x, i) = \cos (x, i) = \frac {x\cdot i}{||x||\cdot ||i||}

    	- Pros
    	
    	- Cons

    ## Collaborative filtering

    	- User-user collaborative filtering, Item-item collaborative filtering

    	- Find similiar users by pearson correlation coefficient

    		```undefined
    		sim(x, y) = \frac {\sum_{s\in S_{xy}} (r_{xs}-\bar{r_x})(r_{ys}-\bar{r_y})}{\sqrt{\sum_{s\in S{xy}}(r_{xs}-\bar{r_x})^2}\sqrt{\sum_{s\in S{xy}}(r_{ys}-\bar{r_y})^2}}
    		```

    	- Rating prediction r_{xi} = \frac 1 k \sum_{y\in N} r_{yi}

    	- Item-item collaborative filtering

    		```undefined
    		r_{xi} = b_{xi}+\frac {\sum_{j \in N(i;x)} s_{ij} \cdot (r_{xj} - b_{xj})}{\sum_{j \in N(i;x)}s_{ij}}
    		```

    	- Pros of collaborative filtering
    	
    	- Cons for collaborative filtering

    - BellKor Recommender System

    	- Multi-scale modeling of the data

    		- Global: overall deviations of users/movies

    		- Regional: Factorization → Addressing regional effects

    		- Local: Collaborative Filtering

    - Interpolation weights: use a **weighted sum** rather than weighted avg:

    	```undefined
    	\hat {r_{xi}} = b_{xi} + \sum_{j \in N(i;x)} w_{ij}(r_{xj}-b_{xj})
    	```

    	- 여기에서 SSE를 minimize하는데, 이는 gradient descent를 이용해서 증명 가능하다

    - Latent Factor Models: R = Q \cdot P^T, and sum of squared error is \min_{U,V,\Sigma} \sum_{ij \in A} \left( A_{ij} - [U\Sigma V^T]_{ij} \right) ^2 = \min_{P,Q} \sum_{(i, x) \in R} (r_{xi} - q_i \cdot p_x)^2

    - 여기에 regularization term을 추가하여 gradient descent를 적용한 다음 optimal value를 찾는다.

# Product Quantization

    - Quantization: the process of constraining an input from a continuous or otherwise large set of values to a discrete set

    	- Efficient Memory usage

    	- Lower power

    	- Saving RAM memory bandwidth

    	- Improvement of inference speed

    	- Reduce accuracy

    - Searching with Quantization

    	- Symmetric distance computation: distance between query centerioids

    	- Asymmetric distance computation: distance between x and queried y

    		- Train k centroids for each sub vector spaces with k means algorithm

    		- Substitute with the id of the nearest centroid from the respective sub-vector spaces

    		- calculate distence between query sub vector and every centroid

    		- For each row of PQ code, look up the partial distances and sum them

    - Inverted File System with asymetric distance

    	- Inverted index: database index storing a mapping from content to its locations

    	- Partitioning with K-mean clustering: the search can only be performed on vectors belonging to specific partitions

    	- Why using residual here? Residual is more compact distribution and uses lower variance
