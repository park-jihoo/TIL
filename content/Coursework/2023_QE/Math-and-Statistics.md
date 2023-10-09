---
id: 7c4d5a76-4b08-4d26-92d0-8fabd0d23bdf
title: Math and Statistics
created_time: 2023-08-07T06:47:00.000Z
last_edited_time: 2023-09-16T07:30:00.000Z
하위 항목: []
subclass: 2023_QE
class: Coursework
작성일시: 2023-08-07T06:47:00.000Z
상위 항목: []

---

# Linear Algebra

    ## Systems of Linear Equations

    	- We write the system in following form

    		```undefined
    		\begin{bmatrix}a_{11}\\\vdots\\a_{m1}\end{bmatrix}x_1+\begin{bmatrix}a_{12}\\\vdots\\a_{m2}\end{bmatrix}x_2+\cdots+\begin{bmatrix}a_{1n}\\\vdots\\a_{mn}\end{bmatrix}x_n=\begin{bmatrix}b_{1}\\\vdots\\b_{m}\end{bmatrix}\iff\begin{bmatrix}a_{11}&\cdots&a_{1n}\\\vdots&&\vdots\\a_{m1}&\cdots&a_{mn}\end{bmatrix}\begin{bmatrix}x_{1}\\\vdots\\x_{m}\end{bmatrix}=\begin{bmatrix}b_{1}\\\vdots\\b_{m}\end{bmatrix}
    		```

    ## Matrices

    	- With m,n\in\N a real valued (m,n) matrix A is an m\cdot n tuple of the element a_{ij},i=1,...,n,j=1,...,n which is ordered according to a rectangular scheme consisting of m rows and n columns

    		```undefined
    		A = \begin{bmatrix}a_{11}&a_{12}&\cdots&a_{1n}\\a_{21}&a_{22}&\cdots&a_{2n}\\\vdots&\vdots&&\vdots\\a_{m1}&a_{m2}&\cdots&a_{mn}\end{bmatrix},a_{ij}\in\R
    		```

    	### Matrix Addition and Multiplication

    	- The sum of two matrices A,B is defined as the elementwise sum

    	- For matrix A \in \R^{m\times n}, B\in\R^{n\times k}, the elements c_{ij} of the product C=AB\in\R^{m\times k} are computed as

    		```undefined
    		c_{ij}=\sum_{l=1}^na_{il}b_{lj}
    		```

    	- In \R^{n\times n}, we define the identity matrix as the n \times n matrix containing 1 on the diagonal and 0 everywhere else

    	- Matrix multiplication, Addition have Associativity and Distributivity

    	### Inverse and Transpose

    	- Consider a square matrix A,B\in\R^{n\times n}. Let AB = I_n = BA then B is called the inverse of A and denoted by A^{-1}

    	- In 2\times 2 matrix

    		```undefined
    		A^{-1} = \frac1{a_{11}a_{22}-a_{21}a_{12}}\begin{bmatrix}a_{22}&-a_{12}\\-a_{21}&a_{11}\end{bmatrix}
    		```

    	- For A \in \R^{m\times n}, the matrix B\in\R^{n\times m} with b_{ij}=a_{ji} is called a transpose of A and we write B^\top = A

    	- If A^\top = A, then A is symmetric

    	### Multiplication by Scalar

    	- Associativity

    		```undefined
    		(\lambda\psi)C=\lambda(\psi C)\\\lambda(BC)=(\lambda B)C=B(\lambda C)=(BC)\lambda
    		```

    	- Distributivity

    		```undefined
    		(\lambda+\psi)C=\lambda C+\psi C\\\lambda(B+C)=\lambda B+\lambda C
    		```

    	### Compact representation of Systems of Linear Equations

    	```undefined
    	Ax =b
    	```

    ## Solving Systems of Linear Equations

    	### Particular and General Solution

    	- Find a particular solution to Ax=b

    	- Find all solutions to Ax=0

    	- Combine the solutions from steps 1 and 2 to the general solutions

    	### Elementary Transformations

    	- Exchange of two matrix

    	- Multiplication of an equation(row) with a constant \lambda\in\R\backslash\{0\}

    	- Addition of two equation(row)

    	- A matrix is in row-echelon form if

    		- All rows that contain only zeros are at the bottom of the matrix

    		- Looking at nonzero rows only, the first nonzero number from the left is always strictly to the right of the pivot of the row above it

    	### Algorithms for Solving a System of Linear Equations

    	- If square, then x=A^{-1}b

    	- If not, then x=(A^\top A)^{-1}A^\top b

    ## Vector Spaces

    	### Groups

    	- Consider a set \mathcal G and an operation \otimes defined on \mathcal G. Then G:=(\mathcal G, \otimes) is called a group if the following holds

    		- Closure of \mathcal G under \otimes: \forall x, y \in \mathcal G: x\otimes y \in \mathcal G

    		- Associativity: \forall x,y,z\in\mathcal G:(x\otimes y)\otimes z = x \otimes(y\otimes z)

    		- Neutral element: \exists e\in\mathcal G\ \forall x\in \mathcal G:x\otimes e=x\text{ and }e\otimes x = x

    		- Inverse element: \forall x\in \mathcal G,\exist y\in\mathcal G:x\otimes y = e \text{ and }y\otimes x=e

    	### Vector Space

    	- A real-valued vector space V=(\mathcal V,+,\cdot) is a set \mathcal V with two operations

    		```undefined
    		\begin{aligned}+&:\mathcal V \times \mathcal V\to\mathcal V\\\cdot&:\R\times\mathcal V\to\mathcal V\end{aligned}
    		```

    		where

    			- (\mathcal V,+) is an Abelian group

    			- Distributivity

    			- Associativity(outer operation)

    			- Neural element with respect to the outer operation

    	### Vector Subspaces

    	- Let V=(\mathcal V,+,\cdot) be a vector space and \mathcal{U}\subseteq\mathcal{V,U\neq }\empty. Then U = (\mathcal U, +,\cdot) is called vector subspace of V if U is a vector space with operations + and \cdot restricted to \mathcal U\times\mathcal U and \R\times\mathcal U

    ## Linear Independence

    	- Consider a vector space V and a finite number of vectors x_1,…,x_k\in V, Then every v\in V of the form

    		```undefined
    		v = \lambda_1x_1+\cdots+\lambda_kx_k=\sum_{i=1}^k\lambda_ix_i\in V
    		```

    		with \lambda_1,…,\lambda_k\in\R is a linear combination of vectors x_1,…,x_k

    	- If there is a non-trivial linear combination with at least one \lambda_i\ne0, the vectors x_1,…,x_k are linearly dependent. If only one trivial solutions exists, i.e., \lambda_1=...=\lambda_k=0 the vectors x_1,…,x_k are linearly independent

    ## Basis and Rank

    	### Generating Set and Basis

    	- Consider a vector space V and set of vectors \mathcal A = \{x_1,...,x_k\}\sube \mathcal V. If every vector v\in\mathcal V can be expressed as a linear combination of x_1,…,x_k, \mathcal A is called a generating set of V

    	- The set of all linear combinations of vectors in \mathcal A is called the span of \mathcal A. We write V=\text{span}[\mathcal A]

    	- If a generating set \mathcal A of V is minimal if there exists no smaller set that spans V. Every linearly independent generating set of V is minimal and is called a basis of V

    	- Basis of subspace U can be found by executing the following steps

    		- Write the spanning vectors as columns of matrix A

    		- Determine the row-echelon form of A

    		- The spanning vectors associated with the pivot columns are a basis of U

    	### Rank

    	- The number of linearly independent columns of a matrix A\in\R^{m\times n} equals the number of linearly independent rows and is called the rank of A and is denoted by \text{rk}(A)

    ## Linear Mappings

    	- For vector spaces V,W, a mapping \Phi:V\to W is called a linear mapping if

    		```undefined
    		\forall x,y\in V,\forall \lambda,\psi\in\R:\Phi(\lambda x+\psi y) =\lambda\Phi(x)+\psi\Phi(y)
    		```

    	- Consider a mapping \Phi:\mathcal{V\to W} where \mathcal{V,W} be arbitrarysets. Then \Phi is called

    		- Injective if \forall x,y\in\mathcal V:\Phi(x)=\Phi(y)\implies x=y

    		- Surjective if \mathcal{\Phi(V)=W}

    		- Bijective if it is injective and surjective

