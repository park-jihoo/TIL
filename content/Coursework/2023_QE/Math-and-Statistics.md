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

    		> 📖 For a real-valued, finite-dimensional vector space V and an ordered basis B of V, it holds that \braket{\cdot,\cdot}:V\times V\to\R is an inner product if and only if there exists a symmetric, positive definite matrix A \in \R^{n\times n} with

    			```undefined
    			\braket{x,y}=\hat x^\top A\hat y
    			```

    ## Lengths and Distances

    	- Any inner product induces a norm

    		```undefined
    		\|x\|:=\sqrt{\braket{x,x}}
    		```

    	- Consider an inner product space \braket{V,\braket{\cdot,\cdot}}, Then

    		```undefined
    		d(x,y):=\|x-y\|=\sqrt{\braket{x-y,x-y}}
    		```

    		is called the distance between x and y for x,y\in V

    	- A metric d satisfies

    		- d is positive definite

    		- d is symmetric

    		- Triangle inequality

    ## Angles and Orthogonality

    	- There exists a unique \omega\in[0,\pi] with

    		```undefined
    		\cos\omega=\frac{\braket{x,y}}{||x||\cdot||y||}
    		```

    	- Two vectors x and y are orthogonal if and only if \braket{x,y}=0, and we write x\perp y. If additionally \|x\|=1=\|y\|, then x and y are orthonormal

    	- A square matrix A \in\R^{n\times n} is an orthogonal matrix if and only if its columns are orthonormal so that

    		 

    		```undefined
    		AA^\top=I=A^\top A
    		```

    ## Orthonormal Basis

    	- Consider an n-dimensional vector space V and a basis \{b_1,...,b_n\} of V. If

    		```undefined
    		\begin{aligned}\braket{b_i,b_j}&=0 &\text{for }i\neq j \\\braket{b_i,b_i}&=1\end{aligned}
    		```

    		for all i,j=1,…,n then the basis is called an orthonormal basis

    ## Orthogonal Complement

    	- Consider a D-dimensional vector space V and M-dimensional subspace U\subseteq V. Then its orthogonal complement U^\perp is a (D-M)-dimensional subspace of V and contains all vectors in V that are orthogonal to every vector in U. Furthermore, U\cap U^\perp =\{0\} so that any vector x\in V can be uniquely decomposed

    ## Orthogonal Projection

    	- The projection \pi_U(x) is closest to x, where **closest** implies that the distance \|x-\pi_U(x)\| is minimal

    	- Find the coordinate \lambda. The orthogonality condition yields

    		```undefined
    		\lambda=\frac{b^\top x}{b^\top b}=\frac{b^\top x}{\|b\|^2}
    		```

    	- Finding the projection point \pi_U(x)\in U, Since \pi_U(x)=\lambda b

    		```undefined
    		\pi_U(x)=\lambda b=\frac{\braket{x,b}}{\|b\|^2}b=\frac{b^\top x}{\|b\|^2}b
    		```

    	- Finding the projection matrix P

    		```undefined
    		P_\pi = \frac{bb^\top}{\|b\|^2}
    		```

    	### Projection into General Subspace

    	- Find the coordinate \lambda_1,...,\lambda_m of the projection

    		```undefined
    		\pi_U(x) = \sum_{i=1}^m\lambda_ib_i=B\lambda\\\lambda=(B^\top B)^{-1}B^\top x
    		```

    	- Finding the projection point \pi_U(x)\in U, Since \pi_U(x)=B\lambda

    		```undefined
    		\pi_U(x)=B(B^\top B)^{-1}B^\top x
    		```

    	- Find the Projection matrix P_\pi

    		```undefined
    		P_\pi = B(B^\top B)^{-1}B^\top
    		```

# Matrix Decompositions

    ## Determinant and Trace

    	- The determinant of a square matrix A \in \R^{n\times n} is a function that maps A onto real number.

    	- For any square matrix A\in\R^{n\times n} it holds that A is invertible iff \det(A)\neq 0

    	- n=2

    		```undefined
    		\det(A)=\begin{vmatrix}a&b\\c&d\end{vmatrix} = ad-bc
    		```

    	- At upper triangular matrix T, \det(T) = \prod_{i=1}^n T_{ii}

    	- Laplace Expansion

    		- Expansion along column j

    			```undefined
    			\det(A)=\sum_{k=1}^n(-1)^{k+j}a_{kj}\det(A_{k,j})
    			```

    		- Expansion along row j

    			```undefined
    			\det(A)=\sum_{k=1}^n(-1)^{j+k}a_{kjk}\det(A_{j,k})
    			```

    	- Determinant has following properties

    		- \det(AB)=\det(A)\det(B)

    		- \det(A)=\det(A^\top)

    		- \det(A^{-1})=\frac{1}{\det(A)}

    		- Adding a multiple of a column to another one does not change \det(A)

    		- \det(\lambda A)=\lambda^n\det(A)

    	- A square matrix A\in\R^{n \times n} has \det(A)\neq 0 iff \text{rk}(A)=n. A is invertible iff it’s full rank

    	- The trace of square matrix A is defined as

    		```undefined
    		\text{tr}(A) :=\sum_{i=1}^na_ii
    		```

    	- For \lambda\in\R and a square matrix A,

    		```undefined
    		\begin{aligned}p_A(\lambda)&\coloneqq\det(A-\lambda I)\\&=c_0+c_1\lambda+c_2\lambda^2+\cdots_+c_{n-1}\lambda^{n-1}+(-1)^n\lambda^n\\c_0&=\det(A),c_{n-1}=(-1)^{n-1}\text{tr}(A)\end{aligned}
    		```

    ## Eigenvalues and eigenvectors

    	- Let A be a square matrix. Then \lambda\in\R is an eigenvalue of A and x\in\R^n\backslash\{0\} is the corresponding eigenvector of A if Ax=\lambda x

    	- The following statements are equivalent

    		- \lambda is an eigenvalue of A

    		- There exists an x\in\R^n\backslash\{0\} with Ax=\lambda x, or equivalently (A-\lambda I_n)x=0 can be solved non-trivially,i.e. x\neq 0

    		- \text{rk}(A-\lambda I_n)<n

    		- \det(A-\lambda I_n)=0

    	- Two vectors that point in same directions are called correlated. Two vectors are colinear if they point in the same or the opposite direction

    	- \lambda\in\R is an eigenvalue of A iff \lambda is a root of the characteristic polynomial p_A(\lambda) of A

    	- For A, the setof all eigenvectors of A associated with eigenvalue \lambda spans a subspace of \R^n, which is called the eigenspace of A with respect to $$\lambda## and is denoted by E_\lambda

    	- \det(A) = \prod_{i=1}^n\lambda_i,\text{tr}(A)=\sum_{i=1}^n\lambda_i

    ## Cholesky Decomposition

    	- A symmetric, positive definite matrix A can be factorized into a product A=LL^\top, where L is a lower-triangular matrix with positive diagonal elements

    	- Given a Cholesky decomposition A=LL^\top, we know that \det(A)=\det(L)\det(L^\top)

    ## Eigendecomposition and Diagonalization

    	- A matrix A is diagonalizable if it is similar to diagonal matrix, if there exists an invertible matrix P such that D=P^{-1}AP

    	- A square matrix A can be factored into

    		```undefined
    		A=PDP^{-1}
    		```

    		where P\in\R^{n\times n} and D is a diagonal matrix whose diagonal entries are the eigenvalues of A, if and only if the eigenvectors of A form a basis of \R^n

    	- A symmetric matrix S can always be diagonalized

    	### Eigendecomposition

    	- Compute eigenvalues and eigenvectors

    	- Check for existence. (Does it can be diagonalized?)

    	- Construct the matrix P to diagonalize A

    ## SVD

    	```undefined
    	A=U\Sigma V^\top
    	```

    	### Geometric intuitions for SVD

    	- The matrix V performs a basis change in domain \R^n from \tilde B to the standard basis B

    	- Having changed the coordinate system to \tilde B, \Sigma scales the new coordinates by the singular values \sigma_i

    	- U performs a basis change in the codomain \R^m from \tilde C to the cannonical basis of \R^m, represented by a rotation of the red and orange vectors out of the e_1-e_2 plane.

    	### Constructions of SVD

    	- A^\top A = (U\Sigma V^\top)^\top(U\Sigma V^\top)=  V\Sigma^\top U^\top U\Sigma V^\top = V\Sigma^\top\Sigma V^\top 

    	- AA^\top = (U\Sigma V^\top)(U\Sigma V^\top)^\top= U\Sigma V^\top V\Sigma^\top U^\top = U\Sigma \Sigma^T U^\top

    		```undefined
    		AV=U\Sigma
    		```

    	- The SVD and the eigendecomposition are closely related through their projections

    		- The left-singular vectors of A are eigenvectors of A A^\top

    		- The right-singular vectors of A are eigenvectors of A^\top A

    		- The nonzero singular values of A are the square roots of the nonzero eigenvalues of both A A^\top and A^\top A

