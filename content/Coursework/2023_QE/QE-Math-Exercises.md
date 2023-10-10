---
id: 5841078d-8328-4c56-88eb-2271eb5f5b65
title: QE Math Exercises
created_time: 2023-07-09T14:54:00.000Z
last_edited_time: 2023-09-16T07:30:00.000Z
하위 항목: []
subclass: 2023_QE
class: Coursework
작성일시: 2023-07-09T14:54:00.000Z
pdf: https://mml-book.github.io/book/mml-book.pdf
상위 항목: []

---

# Week 2

    ## Question 3.1

    	- Show that  \langle \cdot,\cdot\rangle defined for all x = \begin{bmatrix}x_1,x_2\end{bmatrix}^\top\in\R^2 and y = \begin{bmatrix}y_1,y_2\end{bmatrix}^\top\in\R^2 by

    		```undefined
    		\langle x,y\rangle := x_1y_1 - (x_1y_2+x_2y_1)+2(x_2y_2)
    		```

    		is inner product

    	- Solution

    		- Symmetric: \langle y,x\rangle = y_1x_1-(y_1x_2+x_1y_2)+2(y_2x_2) = \langle x,y\rangle

    		- Positive Definite: \langle x,x\rangle = x_1^2 - 2x_1x_2 + 2x_2^2 = (x_1-x_2)^2+x_2^2 \ge0

    		- Linear: \langle x, ay \rangle = ay_1x_1 - ay_1x_2 - ax_1y_2 + 2ay_1x_2 = a \langle x,y \rangle

    ## Question 3.2

    	- Consider \R^2 with \langle \cdot,\cdot\rangle defined for all x and y  in \R^2 as

    		```undefined
    		\langle x, y\rangle:= x^\top\underbrace{ \begin{bmatrix} 2&0\\1&2\end{bmatrix}}_{:=A}y
    		```

    		Is \langle \cdot,\cdot\rangle an inner product?

    	- Solution: A should be symmetric, and positife definite. However A is not symmetric → not inner product!

    ## Question 3.3

    	- Compute the distance between

    		```undefined
    		x=\begin{bmatrix}1\\2\\3\end{bmatrix}, y = \begin{bmatrix}-1\\-1\\0\end{bmatrix}
    		```

    		using

    		- \langle x, y\rangle:=x^\top y

    			- Solution: distance = \sqrt{\langle x-y, x-y\rangle} 인데 dot product이니까,

    				```undefined
    				x-y = \begin{bmatrix}2\\3\\3\end{bmatrix}
    				```

    				이걸 적용하면, 2^2+3^2+3^2 = 13

    		- \langle x, y\rangle:=x^\top A y, A:=\begin{bmatrix}2&1&0\\1&3&1\\0&-1&2 \end{bmatrix}

    			- Solution: 위에서 구한 x-y에다가 A를 양 옆에 곱해줌

    				```undefined
    				\begin{bmatrix}2&3&3\end{bmatrix}\begin{bmatrix}2&1&0\\1&3&1\\0&-1&2\end{bmatrix}\begin{bmatrix}2\\3\\3\end{bmatrix}
    				```

    				계산하면, \begin{bmatrix}7&8&9\end{bmatrix}\begin{bmatrix}2\\3\\3\end{bmatrix} = 14 + 24 + 27 = 65

    ## Question 3.5

    	- Consider the euclidean vector space \R^5 with dot product. A subspace U \subseteq \R^5 and x \in \R^5 are given by

    		```undefined
    		U = span[\begin{bmatrix}0\\-1\\2\\0\\2\end{bmatrix},\begin{bmatrix}1 \\-3\\1\\-1\\2\end{bmatrix},\begin{bmatrix}-3\\4\\1\\2\\1\end{bmatrix},\begin{bmatrix}-1\\-3\\5\\0\\7\end{bmatrix}], x=\begin{bmatrix}-1\\-9\\-1\\4\\1\end{bmatrix}
    		```

    		- Determine the orthogonal projection \pi_U(x) of x onto U

    			- By definition, \sum_{i=1}^4 \frac{v_i\cdot x}{v_i\cdot v_i} v_i

    		- Determine the distance d(x,U)

    			- By definition, \sqrt{(x-\pi_U(x))\cdot(x-\pi_U(x))}

    		```python
    		import numpy as np
    		
    		v1 = np.array([0, -1, 2, 0, 2])
    		v2 = np.array([1, -3, 1, -1, 2])
    		v3 = np.array([-3, 4, 1, 2, 1])
    		v4 = np.array([-1, -3, 5, 0, 7])
    		x = np.array([-1, -9, -1, 4, 1])
    		
    		U = [v1, v2, v3, v4]
    		
    		proj_x_U = np.zeros(5)
    		for v in U:
    		    proj_x_U += np.dot(v, x) / np.dot(v, v) * v #question a
    		
    		dist_x_U = np.linalg.norm(x - proj_x_U) #question b
    		```

    ## Question 3.6

    	- Consider \R^3 with the inner product

    		```undefined
    		\langle x,y\rangle:=x^\top \begin{bmatrix}2&1&0\\1&2&-1\\0&-1&2\end{bmatrix}y
    		```

    		Furthermore, we define e_1,e_2,e_3 as the standard basis in \R^3

    		- Determine the orthogonal projection \pi_U(e_2) of e_2 onto

    			```undefined
    			U = span[e_1,e_3]
    			```

    			- Solution: \sum_{i=1}^2 \frac{\langle v_i\,x\rangle}{\langle v_i, v_i\rangle} v_i = \frac{\langle e_1, e_2\rangle}{\langle e_1, e_1 \rangle}e_1 + \frac{\langle e_3, e_2\rangle}{\langle e_3, e_3 \rangle}e_3

    			- \langle e_1, e_1\rangle = 2, \langle e_3, e_3\rangle = 2, \langle e_1, e_2\rangle =1, \langle e_3, e_2 \rangle = -1

    			- \pi_U(e_2) = \frac1 2e_1-\frac 1 2e_3

    		- Compute the distance d(e_2, U)

    			- e_2 - \pi_U(e_2) = e_2 - (\frac{1}{2}e_1 - \frac{1}{2}e_3)의 norm을 구해야 함

    			- 1/4 * 2 + 1 * 2 + 1/4 * 2 - 1/2 - 1 - 1/2 = 1

    			- distance = \sqrt{1} = 1

    ## Question 3.10

    	- Rotate the vectors x_1, x_2 by 30 \degree

    		```undefined
    		x_1 := \begin{bmatrix} 2\\3\end{bmatrix},\ x_2 := \begin{bmatrix} 0\\-1\end{bmatrix}
    		```

    	- Solution: \cos 30\degree = \frac{\sqrt{3}}{2}, \sin 30\degree = \frac 1 2, R(\theta) = \begin{bmatrix} \frac{\sqrt{3}}{2} & -\frac 1 2 \\ \frac 1 2 &\frac{\sqrt{3}}{2}\end{bmatrix}

    	- \begin{bmatrix}\sqrt{3} - 3/2 \\ 1-3\sqrt3/2 \end{bmatrix}

    	- \begin{bmatrix}1/2 \\ -\sqrt3/2 \end{bmatrix}