# Analytical Geometry

    ## Norms

    	- A norm on vector space V is a function

    		```undefined
    		\begin{aligned}\|\cdot\|:V&\mapsto\R\\x&\mapsto\|x\|\end{aligned}
    		```

    		which assigns each vector x on its length \|x\|\in\R

    	- Norms hold

    		- Absolutely homogeneous: \|\lambda x\|=|\lambda|\|x\|

    		- Triangle inequality: ||x+y||\le\|x\|+\|y\|

    		- Positive definite: \|x\|\ge0\text{ and }\|x\|=0 \iff x=0

    	- Manhattan norm

    		```undefined
    		\|x\|_1:=\sum_{i=1}^n|x_i|
    		```

    	- Euclidean norm

    		```undefined
    		\|x\|_2 :=\sqrt{\sum_{i=1}^nx_i^2}=\sqrt{x^\top x}
    		```

    ## Inner Products

    	### Dot Product

    	- The scalar product/dot product in \R^n is given by

    		```undefined
    		x^\top y = \sum_{i=1}^nx_iy_i
    		```

    	### General Inner Products

    	- Let V be a vector space and \Omega:V\times V\to\R be a bilinear mapping that takes two vectors and maps them onto a real number. Then

    		- \Omega is called symmetric if \Omega(x,y)=\Omega(y,x) for all x,y\in V, i.e the order of the arguments does not matter

    		- \Omega is called positive definite if

    			```undefined
    			\forall x\in V\backslash \{0\}:\Omega(x,x)>0,\,\Omega(0,0)=0
    			```

    	- Let V be a vector space and \Omega:V\times V\to\R be a bilinear mapping that takes two vectors and maps them onto a real number. Then

    		- A positive definite, symmetric bilinear mapping \Omega:V\times V\to\R is called an inner product on V. We typically write \braket{x,y} instead of \Omega(x,y)

    		- The pair (V,\braket{\cdot,\cdot}) is called an inner product space or vector spacew ith inner product

    	### Symmetric, Positive Definite Matrices

    	- It holds for all x,y\in V that

    		```undefined
    		\braket{x,y}= \left\lang\sum_{i=1}^n\psi_ib_i\sum_{j=1}^n\lambda_jb_j\right\rang = \hat xA^\top\hat y
    		```

    	- A symmetric matrix A \in\R^{n\times n} satisfies \forall x\in V\backslash\{0\}:x^\top Ax>0 is called symmetric, positive definite or just positive definite. If only \ge holds, then symmetric, positive semidefinite

    	- Theorem

    ## Lengths and Distances

    ## Angles and Orthogonality

    ## Orthonormal Basis

    ## Orthogonal Complement

    ## Orthogonal Projection

# Matrix Decompositions

# Vector Calculus

# Probability

# Random variables

# Expectation, Variance and Convergence

# Convergence, LLN, CLT

# Statistical Inference, Bias, MSE

# Cumulative Distribution function and Bootstrap

# Parametric Inference, Likelihood, MLE

# Hypothesis test, P-value, multiple test correction

# Bayesian inference

# Inequalities(Extra)
