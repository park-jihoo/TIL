---
id: b0e3e8fd-7ac6-4870-b8b8-ceb7daf6f35d
title: Data
created_time: 2023-08-07T06:47:00.000Z
last_edited_time: 2023-08-17T06:48:00.000Z
하위 항목: []
subclass: 2023_QE
class: Coursework
작성일시: 2023-08-07T06:47:00.000Z
상위 항목: []

---

# SQL

    - **S**tructured **Q**uery **L**anguage

    ## DDL

    	- DDL: Data Definition Language

    	- CREATE, DROP, ALTER,…

    	- Defining database schema

    		- Define tables with schema - columns and data types

    		- Define constraints - primary key and foreign key

    	```sql
    	CREATE TABLE Students(Sid int, Sname text, Gpa real);
    	CREATE TABLE Enrollment(Sid int, Cid int);
    	CREATE TABLE Courses(Cid int, Cname text);
    	ALTER TABLE Students ADD PRIMARY KEY(Sid);
    	ALTER TABLE Enrollment ADD PRIMARY KEY(Sid, Cid);
    	ALTER TABLE Courses ADD PRIMARY KEY(Cid);
    	ALTER TABLE Enrollment
    	ADD FOREIGN KEY(Sid) REFERENCES Students(Sid);
    	ALTER TABLE Enrollment
    	ADD FOREIGN KEY(Cid) REFERENCES Courses(Cid);
    	```

    ## DML

    	- DML: Data Manipulation Language

    	- DML change and retrieve database content

    	- A syntax for insert, delete, update, and analyze data in a database

    	```sql
    	INSERT INTO Students VALUES (3, 'Alice', 4.0);
    	INSERT INTO Students (Sid, Sname) VALUES (5, 'Bob');
    	INSERT INTO Students VALUES
    	(6, 'Charlie', 3.3), (7, 'Daniel', 3.9), (9, 'Eric', 3.6), (10, 'Fred', 4.2);
    	DELETE FROM Courses WHERE Cname = 'CS6320';
    	UPDATE Courses SET Cid = 7 WHERE Cname = 'CS4320';
    	```

    	- Diverse SELECT clauses

    		- ***** selects all columns

    		- Can use arithmetic expression in select clause

    		- Can assign new names for output columns

    	- Diverse WHERE conditions

    		- Equal, Inequalities: =, >, <, ≤, ≥

    		- Writing not equal <>

    		- Dealing with null values: IS NULL, IS NOT NULL

    		- Check if value is in list: IN

    		- Regular Expressions: LIKE ‘CS_320’, ‘CS43%’

    - DCL: Data Control Language

# Storage

    - Computer memory hierarchy

    	- Tape storage: bits as magnetic information, very slow access but very cheap

    	- Hard Disk: Slow access, cheap, used for less frequently accessed data

    	- SSD: Elevated price, fast access, elevated speed, but limited number of write cycles

    	- Main memory(volatile): expensive, very fast access, high bandwidth

    	- Caches: organized as cache hierarchy(L1,L2,L3), Very expensive, near-instantaneous access, very high bandwidth

    - Row-wise data store: data for same row is close together

    - Record Format: Fixed length

    	- Each row has the same data size

    	- Column type information is stored in system catalogs

    	- Finding i’th column doesn’t require scan of record

    - Page Format: Fixed-Length records:

    	- In packed page, records will move for free space

    	- Record id = <page id, slot id>

    - Record Format: Variable length

    	- Each row has different datasize(VARCHAR)

    	- Second format offers direct access to i’th columns

    - Page Format: Variable Length Records:

    	- Can move records within page without changing Rid

