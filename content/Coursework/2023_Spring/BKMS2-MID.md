---
id: e6921ebb-b53b-4d1d-918d-36322a492bae
title: BKMS2 MID
created_time: 2023-08-01T03:38:00.000Z
last_edited_time: 2023-10-07T08:35:00.000Z
icon_emoji: 📖
하위 항목: []
subclass: 2023_Spring
class: Coursework
작성일시: 2023-08-01T03:38:00.000Z
상위 항목: []

---

# Data Warehouse

    ## Why Business Intelligence?

    - Business intelligence is the activity which contributes to the growth of any company

    - How does it work?

    	- BI based on Data warehouse technology extracts informations from a company's operational systems

    	- The data is transformed and loaded to data warehouses

    	- Since this data is credible, it is used for business insights

    ## Why Data Warehouse?

    - Data collected from various sources & stored in various databases cannot be directly visualized

    - The data first needs to be **integrated** and then **processed** before visualization takes place

    ## What is a Data Warehouse?

    - A central location where consolidated data from multiple locations are stored

    - Data warehouse is maintained separately from an organization's operational database

    - End users access it whenever any information is needed

    - Data warehouse is like a relational database designed for analytical needs

    - It functions on the basis of OLAPp

    - It is a central location where consolidated data from multiple locations are stored

    ## What are the advantages of DW?

    - Faster and more accurate

    ## Properties of a DW

    - Subject-oriented: Data is categorized and stored by business subject rather than by application

    - Integrated: Data on a given subject is collected from disparate sources and stored in a single place

    - Time-variant: Data is stored as a series of snapshots, each representing a period of time

    - Non-volatile: Typically data in the data warehouse is not updated or deleted

    ### OLTP vs OLAP

    | Relational Database(OLTP)                       | Analytical Data Warehouse(OLAP)                 |
    |-------------------------------------------------|-------------------------------------------------|
    | Contains current data                           | Contains Historical Data                        |
    | Useful in running business                      | Useful in analyzing business                    |
    | Based on ER model                               | Based on Star, snowflake schema                 |
    | Provides primitive and highly<br/>detailed data | Provieds summarized and <br/> consolidated data |
    | Used for writing data into DB                   | Used for reading data from DW                   |
    | DB size ranges from 100MB to 1GB                | DW size ranges from 100GB to 1TB                |
    | Fast: high performance                          | Highly flexible, slow                           |
    | Numbers of records accessed<br/> is in tens     | Number of records accesssed<br/> is in millions |

    ## ETL (Extract, Transform & Load)

    > ETL is the process of extracting the data from various sources, transforming this data to meet your requirement and  
    >then loading it into a target DW

    ## Data Mart

    - Smaller version of DW which deals with single subject

    - It's focused on one area. Hence, they draw data from a limited number of sources

    - Time taken to build Data mart is very less compared to time build a DW

    ```mermaid
    flowchart LR
    a[(Data Warehouse)]---b1[(Data Mart1, Sales)]
    a --- b2[(Data Mart2, Marketing)]
    a --- b3[(Data Mart3, Operations)]

    ```

    ### Types of Data Mart

    - Dependent Data Mart

    	- The data is first extracted from the OLTP systems and then populated in the central DWH

    	- From the DWH, the data travels to the data mart

    		```mermaid
    		    flowchart LR
    		    a[(OLTP)]-->b[(DW)]-->c[(Data Mart)]
    		
    		```

    - Independent Data Mart

    	- The data is directly received from the source system

    	- This is suitable for small organizations or smaller group within an organization

    	```mermaid
    	flowchart LR
    	A[(OLTP)]-->B[(Data Mart)]
    	
    	```

    - Hybrid Data Mart

    	- The data is fed both from OLTP system and DW

    	```mermaid
    	flowchart LR
    	A[(OLTP)] & B[(DW)] --> C[(Data Mart)]
    	
    	```

    ## Metadata

    - Metadata is defined as about data

    - Metadata in DW defines the source data

    - Metadata is used to define which table is source and target, and which concept is used to build business logic called
    transformation to actual output

    ## What is Data Warehousing?

    - Data Warehousing is the act of organizing&storing data in a way so as to make its retrieval effect and insightful

    - It's also called as the process of transforming data into information

    ## OLAP

    - OLAP is a flexible way for you to make complicated analysis of multidimensional data.

    - DW is modeled on the concept of **OLAP**. DBs are modeled on the concept of OLTP

    - OLTP system use data stored in the form of two-dimensional tables, with rows and columns

    ### Advantages of OLTP over OLAP

    - Opens up new views of looking at data.

    - Supports filtering/sorting of data.

    - Data can be refined

    ### Multidimensional modeling

    - Predict analytic pattern of users

    - Data Structures

    	- Descriptive information(**cube edges**) -> dimensions

    		- Hierarchies, dimensional attributes

    		- Structural basis for selection and aggregation

    	- Quantified information(**cube cells**) -> facts

    		- Measures / key performances indicators for analysis / aggregation

    - Goal

    	- Orthogonal dimensional descriptions

    	- Clear separation of measures

    ### Mapping the Multidimensional Model(MOLAP)

    - Multidimensional model is _conceptual_ not physical

    - Requirements

    	- Physical storage of OLAP system data

    	- Historic data

    	- Consistency fast response times

    	- Multi-user operation

    	- Scalability, maintainability, flexibility, secure data access

    - Realization w.r.t analysis and loading phase

    	- Goal of analysis: efficient extraction of information from data

    	- Specialized data base for applications and users

    ### ROLAP

    - Properties

    	- Data is stored in RDBMS

    	- Information is created via SQL

    	- Additional tables for aggregates

    - Pros

    	- Proven DB technology

    	- Scalability for big volume data

    	- High number of dimensions

    - Cons

    	- Installation overhead, slow

    	- Overhead for mapping complex queries

    	- Extensive meta data management

    - Products: Almost all RDBMS Vendors

    ### OLAP Operations

    ### Roll-up

    - Roll-up performs aggregation on a data cube by either

    	- Climbing up a concept hierarchy for a dimension

    	- Dimension reduction

    ### Drill-down

    - Drill-down is the reverse operation of roll-up, and it's performed by either

    	- Stepping down a concept hierarchy for a dimension

    	- Introducing a new dimension

    ### Slice

    - The slice operation provides new sub-cube from one particular dimension in a given cube

    ### Dice

    - The dice operation provides a new sub-cube from two or more dimensions in a given cube

    ### Dimensions

    - The tables that describe the dimensions involved are called **Dimension tables**.

    - Dividing a data warehouse project into dimensions provides structured information for analysis and reporting

    ### Facts & Measures

    - A fact is a measure that can be summed, averaged or manipulated

    - A fact table contains 2 kinds of data - a dimension key and a measure

    - Every Dimension table is linked to a Fact table

    ```mermaid
    flowchart LR
    A[Product]-->B[Product ID]
    A --> D[Number of units sold]
    B --- C(Dimension Key)
    D --- E(Measure)

    ```

    ### Schemas

    - A schema gives the local description of entire DB

    - It gives details about the constraints placed on the tables, key values present & how the key values are linked
    between the different tables

    - A database uses relational model, while a data warehouse uses star, snowflake and fact constellation schema

    ### Star Schema

    - Each dimension in a star schema is represented with one-dimensional table and fact table is at the center

    ### Snowflake Schema

    - Dimension tables in the snowflake schema are normalized

    ## Federated Database System

    ### What is a federated database?

    - Logical association of independent database that provides a single, integrated, coherent view.

    - Federation also provide a cohesive, unified view of data derived from multiple sources.

    ### Characteristics of Federate Database System

    - Transparency: Federated databases masks from the user difference, idiosyncrasies, and implementations of underlying
    data sources

    - Heterogeneity of data sources: Heterogeneity is the degree of differentiation in the various data sources.

    - Extensibility and openness of the federation: In a federated system, new sources may be needed to meet the changing
    needs of the users' business.

    - Autonomy for data sources: Federated database does not disturb the local operation of an existing data source.

    - Data integration: Federated database system can integrate data from different procotols, DBMS, using wrapper

    ### Benefits of Federated Database

    - Offer an alternative to merge database together

    - Help programmers avoid the tight coupling of application

    - Applications only need to be connected to the federal database

    ### Issues in Database Federation

    - Query Performance: The query algorithm for federated database should be carefully designed, or get slow response time

    - Dependence on autonomous data sources: The federation is highly dependent on data sources that are largely beyond
    direct control of the federation management system.

    - Scalability: Federated system can add new data sources relatively quickly and with minimal cost, and are thus
    reasonably scalable architectures. However scaling up new sources adds to the complexity of the infrastructure

    - Technical Skills: Considerable expertise my be required to design and manage federated DB system.

