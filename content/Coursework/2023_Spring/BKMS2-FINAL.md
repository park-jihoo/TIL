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

    ![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/39e0b223-1835-42aa-b402-55c900b7fe90/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20231009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20231009T222521Z&X-Amz-Expires=3600&X-Amz-Signature=b2a7862777c5214e5c6a8206540b8534b8e2894ae600189cdc155bfd2f96c514&X-Amz-SignedHeaders=host&x-id=GetObject)

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

    - We can solve this by power iteration!

    - Imagine a random walk surfer: at time t+1, the surfer follows an out-link from i uniformly at random and ends up some page j linked from i

    - If it’s stationary distribution, p(t+1) = M \cdot p(t) = p(t)

    - In undirected graph, r_i = d_i/2m

    - Two problems: Dead end, spider traps → teleport!

    - Random teleport, then equation changes like this

    - Google Matrix A

    - Sparse Matrix Encoding: encode sparse matrix using only nonzero entries → 2|r|+|M|

    - Block-based Update Algorithm → break r_new into k blocks that fit in memory → k(|M|+|r|)+|r|

    - Block-stripe Update Algorithm → break M into stripes! Each stripe only contain destinatioin nodes in corresponding block of r new → |M| (1+\epsilon) + (k+1)|r|

    ### Topic-specific Pagerank

    ### TrustRank: combating web spam

    ### HITS

# Community Detection in Graphs

# Recommender System

# Product Quantization