# Vector Calculus

    ## Differentiation of Univariate Functions

    	- The difference quotient computes the slope

    		```undefined
    		\frac{\delta y}{\delta x}:=\frac{f(x+\delta x)-f(x)}{\delta x}
    		```

    	- More formally, for h>0 the derivative is

    		```undefined
    		\frac{df}{dx}:=\lim_{h\to 0}\frac{f(x+h)-f(x)}h
    		```

    	### Taylor Series

    	- Taylor Polynomial of degree n of f at x_0 is defined as

    		```undefined
    		T_n(x)\coloneqq \sum_{k=0}^n\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k
    		```

    	- Taylor Series: For a smooth function f\in\mathcal C^\infty, the taylor series is defined as

    		```undefined
    		T_\infty(x)=\sum_{k=0}^\infty\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k
    		```

    	### Differential Rules

    	- Product rule

    		```undefined
    		(f(x)g(x))'=f'(x)g(x)+f(x)g'(x)
    		```

    	- Quotient rule

    		```undefined
    		\left(\frac{f(x)}{g(x)}\right)'=\frac{f'(x)g(x)-f(x)g'(x)}{(g(x))^2}
    		```

    	- Sum rule

    		```undefined
    		(f(x)+g(x))'=f'(x)+g'(x)
    		```

    	- Chain rule

    		```undefined
    		(g(f(x)))'=g'(f(x))f'(x)
    		```

    ## Partial Differentiation and Gradients

    	- For a function f of n variables, partial derivatives are

    		```undefined
    		\frac{\partial f}{\partial x_i} = \lim_{h\to 0}\frac{f(x_1,...,x_i+h,...,x_n)-f(x)}h
    		```

    	- We collect them to row vector and it’s gradient

    		```undefined
    		\nabla_x f=\text{grad}f=\frac{df}{dx}=\begin{bmatrix}\frac{\partial f(x)}{\partial x_1}&\frac{\partial f(x)}{\partial x_2}&\cdots&\frac{\partial f(x)}{\partial x_n}\end{bmatrix}
    		```

    	### Basic rules of Partial differentiation

    	- Product rule

    		```undefined
    		\frac{\partial}{\partial x}(f(x)g(x))=\frac{\partial f}{\partial x}g(x)+\frac{\partial g}{\partial x}f(x)
    		```

    	- Sum rule

    		```undefined
    		\frac{\partial}{\partial x}(f(x)+g(x)) = \frac{\partial f}{\partial x}+\frac{\partial g}{\partial x}
    		```

    	- Chain rule

    		```undefined
    		\frac \partial{\partial x}(g(f(x)))=\frac{\partial g}{\partial f}\frac{\partial f}{\partial x}
    		```

    	### Chain Rule

    	```undefined
    	\frac{df}{dt}=\frac{\partial f}{\partial x_1}\frac{\partial x_1}{\partial t}+\frac{\partial f}{\partial x_2}\frac{\partial x_2}{\partial t}
    	```

    ## Gradients of Vector-Valued functions

    	- The collection of all first-order partial derivatives of a vector values function f:\R^n\to\R^m is called the Jacobian

    		```undefined
    		J(i,j)=\frac{\partial f_i}{\partial x_j}
    		```

    	- The Jacobian represents the coordinate transformation we are looking for.

    ## Gradients of matrices

    	```undefined
    	J_{ijkl}=\frac{\partial A_{ij}}{\partial B_{kl}}
    	```

    ## Useful Identities for computing gradients

    	```undefined
    	\begin{aligned}\frac{\partial}{\partial X}f(X)^\top &=\left(\frac{\partial f(X)}{\partial X}\right)^\top\\\frac{\partial}{\partial X}\text{tr}(f(X))&=\text{tr}\left(\frac{\partial f(X)}{\partial X}\right)\\\frac{\partial}{\partial X}\det(f(X))&=\det(f(X))\text{tr}\left(f(X)^{-1}\frac{\partial f(X)}{\partial X}\right)\\\frac{\partial}{\partial X}f(X)^{-1}&=-f(X)^{-1}\frac{\partial f(X)}{\partial X}f(X)^{-1}\end{aligned}
    	```

    ## Backpropagation and Automatic Differentiation

    	### Gradients in a deep network

    	- We need minimized squared loss

    		```undefined
    		L(\theta)=\|y-f_K(\theta,x)\|^2
    		```

    	- The chain rule allows us to determine the partial derivative as

    		```undefined
    		\frac{\partial L}{\partial\theta_i}=\frac{\partial L}{\partial f_K}\frac{\partial f_K}{\partial f_{K-1}}\cdots\frac{\partial f_{i+2}}{\partial f_{i+1}}\frac{\partial f_{i+1}}{\partial \theta_i}
    		```

    	### Automatic Differentiation

    	- We can apply chain rule for variables x_i

    		```undefined
    		\frac{\partial f}{\partial x_i}=\sum_{x_j:x_i\in\text{Pa}(x_j)}\frac{\partial f}{\partial x_j}\frac{\partial x_j}{\partial x_i}=\sum_{x_j:x_i\in\text{Pa}(x_j)}\frac{\partial f}{\partial x_j}\frac{\partial g_j}{\partial x_i}
    		```

# Probability

    ## Probability

    	- A function \mathbb P that assigns a real number \mathbb P(A) to each event A is a probability distribution or a probability measure if it satisfies following 3 axioms

    		- \mathbb P(A)\ge 0 for every A

    		- \mathbb P(\Omega)=1

    		- If A_1,A_2,… are disjoint then

    			```undefined
    			\mathbb P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty\mathbb P(A_i)
    			```

    ## Probability on Finite Sample Spaces

    	- If \Omega is finite and if each outcome is equally likely, then

    		```undefined
    		\mathbb P(A)=\frac{|A|}{|\Omega|}
    		```

    		which is called the **uniform probability distribution**

    ## Independent Events

    	- Two events A and B are independent if

    		```undefined
    		\mathbb P(AB) =\mathbb P(A)\mathbb P(B)
    		```

    		and we write A\amalg B.

    	- Independence is sometimes assumed and sometimes derived

    	- Disjoint events with positive probability are not independent

    ## Conditional Probability

    	- If \mathbb P(B)>0 then the conditional probability of A given B is

    		```undefined
    		\mathbb P(A|B)=\frac{\mathbb P(AB)}{\mathbb P(B)}
    		```

    	- A and B are independent events if and only if \mathbb P(A|B)=\mathbb P(A)

    	- In general, \mathbb P(A|B) \neq \mathbb P(B|A)

    ## Bayes’ Theorem

    	- Let A_1,…,A_k be a partition of \Omega. Then, for any event B,

    		```undefined
    		\mathbb P(B) = \sum_{i=1}^k\mathbb P(B|A_i)P(A_i)
    		```

    	- Let A_1,…,A_k be a partition of \Omega such that \mathbb P(A_i)>0 for each i. If \mathbb P(B)>0, then for each i=1,…,k,

    		```undefined
    		\mathbb P(A_i|B)=\frac{\mathbb P(B|A_i)\mathbb P(A_i)}{\sum_j \mathbb P(B|A_j)\mathbb P(A_j)}
    		```

    	- We call \mathbb P(A_i) the prior probability of A and \mathbb P(A_i|B) the posterior probability of A