# Tree Index

    - Index: auxiliary data structure for finding data faster

    	- Index stores references to data records

    	- Index sorts rows by values in specific columns

    	- Index retrieves rows for specific search key values

    ## B Tree

    	- A balanced multi-way search tree

    	- Each tree node must have elements at least 50% of capacity of node, except the root

    	- All leaf nodes have the same depth

    	### Find

    	- Starting at root node, recursively traverse child nodes from top to bottom

    	### Traverse

    	- Inorder traversal

    	- A leaf node: list the element at the first time we pass it

    	- A non-leaf node: list the element the second time we pass it

    	### Insert

    	- First, find a leaf node to insert the value

    	- Insert the new element on the leaf node

    	- If the node overflows

    		- Pick a single median among elements of the leaf node

    		- Split the leaf node

    		- The median node is inserted to the parent node

    	### Delete

    	- Delete from left node

    		- If node underflows → borrow from adjacent sibling nodes or merge them

    	- Delete fron non-leaf node

    		- Delete and borrow element from child node

    ## B+ Tree

    	- Leaf node contain all data values

    	- Adjacent leaf nodes are bidirectionally linked

    	- Efficient data traversal than B Tree

    	- Consists of index node and data node(bidirectionally linked)

    	### Find

    	- Same as B tree but recursively search to a data node even if the value matches the element in index node

    	### Traverse

    	- Search the smallest value and then traverse sequentially using links

    	### Insert

    	- Split data nodes, copy median key ot the parent(first element in the right child node)

    	### Delete

    	- In borrow/merge procedure, parent node must keep the first value of its right child node

    	> 📖 B+ Tree can cover large table with shallow depth

# Hashing

    - Performs the operations rapidly

    	- Find, Insert, Delete in O(1) with high probability

    - Hash function maps each key to a hash value

    	- Key x is usually a character string

    	- Hash value h(x) is bucket(=cell) index in a hash table 0≤h(x)<B

    	- Hash table: a B-element array

    - Collision: it’s possible that different keys may be mapped into the same location

    	- Open hashing: keeps a list of all elements that hash to the same value

    	- Closed Hashing: To keep all keys in the table itself

    - A good hash function is simple, and produce less collisions

    	- For a K-character key x, h(x) can be given by

    		```undefined
    		h(x) = \left(\sum_{i=0}^{K-1}x[K-i-1]*32^i\right)\%B
    		```

    - Probing sequence

    	- Linear probing: f(i)=i → Leads to primary clustering

    	- Quadratic probing: f(i)=i^2 → secondary clustering

    	- Double hashing: f(i)=i\times g(x), where g(x) is a hash function

# Query Processing

    ```mermaid
    graph LR
      A[Input Query] -->|Parse| B[Query Parser]
      B -->|Rewrite| C[Query Rewriter]
      C -->|Optimize| D[Query Optimizer]
      D -->|Plan| E[Physical Plan]
      E -->|Execute| F[Query Executor]
      F -->|Result| G[Query Result]
    ```

    ## Relational Algebra

    	- Example

    		```undefined
    		\pi_{\text{S.sname}}((\sigma\text{S.major}=\text{'Data science'}\land \text{C.cname='DS5700'}((\text{students}\Join_{\text{S.sid=E.sid}}\text{enrollment})\Join_{\text{E.cid=C.cid}}\text{courses})))
    		```

    	- Operational description of a computation

    	- Systems execute relational algebra query plan

    	- Unary operators: on single relation

    		- Projection(\pi) : Retains only desired columns

    		- Selection(\sigma): Selects a subset of rows

    		- Renaming(\rho): Rename attributes and relations

    	- Binary operators: on pairs of relations

    		- Union(\cup): Tuples in r1 or in r2

    		- Set-difference(-): Tuples in r1, but not in r2

    		- Cross-product(\times): Allows us to combine two relations

    	- Compound operators: common “macros” for above

    		- Intersection(\cap): Tuples in r1 and in r2

    		- Joins(\Join): Combine relations that satisfy predicates(= \sigma_\theta(R\times S))

    ## Projection, Selection

    	- Query Execution in Row store

    		- On every Page, check condition for all slots

    	- Query Execution in Column store

    		- Look-up the sorted dictionary to find the value which satisfies condition

    		- Calculate the binary code of condition

    		- Compare the binary code with the encoded column of target column

    		- Create a bit vector with length of #rows

    		- Materialize the result with the bit vector, encoded column of sname and the dictionary of sname

    ## Join, Query Plan and Optimization

    	### Join(\Join)

    	- Simple nested loops join: Cost O(MN)

    	- Index nested loops join: if there is an index of join column of one table, can make it the inner and exploit the index

    	- Sort-merge join: sort two tables on the join column, and scan them to do a merge

    	- Hash join: Same value in join column implies same hash values

    	- Join in Column Store

    		- Make a dictionary translation table for join columns

    		- List row IDs of T2 with the value IDs of T1.A using the translation table

    		- List matching row IDs

    	### Query Plan

    	- Logical query plan just specifies types of operators

    	- Physical query plan specifies implementations as well(ex. if join, then use hash join)

    	### Query Optimization

    	- Query Plan search space: heuristic restrictions for query plan

    		- Apply predicate/projection early

    		- Avoid predicate-less joins

    		- Focus on left-deep plans to allow pipelining