# DocumentDB

    ## Row-Oriented Database

    - Tables are stored as rows in disk

    - A single block io read the table fetches multiple rows with their columns

    - More IOs are required to find a particular row in the table

    ## Column-Oriented Database

    - Tables are stored as columns in disk

    - A single block io read the table fetches multiple columns with their rows

    - Less IOs are required to find a particular row in the table

    ## Pros and Cons

    - Row-Based

    	- Optimal for read/write

    	- OLTP

    	- Compression, aggregation is not efficient

    	- Efficient queries with multi-columns

    - Column-Based

    	- Slow Write

    	- OLAP

    	- Compression, aggregation is efficient

    	- Inefficient queries with multi-columns

    ## NoSQL Databases

    - Relational Databases scale vertically, and NoSQL scale horizontally

    - It's schema-less and non-relational

    - Uses for cashing, pub/sub, leaderboards, etc.

    - Tradeoff between schema-less and joins

    - Good for time-series data, historical records, high-write but low-read

    - Graph Databases are used for graphs, knowledge, recommendation, etc.

# StreamDB

    ## Data Streams

    ### Traditional Data Ingestion

    - Data sources are extracted, transformed, Loaded to a data warehouse

    - It's unsuitable for Reacting in Real Time!

    ### Stream Data Requirements

    - Traditional ETL supports queries on static snapshots

    - Delay between snapshots is often too high

    - Streams keep generating new data with high frequency

    - Query results keep changing

    - It's useful to have a query result that is always up-to-date

    ### Comparing Stream and DBMS

    |       | Stream  | DBMS    |
    |-------|---------|---------|
    | Data  | Static  | Dynamic |
    | Query | Dynaimc | Static  |

    ### ksqlDB - Streaming SQL

    ### Collection types

    |                         | Stream                               | Table                                                     |
    |-------------------------|--------------------------------------|-----------------------------------------------------------|
    | Insertion<br/>Semantics | New entries are<br/>appended         | New entries override<br/>prior entries with<br/> same key |
    | Purpose                 | Represent historical<br/>information | Represent the<br/>current state                           |

    ## Data Stream Topics

    - Temporal DB(Database with time stamp)

    - STREAM system(~2003)

    - kSQL system: kafka as the engine started as a project in LinkedIn

    ## Stream Data Types

    | Database <br/>management system       | Data Stream <br/> mamagement system  |
    |---------------------------------------|--------------------------------------|
    | Relation R : static<br/>until changed | Relation R(t) : varies<br/>over time |
    |                                       | Stream S: timestamped tuples         |

    ### Stream to relation

    - Relation R(t) is specified as a window over stream S

    - Tuple-based sliding window: S [Rows N]

    	- R(t) contains N tuples from S with the highest timestamps

    - Time-based sliding window: S [Range T]

    	- R(t) contains tuples from S starting from Now() - T

    - Partitioned sliding window: S [Partition by A1,A2,... Rows N]

    	- Separate windows for each value combination in A1,A2,...

    ### Relation to stream

    - Istream(R): R's inserted tuples with insertion timestamp

    - Dstream(R): R's deleted tuples with deletion timestamp

    - Rstream(R): R's inserted tuples with current timestamp

    ### Query Processing

    - Input query is compiled into continuous query plan

    - Query plan is composed from standard operators

    - Operators exchange tuple additions and deletions(Streams - additions, Relations - addition and deletions)

    ## Operators

    ```mermaid
    graph LR
    A[Input queue] --> B[Operator]
    B-->C[Output Queue]
    B-.->D[query synopsis]

    ```

    ### Join operator

    ```mermaid
    graph LR
    A[Input 1] --> O[operator]
    B[Input 2] --> O
    O --> C[Output]
    O -.-> D[Hash table for each input]

    ```

    - Join Algorithm

    	- Tuple addition/deletion in input 1 queue

    	- Extract join key from added queue

    	- Probe hash table of input 2 with key

    	- Add/delete resulting join tuples to output

    	- Update synopsis(hash table for input 1)

    ## Adaptive Query Planning

    ```mermaid
    graph LR
    A[Executor] -.Can Combine.- B[Profiler]
    B--Statistics-->C[Re-Optimizer]
    C--Join Order Cashing Constraints-->A
    C--Request Statistics-->B

    ```

    ### Minimizing Space Requirements

    - Very important for Stream DBs(it's size is unbounded)

    - Eliminate redundant data by synopsis sharing(especially in pub/sub)

    - Exploit constraints to prune unnecessary data

    - Shrink intermediate results via optimized scheduling

    ### Synopsis Sharing

    - Synopses of operators in same plan often overlap

    - Storing synopses separately means redundancy

    - Instead: global synopses with operator-specific views

    - Can extend to merge synopses of different plans

    ## Constraint Types

    - Referential integrity k-constraint

    	- Refers to key-foreign key joins

    	- Delay at most k between matching tuples arriving

    - Ordered-arrival k-constraint

    	- Stream elements at least k tuple apart are sorted

    - Clustered-arrival k-constraint

    	- Elements with same key can be at most k tuples apart

    - These can exploit each constraint for dropping tuples in certain scenarios

    ## Scheduling Policies

    - We have flexibility to decide when to invoke operators

    - Scheduling policy may influence queue sizes

    - FIFO: Fully process tuple batches in the order of arrival

    - Greedy: invoke operator discarding most tuples

    - Mix: combine a=operators into chains

    ### Example

    ```mermaid
    graph LR
    A[Input 1] --> B[Operator 1 with Selectivity:0.2]
    B --> C[Intermediate Result]
    C --> D[Operator 2]
    D --> E[Output]

    ```

    | Policy | T=0 | T=1 | T=2 | T=3 | T=4 | T=5 | T=6 |
    |--------|-----|-----|-----|-----|-----|-----|-----|
    | FIFO   | 1   | 1.2 | 2   | 2.2 | 3   | 3.2 | 4   |
    | Greedy | 1   | 1.2 | 1.4 | 1.6 | 1.8 | 2   | 2.2 |

    ## Approximation

    - Load Shedding: drop tuples to save overheads

    	- Can approximate aggregates based on samples

    	- Try to balance impact over all aggregates

    - Reducing synopses size: save memory

    	- Often reduces output size of following operators with potential drawback

    ## Apache Kafka Overview

    - Kafka is a java-based, distributed stream processing engine

    - Producer: Add records to different topics

    - Consumer: Subscribe to specific topics

    - Kafka Streams API offers filter, grouping, ... operators

    ## Kafka Topics

    - Each topic corresponds to a log of ordered records and each are key-value pair

    - Producers append to this log

    - Consumers receive updates for topics they subscribe to

    - Regular topic: delete tuples by space/time constraint

    - Compacted topic: new tuples override old keys

    ## Distributed Processing

    - Each topic is divided into partitions

    - Partitions are replicated across servers

    - Each partition has one dedicated leader

    ### Example

    ```mermaid
    flowchart TD
    subgraph s1 [server1]
    direction TB
    a1([Topic1,Partition1])
    a2[Topic1,Partition2]
    a3[Topic2,Partition1]
    end
    subgraph s2 [server2]
    direction TB
    b1[Topic1,Partition1]
    b2([Topic1,Partition2])
    b3[Topic2,Partition1]
    end
    subgraph s3 [servern]
    direction TB
    c1[Topic1,Partition1]
    c2[Topic1,Partition2]
    c3([Topic2,Partition1])
    end
    a1-->b1
    a1-->|Forward Changes|c1
    b2-->a2
    b2-->c2
    c3-->a3
    c3-->b3

    ```

    ## Copying with Insertions

    - Need to handle insertions with a very high frequency

    - Kafka streams uses RocksDB as underlying engine

    - Highly optimized for writes, good read performance(Key idea: sequential access)

    - Put logs in buffer first and then make page in disk

    ## Optimize for Reads

    - Typically use index structure

    - But then insertions require random data access, which leads to slow insertions

    - Instead: Log structured Merge Tree

    ### Log Structured Merge Tree

    - Maintains multiple levels containing sorted/indexed data

    - Data from one level is merged into next at overflow

    ### Reading LSM Tree

    - May have to check every level to find data

    - Checking each level is fast as data is sorted/indexed

    - Bloom filters reduce the number of levels to consider

    ## ksqlDB

    - High-level API on top of Kafka Streams

    - Trans SQL-like queries to kafka operators(Some similarities to STREAM query language)

    - Process collections of events: streams, tables

    - Pull queries execute once on current state

    - Push query results get continuously updated

    ### ksqlDB Collection Types

    ||
    ||

    ### ksqlDB Example

    - Creating Collections

    - Deriving Collections

    - Inserting Data

    - Pull Query

    - Push Query

    ### Query Types

    ||
    ||

# SpatialDB