# Random variables

    ## Distribution Functions and Probability Functions

    	- The cumulative distribution function, or cdf is the function F_X:\R \to [0,1], defined by

    		```undefined
    		F_X(x)=\mathbb P(X\le x)
    		```

    	- Let X have CDF F and Y have CDF G. If F(x)=G(x) for all x, then \mathbb P(X\in A)=\mathbb P(Y\in A) for all A

    	- A function F mapping the real line to [0,1] is a CDF for some probability \mathbb P if and only if F satisfies the following 3 conditions

    		- F is non-decreasing

    		- F is normalized

    		- F is right-continuous

    	- X is discrete if it takes countably many values. We define the probability function or probability mass function for X by f_X(x)=\mathbb P(X=x)

    	- X is continuous if there exists a function f_X such that f_X(x)\ge 0 for all x, \int_{-\infty}^\infty f_X(x)dx=1 and for every a\le b,

    		```undefined
    		\mathbb P(a<X<b)=\int_a^b f_X(x)dx
    		```

    		The function f_X is called the probability density function. We have that

    		```undefined
    		F_X(x)=\int_{-\infty}^x f_X(t)dt
    		```

    		and f_X(x)=F'_X(x) at all points x at which F_X is differentiable

    	- Let X be a random variable with cdf F. The inverse cdf or quantile function is defined by 

    		```undefined
    		F^{-1}(q)=\inf\left\{x:F(x)>q\right\}
    		```

    		for q\in [0,1]. If F is strictly increasing and continuous then F^{-1}(q) is the unique real number x such that F(x)=q

    ## Some Important Discrete Random Variables

    	### Point Mass Distribution

    	```undefined
    	F(x)=\begin{cases}0&x<a\\1&x\ge a\end{cases}
    	```

    	### Discrete Uniform Distribution

    	```undefined
    	f(x)=\begin{cases}1/k&\text{for }x=1,...,k\\0&\text{otherwise.}\end{cases}
    	```

    	### Bernoulli Distribution

    	```undefined
    	f(x) = p^x(1-p)^{1-x}, x\in\{0,1\}
    	```

    	### Binomial Distribution

    	```undefined
    	f(x)=\begin{cases}\binom nxp^x(1-p)^{n-x}&\text{for }x=0,...,n\\0&\text{otherwise.}\end{cases}
    	```

    	### Geometric Distribution

    	```undefined
    	\mathbb P(X=k)=p(1-p)^{k-1},k\ge 1
    	```

    	### Poisson Distribution

    	```undefined
    	f(x)=e^{-\lambda}\frac{\lambda^x}{x!}
    	```

    ## Some Important Continuous Random Variables

    	### Uniform Distribution

    	```undefined
    	f(x)=\begin{cases}\frac 1{b-a}&\text{for }x\in[a,b]\\0&\text{otherwise}\end{cases}
    	```

    	### Normal(Gaussian)

    	```undefined
    	f(x)=\frac 1{\sigma\sqrt{2\pi}}\exp\left\{-\frac1{2\sigma^2}(x-\mu)^2\right\}
    	```

    	- If \mu=0 and \sigma=1, then X has a standard Normal distribution

    	- If X\sim N(\mu,\sigma^2), then Z=(X-\mu)/\sigma\sim N(0,1)

    	- If Z\sim N(0,1), then X=\mu+\sigma Z \sim N(\mu,\sigma^2)

    	- If X_i \sim N(\mu_i,\sigma_i^2), i=1,…,n are independent, then

    		```undefined
    		\sum_{i=1}^n X_i\sim N\left(\sum_{i=1}^n\mu_i,\sum_{i=1}^n\sigma_i^2 \right)
    		```

    	### Exponential Distribution

    	```undefined
    	f(x)=\frac1\beta e^{-x/\beta}
    	```

    	### Gamma Distribution

    	- For \alpha>0, Gamma function is defined by \Gamma(\alpha)=\int_0^\infty y^{\alpha-1}e^{-y}dy

    	- X has gamma distribution if

    		```undefined
    		f(x)=\frac1{\beta^\alpha\Gamma(\alpha)}x^{\alpha-1}e^{-x/\beta},x>0
    		```

    	### Beta Distribution

    	```undefined
    	f(x)=\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}x^{\alpha -1}(1-x)^{\beta-1},0<x<1
    	```

    	### t and Cauchy Distribution

    	```undefined
    	f(x)=\frac{\Gamma\left(\frac{\nu+1}{2}\right)}{\Gamma\left(\frac{\nu}{2}\right)}\frac1{\left(1+\frac{x^2}{\nu}\right)^{(\nu+1)/2}}
    	```

    	### \chi^2 Distribution

    	```undefined
    	f(x)=\frac1{\Gamma(p/2)2^{p/2}}x^{(p/2)-1}e^{-x/2},x>0
    	```

    ## Bivariate Distributions

    	- In the continuous case, we call a function f(x,y) a pdf for the random variables (X,Y) if

    		- f(x,y)\ge0 for all (x,y)

    		- \int_{-\infty}^\infty\int_{-\infty}^\infty f(x,y)dxdy=1

    		- for any set A\in\R\times\R, \mathbb P((X,Y)\in A)=\int\int_A f(x,y)dxdy

    ## Marginal Distributions

    	- If (X,Y) have joint distribution with mass function f_{X,Y}, then the marginal mass function for X is defined by

    		```undefined
    		f_X(x)=\mathbb P(X=x)=\sum_y\mathbb P(X=x,Y=y)=\sum_yf(x,y)
    		```

    		and the marginal function for Y is defined by

    		```undefined
    		f_Y(y)=\mathbb P(Y=y)=\sum_x\mathbb P(X=x,Y=y)=\sum_xf(x,y)
    		```

    	- For continuous random variables, the marginal densities are

    		```undefined
    		f_X(x)=\int f(x,y)dy,\text{ and }f_Y(y)=\int f(x,y)dx
    		```

    ## Independent Random Variables

    	- Two random variables X and Y are independent if, for every A and B,

    		```undefined
    		\mathbb P(X\in A, Y\in B)=\mathbb P(X\in A)\mathbb P(Y\in B)
    		```

    		and we write X\amalg Y

    	- Let X and Y have joint PDF f_{X,Y}. Then X\amalg Y if and only if f_{X,Y}(x,y)=f_X(x)f_Y(y) for all values x and y

    	- Suppose that the range of X and Y is a (possibly infinite) rectangle. If f(x,y)=g(x)h(y) for some functions g and h then X and Y are independent

    ## Conditional Distributions

    	- The conditional probability mass function is

    		```undefined
    		f_{X|Y}(x|y)=\mathbb P(X=x|Y=y)=\frac{\mathbb P(X=x,Y=y)}{\mathbb P(Y=y)}=\frac{f_{X,Y}(x,y)}{f_Y(y)}
    		```

    		if f_Y(y)>0

    	- For continuous random variables, the conditional probability density function

    		```undefined
    		f_{X|Y}(x|y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}
    		```

    		assuming that f_Y(y)>0. Then

    		```undefined
    		\mathbb P(X\in A|Y=y)=\int_A f_{X|Y}(x|y)dx
    		```

    ## Multivariate Distributions and iid samples

    	- We say that X_1,…,X_n are independent if, for every A_1,…,A_n,

    		```undefined
    		\mathbb P(X_1\in A_1,...,X_n\in A_n)=\prod_{i=1}^n\mathbb P(X_i\in A_i)
    		```

    	- If X_1,…,X_n are independent and each has the same marginal distribution with cdf F, we say that X_1,…,X_n are iid and we write

    		```undefined
    		X_1,…,X_n\sim F
    		```

    ## Two important Multivariate Distributions

    	### Multinomial

    	- The multivariate version of a Binomial

    		```undefined
    		f(x)=\binom{n}{x_1,...x_k}p_1^{x_1}\cdots p_k^{x_k}
    		```

    	- Suppose that X\sim \text{Multinomial}(n,p) where X=(X_1,…,X_k) and p=(p_1,…,p_k). The marginal distribution of X_j is \text{Binomial} (n,p_j)

    	### Multivariate Normal

    	- Let

    		```undefined
    		Z=\begin{pmatrix}Z_1\\\vdots\\Z_k\end{pmatrix}
    		```

    		where Z_1,…,Z_k \sim N(0,1) are independent. The density of Z is

    		```undefined
    		\begin{aligned}f(z)&=\prod_{i=1}^k f(z_i)=\frac1{(2\pi)^{k/2}}\exp\left\{-\frac12\sum_{j=1}^kz_j^2\right\}\\&=\frac1{(2\pi)^{k/2}}\exp\left\{-\frac12z^\top z \right\}\end{aligned}
    		```

    	- More generally, X \sim N(\mu,\Sigma)

    		```undefined
    		f(x;\mu,\Sigma)=\frac1{(2\pi)^{k/2}|(\Sigma)|^{1/2}}\exp\left\{-\frac12(x-\mu)^\top\Sigma^{-1}(x-\mu)\right\}
    		```

    	- Suppose we partition a random normal vector X as X=(X_a,X_b), We can similarly partition \mu=(\mu_a,\mu_b) and

    		```undefined
    		\Sigma=\begin{pmatrix}\Sigma_{aa}&\Sigma_{ab}\\\Sigma_{ba}&\Sigma_{bb}\end{pmatrix}
    		```

    ## Transformations of Random Variables

    	- Three steps for transformations

    		- For each y, find the set A_y=\{x:r(x)\le y\}

    		- Find the CDF

    			```undefined
    			\begin{aligned}F_Y(y)&=\mathbb P(Y\le y)=\mathbb P(r(X)\le Y)\\&=\mathbb P(\{x;r(x)\le y\})\\&=\int_{A_y}f_X(x)dx\end{aligned}
    			```

    		- The PDF is f_Y(y)=F'_Y(y)

    ## Transformations of Several Random Variables

    	- Three steps for transformations

    		- For each y, find the set A_z=\{(x,y):r(x,y)\le z\}

    		- Find the CDF

    			```undefined
    			\begin{aligned}F_Z(z)&=\mathbb P(Z\le z)=\mathbb P(r(X, Y)\le z)\\&=\mathbb P(\{(x,y);r(x,y)\le z\})\\&=\int\int_{A_z}f_{X,Y}(x,y)dx\end{aligned}
    			```

    		- The PDF is f_Y(y)=F'_Y(y)

