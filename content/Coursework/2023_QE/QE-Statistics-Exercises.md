---
id: 56e8ca2e-ca6c-409a-8bf0-50922da30843
title: QE Statistics Exercises
created_time: 2023-07-09T14:55:00.000Z
last_edited_time: 2023-09-16T07:30:00.000Z
하위 항목: []
subclass: 2023_QE
class: Coursework
작성일시: 2023-07-09T14:55:00.000Z
pdf: https://egrcc.github.io/docs/math/all-of-statistics.pdf
상위 항목: []

---

# Week 2

    ## Question 2.9

    	- Let X \sim \exp(\beta). Find F(x) and F^{-1}(q)

    	- Solution

    		- f(x;\beta) = \frac 1 \beta \exp(-\frac x \beta), x\ge0, \beta>0

    		- F(x;\beta) = \int_{-\infty}^{x} \frac 1 \beta \exp(-\frac t \beta) dt = 1-\exp(-\frac t\beta)

    		- q = 1 - \exp(-\frac t \beta) \rightarrow F^{-1}(q;\beta) = -\beta\ln(1-q)

    ## Question 2.14

    	- Let (X, Y) be uniformly distributed on the unit disk \{(x,y): x^2+y^2 \le 1 \}. Let R = \sqrt{X^2+Y^2} Find the CDF and PDF of R

    	- Solution

    		- PDF of (X, Y)

    			```undefined
    			f(x,y) = \begin{cases}1/\pi & \text{if } x^2 + y^2 \le 1 \\ 0 & \text{otherwise}  \end{cases}
    			```

    		- CDF: \Pr(R\le r) = \begin{cases} r^2 & \text{if } 0 \leq r \leq 1 \\ 0 & \text{if } r < 0 \\ 1 & \text{if } r > 1\end{cases}

    		- PDF: derivation of cdf

    			```undefined
    			f_R(r) = \begin{cases} 2r & \text{if  } 0 \leq r \leq 1 \\ 0 & \text{if } r < 0 \\ 1 & \text{if } r > 1\end{cases}
    			```

    ## Question 2.17

    	- Let 

    		```undefined
    		f_{X,Y}(x,y) = \begin{cases} c(x+y^2) & 0\le x \le1 \text{ and } 0\le y\le 1 \\ 0 & \text{otherwise} \end{cases}
    		```

    		Find P(X<1/2 | Y = 1/2)

    	- Solution: f_Y(y) = \int_0^1 c(x+y^2)dx = \int_0^1 cxdx + \int_0^1 cy^2 dx = c(1/2 + y^2)

    	- f_{X|Y}(x|y) = \frac{x+y^2}{1/2+y^2}, answer = \int_0^{1/2} f_{X|Y}(x|\frac 1 2)dx = \int_0^{1/2} \frac{x+1/4}{1/2+1/4}dx = 1/6 + 1/3 = 1/2

    ## Question 2.20

    	- Let X, Y \sim \text{Uniform}(0,1) be independent. find the pdf of X-Y and X/Y

    	- Solution

    		- X-Y = Z

    			- CDF : F_z(Z) = P(Z \le z) = P(X-Y \le z) = P(X \le z+Y)

    				- z< -1: F_Z(z) = 0

    				- -1\leq z < 0

    					```undefined
    					F_Z(z) = P(X \leq Y + z) \\
    					= \int_0^1 \int_{y+z}^1 1 \, dx \, dy \\
    					= \int_0^1 (1 - (y + z)) \, dy \\
    					= \left[y - \frac{(y+z)^2}{2}\right]_0^1 \\
    					= \frac{1}{2} - \frac{(1+z)^2}{2}.
    					```

    				- If 0 \leq z < 1, we have

    					```undefined
    					F_Z(z) = P(X \leq Y + z) \\
    					= \int_0^{1-z} \int_{y+z}^1 1 \, dx \, dy + \int_{1-z}^1 \int_0^1 1 \, dx \, dy \\
    					= \int_0^{1-z} (1 - (y + z)) \, dy + \int_{1-z}^1 1 \, dy \\
    					= \left[y - \frac{(y+z)^2}{2}\right]0^{1-z} + \left[y\right]{1-z}^1 \\
    					= \frac{(1-z)^2}{2} + z.
    					```

    				- z \geq 1, then F_Z(z) = 1

    			- PDF

    				```undefined
    				\left[\begin{aligned}
    				f_Z(z) &= -2(1+z) \quad \text{for } -1 \leq z < 0, \\
    				f_Z(z) &= 2(1-z) \quad \text{for } 0 \leq z < 1, \\
    				f_Z(z) &= 0 \quad \text{otherwise}.
    				\end{aligned}\right]
    				```

    		- X/Y = Z

    			- CDF: F_Z(z) = P(Z\le z) = P(X/Y \le z)

    				- z \leq 0: F_Z(z)=0 since \frac XY \leq z doesn’t satisfy(좌변은 양수고 우변은 음수)

    				- z>0: F_Z(z) = F(X \le zY) = \int_0^1(\int_0^{zy}dx)dy = \int_0^1 zydy = \frac z 2

    			- PDF: for z>0, f_Z(z) = \frac12, otherwise 0

    ## Question 2.21

    	- Let X_1, ...,X_n \sim \exp(\beta) be iid. Let Y = \max\{ X_1,...,X_n\}. Find the pdf of Y

    		- CDF: F_Y(y) = P(Y \le y) = P(\max\{X_1,...,X_n\} \le y) = \prod_{i=1}^n(P(X_i)\le y) = \prod_{i=1}^n\int_0^y \beta e^{-\beta x}dx= (1-e^{-\beta y})^n

    		- PDF: \frac {d}{dy}(1-e^{-\beta y})^n

    			```undefined
    			f_Y(y) = n(1-e^{-\beta y})^{(n-1)}(\beta e^{-\beta y})
    			```

