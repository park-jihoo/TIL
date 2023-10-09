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

    	![](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d7063d19-cfca-4f2e-bf03-8612cc0c7418/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20231009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20231009T222519Z&X-Amz-Expires=3600&X-Amz-Signature=d88a194b24cfcab700fa28c6f4612efd91f796a6409358cd9ef7362c77ede8e8&X-Amz-SignedHeaders=host&x-id=GetObject)

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

    	- Eigenvectors for matrix A^\top A

    	- \Sigma = \begin{pmatrix}5&0&0\\0&3&0\end{pmatrix}

    	- u_1 = \begin{pmatrix}\sqrt2/2\\\sqrt2/2\end{pmatrix}, u_2 = \begin{pmatrix}\sqrt2/2\\-\sqrt2/2\end{pmatrix}

    ## Problem 4.9

    ## Problem 4.11

# Week 5

# Week 6