# Expectation, Variance and Convergence

    ## Expectation of a Random Variable

    	- The expected value, or mean, or first moment of X is defined to be

    		```undefined
    		\mathbb E(X)=\int xdF(x)=\begin{cases}\sum_xxf(x)&\text{if }X\text{ is discrete}\\\int xf(x)dx&\text{if }X\text{ is continuous}\end{cases}
    		```

    	- The rule of lazy statistician: Let Y=r(X). Then

    		```undefined
    		\mathbb E(Y)=\mathbb E(r(X))=\int r(x)dF_x(x)
    		```

    	- The k^{th} moment of X is defined to be \mathbb E(X^k) assuming that \mathbb E(|X|^k)<\infty

    	- It the k^{th} moment exists and if j<k then the j^{th} moment exists

    ## Properties of Expectations

    	- If X_1,…,X_n are random variables and a_1,…,a_n are constants, then

    		```undefined
    		\mathbb E\left(\sum_i  a_iX_i\right)=\sum_i a_i\mathbb E(X_i)
    		```

    	- Let X_1,…,X_n be independent random variables. Then,

    		```undefined
    		\mathbb E\left(\prod_{i=1}^n X_i\right)=\prod_i \mathbb E(X_i)
    		```

    ## Variance and Covariance

    	- The variance measures the spread of a distribution

    	- Let X be a random variable with mean \mu. The variance of X is defined by

    		```undefined
    		\sigma^2=\mathbb E(X-\mu)^2=\int(x-\mu)^2 dF(x)
    		```

    	- Assuming the variance is well defined, it has the following properties

    		- \mathbb V(X)=\mathbb E(X^2)-\mu^2

    		- If a and b are constants, then \mathbb V(aX+b)=a^2\mathbb V(X)

    		- If X_1,…,X_n are independent and a_1,…,a_n are constants, then

    			```undefined
    			\mathbb V\left(\sum_{i=1}^n a_iX_i \right)=\sum_{i=1}^na_i^2\mathbb V(X_i)
    			```

    	- Let X_1,…,X_n be iid and let \mu=\mathbb E(X_i) and \sigma^2=\mathbb V(X_i). Then,

    		```undefined
    		\mathbb E(\bar X_n)=\mu,\ \mathbb V(\bar X_n)=\frac{\sigma^2}n,\ \mathbb E(S_n^2)=\sigma^2
    		```

    	- Let X and Y be random variables with means \mu_X and \mu_Y and standard deviations \sigma_X and \sigma_Y. Define the covariance between X and Y by

    		```undefined
    		\text{Cov}(x,y)=\mathbb E\left((X-\mu_X)(Y-\mu_Y)\right)
    		```

    		and the correlation by

    		```undefined
    		\rho=\rho(X,Y)=\frac{\text{Cov}(x,y)}{\sigma_x\sigma_y}
    		```

    	- The covariance satisfies

    		```undefined
    		\text{Cov}(X,Y)=\mathbb E(XY)-\mathbb E(X)\mathbb E(Y)
    		```

    	- For random variables X_1,…,X_n

    		```undefined
    		\mathbb V\left(\sum_i a_iX_i\right)=\sum_i a_i^2\mathbb V(X_i)2\sum\sum_{i<j}a_ia_j\text{Cov}(X_i,X_j)
    		```

    ## Expectation and Variance of Important Random Variables

    	| Distribution                    | Mean                  | Variance                                                                                                                                                                  |
    	|---------------------------------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    	| Point mass at a                 | a                     | 0                                                                                                                                                                         |
    	| Bernoulli(p)                    | p                     | p(1-p)                                                                                                                                                                    |
    	| Binomial(n,p)                   | np                    | np(1-p)                                                                                                                                                                   |
    	| Geometric(p)                    | 1/p                   | (1-p)/p^2                                                                                                                                                                 |
    	| Poisson(\lambda)                | \lambda               | \lambda                                                                                                                                                                   |
    	| Uniform(a,b)                    | (a+b)/2               | (b-a)^2/12                                                                                                                                                                |
    	| Normal(\mu,\sigma^2)            | \mu                   | \sigma^2                                                                                                                                                                  |
    	| Exponential(\beta)              | \beta                 | \beta^2                                                                                                                                                                   |
    	| Gamma(\alpha,\beta)             | \alpha\beta           | \alpha\beta^2                                                                                                                                                             |
    	| Beta(\alpha,\beta)              | \alpha/(\alpha+\beta) | \alpha\beta/((\alpha\beta)^2(\alpha+\beta+1))                                                                                                                             |
    	| t_\nu                           | 0 (if \nu>1)          | \nu/(\nu-2) (if \nu>2)                                                                                                                                                    |
    	| \chi_p^2                        | p                     | 2p                                                                                                                                                                        |
    	| Multinomial(n,p)                | np                    | \begin{pmatrix}np_1(1-p_1)&-np_1p_2&\cdots&-np_1p_k\\-np_2p_1&np_2(1-p_2)&\cdots&-np_2p_k\\\vdots&\vdots&\vdots&\vdots\\-np_kp_1&-np_kp_2&\cdots&np_k(1-p_k)\end{pmatrix} |
    	| Multivariate Normal(\mu,\Sigma) | \mu                   | \Sigma                                                                                                                                                                    |

    ## Conditional Expectation

    	- The conditional expectation of X given Y=y os

    		```undefined
    		\mathbb E(X|Y=y)=\begin{cases}\sum_x f_{X|Y}(x|y)dx&\text{discrrete case}\\\int_x f_{X|Y}(x|y)dx &\text{continuous case}\end{cases}
    		```

    		If r(x,y) is a function of x and y then

    		```undefined
    		\mathbb E(r(X,Y)|Y=y)=\begin{cases}\sum r(x,y) f_{X|Y}(x|y)dx&\text{discrrete case}\\\int r(x,y)f_{X|Y}(x|y)dx &\text{continuous case}\end{cases}
    		```

    	- The Rule of Iterated Expectations: For random variables X,$$Y$$, assuming the expectations exist, we have that

    		```undefined
    		\begin{aligned}\mathbb{E[E(}Y|X)]=\mathbb E(Y)&&\text{and}&&\mathbb{E[E}(X|Y)]=\mathbb E(X)\end{aligned}
    		```

    	- The conditional variance is defined as

    		```undefined
    		\mathbb V(Y|X=x)=\int(y-\mu(x))^2f(y|x)dy
    		```

    	- For random variables X and Y

    		```undefined
    		\mathbb V(Y)=\mathbb{EV}(Y|X)+\mathbb{VE}(Y|X)
    		```

    ## Moment Generating Functions

    	- The moment generating function, or Laplace transform of X is defined by

    		```undefined
    		\psi_X(t)=\mathbb E(e^{tX})=\int e^{tx}dF(x)
    		```

    	- Properties of MGF

    		- If Y=aX+b, then \psi_Y(t)=e^{bt}\psi_X(at)

    		- If X_1,…,X_n are independent and Y=\sum_i X_i then \psi_Y(t)=\prod_i\psi_i(t) where \psi_i is the MGF of X_i

    	- MGF for some common distribution

    		| Distribution        | MGF \psi(t)                                         |
    		|---------------------|-----------------------------------------------------|
    		| Bernoulli(p)        | pe^t+(1-p)                                          |
    		| Binomial(n,p)       | (pe^t+(1=p))^n                                      |
    		| Poisson(\lambda)    | e^{(\lambda e^t - 1)}                               |
    		| Normal(\mu,\sigma)  | \exp\left\{\mu t+\frac{\sigma^2+t^2}2 \right\}      |
    		| Gamma(\alpha,\beta) | \left(\frac1{1-\beta t}\right)^\alpha for t<1/\beta |