# Week 3

    ## Question 3.1

    	- Suppose we play a game where we start with c dollars. On each play of the game you either double or halve your money, with equal probability. What is your expected fortune after n trials?

    	- Solution: E[x] = p_1x_1+\dots+p_nx_n

    	- 일단 each play가 independent이고, 1번 던졌을 때 expected value가 \frac 12 \cdot \frac 1 2 + \frac 12 \cdot 2 = \frac 34이니까, n회 한 뒤에는 \left(\frac 34\right)^n이 될 것임

    ## Question 3.3

    	- Let X_1, ...,X_n\sim\text{Uniform}(0,1) and let Y_n = \max\{X_1,...X_n\}, Find \mathbb{E}(Y_n)

    	- Solution: Let F_{Y_n}(y) denote the cumulative distribution function (CDF) of Y_n. Then, we have

    		```undefined
    		\begin{aligned}
    		F_{Y_n}(y) &= \mathbb{P}(Y_n \leq y) \\
    		&= \mathbb{P}(X_1 \leq y, X_2 \leq y, \ldots, X_n \leq y) \\&= \mathbb{P}(X_1 \leq y) \cdot \mathbb{P}(X_2 \leq y) \cdots  \mathbb{P}(X_n \leq y) \\&= y^n\end{aligned}
    		```

    	- PDF of Y_n: 

    	```undefined
    	\begin{aligned}
    	f_{Y_n}(y) &= \frac{d}{dy} F_{Y_n}(y) \\
    	&= ny^{n-1}.
    	\end{aligned}
    	```

    	- \mathbb{E}(Y_n):

    		```undefined
    		\begin{aligned}
    		\mathbb{E}(Y_n) &= \int_{0}^{1} y\cdot f_{Y_n}(y)  dy \\
    		&= \int_{0}^{1} y \cdot n y^{n-1} dy \\
    		&= \left[\frac{n}{n+1} y^{n+1}\right]_{0}^{1} \\
    		&= \frac{n}{n+1}.
    		\end{aligned}
    		```

    ## Question 3.5

    	- A fair coin is tossed until a head is obtained. What is the expected number of tosses that will be required?

    	- Solution

    		```undefined
    		\begin{aligned}\mathbb{E}(N) &= \frac 12\cdot 1 + \left(\frac12\right)^2\cdot2+\cdots\\&=\sum_{i=1}^\infty\left(\frac 12\right)^i\cdot i\\&=x\end{aligned}
    		```

    	- Then, x = \frac 12 + \frac 12 x , \mathbb{E}(N) = 2

    ## Question 3.13

    	- Suppose we generate a random variable X in the following way. First we flip a fair coin. If the coin is heads, take X to have a \text{Unif}(0,1) distribution. If the coin is tails, take X to have a \text{Unif}(3,4) distribution.

    		- Find the mean of X.

    			- Solution

    				```undefined
    				\begin{aligned}
    				\mathbb{E}(X) &= \mathbb{E}(X \mid H)  \mathbb{P}(H) + \mathbb{E}(X \mid T)  \mathbb{P}(T) \\
    				&= \frac{1}{2} \cdot \frac{1}{2} + \frac{7}{2} \cdot \frac{1}{2} \\
    				&= 2
    				\end{aligned}
    				```

    		- Find the standard deviation of X.

    			- Solution

    				```undefined
    				\begin{aligned}
    				\text{Var}(X) &= \mathbb{E}[(X - \mathbb{E}(X))^2] \\
    				&= \mathbb{E}[(X - 2)^2] \\
    				&= \mathbb{E}[(X - \mathbb{E}(X) \mid H)^2]  \mathbb{P}(H) + \mathbb{E}[(X - \mathbb{E}(X) \mid T)^2]  \mathbb{P}(T) \\
    				&= \frac{1}{12} \cdot \frac{1}{2} + \frac{1}{12} \cdot \frac{1}{2} \\
    				&= \frac{1}{12}.
    				\end{aligned}
    				```

    ## Question 3.14

    	- Let X_1, ...,X_m and Y_1,...,Y_n be random variables and let a_1, ...,a_m and b_1,...b_n be constants. Show that

    		```undefined
    		\text{Cov}\left(\sum_{i=1}^ma_iX_i, \sum_{j=1}^nb_jY_j \right) = \sum_{i=1}^m\sum_{j=1}^na_ib_j\text{Cov}(X_i,Y_j)
    		```

    	- Solution(use theorem 3.19 in textbook)

    		```undefined
    		\begin{aligned}\text{Cov}\left(\sum_{i=1}^ma_iX_i, \sum_{j=1}^nb_jY_j \right) &= \mathbb{E}\left(\sum_{i=1}^ma_iX_i\cdot \sum_{j=1}^nb_jY_j \right)-\mathbb{E}\left(\sum_{i=1}^ma_iX_i\right)\mathbb{E}\left(\sum_{j=1}^nb_jY_j \right)\\&= \mathbb{E}\left(\sum_{i=1}^m\sum_{j=1}^na_ib_jX_i\cdot Y_j\right)- \sum_{i=1}^m\sum_{j=1}^na_ib_j\mathbb{E}\left(X_i\right)\mathbb{E}\left(Y_j \right)\\&=\sum_{i=1}^m\sum_{j=1}^na_ib_j\mathbb{E}\left(X_i\cdot Y_j\right)- \sum_{i=1}^m\sum_{j=1}^na_ib_j\mathbb{E}\left(X_i\right)\mathbb{E}\left(Y_j \right)\\&=\sum_{i=1}^m\sum_{j=1}^na_ib_j\text{Cov}(X_i,Y_j)\end{aligned}
    		```

    ## Question 3.22

    ## Question 3.23

    ## Question 3.24

# Week 4

# Week 5

# Week 6

# Week 7