# Week 3

    ## Question 4.1

    	- Compute the determinant using the Laplace expansion(using the first row) and the Sarrus rule for

    		```undefined
    		A = \begin{bmatrix} 1&3&5\\2&4&6\\0&2&4 \end{bmatrix}
    		```

    	- Solution for laplace expansion

    		```undefined
    		\det(A) = (-1)^{1+1}\cdot1\begin{vmatrix}4&6\\2&4\end{vmatrix} + (-1)^{1+2}\cdot3\begin{vmatrix}2&6\\0&4\end{vmatrix} + (-1)^{1+3}\cdot 5\begin{vmatrix}2&4\\0&2\end{vmatrix} = 16-12 + -3\times(8)+5\times 4 = 0
    		```

    	- Solution for Sarrus’ rule

    		```undefined
    		1 \times 4 \times 4 + 3\times 6\times0+5\times2\times2 - 5\times4\times0-3\times2\times4-1\times6\times2 = 16 + 20 - 24 - 12 = 0
    		```

    ## Question 4.2

    	- Compute the following determinant efficiently

    		```undefined
    		\begin{bmatrix} 2&0&1&2&0\\2&-1&0&1&1\\0&1&2&1&2\\-2&0&2&-1&2\\2&0&0&1&1 \end{bmatrix}
    		```

    	- Solution: LU decomposition

    		```undefined
    		\begin{bmatrix} 2&0&1&2&0\\0&-1&-1&-1&1\\0&1&2&1&2\\0&0&3&1&2\\0&0&-1&-1&1 \end{bmatrix}
    		```

    		```undefined
    		\begin{bmatrix} 2&0&1&2&0\\0&-1&-1&-1&1\\0&0&1&0&3\\0&0&3&1&2\\0&0&-1&-1&1 \end{bmatrix}
    		```

    		```undefined
    		\begin{bmatrix} 2&0&1&2&0\\0&-1&-1&-1&1\\0&0&1&0&3\\0&0&0&1&-7\\0&0&0&-1&4 \end{bmatrix}
    		```

    		```undefined
    		\begin{bmatrix} 2&0&1&2&0\\0&-1&-1&-1&1\\0&0&1&0&3\\0&0&0&1&-3\\0&0&0&0&-3 \end{bmatrix}
    		```

    	- \det(A) = 2 \times -1 \times 1 \times 1 \times -3 = 6

    	- [https://matrixcalc.org/ko/det.html#determinant-Gauss({{2,0,1,2,0},{2,-1,0,1,1},{0,1,2,1,2},{-2,0,2,-1,2},{2,0,0,1,1}})](https://matrixcalc.org/ko/det.html#determinant-Gauss%28%7B%7B2,0,1,2,0%7D,%7B2,-1,0,1,1%7D,%7B0,1,2,1,2%7D,%7B-2,0,2,-1,2%7D,%7B2,0,0,1,1%7D%7D%29) 돌려본 거 첨부

    	![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d7063d19-cfca-4f2e-bf03-8612cc0c7418/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20231010%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20231010T004159Z&X-Amz-Expires=3600&X-Amz-Signature=17d85b87a4c0e88c6d812590f6d0a0f0ee70c26b4534d71d6884bfdc4a0c1707&X-Amz-SignedHeaders=host&x-id=GetObject)

    ## Question 4.3

    	- Compute the eigenspace of

    		- A:=\begin{bmatrix}1&0\\1&1 \end{bmatrix}

    			- \det(A-\lambda I) = (1-\lambda)(1-\lambda) - 0\cdot 1

    			- \lambda = 1

    			- \begin{bmatrix}0&0\\1&0 \end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix} = 0

    			- eigenspace = span([0, 1])

    		- B := \begin{bmatrix} -2 & 2 \\ 2 & 1\end{bmatrix}

    			- \det(A-\lambda I) = (-2-\lambda)(1-\lambda)-4 = -\lambda^2 +\lambda -6 = (-3-\lambda)(2-\lambda)

    			- \lambda = 2, -3

    				- For 2, \begin{bmatrix}-4&2\\2&-1 \end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix} = 0, eigenspace span([1, 2])

    				- For -3,\begin{bmatrix}1&2\\2&4 \end{bmatrix}\begin{bmatrix}x_1\\x_2\end{bmatrix} = 0, eigenspace span([-2, 1])

    ## Question 4.4

    	- Compute all eigenspaces of

    		```undefined
    		A = \begin{bmatrix} 0&-1&1&1\\-1&1&-2&3\\2&-1&0&0\\1&-1&1&0 \end{bmatrix}
    		```

    	- [https://www.wolframalpha.com/input?i2d=true&i={{0%2C-1%2C1%2C1}%2C{-1%2C1%2C-2%2C3}%2C{2%2C-1%2C0%2C0}%2C{1%2C-1%2C1%2C0}}](https://www.wolframalpha.com/input?i2d=true&i=%7B%7B0%2C-1%2C1%2C1%7D%2C%7B-1%2C1%2C-2%2C3%7D%2C%7B2%2C-1%2C0%2C0%7D%2C%7B1%2C-1%2C1%2C0%7D%7D)

    	- Eigenvalues 2, -1, 1

    	- \lambda = 2

    	- \lambda = -1

    	- \lambda = 1

# Week 4

    ## Problem 4.5

    	- Diagonalizability of a matrix is unrelated to its invertibility. Determine for the following 4 matrices whether they are diagonalizable and/or invertible

    		```undefined
    		\begin{bmatrix}1&0\\0&1 \end{bmatrix},\begin{bmatrix}1&0\\0&0 \end{bmatrix},\begin{bmatrix}1&1\\0&1 \end{bmatrix},\begin{bmatrix}0&1\\0&0 \end{bmatrix},
    		```

    	- By theorem 4.21, A symmetric matrix can always be diagonalized, 당연히 invertible

    	- Matrix 자체가 이미 diagonal term에만 nonzero term을 가지고 있기 때문에, P를 I로 두면 D가 나옴, determinant가 1이므로 invertible

    	- eigenvalue (\lambda -1)^2 =0, \lambda = 1이니까 eigenvalue가 n개가 아니고 eigenvector도 마찬가지. 그렇기 때문에 diagonalizable하지 않다. 하지만 determinant는 1로 invertible

    	- 2번과 마찬가지 이유로 diagonalizable하며 determinant가 -1로 invertible

    ## Problem 4.6

    	- Compute the eigenspaces of the following transformation matrices. Are they diagonalizable?

    		- For

    			```undefined
    			A = \begin{bmatrix}2&3&0\\1&4&3\\0&0&1\end{bmatrix}
    			```

    			- eigenvalues \lambda = 1, 5이고 얘네가 각각 하나씩의 eigenvector만 생성하므로 not diagonalizable

    				- \lambda = 1: \begin{bmatrix}1&3&0\\1&3&3\\0&0&0\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\begin{bmatrix}0\\0\\0\end{bmatrix}

    					- x_1 + 3x_2 = 0,x_1+3x_2+x_3=0, x_1=-3, x_2=1 ,x_3=0 

    					- \text{span}\left(\begin{bmatrix}-3\\1\\0\end{bmatrix}\right)

    				- \lambda=5: \begin{bmatrix}-3&3&0\\1&-1&3\\0&0&-4\end{bmatrix}\begin{bmatrix}x_1\\x_2\\x_3\end{bmatrix}=\begin{bmatrix}0\\0\\0\end{bmatrix}

    					- x_1-x_2=0, x_1-x_2+x_3=0,-4x_3=0

    					- \text{span}\left(\begin{bmatrix} 1\\1\\0\end{bmatrix} \right)

    		- For

    			```undefined
    			A = \begin{bmatrix}1&1&0&0\\0&0&0&0 \\0&0&0&0 \\0&0&0&0 \end{bmatrix}
    			```

    			- eigenvalues \lambda=0,1

    				- \lambda=0, there are 3 eigenvectors \begin{bmatrix}-1\\1\\0\\0\end{bmatrix}, \begin{bmatrix}0\\0\\1\\0\end{bmatrix}, \begin{bmatrix}0\\0\\0\\1\end{bmatrix}, eigenspace spans those three vectors

    				- \lambda = 1, there is 1 eigenvector \begin{bmatrix}1\\0\\0\\0\end{bmatrix}, eigenspace spans this.

    				- 4 eigenvectors, so diagonalizable

    ## Problem 4.7

    	- Are the following matrices diagonalizable? If yes, determine their diagonal form and a basis with respect to which the transformation matrices are diagonal. If no, give reasons why they are not diagonalizable

    		- A = \begin{bmatrix}0&1\\-8&4\end{bmatrix}

    			- -\lambda^2+4\lambda+8 = 0, \lambda=2\pm2i

    			- 2+2i case: eigenvector \begin{pmatrix} \frac{1-i}{4}\\1 \end{pmatrix}

    			- 2-2i case: eigenvector \begin{pmatrix} \frac{1+i}{4}\\1 \end{pmatrix}

    			- P = \begin{pmatrix}(1+i)/4&(1-i)/4\\1&1 \end{pmatrix}, P^{-1}=\begin{pmatrix}-2i &(1+i)/2\\2i&(1-i)/2 \end{pmatrix}

    			- D = \begin{pmatrix} 2-2i&0\\0&2+2i\end{pmatrix}

    		- A=\begin{bmatrix}1&1&1\\1&1&1\\1&1&1\end{bmatrix}

    			- Symmetric matrix라서 diagonalizable하다

    			- \det(A-\lambda I) = (1-\lambda)^3+1+1-3(1-\lambda) = -\lambda^3+3\lambda^2

    			- \lambda = 0: v_1 = \begin{pmatrix}-1\\1\\0 \end{pmatrix},v_2 = \begin{pmatrix}-1\\0\\1 \end{pmatrix}

    			- \lambda = 3: v_3 = \begin{pmatrix}1\\1\\1 \end{pmatrix}

    			- D = \begin{pmatrix}0&0&0\\0&0&0\\0&0&3 \end{pmatrix},P = \begin{pmatrix}-1&-1&1\\1&0&1\\0&1&1 \end{pmatrix}

    		- A=\begin{bmatrix}5&4&2&1\\0&1&-1&-1\\-1&-1&3&0\\1&1&-1&2\end{bmatrix}

    		- A=\begin{bmatrix}5&-6&-6\\-1&4&2\\3&-6&-4\end{bmatrix}

    ## Problem 4.8

    	- Find the SVD of the matrix

    		```undefined
    		A = \begin{bmatrix}3&2&2\\2&3&-2\end{bmatrix}
    		```

    	- AA^\top, A^\top A  계산 필요

    		```undefined
    		AA^\top = \begin{bmatrix}17&8\\8&17\end{bmatrix},A^\top A = \begin{bmatrix}13&12&2\\12&13&-2 \\2&-2&8\end{bmatrix} 
    		```

    	- Eigenvectors for matrix A^\top A

    		```undefined
    		v_1 = \begin{pmatrix}-2/3\\2/3\\1/3\end{pmatrix}, \lambda_1 = 0\\v_2 = \begin{pmatrix}\sqrt2/6\\-\sqrt2/6\\2\sqrt2/3\end{pmatrix}, \lambda_2 = 9\\v_3 = \begin{pmatrix}\sqrt2/2\\\sqrt2/2\\0\end{pmatrix}, \lambda_3 = 25\\
    		```

    	- \Sigma = \begin{pmatrix}5&0&0\\0&3&0\end{pmatrix}

    	- u_1 = \begin{pmatrix}\sqrt2/2\\\sqrt2/2\end{pmatrix}, u_2 = \begin{pmatrix}\sqrt2/2\\-\sqrt2/2\end{pmatrix}

    ## Problem 4.9

    	- Find the singular value decomposition of

    		```undefined
    		A = \begin{bmatrix}2&2\\-1&1\end{bmatrix}
    		```

    	- A^\top A = \begin{bmatrix}5&3\\3&5\end{bmatrix}, v_1 = \begin{bmatrix}\sqrt2/2\\\sqrt2/2\end{bmatrix}, \sigma_1 = 2\sqrt2,v_2 = \begin{bmatrix}-\sqrt2/2\\\sqrt2/2\end{bmatrix}, \sigma = \sqrt2,

    	- \Sigma = \begin{bmatrix}2\sqrt2&0\\0&\sqrt2\end{bmatrix}

    	- U = \begin{bmatrix}1&0\\0&1\end{bmatrix}

    ## Problem 4.11

    	- Show that for any A \in \R^{m\times n} the matrices A^\top A and A A^\top possess the same nonzero eigenvalues

    	- Let \lambda be a nonzero eigenvalue of A^\top A. Then there exists a nonzero vector x \in \mathbb{R}^n such that A^\top Ax = \lambda x

    	- Similarly, let \mu be a nonzero eigenvalue of A A^\top. Then there exists a nonzero vector y \in \mathbb{R}^m such that A A^\top y = \mu y

    	- (A^⊤Ax)^⊤=(Ax)^⊤A^⊤=x^⊤A^⊤A=x^⊤λx=λ∥x∥^2

    	- 또, y^\top AA^\top y = y^\top\mu y에 y^\top A A^\top y = (A^\top y)^\top (A^\top y) = |A^\top y|^2를 합치면, \|A^\top y\|^2 = \mu\|y\|^2

    	- 결국 위의 2개의 식이 같은 form을 가지게 되어, λ∥x∥^2=μ∥y∥^2라고 할 수 있고, 이 때 \lambda, \mu는 nonzero eigenvalue이기 때문에 \lambda = \mu

# Week 5

    ## Problem 5.1

    	- Compute the derivative f'(x) for f(x) = \log(x^4)\sin(x^3)

    		```undefined
    		\begin{aligned}\frac d {dx}f(x) &=\frac d {dx} \log(x^4)\sin(x^3)\\&=\log(x^4)\left(\frac d {dx}\sin(x^3)\right)+\sin(x^3)\left(\frac d {dx}\log(x^4)\right)\\&=\frac{4\sin(x^3)}{x}+3x^2\log(x^4)\cos(x^3)\end{aligned}
    		```

    ## Problem 5.2

    	- Compute the derivative f'(x) of the logistic sigmoid f(x) = \frac 1{1+\exp(-x)}

    	- Let u = 1+\exp(-x) then 

    		```undefined
    		\begin{aligned}\frac d {dx}\left(\frac1{u}\right) &=\frac d{du}\frac1u\frac{du}{dx}=-\frac1{u^2}\frac{du}{dx}\\&=-\frac{\frac d{dx}(1+\exp(-x))}{(1+\exp(-x))^2} &=\frac{\exp(-x)}{(1+\exp(-x))^2}\end{aligned}
    		```

    ## Problem 5.3

    	- Compute the derivative f'(x) of the function

    		```undefined
    		f(x) = \exp(-\frac 1{2\sigma^2}(x-\mu)^2)
    		```

    	- g'(u(x))\cdot u'(x) 이용, u(x) = -\frac{1}{2\sigma^2}(x-\mu)^2

    		```undefined
    		\begin{aligned}u'(x) &= \frac{d}{dx}\left(-\frac{1}{2\sigma^2}(x-\mu)^2\right) \\&= -\frac{1}{\sigma^2}(x-\mu) \cdot \frac{d}{dx}(x-\mu) \\&= -\frac{1}{\sigma^2}(x-\mu) \cdot 1 = -\frac{x-\mu}{\sigma^2}\end{aligned}
    		```

    	- g(u) = \exp(u), g'(u) = \frac{d}{du} \exp(u) = \exp(u)

    		```undefined
    		\begin{aligned}f'(x) &= g'(u(x)) \cdot u'(x) \\&=-\frac{x-\mu}{\sigma^2} \exp\left(-\frac{1}{2\sigma^2}(x-\mu)^2\right)\end{aligned}
    		```

    ## Problem 5.5

    	- Consider the following functions

    		```undefined
    		\begin{aligned}f_1(x)=\sin(x_1)\cos(x_2),&& x\in\R^2\\f_2(x,y)=x^\top y, &&x,y\in\R^n\\f_3(x)=xx^\top,&&x\in \R^n \end{aligned}
    		```

    		- What are the dimensions of \frac{\partial f_i}{\partial x}

    			- f_1: 1\times 2

    			- f_2: 1\times n

    			- f_3: n \times n

    		- Compute the Jacobians

    			- f_1

    				```undefined
    				\begin{aligned}\frac{\partial f_1}{\partial x_1} &= \cos(x_1) \cos(x_2) \\\frac{\partial f_1}{\partial x_2} &= -\sin(x_1) \sin(x_2)\\\frac{\partial f_1}{\partial x} &= \begin{bmatrix} \cos(x_1) \cos(x_2) & -\sin(x_1) \sin(x_2) \end{bmatrix}\end{aligned}
    				```

    			- f_2

    				```undefined
    				\begin{aligned}\frac{\partial f_2}{\partial x_i} &= \frac{\partial (x^\top y)}{\partial x_i} \\&= \frac{\partial (x_1 y_1 + x_2 y_2 + \ldots + x_n y_n)}{\partial x_i} \\&= y_i\\\frac{\partial f_2}{\partial x} &= \begin{bmatrix} y_1 & y_2 & \ldots & y_n \end{bmatrix}\end{aligned}
    				```

    			- f_3

    				```undefined
    				\begin{aligned}\frac{\partial f_{3_{ij}}}{\partial x_k} &= \frac{\partial (x_i x_j)}{\partial x_k} \\&= \begin{cases}x_i & \text{if } k = j \\x_j & \text{if } k = i \\0 & \text{otherwise}\end{cases}\\\frac{\partial f_3}{\partial x} &= \begin{bmatrix}
    				x_1 & 0 & \ldots & 0 \\
    				0 & x_2 & \ldots & 0 \\
    				\vdots & \vdots & \ddots & \vdots \\
    				0 & 0 & \ldots & x_n
    				\end{bmatrix}\end{aligned}
    				```

    ## Problem 5.7

    	- Compute the derivatives \frac{df}{dx} of the following functions by using the chain rule. Provide the dimensions of every single partial derivative. Describe your steps in detail.

    		- f(z) = \log(1+z), z=x^\top x, x\in\R^D

    		- f(z)=\sin(z), z = Ax+b, A\in \R^{E\times D}, x\in\R^d,b\in\R^E where \sin(\cdot) is applied to every element of z

    	- Let u(z) = (1+z), v(z)=\log(z), then

    		```undefined
    		\frac{du}{dz} = \frac{d(1+z)}{dz} = 1 \\\frac{dv}{dz} = \frac{d\log(z)}{dz} = \frac{1}{z}
    		```

    		- f(z)=v(u(z))

    			```undefined
    			\frac{df}{dz} = \frac{dv}{du} \cdot \frac{du}{dz} = \frac{1}{u(z)} \cdot 1 = \frac{1}{1+z}
    			```

    		- z=x^\top x

    			```undefined
    			\frac{dz}{dx} = \begin{bmatrix} \frac{dz}{dx_1} \\ \frac{dz}{dx_2} \\ \vdots \\ \frac{dz}{dx_D} \end{bmatrix} = \begin{bmatrix} 2x_1 \\ 2x_2 \\ \vdots \\ 2x_D \end{bmatrix} = 2x
    			```

    		- \frac{df}{dx}

    			```undefined
    			\frac{df}{dx} = \frac{df}{dz} \cdot \frac{dz}{dx} = \frac{1}{1+z} \cdot 2x = \frac{2x}{1+z}
    			```

    	- u(z)=\sin(z), v(z)=z=Ax+b

    		```undefined
    		\frac{du}{dz} = \cos(z)\\\frac{\partial z_i}{\partial x_j} = A_{ij}
    		```

    		- f(z)=u(v(z))

    			```undefined
    			\frac{df}{dx} = \frac{du}{dv} \cdot \frac{dv}{dx} = \cos(z) \cdot \frac{dz}{dx}
    			```

    		```undefined
    		\begin{bmatrix}\frac{\partial z_2}{\partial x_1} & \frac{\partial z_2}{\partial x_2} & \dots & \frac{\partial z_2}{\partial x_d} \\
    		\vdots & \vdots & \ddots & \vdots \\
    		\frac{\partial z_E}{\partial x_1} & \frac{\partial z_E}{\partial x_2} & \dots & \frac{\partial z_E}{\partial x_d} \end{bmatrix} = \begin{bmatrix} A_{11} & A_{12} & \dots & A_{1d} \\
    		A_{21} & A_{22} & \dots & A_{2d} \\
    		\vdots & \vdots & \ddots & \vdots \\
    		A_{E1} & A_{E2} & \dots & A_{Ed} \end{bmatrix} = A
    		```

    		Therefore, the derivative \frac{df}{dx} is a matrix of dimensions E \times d, where each element is given by \frac{df_i}{dx_j} = \cos(z_i) \cdot A_{ij}. 

    ## Problem 5.9

    	- We define

    		```undefined
    		\begin{aligned}g(x,z,\nu)&\coloneqq\log p(x,z)-\log q(z,\nu)\\z&\coloneqq t(\epsilon,\nu)\end{aligned}
    		```

    		for different functions p,q,t and x\in\R^D,z\in\R^E,\nu\in\R^F,\epsilon\in\R^G. By using the chain rule, compute the gradient \frac d{d\nu}g(x,z,\nu)

    	- \frac{dh}{dx} = \frac{dh}{df} \cdot \frac{df}{dg} \cdot \frac{dg}{dx}를 이용해서 g(x,z,\nu)에 대입하면,

    		```undefined
    		\frac{d}{d\nu} g(x, z, \nu) = \frac{\partial g}{\partial \nu} + \frac{\partial g}{\partial z} \cdot \frac{\partial z}{\partial \nu}
    		```

    	- \frac{\partial g}{\partial \nu}

    		```undefined
    		\frac{\partial g}{\partial \nu} = \frac{\partial}{\partial \nu} \left(\log p(x, z) - \log q(z, \nu)\right) = 0 - \frac{\partial}{\partial \nu} \log q(z, \nu) = -\frac{1}{q(z, \nu)} \frac{\partial q(z, \nu)}{\partial \nu}
    		```

    	- \frac{\partial g}{\partial z}

    		```undefined
    		\frac{\partial g}{\partial z} = \frac{\partial}{\partial z} \left(\log p(x, z) - \log q(z, \nu)\right) = \frac{\partial}{\partial z} \log p(x, z) - \frac{\partial}{\partial z} \log q(z, \nu)
    		```

    	- \frac{\partial z}{\partial \nu}

    		```undefined
    		\frac{\partial z}{\partial \nu} = \frac{\partial}{\partial \nu} t(\epsilon, \nu)
    		```

    	- 저 3개의 값들을 다 대입하면,

    		```undefined
    		\frac{d}{d\nu} g(x, z, \nu) = -\frac{1}{q(z, \nu)} \frac{\partial q(z, \nu)}{\partial \nu} + \left(\frac{\partial}{\partial z} \log p(x, z) - \frac{\partial}{\partial z} \log q(z, \nu)\right) \cdot \frac{\partial}{\partial \nu} t(\epsilon, \nu)
    		```

# Week 6

    ## Exercise 5.4

    	- Compute the Taylor polynomials T_n, n=0,…,5 of f(x)=\sin(x)+\cos(x) at x_0=0

    	- Taylor polynomial

    		```undefined
    		T_n(x) := \sum_{k=0}^n\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k
    		```

    	- n=0

    		```undefined
    		T_0(x)=f(0)=\sin(0)+\cos(0)=1
    		```

    	- n=1

    		```undefined
    		T_1(x)=f(0)+f'(0)x = 1 + (\cos(0)-\sin(0))x = 1+x
    		```

    	- n=2

    		```undefined
    		\begin{aligned}T_2(x) &= f(0)+f'(0)x+\frac{f''(0)}2x^2\\&=1+x-\frac{(\sin(0)+\cos(0))}2x^2 \\&= 1+x-\frac{x^2}2\end{aligned}
    		```

    	- n=3 → 미분하면 반복되는 걸 위에서 발견했음.

    		```undefined
    		\begin{aligned}T_3(x) &= 1+x-\frac{x^2}2+\frac{f'''(0)}{6}x^3\\&=1+x-\frac{x^2}2-\frac{\cos(0)-\sin(0)}6x^3 \\&= 1+x-\frac{x^2}2-\frac{x^3}6\end{aligned}
    		```

    	- n=4

    		```undefined
    		\begin{aligned}T_4(x) &= 1+x-\frac{x^2}2-\frac{x^3}6+\frac{f''''(0)}{24}x^4\\&=1+x-\frac{x^2}2-\frac{x^3}6+\frac{\sin(0)+\cos(0)}{24}x^4\\&=1+x-\frac{x^2}2-\frac{x^3}6+\frac{x^4}{24}\end{aligned}
    		```

    	- n=5

    		```undefined
    		\begin{aligned}T_5(x) &= 1+x-\frac{x^2}2-\frac{x^3}6+\frac{x^4}{24}+\frac{f'''''(0)}{120}x^5\\&=1+x-\frac{x^2}2-\frac{x^3}6+\frac{x^4}{24}+\frac{\cos(0)-\sin(0)}{120}x^5\\&=1+x-\frac{x^2}2-\frac{x^3}6+\frac{x^4}{24}+\frac{x^5}{120}\end{aligned}
    		```