# Transactions

    ## ACID Properties

    	- Lifecycles of transaction

    		- Begin a transaction with command BEGIN

    		- End a transaction with command COMMIT

    		- Abort a transaction with command ROLLBACK

    	- Integrity Constraints must be maintained before and after transaction

    	### Atomicity

    	- A transaction’s all steps are executed OR none of them are executed

    	### Consistency

    	- Data is consistent with all constraints(PK, FK, Domain integrity)

    	- DBMS will abort transactions threatening consistency

    	### Isolation

    	- Different users may execute transactions concurrently

    	- Isolation means give an illusion of sequential execution to users

    	### Durability

    	- Durability guarantees that committed updates persist

    ## Concurrency Control

    	- A procedure of managing simultaneous operations without conflicting with each other

    	- Ensures that transactions are performed concurrently and to produce correct results without violating data integrity

    	- Schedule: ordered steps from multiple tranactions and a good schedule preserves the illusion of isolation

    	- Final state equivalence: comparing two schedules based on final database state

    	- Final state serializable if there is a serial schedule that is final state equivalent

    	- View equivalence

    		- If transaction X reads the initial value for some object in S1, then also does S2

    		- If transaction X reads a value written by transaction Y in S1, then also does S2

    		- If transaction X writes the final value written by transaction Y in S1, then also does S2

    	- View serializable if there is a serial schedule that is view equivalent

    	- Conflict Equivalence

    		- Conflict: if one of two operations of different transactions on the same object is a write operation

    		- Swapping conflicting options changes results and view

    		- Can get from S1 to S2 by swapping non-conflicting operation is conflict equivalence

    	- Conflict Serializable if conflict equivalent with serial schedule

    		- Draw conflict graph for schedule to test conflict serializability

    ## MVCC

    	### Lock-based CC

    	- Read lock disallows write access to the object, other transactions can read the object freely

    	- Write lock disallows read/write access to the object

    	### MVCC Protocol

    	- Each transaction receives start timestamp(STS)

    	- Each writing transaction creates a new version of an object which has commit timestamp(CTS)

    	- Read operation reads latest version’s value, which depends on isolation level

    	### Isolation Level

    	|                  | Dirty Reads  | Non-repeatable reads | Phantom reads |
    	|------------------|--------------|----------------------|---------------|
    	| Read Uncommitted | Possible     | Possible             | Possible      |
    	| Read Committed   | Not possible | Possible             | Possible      |
    	| Repeated Read    | Not possible | Not possible         | Possible      |
    	| Serializable     | Not possible | Not possible         | Not possible  |

    	### Garbage collection

    	- There are no running transactions looking previous versions of A which can lead to memory overhead

    	- Copy the latest version with CTS is less than the minimum STS of running transactions

    	- Delete all versions with CTS is less then the minimum STS of running transactions

# Column Store RDBMS

    - Data for some column is close together

    - Values in same columns are often repeated → we can compress the data

    - Dictionary Encoding: create sorted dictionary of each column

    	- Consists of encoded values in bit string and corresponding original values

    	- Values are stored in sorted order

    	- We can use array index and code size to get each encoded value

    - Insert/Delete/Update

    	- If values are unique, then we need to recreate dictionaries and re-encode columns

    	- Solution: Delta with row store

    		- Divide table into main and delta

    		- Delta store captures recent changes

    - Contiguous storage : store table in contiguously allocated memory

    - Paged storage : split table into multiple pages