# Convergence, LLN, CLT

    ## Types of convergence

    	## Convergence in calculus

    	- 책에 나오지는 않지만, 알아두면 괜찮을 듯 하여 첨부

    		![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/0ac2665f-9ed9-4b4a-ad9b-55000ae2a79c/Screenshot_20230728_083828_Drive.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20231227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20231227T004354Z&X-Amz-Expires=3600&X-Amz-Signature=51a17815fe4028263d00c2d9932293ca58ab66064461d218204b9efbe0f8e8b8&X-Amz-SignedHeaders=host&x-id=GetObject)

    	### Converges in probability/distribution

    	- Let X_1,X_2,... be a sequence of random variables and let X be another random variable. Let F_n denote the CDF of X_n and F denote the CDF of X

    		- X_n **converges to X in probability**, written X_n \xrightarrow{P} X if for every \epsilon > 0,

    			```undefined
    			\mathbb P(|X_n - X| > \epsilon)\rightarrow 0
    			```

    		- X_n **converges to X in distribution**, written X_n \rightsquigarrow X, if

    			```undefined
    			\lim_{n\rightarrow\infty}F_n(t)=F(t)
    			```

    			at all t for which F is continuous

    	### Convergence in quadratic mean

    	- X_n **converges to X in quadratic mean**(also called convergence in L_2), written X_n \xrightarrow{qm}X, if \mathbb E(X_n-X)^2\rightarrow 0 as n \rightarrow \infty

    	- This convergence is stronger than probability convergence!

    	### Theorems

    	- The following relationships hold

    		- X_n \xrightarrow{qm}X implies that X_n \xrightarrow{p}X

    		- X_n \xrightarrow{p}X implies that X_n \rightsquigarrow X

    		- If X_n \rightsquigarrow X and \mathbb{P}(X=c)=1 for some real number c, then X_n \xrightarrow{p}X

    		- None of reverse implications hold except the special case in (c)

    		```mermaid
    		graph LR
    		  A(Quadratic Mean) --> B(probability)
    			B --> C(Distribution)
    			C -.point-mass distribution.-> B
    		```

    	- Let X_n, X, Y_n, Y be random variables and let g be a continuous function

    		- If X_n \xrightarrow{p}X and Y_n \xrightarrow{p}Y, then X_n+Y_n \xrightarrow{p}X+Y

    		- If X_n \xrightarrow{qm}X and Y_n \xrightarrow{qm}Y, then X_n+Y_n \xrightarrow{qm}X+Y

    		- If X_n \rightsquigarrow X and Y_n \rightsquigarrow c, then X_n+Y_n \rightsquigarrow X+c

    		- If X_n \xrightarrow{p}X and Y_n \xrightarrow{p}Y, then X_nY_n \xrightarrow{p}XY

    		- If X_n \rightsquigarrow X and Y_n \rightsquigarrow c, then X_nY_n \rightsquigarrow cX

    		- If X_n \xrightarrow{p}X, then g(X_n) \xrightarrow{p}g(X) 

    		- If X_n \rightsquigarrow X, then g(X_n) \rightsquigarrow g(X)

    	- 위에서 3, 5번의 경우, Random variable 2개에 대해서는 generally 성립하지 않음

    ## Law of Large Numbers

    	> 💡 The sample average \bar X_n = n^{-1}\sum_{i=1}^n X_i converges in probability to the expectation \mu=\mathbb E(X_i)

    	- (Weak Law) If X_1,...X_n are iid, then \overline X_n\xrightarrow P \mu

    	- As the sample size increases, sample mean will be more concentrated around the mean

    	- The distribution of \overline X_n becomes more concentrated around \mu as n gets large

    	- Proof: Chebyshev’s inequality!

    	- Example: In rolling dice,

    		![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/a03bd44b-965c-46d2-8593-d306fac8cf37/output.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20231227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20231227T004356Z&X-Amz-Expires=3600&X-Amz-Signature=8298ec065578f754fb7b492f075cffca9dd511b395cd1b0354c1c183b89b7851&X-Amz-SignedHeaders=host&x-id=GetObject)

    ## The Central Limit Theorem

    	> 💡 \sqrt n(\bar X_n-\mu) converges in distribution to a normal distribution

    	### The Central Limit Theorem

    	- Let X_1,…,X_n be iid with mean \mu and variance \sigma^2. Let \overline X_n = n^{-1}\sum_{i=1}^n X_i. Then

    		```undefined
    		Z_n \equiv \frac{\overline X_n -\mu}{\sqrt{\mathbb V(\overline X_n)}} = \frac {\sqrt n (\overline X_n-\mu)}{\sigma}\rightsquigarrow Z
    		```

    		where Z \sim (0,1). In other words,

    		```undefined
    		\lim_{n\rightarrow\infty}\mathbb P(Z_n\le Z)= \Phi(z) = \int_{-\infty}^z\frac1{\sqrt{2\pi}}e^{-x^2/2}dx
    		```

    	- Whatever distribution X comes from, sample mean asymptotically follows normal distribution! Notation is like Z_n \approx N(0,1)

    	- Probability statements about \overline X_n can be approximated using a Normal distribution. It’s the probability statements that we are approximating, not the random variable itself

    	![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/8dc9dde5-643f-40ce-abe7-736ad261f808/output2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20231227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20231227T004356Z&X-Amz-Expires=3600&X-Amz-Signature=b25b0f0918eb9b9638825d02d93aac9a1d08beb411fa98374fb37d46d7d9c769&X-Amz-SignedHeaders=host&x-id=GetObject)

    	- Theorem: Assume the same conditions with CLT, then

    		```undefined
    		\frac{\sqrt n (\overline X_n-\mu)}{S_n}\rightsquigarrow N(0,1)
    		```

    	- Example: Coin toss 100 times, can we get the distribution of # of head?

    		- X_i \sim \text{Bernoulli}(0.5), \mathbb{E}(X_i) =0.5, \mathbb{V}(X_i)=0.25

    		- CLT 이용시 \bar{X} \approx N(0.5, 0.25/100)

    	### Multivariate CLT

    	Let X_1,...X_n be iid random vectors and \mu=\begin{pmatrix}\mathbb E(X_{1i})\\\mathbb E(X_{2i})\\\vdots\\\mathbb E(X_{ki})\end{pmatrix} and variance \Sigma

    	Let \overline X with \overline X_j = n^{-1}\sum_{i=1}^n X_{ji}. Then \sqrt n (\overline X-\mu)\rightsquigarrow N(0, \Sigma) 

    	![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/726a0a10-f3d6-4669-9852-7fdbb27f430b/multivariate_central_limit_theorem.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20231227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20231227T004356Z&X-Amz-Expires=3600&X-Amz-Signature=9f5d7e6f8affd3e406e4213c9ce0cfca7f9c730becbe9b9b6c56548358f104e8&X-Amz-SignedHeaders=host&x-id=GetObject)

    ## Delta Method

    	- Suppose we know that Y_n asymptotically follows normal distribution. Then how about the distribution of g(Y_n)?

    	- Suppose that

    		```undefined
    		\frac{\sqrt n (Y_n-\mu)}{\sigma}\rightsquigarrow N(0,1)
    		```

    		and that g is differentiable function such that g'(\mu)\not= 0. Then

    		```undefined
    		\frac{\sqrt n (g(Y_n)-g(\mu))}{|g'(\mu)|\sigma}\rightsquigarrow N(0,1)
    		```

    	- In other words, Y_n \approx N\left(\mu, \frac{\sigma^2}n \right) implies that g(Y_n) \approx N\left(g(\mu), (g'(\mu))^2\frac{\sigma^2}n \right)

    	- 어떤 함수 g(X)의 기댓값이나 분산을 몰라도, random variable X를 사용한 근사를 통해 g(X)를 찾아가는 방법임

    	- Proof: Using Central Limit Theorem + taylor’s theorem(to find expectation and variance)

    		```undefined
    		\mathbb E(g(X)) \approx g(\mu_x)+g'(\mu_x)\mathbb E(X-\mu_x)+\frac{g''(\mu_x)}{2}\mathbb E(X-\mu_x)^2 = g(\mu_x)+\frac{g''(\mu_x)}{2}\sigma_x^2 \\\text{Var}(g(X))\approx \text{Var}(g(\mu_x)+g'(\mu_x)(X-\mu_x)) = \{g'(\mu_x)\}^2\sigma_x^2
    		```

# Statistical Inference, Bias, MSE

    ## Parametric and Nonparametric Models

    	- A statistical model \frak F is a set of distributions

    	- A parametric model is a set \frak F that can be paramerized by a finite number of parameters.

    	- In general, parametric model takes the form

    		```undefined
    		\mathfrak F=\{f(x;\theta):\theta\in\Theta\}
    		```

    ## Fundamental Concepts in Inference

    	### Point Estimation

    		- Point estimation refers to providing a single “best guess” of some quantity of interest.

    		- A point estimator \hat\theta_n on a parameter \theta is some function of X_1,…X_n

    			```undefined
    			\hat\theta_n=g(X_1,...,X_n)
    			```

    		- The bias of an estimator is defined by

    			```undefined
    			\text{bias}(\hat\theta_n)=\mathbb E_\theta(\hat\theta_n)-\theta
    			```

    		- We say that \hat\theta_n is unbiased if \mathbb E(\hat\theta_n)=\theta

    		- A point estimator \hat\theta_n of a parameter \theta is consistent if \hat\theta_n\xrightarrow{P}\theta

    		- The standard deviation of \hat\theta_n is called the standard error, denoted by se:

    			```undefined
    			\text{se}=\text{se}(\hat\theta_n)=\sqrt{\mathbb V(\hat\theta_n)}
    			```

    		- The MSE can be written as

    			```undefined
    			\text{MSE}=\text{bias}^2(\hat\theta_n)+\mathbb V_\theta(\hat\theta_n)
    			```

    		- An estimator is asymptotically Normal if

    			```undefined
    			\frac{\hat\theta_n-\theta}{\text{se}}\rightsquigarrow N(0,1)
    			```

    	### Confidence Sets

    		- A 1-\alpha confidence interval for parameter \theta si an interval C_n=(a,b) where a,b are functions of data such that

    			```undefined
    			\mathbb P_\theta(\theta\in C_n)\ge 1-\alpha,\forall \theta\in\Theta
    			```

    	### Hypothesis Testing

    		- Default Theory H_0: null hypothesis

    		- We ask if the data provides sufficient evidence to reject the theory

# Cumulative Distribution function and Bootstrap

    ## The Empirical Distribution Function

    	- The empirical distribution function \hat F_n is the CDF that puts mass 1/n at each point X_i. Formally

    		```undefined
    		\hat F_n(x) = \frac{\sum_{i=1}^n I(X_i\le x)}n
    		```

    	- At any fixed value of x,

    		```undefined
    		\begin{aligned}\mathbb E(\hat F_n(x))&=F(x)\\\mathbb V(\hat F_n(x))&=\frac{F(x)(1-F(x))}n\\\text{MSE}&=\frac{F(x)(1-F(x))}n\to 0\\\hat F_n(x)&\xrightarrow{P}F(x)\end{aligned}
    		```

    	- The Glivenko-Cantelli Theorem: Let X_1,…,X_n \sim F. Then

    		```undefined
    		\sup_x|\hat F_n(x)-F(x)|\xrightarrow{P}0
    		```

    	- The DKW inequality: Let X_1,…,X_n \sim F. Then, For any \epsilon > 0,

    		```undefined
    		\mathbb P\left(\sup_x|F(x)-\hat F_n(x)|>\epsilon \right)\le 2e^{-2n\epsilon^2}
    		```

    ## Statistical Functionals

    	- The plug-in estimator of \theta=T(F) is defined by

    		```undefined
    		\hat\theta_n = T(\hat F_n)
    		```

    	- If T(F)=\int r(x)dF(x) for some function r(x) then T is called linear functional

    	- The plug-in estimator for linear functional T(F)=\int r(x)dF(x) is

    		```undefined
    		T(\hat F_n)=\int r(x)d\hat F_n(x)=\frac 1n\sum_{i=1}^n r(X_i)
    		```

    ## Simulation

    	- Suppose we draw an iid sample Y_1,…,Y_B from a distribution G. By the law of large numbers, as B\to\infty

    		```undefined
    		\bar Y_n = \frac 1B\sum_{i=1}^nY_j\xrightarrow P\int ydG(y)=\mathbb E(Y)
    		```

    ## Bootstrap Variance Estimation

    	- Draw X_1^*,…,X_n^*\sim\hat F_n

    	- Compute T^*_n=g(X_1^*,…,X_N^*)

    	- Repeat steps 1 and 2 B times, to get T_{n,1}^*,…,T_{n,B}^*

    	- Let

    		```undefined
    		v_\text{boot}=\frac1B\sum_{b=1}^B\left(T_{n,b}^*-\frac1B\sum_{r=1}^B T_{n,r}^*\right)^2
    		```

    ## Bootstrap Confidence Intervals

    	- Normal interval

    		```undefined
    		T_n\pm z_{\alpha/2}\hat{\text{se}}_\text{boot}
    		```

    	- Pivotal interval

    		- Let \theta=T(F) and \hat\theta_n=T(\hat F_n) and define the pivot R_n=\hat\theta_n-\theta. Let \hat\theta_{n,1}^*,...\hat\theta_{n,B}^* denote bootstrap replication of \hat\theta_n.

    			```undefined
    			H(r)=\mathbb P_F(R_n\le r)
    			```

    		- Define C^*_n=(a,b) where a=\hat\theta_n-H^{-1}(1-\frac\alpha2), b=\hat\theta_n-H^{-1}(\frac\alpha2)

    		- In summary, the 1-\alpha bootstrap pivotal confidence interval is

    			```undefined
    			C_n = (2\hat\theta_n-\hat\theta^*_{1-\alpha/2},2\hat\theta_n-\hat\theta^*_{\alpha/2})
    			```

    	- Percentile intervals

    		- The bootstrap percentile interval is defined by

    			```undefined
    			C_n = (\theta^*_{\alpha/2},\theta^*_{1-\alpha/2})
    			```

# Parametric Inference, Likelihood, MLE

    ## Parameter of Interest

    	- If our goal is to estimate \mu then \mu=T(\theta) is called the parameter interest and \sigma is a nuisance parameter.

    ## The Method of Moments

    	- We define j^{th} moment

    		```undefined
    		\alpha_j\equiv\alpha_j(\theta)=\mathbb E_\theta(X^j)=\int x^jdF_\theta(x)
    		```

    	- We define j^{th} sample moment

    		```undefined
    		\hat\alpha_j=\frac 1n\sum_{i=1}^nX_i^j
    		```

    	- The method of moments estimator \hat\theta_n is defined to be the value of \theta such that \alpha_k(\hat\theta_n)=\hat\alpha_k

    ## Maximum Likelihood

    	- The likelihood function is defined by

    		```undefined
    		\mathcal L_n(\theta)=\prod_{i=1}^nf(X_i;\theta)
    		```

    	- The maximum likelihood estimator MLE, denoted by \hat\theta_n is the value of \theta that maximizes \cal L_n(\theta)

    ## Properties of MLE

    	- The MLE is consistent: \hat\theta_n\xrightarrow P \theta_*

    	- The MLE is equivalent: if \hat\theta_n is MLE of \theta then g(\hat\theta_n) is the MLE of g(\theta)

    	- The MLE is asymptotically Normal: (\hat\theta-\theta_*)/\hat{\text{se}}\rightsquigarrow N(0,1)

    	- THE MLE is asymptotically optimal or efficient

    	- The MLE is approximately the Bayes estimator

    ## Consistency of MLE

    	- Let \theta_* denote the true value of \theta. Define

    		```undefined
    		M_n(\theta)=\frac 1n\sum_i \log\frac{f(X_i;\theta)}{f(X_i;\theta_*)}
    		```

    		and M(\theta)=-D(\theta_*,\theta). Suppose that

    		```undefined
    		\sup_{\theta\in\Theta}|M_n(\theta)-M(\theta)|\xrightarrow P 0
    		```

    		and that, for every \epsilon > 0,

    		```undefined
    		\sup_{\theta:|\theta-\theta_*|\ge\epsilon}M(\theta)<M(\theta_*)
    		```

    ## Equivalence of MLE

    	- Let \tau=g(\theta) be a function of \theta, Let \hat\theta_n be the MLE of \theta. Then \hat\tau_n=g(\hat\theta_n) is the MLE of \tau

    ## Asymptotic normality

    	- The score function is defined to be

    		```undefined
    		s(X;\theta)=\frac{\partial\log f(X;\theta)}{\partial\theta}
    		```

    	- The fisher information is defined to be

    		```undefined
    		\begin{aligned}I_n(\theta)&=\mathbb V_\theta\left(\sum_{i=1}^n s(X_i;\theta)\right)\\&=-\mathbb E_\theta\left(\frac{\partial^2\log f(X;\theta)}{\partial \theta^2}\right)\end{aligned}
    		```

    	- Let se=\sqrt{\mathbb V(\hat\theta_n)}. Under appropriate regularity conditions, the following hold:

    		- \text{se}\approx\sqrt{1/I_n(\theta)} and

    			```undefined
    			\frac{(\hat\theta_n-\theta)}{\text{se}}\rightsquigarrow N(0,1)
    			```

    		- Let \hat{\text{se}}=\sqrt{1/I_n(\hat\theta_n)}. Then,

    			```undefined
    			\frac{(\hat\theta_n-\theta)}{\hat{\text{se}}}\rightsquigarrow N(0,1)
    			```

    	- Let C_n=\theta_n\pm z_{\alpha/2}\hat{\text{se}}, then \mathbb P_\theta(\theta\in C_n)\to 1-\alpha as n\to\infty

    ## Optimality

    	- Suppose that X_1,…,X_n \sim N(\theta,\sigma^2). The MLE is \theta_n=\bar X_n. Another reasonable estimator of \theta is the sample median \widetilde\theta_n. The MLE satisfies

    		```undefined
    		\sqrt n(\hat\theta_n-\theta)\rightsquigarrow N(0,\sigma^2)
    		```

    ## The Delta Method

    	- If \tau=g(\theta) where g is differentiable and g'(\theta)\neq 0 then

    		```undefined
    		\frac{(\hat\tau_n-\tau)}{\hat{\text{se}}(\hat\tau)}\rightsquigarrow N(0,1)
    		```

    		where \hat\tau_n=g(\hat\theta_n) and

    		```undefined
    		\hat{\text{se}}(\hat\tau_n)=|g'(\hat\theta)|\hat{\text{se}}(\hat\theta_n)
    		```

    ## Multiparameter models

    	- Let \mathscr l_n=\sum_{i=1}^n\log f(X_i;\theta),

    		```undefined
    		H_{jj}=\frac{\partial^2 l_n}{\partial\theta^2_j}\ \text{ and }\ H_{jk}=\frac{\partial^2l_n}{\partial\theta_j\partial\theta_k}
    		```

    	- Define the Fisher Information matrix by

    		```undefined
    		I_n(\theta)=-\begin{bmatrix}\mathbb E_\theta(H_{11})&\mathbb E_\theta(H_{12})&\cdots&\mathbb E_\theta(H_{1k})\\\mathbb E_\theta(H_{21})&\mathbb E_\theta(H_{22})&\cdots&\mathbb E_\theta(H_{2k})\\\vdots&\vdots&\vdots&\vdots\\\mathbb E_\theta(H_{k1})&\mathbb E_\theta(H_{k2})&\cdots&\mathbb E_\theta(H_{kk})\end{bmatrix}
    		```

    	- Multiparameter delta method: Suppose that \nabla g evaluated at \hat\theta is not 0. Let \hat\tau=g(\hat\theta). Then

    		```undefined
    		\frac{(\hat\tau-\tau)}{\hat{\text{se}}(\hat\tau)}\rightsquigarrow N(0,1)
    		```

    		where

    		```undefined
    		\hat{\text{se}}(\hat\tau)=\sqrt{(\hat\nabla g)^\top\hat J_n(\hat\nabla g)}
    		```

    ## The Parametric BootStrap

    	- The estimated standard error of bootstrap is

    		```undefined
    		\hat{\text{se}}_{\text{boot}}=\sqrt{\frac{\sum_{b=1}^B(\hat\tau_b^*-\hat\tau)^2}B}
    		```

    ## Checking Assumptions

    	- A formal way to test a parametric model is to use goodness-of-fit test

# Hypothesis test, P-value, multiple test correction

    - The power function of test with rejection region R is defined by

    	```undefined
    	\beta(\theta)=\mathbb P_\theta(X\in R)
    	```

    	The size of a test is defined to be

    	```undefined
    	\alpha=\sup_{\theta\in\Theta_0}\beta(\theta)
    	```

    ## The Wald Test

    	- Consider testing

    		```undefined
    		\begin{aligned}H_0:\theta=\theta_0&&\text{versus}&&H_1:\theta\neq\theta_0\end{aligned}
    		```

    		Assume that \hat\theta is asymptotically Normal, and the size \alpha Wald test is, reject H_0 when |W|>z_{\alpha/2} where

    		```undefined
    		W=\frac{\hat\theta-\theta_0}{\hat{\text{se}}}
    		```

    	- Asymptotically, the Wald test has size \alpha, that is with n\to\infty

    		```undefined
    		\mathbb P_{\theta_0}(|W|>z_{\alpha/2})\to\alpha
    		```

    	- The size \alpha Wald test rejects H_0:\theta=\theta_0 versus H_1:\theta\neq\theta_0 if and only if \theta_0\not\in C where

    		```undefined
    		C=\hat\theta\pm\hat{\text{se}}z_{\alpha/2}
    		```

    ## p-values

    	- Suppose that for every \alpha\in(0,1) we have a size \alpha test with rejection region R_\alpha. Then,

    		```undefined
    		\text{p-value}=\inf\{\alpha:T(X^n)\in R_\alpha\}
    		```

    		That is, the p-value is the smallest level at which we can reject H_0

    	- p-value is not the probability that the null hypothesis is true

    	- Let w=(\hat\theta-\theta_0)/\hat{\text{se}} denote the observed value of the wald statistics W. The p-value is given by

    		```undefined
    		\text{p-value}=\mathbb P_{\theta_0}(|W|>|w|)\approx \mathbb P(|Z|>|w|)=2\Phi(-|w|)
    		```

    		where Z\sim N(0,1)

    	- If the test statistic has a continuous distribution, then under H_0:\theta=\theta_0, the p-value has Uniform(0,1) distribution. Therefore, if we reject H_0 when the p value is less than \alpha, the probability of a type I error is \alpha

    ## The \chi^2 Distribution

    	- Let Z_1,…,Z_k be independent, standard Normals. Let V=\sum_{i=1}^k Z_i^2. Then we say that V has a \chi^2 distribution with k degrees of freedom.

    	- It can be shown that \mathbb E(V)=k and \mathbb V(V)=2k

    ## Pearson’s \chi^2 test for multinomial data

    	- Pearson’s \chi^2 statistic is

    		```undefined
    		T = \sum_{j=1}^k\frac{(X_j-n{p_{0}}_j)^2}{n{p_0}_j}=\sum_{j=1}^k\frac{(X_j-E_j)^2}{E_j}
    		```

    		where E_j=\mathbb E(X_j)=n{p_0}_j is the expected value of X_j under H_0

    	- Under H_0, T\rightsquigarrow \chi^2_{k-1}, Hence the test: reject H_0 if T>\chi^2_{k-1,\alpha} has asymptotic level \alpha. The p-value is \mathbb P(\chi^2_{k-1}>t) where t si the observed value of the test statistic 

    ## The Permutation Test

    	- Suppose that X_1,…,X_m \sim F_X, Y_1,…,Y_n \sim F_Y

    	- H_0:F_X=F_Y

    	- H_1:F_X\neq F_Y

    	- Algorithm for permutation test

    		- Compute the observed value of the test statistic

    			```undefined
    			t_{obs}=T(X_1,...,X_m,Y_1,...,Y_n)
    			```

    		- Randomly permute the data. Compute the statistic again using the permuted data.

    		- Repeat the previous step B times and let T_1,…,T_B denote the resulting values

    		- The approximate p-value is

    			```undefined
    			\frac 1B\sum_{j=1}^B I(T_j>t_{obs})
    			```

    ## The Likelihood Ratio Test

    	- Consider testing

    		```undefined
    		\begin{aligned}H_0:\theta\in\Theta_0&&\text{versus}&&H_1:\theta\not\in\Theta_0\end{aligned}
    		```

    		The likelihood ratio statistic is

    		```undefined
    		\lambda = 2\log\left(\frac{\sup_{\theta\in\Theta}\mathcal L(\theta)}{\sup_{\theta\in\Theta_0}\mathcal L(\theta)}\right)=2\log\left(\frac{\mathcal L(\hat\theta)}{\mathcal L(\hat\theta_0)}\right)
    		```

    		where \hat\theta is MLE and \hat\theta_0 is the MLE when \theta is restricted to lie in \Theta_0

    ## Multiple Testing

    	- The Bonferroni Method

    		- Given p-values P_1,…,P_m, reject null hypothesis H_{0i} if

    			```undefined
    			P_i<\frac\alpha m
    			```

    	- The Benjamini-Hochberg Method

    		- Let P_{(1})<\cdots<P_{(m)} denote the ordered p-values.

    		- Define

    			```undefined
    			\begin{aligned}l_i=\frac{i\alpha}{C_mm},&&\text{and}&&R=\max\{i:P_{(i)}<l_i\}\end{aligned}
    			```

    			where C_m is defined to be 1 if p-values are independent and C_m=\sum_{i=1}^m(1/i) otherwise

    		- Let T=P_{(R)} and call it BH rejection threshold

    		- Reject all null hypothesis H_{0i} for which P_i\le T

    ## Goodness-of-fit Tests

    	- Let H_0 be the null hypothesis that the data are iid draws from the model \mathfrak F=\{f(x,\theta):\theta\in\Theta\}. Under H_0, the statistic Q converges in distribution to a \chi^2_{k-1-s} random variable. Thus, the p-value for the test is \mathbb P(\chi^2_{k-1-s}>q) where q denotes the observed value of Q

# Bayesian inference

    ## The Bayesian Method

    	- We choose a probability density f(\theta) - called the prior distribution - that express our beliefs about a parameter \theta before we see any data

    	- We choose a statistical model f(x|\theta) that reflects our beliefs about x given \theta Notice that we now write this as f(x|\theta) instead of f(x;\theta)

    	- After observing data X_1,…,X_n, we update our beliefs and calculate the posterior distribution f(\theta|X_1,…,X_n)

    	- Posterior is proportional to likelihood times prior

    		```undefined
    		f(\theta|x^n)\propto\mathcal L(\theta)f(\theta)
    		```

    	- The posterior mean is

    		```undefined
    		\bar\theta_n=\int \theta f(\theta|x^n)d\theta=\frac{\int\theta\mathcal L_n(\theta)f(\theta)}{\int\mathcal L_n(\theta)f(\theta)d\theta}
    		```

    ## Functions of Parameters

    	- The posterior CDF for \tau is

    		```undefined
    		H(\tau|x^n)=\mathbb P(g(\theta)\le r|x^n)=\int_A f(\theta|x^n)d\theta
    		```

    ## Simulation

    	- Suppose we draw \theta_1,…,\theta_B \sim  p(\theta|x^n). Then a histogram of \theta_1,…\theta_B approximates the posterior density p(\theta|x^n)

    ## Large Sample Properties of Bayes’ Procedures

    	- Let \hat\theta_n be the MLE and let \hat{se}=1/\sqrt{nI(\hat\theta_n)}. Under appropriate regularity conditions, the posterior is approximately normal with mean \hat\theta_n and standard deviation \hat{se}. Hence, \bar\theta_n\approx\widetilde\theta_n.

    ## Flat Priors, Improper Priors and Noninformative Priors

    	- Subjectivism says that the prior should reflect our subjective opinion about \theta.

    	- An obvious candidate for a noninformative prior is to use a flat prior f(\theta)\propto \text{constant}.

    ## Multiparameter Problems

    	- Suppose that \theta=(\theta_1,…,\theta_p). The posterior density is still given by

    		```undefined
    		f(\theta|x^n)\propto\mathcal L_n(\theta)f(\theta)
    		```

    	- The marginal posterior for \theta_1 is

    		```undefined
    		f(\theta_1|x^n)=\int\cdots\int f(\theta_1,...,\theta_p|x^n)d\theta_2...d\theta_p
    		```

    ## Bayesian Testing

    	- The bayesian approach to testing involves putting a prior on H_0 and on the parameter \theta and then computing \mathbb P(H_0|X^n)

# Inequalities(Extra)

    ## 4.1 Probability Inequality

    	### Markov’s Inequality

    	- Let X be a non-negative random variable and suppose that \mathbb{E}(X) exists. For any t > 0,

    		```undefined
    		\mathbb{P}(X>t)\le \frac{\mathbb{E}(X)}{t}
    		```

    	- Proof: By definition of \mathbb{E}(X)

    		```undefined
    		\begin{align}\mathbb{E}(X) &\ge \int_t^\infty xf(x)dx \\ &\ge t \int_t^\infty f(x)dx = t\mathbb{P}(X>t)\end{align}
    		```

    	- 여기서 1 → 2로 가는 이유는 [t, \infty]의 범위에 있는 모든 x가 t보다 크거나 같기 때문

    	### Chebyshev’s Inequality

    	- Let \mu = \mathbb{E}(X) and \sigma^2 = \mathbb{V}(X). Then

    		```undefined
    		\mathbb{P}(|X-\mu|\ge t)\le\frac{\sigma^2}{t^2}\text{ and } \mathbb P(|Z|\ge k) ≤ \frac 1 {k^2}
    		```

    		where Z = (X-\mu)/\sigma

    	- Proof: 양 변에 제곱을 해도 확률은 변화가 없음(절댓값이니까 마이너스 쪽이 들어오지도 않을거고)을 이용함

    	### Hoeffding’s Inequality

    	- Let Y_1, ..., Y_n be independent observations such that \mathbb{E}(Y_i) = 0 and a_i≤Y_i≤b_i. Let \epsilon<0. Then for any t > 0,

    		```undefined
    		\mathbb{P}\left(\sum_{i=1}^n Y_i\ge \epsilon \right)\le e^{-t\epsilon}\prod_{i=1}^n e^{t^2(b_i-a_i)^2/8}
    		```

    	- Another Version: Let X_1, ...,X_n be independent random variables such that a_i≤X_i≤b_i, and let S_n = X_1 + ...+X_n, then for all t > 0,

    		```undefined
    		\mathbb P(|S_n - \mathbb E(S_n)|≥t)≤2\exp\left(-\frac{2n^2\epsilon^2}{\sum_{i=1}^n(b_i-a_i)^2}\right)
    		```

    	- Proof: 복잡하고, 안 나올 거 같아서 생략 (RL에서 많이 나오는 부등식임에도 불구하고, 증명을 안 하고 그냥 이런 게 있다 수준으로 넘어갔기 때문에 논자시 단계에서는 당연히 증명은 안 나올것)

    	### Theorem 4.5(Bernstein’s inequality)

    	- Let X_1, ..., X_n \sim \text{Bernoulli}(p). Then for any \epsilon>0,

    		```undefined
    		\mathbb P (|\overline X_n - p|>\epsilon) \le 2e^{-2n\epsilon^2}
    		```

    		where \overline X_n = n^{-1}\sum_{i=1}^nX_i

    	- Proof: apply Bernoulli in hoeffding’s inequality

    	### Mill’s inequality

    	- Let Z \sim (0,1). Then,

    		```undefined
    		\mathbb{P}(|Z|>t) \le \sqrt{\frac{2}{\pi}}\frac{e^{-t^2/2}}{t}
    		```

    	- Proof: use chernoff’s bound. 근데 얘도 교재 밖의 범위임. 대충 moment generate function 가지고 푸는 느낌…

    ## 4.2 Inequalities for Expectations

    	### Cauchy-Schwartz inequality

    	- If X and Y have finite variances then

    		```undefined
    		\mathbb E|XY| \le\sqrt{\mathbb E(X^2)\mathbb E(Y^2)}
    		```

    	- 고등학교 수학 과정에서 나왔던 내용

    	### Jensen’s inequality

    	- If g is convex, then \mathbb Eg(X)\le g(\mathbb EX)

    	- If g is concave, then \mathbb Eg(X)\ge g(\mathbb EX)

    		- A function g is convex if for each x, y and each \alpha \in[0,1]

    			```undefined
    			g(\alpha x+(1-\alpha)y)\le\alpha g(x)+(1-\alpha)g(y)
    			```

    		- Convex Graph Example

    			![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/df3ddadd-6fd6-4b28-8d2a-f400cbd45605/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20231227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20231227T004439Z&X-Amz-Expires=3600&X-Amz-Signature=a14da14a99f2568662eca43f53be2cf4b971bffad85eea23aef79ee005a12e04&X-Amz-SignedHeaders=host&x-id=GetObject)
