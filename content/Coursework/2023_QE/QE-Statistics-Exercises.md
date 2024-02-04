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

    	- Let X \sim \text{Uniform}(0,1). Let 0<a<b<1. Let

    		```undefined
    		Y = \begin{cases}1 & 0<x<b \\ 0 & \text{otherwise}\end{cases}
    		```

    		```undefined
    		Z = \begin{cases}1 & a<x<1 \\ 0 & \text{otherwise}\end{cases}
    		```

    	- Are Y and Z independent? Why or why not?

    		- Solution: not independent, a < b이기 때문에, a<x<b인 x에서는 overlap이 발생함

    	- Find \mathbb{E}(Y|Z). Hint: What values z can Z take? Noe find \mathbb{E}(Y|Z=z)

    		- Z=1: a<x<1

    			```undefined
    			\begin{aligned}\mathbb{E}(Y|Z=1) &= \mathbb{P}(0<X<b|a<X<1)\\ &=\frac{\mathbb{P}(a<X<b)}{\mathbb{P}(a<X<1)}\\&=\frac{b-a}{1-a}  \end{aligned}
    			```

    		- Z=0: 0<x<a<b so Y=0, \mathbb{E}(Y|Z=0) = 0

    		```undefined
    		\mathbb{E}(Y|Z) = \begin{cases}
    		0 & \text{if } Z=0 \\
    		\frac{b-a}{1-a} & \text{if } Z=1
    		\end{cases}
    		```

    ## Question 3.23

    	- Find the moment generating function for the Poisson, Normal, and Gamma distributions

    	- Find from [https://en.wikipedia.org/wiki/Moment-generating_function](https://en.wikipedia.org/wiki/Moment-generating_function)

    	- Solution: Moment generating function M(t)  = \mathbb{E}\left[e^{tX}\right] = \int_{-\infty}^\infty p(x)e^{tX}dx

    		- Poission: \mathbb{E}\left[e^{tX}\right] = \sum_{k=0}^\infty e^{tk}\frac{\lambda^k e^{-\lambda}}{k!} = e^{-\lambda}\sum_{k=0}^\infty\frac{\left(\lambda e^t\right)^k}{k!} = e^{-\lambda}e^{\lambda e^t}

    		- Normal: \int_{-\infty}^\infty e^{tx}\frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}}dx = e^{t\mu+\frac 12 \sigma^2t^2}

    		- Gamma: M_X(t) = \mathbb{E}\left[e^{tX}\right] = \int_0^\infty e^{tx}\frac{1}{\Gamma(k)\theta^k}x^{k-1}e^{-\frac{x}{\theta}}dx = (1-t\theta)^{-k},t<\frac1\theta

    ## Question 3.24

    	- Let X_1,...,X_n \sim \exp(\beta). Find the moment generating function of X_i. Prove that \sum_{i=1}^n X_i\sim \text{Gamma}(n,\beta)

    	- Solution:

    		- Moment generating function of X_i = \int_{-\infty}^\infty p(x)e^{tx}dx = \int_0^{\infty}e^{tx}\beta e^{-\beta x}dx = \frac{\beta}{\beta-t}

    		- Let Y = \sum_{i=1}^n X_i, then

    			```undefined
    			M_Y(t) = \prod_{i=1}^n M_{X_i}(t) = \left(\frac{\beta}{\beta-t}\right)^n
    			```

    		- Moment generating function of \text{Gamma}(\alpha, \beta) = \left( \frac{1}{1-\beta t}\right)^\alpha로 위의 mnoment generating function과 일치함

# Week 4

    ## Question 5.1

    	- Let X_1, ...,X_n be iid with finite mean \mu=\mathbb{E}(X_i) and finite variance \sigma^2=\mathbb{V}(X_i). Let \bar{X_n} be the sample mean and let S_n^2 be the sample variance.

    		- Show that \mathbb{E}(S_n^2)=\sigma^2.

    			```undefined
    			\begin{aligned}\mathbb{E}(S_n^2)&=\mathbb{E}(\frac{1}{n-1}\sum_{i=1}^n (X_i-\bar{X_n})^2)\\&=\frac{1}{n-1}\mathbb{E}(n\sigma^2)\\&=\sigma^2\end{aligned}
    			```

    		- Show that S_n^2\xrightarrow{P}\sigma^2. Hint: Show that S_n^2=c_nn^{-1}\sum_{i=1}^n X_i^2 - d_n \bar{X_n^2} where c_n\rightarrow 1 and d_n\rightarrow 1. Apply the large number theorem to \sum_{i=1}^n X_i^2 and \bar{X_n^2}. Then use part (e) of Theorem 5.5

    			```undefined
    			\begin{aligned}S_n^2&=\frac{1}{n-1}\sum_{i=1}^n (X_i-\bar{X_n})^2=\frac{1}{n-1}\sum_{i=1}^n X_i^2-\frac{n}{n-1}\bar{X_n^2}\\&=\frac{1}{n}\frac{n}{n-1}\sum_{i=1}^n X_i^2-\frac{n}{n-1}\bar{X_n^2}\end{aligned}
    			```

    			그러니까 c_n=\frac{n}{n-1}\rightarrow 1 and d_n=\frac{n}{n-1}\rightarrow 1

    			Then apply LLN to \sum_{i=1}^n X_i^2 and \bar{X_n^2}, then \sum_{i=1}^nX_i^2\xrightarrow{P}n\sigma^2 and \bar{X_n^2}\xrightarrow{P}\mathbb{E}(X_i^2). So, S_n^2\xrightarrow{P} = \sigma^2

    ## Question 5.3

    	- Let X_1,...X_n be iid and let \mu=\mathbb{E}(X_1). Suppose that variance is finite. Show that \bar{X_n}\xrightarrow{qm}\mu

    		```undefined
    		\begin{aligned}\mathbb{E}(\bar{X_n})&=\mu\\\mathbb{V}(\bar{X_n})&=\frac{\sigma^2}{n}\\\mathbb{E}(\bar{X_n}-\mu)^2&=\mathbb{V}(\bar{X_n})=\frac{\sigma^2}{n}\end{aligned}
    		```

    		If n\rightarrow\infty, then \mathbb{E}(\bar{X_n}-\mu)^2\rightarrow 0 so \bar{X_n}\xrightarrow{qm}\mu

    ## Question 5.5

    	- Let X_1,...,X_n\sim\text{Bernoulli}(p). Prove that \frac{1}{n}\sum_{i=1}^n X_i\xrightarrow{P}p \text{ and } \frac{1}{n}\sum_{i=1}^n X_i^2\xrightarrow{qm}p

    	- Converge in probability

    		```undefined
    		\begin{aligned}\mathbb{P}\left(\left|\frac{1}{n}\sum_{i=1}^n X_i-p\right|>\epsilon\right) &= \mathbb{P}\left(\left|\frac{1}{n}\sum_{i=1}^n X_i-\mathbb{E}\left(\frac{1}{n}\sum_{i=1}^n X_i\right)\right|>\epsilon\right) \\
    		&= \mathbb{P}\left(\left|\frac{1}{n}\sum_{i=1}^n X_i-\mathbb{E}(X_i)\right|>\epsilon\right) \\
    		&= \mathbb{P}\left(\left|\frac{1}{n}\sum_{i=1}^n X_i-\mu\right|>\epsilon\right) \\
    		&= \mathbb{P}\left(\left|\bar{X}_n-\mu\right|>\epsilon\right) \\
    		&= \mathbb{P}\left(|\bar{X}_n-\mu|^2>\epsilon^2\right) \\
    		&\leq \frac{\mathbb{E}\left(|\bar{X}_n-\mu|^2\right)}{\epsilon^2} \\
    		&= \frac{\mathbb{V}(\bar{X}_n)}{\epsilon^2} \\
    		&= \frac{p(1-p)}{n\epsilon^2} \rightarrow 0\end{aligned}
    		```

    	- Converge in Quadratic Mean

    		```undefined
    		\begin{aligned}\mathbb{E}\left(\frac{1}{n}\sum_{i=1}^n X_i^2 - p\right)^2 &= \mathbb{E}\left(\frac{1}{n}\sum_{i=1}^n X_i^2 - \mathbb{E}\left(\frac{1}{n}\sum_{i=1}^n X_i^2\right)\right)^2 \\
    		&= \mathbb{E}\left(\frac{1}{n}\sum_{i=1}^n X_i^2 - \mathbb{E}(X_i^2)\right)^2 \\
    		&= \mathbb{E}\left(\frac{1}{n}\sum_{i=1}^n (X_i^2 - p)^2\right) \\
    		&= \mathbb{V}\left(\frac{1}{n}\sum_{i=1}^n X_i^2\right) \\
    		&= \frac{\mathbb{V}(X_i^2)}{n} \\
    		&= \frac{p(1-p)}{n} \rightarrow 0\end{aligned}
    		```

    ## Question 5.6

    	- Suppose that the height of men has mean 68 inches and standard deviation 2.6 inches. We draw 100 men at random. Find (approximately) the probability that the average height of men in our sample will be at least 68 inches.

    		```undefined
    		\begin{aligned}\mathbb{P}(\bar{X}_n \geq 68) &= \mathbb{P}\left(\frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \geq \frac{68 - \mu}{\sigma/\sqrt{n}}\right) \\
    		&= \mathbb{P}\left(Z \geq \frac{68 - \mu}{\sigma/\sqrt{n}}\right) \\
    		&= 1 - \Phi\left(\frac{68 - \mu}{\sigma/\sqrt{n}}\right) \\
    		&= 1 - \Phi\left(\frac{68 - 68}{2.6/\sqrt{100}}\right) \\
    		&= 1 - \Phi(0) = 0.5\end{aligned}
    		```

    	- Use CLT, \bar{X_n}\xrightarrow{d}N(\mu,\frac{\sigma^2}{n}), so \frac{\bar{X_n}-\mu}{\sigma/\sqrt{n}}\xrightarrow{d}N(0,1)이므로 위의 식을 적용할수 있음

    ## Question 5.8

    	- Suppose we have a computer program consisting of n=100 pages of code. Let X_i be the number of errors on the i^{th} page of code. Suppose that X_i's are Poission with mean 1 and that they are independent. Let Y=\sum_{i=1}^nX_i be the total number of errors in the program. Use CLT to approximate \mathbb{P}(Y<90)

    		```undefined
    		\begin{aligned} \mathbb{P}(Y < 90) &= \mathbb{P}\left(\frac{Y - n\mu}{\sqrt{n\sigma^2}} < \frac{90 - n\mu}{\sqrt{n\sigma^2}}\right) \\
    		&= \mathbb{P}\left(Z < \frac{90 - n\mu}{\sqrt{n\sigma^2}}\right) \\
    		&= \Phi\left(\frac{90 - n\mu}{\sqrt{n\sigma^2}}\right) \\
    		&= \Phi\left(\frac{90 - 100}{\sqrt{100}}\right) \\
    		&= \Phi(-1) = 0.1587\end{aligned}
    		```

    ## Question 5.9

    	- Suppose that \mathbb{P}(X=1)=\mathbb{P}(X=-1)=1/2. Define

    		```undefined
    		X_n=\begin{cases}X&\text{with probability }1-\frac{1}{n}\\e^n&\text{with probability }\frac1n\end{cases}
    		```

    		Does X_n converge to X in probability? Does X_n converge to X in distribution? Does \mathbb{E}(X-X_n)^2 converge to 0?

    	- Probability: \mathbb{P}(|X_n-X|>\epsilon)=\mathbb{P}(X_n=e^n)=\frac{1}{n}\rightarrow 0

    	- Distribution

    		```undefined
    		\begin{aligned}\lim_{n\rightarrow\infty}\mathbb{P}(X_n\leq x) &= \lim_{n\rightarrow\infty}\mathbb{P}(X_n\leq x|X_n=X)\mathbb{P}(X_n=X) \\
    		&\quad + \lim_{n\rightarrow\infty}\mathbb{P}(X_n\leq x|X_n=e^n)\mathbb{P}(X_n=e^n) \\
    		&= \mathbb{P}(X\leq x) + 0 \\
    		&= \mathbb{P}(X\leq x)\end{aligned}
    		```

    	- \mathbb{E}(X-X_n)^2 converge to 0?

    		```undefined
    		\begin{aligned}\mathbb{E}(X - X_n)^2 &= \mathbb{E}(X^2 - 2X_nX_n + \mathbb{E}(X_n)^2) \\
    		&= \mathbb{E}(X^2) - 2\mathbb{E}(X_n^2) + \mathbb{E}(X_n)^2\end{aligned}
    		```

    		```undefined
    		\begin{aligned}\mathbb{E}(X^2) &= 1 \\
    		\mathbb{E}(X_n^2) &= \mathbb{E}(X^2) = 1 \\
    		\mathbb{E}(X_n) &= \mathbb{E}(X) = 0\\\mathbb{E}(X - X_n)^2 &= 1 - 2(1) + (0)^2 \\
    		&= 1 - 2 + 0 \\
    		&= 1\end{aligned}
    		```

    ## Question 5.11

    	- Suppose that X_n\sim N(0,1/n) and Let X be a random variable with distribution F(X)=0 if x<0 and F(x)=1 if x\geq 0. Does X_n converge to X in probability? Does X_n converge to X in distribution?

    	- Probability:

    		- Definition of the random variable: X_n

    		- Relationship with the absolute value: |X_n - X| = |X_n| = X_n

    		- Probability of the absolute value exceeding a threshold \epsilon:

    			```undefined
    			P(∣X_n∣≥ϵ)=P\left(\left|\frac1{\sqrt{n}}Z_n\right|≥ϵ\right)=P(∣Z_n∣≥ϵ\sqrt{n})
    			```

    		- As n becomes larger, \epsilon\sqrt{n} becomes larger, so:
    		\lim_{n→∞}P(|X_n|≥ϵ)→0

    	- Distribution:

    		- Cumulative distribution function (CDF) of X_n:

    			```undefined
    			F_{X_n}(x)=P(X_n≤x)=P(\frac1{\sqrt{n}}Z_n≤x)=P(Z_n≤x\sqrt n)=Φ(x\sqrt n)
    			```

    		- Limit of the CDF as n approaches infinity:

    			```undefined
    			\lim_{⁡n→∞}F_{X_n}(x)=\lim_{⁡n→∞}Φ(\sqrt nx)
    			```

    		- As n becomes larger, \sqrt{n} becomes larger, so \sqrt{n}x can be any real value. Therefore:

    			- For x \geq 0: \lim_{n\rightarrow\infty} F_{X_n}(x) = \Phi(\infty) = 1

    			- For x < 0: \lim_{n\rightarrow\infty} F_{X_n}(x) = \Phi(-\infty) = 0 because \Phi is continuous.

    ## Question 5.15

    	- \begin{pmatrix}X_{11}\\X_{21}\end{pmatrix},\begin{pmatrix}X_{12}\\X_{22}\end{pmatrix},...,\begin{pmatrix}X_{1n}\\X_{2n}\end{pmatrix} are iid random vectors with mean \mu=(\mu_1, \mu_2) and variance \Sigma. \bar{X_1}=\frac1n\sum_{i=1}^nX_{1i} and \bar{X_2}=\frac1n\sum_{i=1}^nX_{2i}. Y_n=\frac{\bar{X_1}}{\bar{X_2}}.

    	- The mean of \bar{X_1} is \mu_1, and its variance is \frac{\Sigma_{11}}{n}.

    	- The mean of \bar{X_2} is \mu_2, and its variance is \frac{\Sigma_{22}}{n}.

    	- The variance of Y_n is given by Var(Y_n) = \frac{Var(\bar{X_1})}{Var(\bar{X_2})} = \frac{\Sigma_{11}}{\Sigma_{22}}.

    	- Applying the Central Limit Theorem (CLT), as n becomes larger, Y_n will have a normal distribution with mean \frac{\mu_1}{\mu_2} and variance \frac{\Sigma_{11}}{\Sigma_{22}}. Thus, the limiting distribution of Y_n is a normal distribution with mean \frac{\mu_1}{\mu_2} and variance \frac{\Sigma_{11}}{\Sigma_{22}}.

    ## Question 5.16

    	- Construct an example where X_n\rightsquigarrow X and Y_n\rightsquigarrow Y but X_n+Y_n\not\rightsquigarrow X+Y

    	- X_n\sim N(0,1) and Y_n\sim N(0,1)

    	- X_n\rightsquigarrow X and Y_n\rightsquigarrow Y because X_n and Y_n are normal distribution

    		- X_n+Y_n\sim N(0,2)

    		- X_n+Y_n\not\rightsquigarrow X+Y because X_n+Y_n is not normal distribution

# Week 5

    ## HW4 3

    ## HW4 4

    ## HW4 5

    ## HW4 6

    ## Exercise 6.1

    	- Let X_1,…,X_n\sim\text{Poission}(\lambda) and let \hat\lambda=n^{-1}\sum_{i=1}^nX_i. Find the bias, se and mse of this estimator

    	- bias

    		```undefined
    		\begin{aligned}\text{bias}(\hat\lambda)&=\mathbb{E}(\hat \lambda)-\lambda= \mathbb{E}\left[\frac 1n\sum_{i=1}^n X_i\right]-\lambda\\& = \frac 1n\sum_{i=1}^n\mathbb E[X_i]-\lambda \\&= \frac1n\sum_{i=1}^n\lambda = \lambda-\lambda=0\end{aligned}
    		```

    	- SE

    		```undefined
    		\begin{aligned}\text{SE}(\hat\lambda)&=\sqrt{\text{Var}(\hat\lambda)}\\&=\sqrt{\text{Var}\left(\frac 1n\sum_{i=1}^nX_i\right)} \\&=\sqrt{\frac 1{n^2}\text{Var}\left(\sum_{i=1}^nX_i\right)}\\&=\sqrt{\frac\lambda n}\end{aligned}
    		```

    	- MSE

    		```undefined
    		\text{MSE}(\hat\lambda)=\text{Var}(\hat\lambda)+\text{bias}(\hat\lambda)^2 = \frac\lambda n
    		```

    ## Exercise 6.2

    	- Let X_1,…,X_n\sim\text{Uniform}(0, \theta) and let \hat\theta=\max\{X_1,...,X_n\}. Find the bias, se and mse of this estimator

    	- bias

    		- \mathbb E(\hat\theta)=\mathbb E[\max\{X_1,...,X_n\}] and Let Y=\max\{X_1,…,X_n\}

    		- F_Y(y)=P(Y\le y)=(P(X_i\le y))^n = \left(\frac y\theta\right)^n

    		- f_Y(y)=n\left(\frac y\theta\right)^{n-1}\frac1 \theta = \frac{ny^{n-1}}{\theta^n}

    		- \mathbb E(\hat\theta) = \int_0^\theta y\frac{ny^{n-1}}{\theta^n}dy = \frac n{n+1}\theta

    		- \text{bias}(\hat\theta) = \frac n{n+1}\theta - \theta = -\frac\theta{n+1}

    	- se

    		- \text{Var}(\hat\theta) = \text{Var}(\max\{X_1,...,X_n\}) = n\times \text{Var}(X_i) = n \times \frac{\theta^2}{12}

    		- \text{SE}(\hat\theta)=\sqrt{\frac{n\theta^2}{12}}

    	- mse

    		```undefined
    		\text{MSE}(\hat\theta) = \frac{n\theta^2}{12} +\frac{\theta^2}{(n+1)^2}
    		```

    ## Exercise 6.3

    	- Let X_1,…,X_n\sim\text{Uniform}(0, \theta) and let \hat\theta=2\bar X_n. Find the bias, se and mse of this estimator

    	- bias

    		```undefined
    		\begin{aligned}\text{bias}(\hat\theta)&=\mathbb E(\hat\theta)-\theta=2\mathbb E[\bar X_n]-\theta\\&=2\frac 1n\sum_{i=1}^n\frac\theta2-\theta =0 \end{aligned}
    		```

    	- se

    		```undefined
    		\begin{aligned}\text{SE}(\hat\theta)&=\sqrt{\text{Var}(\hatθ)}\\&=\sqrt{\text{Var}(2\bar X_n)}=\sqrt{2^2⋅\text{Var}(\bar X_n)}\\&=\sqrt{4⋅\frac{θ^2}{12n}}=\sqrt{\frac{θ^2}{3n}}\end{aligned}
    		```

    	- mse \frac{\theta^2}{3n}

    ## Exercise 7.1

    	- Prove Theorem 7.3

    	- At any fixed Value of x

    		```undefined
    		\begin{aligned}\mathbb{E}\left(\hat F_n(x)\right)&=F(x)\\\mathbb{V}\left(\hat F_n(x)\right)&=\frac{F(x)(1-F(x))}{n}\\\text{MSE}&= \frac{F(x)(1-F(x))}{n}\rightarrow0\\\hat F_n(x)&\xrightarrow{P}F(x)\end{aligned}
    		```

    	- Expectation

    		```undefined
    		\begin{aligned}\mathbb{E}(\hat F_n(x)) &= \mathbb{E}\left(\frac{1}{n} \sum_{i=1}^{n} I(X_i \leq x)\right) \\&= \frac{1}{n} \sum_{i=1}^{n} \mathbb{E}\left(I(X_i \leq x)\right) \\&= \frac{1}{n} \sum_{i=1}^{n} F(x) \\&= F(x) \quad \text{(since each term is equal to } F(x) \text{)}\end{aligned}
    		```

    	- Variance

    		```undefined
    		\begin{aligned}\mathbb{V}(\hat F_n(x)) &= \mathbb{V}\left(\frac{1}{n} \sum_{i=1}^{n} I(X_i \leq x)\right) \\&= \frac{1}{n^2} \sum_{i=1}^{n} \mathbb{V}\left(I(X_i \leq x)\right) \quad \text{(observations are independent)} \\&= \frac{1}{n^2} \sum_{i=1}^{n} \left[F(x)(1 - F(x))\right]\quad(I(X_i \leq x) \text{ Bernoulli random variable } F(x)) \\&= \frac{F(x)(1 - F(x))}{n} \quad \text{(there are } n \text{ terms in the sum)}\end{aligned}
    		```

    	- MSE

    		```undefined
    		\begin{aligned}\text{MSE} &= \mathbb{E}\left[\left(\hat F_n(x) - F(x)\right)^2\right] \\&= \mathbb{E}\left[\left(\hat F_n(x) - F(x)\right)\left(\hat F_n(x) - F(x)\right)\right] \\&= \mathbb{E}\left[\left(\hat F_n(x)^2 - 2\hat F_n(x)F(x) + F(x)^2\right)\right] \\&= \mathbb{E}\left[\hat F_n(x)^2\right] - 2\mathbb{E}\left[\hat F_n(x)F(x)\right] + \mathbb{E}\left[F(x)^2\right] \\&= \mathbb{E}\left[\hat F_n(x)^2\right] - 2F(x)\mathbb{E}\left[\hat F_n(x)\right] + F(x)^2 \\&= \mathbb{E}\left[\hat F_n(x)^2\right] - 2F(x)^2 + F(x)^2 \\&= \mathbb{E}\left[\hat F_n(x)^2\right] - F(x)^2\\&= \frac{F(x)(1 - F(x))}{n} + F(x)^2 - F(x)^2 = \frac{F(x)(1 - F(x))}{n}\end{aligned}
    		```

    	- Convergence

    		```undefined
    		\begin{aligned}\text{Pr}\left(|\hat F_n(x) - F(x)| \geq \epsilon\right) &\leq \frac{\mathbb{V}(\hat F_n(x))}{\epsilon^2} \\&= \frac{F(x)(1 - F(x))}{n\epsilon^2} \rightarrow 0 \quad \text{as } n \rightarrow \infty\end{aligned}
    		```

    ## Exercise 7.2

    	- Let X_1,...,X_n \sim \text{Bernoulli}(p) and let Y_1,...,Y_m \sim \text{Bernoulli}(q). Find the plug-in estimator and estimated standard error for p. Find an approximate 90 percent confidence interval for p. Find the plug-in estimator and estimated standard error for p − q. Find an approximate 90 percent confidence interval for p − q.

    	- Plug-in estimator for p:

    		```undefined
    		\hat p = \frac 1 n \sum_{i=1}^nX_i
    		```

    	- Estimated SE for \hat{p}

    		```undefined
    		SE(\hat{p}) = \sqrt{\frac{\hat{p}(1-\hat{p})}{n}}
    		```

    	- Plug-in estimator for p-q

    		```undefined
    		\hat{p} - \hat{q} = \frac{1}{n} \sum_{i=1}^{n} X_i - \frac{1}{m} \sum_{i=1}^{m} Y_i
    		```

    	- Estimated SE for \hat p - \hat q

    		```undefined
    		SE(\hat{p} - \hat{q}) = \sqrt{\frac{\hat{p}(1-\hat{p})}{n} + \frac{\hat{q}(1-\hat{q})}{m}}
    		```

    	- 90% confidence interval for p(z is approximately 1.645)

    		```undefined
    		\hat{p} \pm z \cdot SE(\hat{p})
    		```

    	- 90% confidence interval for p-q

    		```undefined
    		(\hat{p} - \hat{q}) \pm z \cdot SE(\hat{p} - \hat{q})
    		```

    ## Exercise 7.3

    	- Generate 100 observations from a N(0,1) distribution. Compute a 95 percent confidence band for the cdf F (as described in the appendix). Repeat this 1000 times and see how often the confidence band contains the true distribution function. Repeat using data from a Cauchy distribution

    	- Python Code

    		```python
    		import math
    		import numpy as np
    		from scipy.stats import norm, cauchy
    		import matplotlib.pyplot as plt
    		from tqdm import tqdm
    		
    		def compute_bounds(n, alpha, r):
    		    epsilon = math.sqrt((1 / (2 * n)) * math.log(2 / alpha))
    		
    		    F_n = lambda x: sum(r < x) / n
    		    L_n = lambda x: max(F_n(x) - epsilon, 0)
    		    U_n = lambda x: min(F_n(x) + epsilon, 1)
    		
    		    xx = sorted(r)
    		
    		    df = pd.DataFrame({
    		        'x': xx,
    		        'F_n': np.array(list(map(F_n, xx))),
    		        'U_n': np.array(list(map(U_n, xx))),
    		        'L_n': np.array(list(map(L_n, xx))),
    		        'CDF': np.array(list(map(norm.cdf, xx))),
    		    })
    		    return df
    		
    		normal_bounds = []
    		cauchy_bounds = []
    		n_simulations = 1000
    		
    		for k in tqdm(range(n_simulations)):
    		    n = 100
    		    alpha = 0.05
    		    r_normal = norm.rvs(size=n)
    		    r_cauchy = cauchy.rvs(size=n)
    		
    		    df_normal = compute_bounds(n, alpha, r_normal)
    		    df_cauchy = compute_bounds(n, alpha, r_cauchy)
    		
    		    # Check if all values are within the bounds for each distribution
    		    all_in_bounds_normal = ((df_normal['U_n'] >= df_normal['CDF']) & (df_normal['CDF'] >= df_normal['L_n'])).all()
    		    all_in_bounds_cauchy = ((df_cauchy['U_n'] >= df_cauchy['CDF']) & (df_cauchy['CDF'] >= df_cauchy['L_n'])).all()
    		
    		    normal_bounds.append(all_in_bounds_normal)
    		    cauchy_bounds.append(all_in_bounds_cauchy)
    		```

    	- Plots

    		![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/325b51ce-0dd0-449b-9b2e-aa5260bbc869/normal_cauchy.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240204T004628Z&X-Amz-Expires=3600&X-Amz-Signature=89ef878915ddf0082d053937dd35defc3aacb3fb53b69f27b957ed7090bb25e1&X-Amz-SignedHeaders=host&x-id=GetObject)

    ## Exercise 7.4

    	- Let X_1,...,X_n \sim F and let F_n(x) be the empirical distribution function. For a fixed x, use the central limit theorem to find the limiting distribution of F_n(x).

    	- F_n(x) = \frac{1}{n} \sum_{i=1}^{n} I(X_i \leq x) where I(X_i \leq x) is indicator function

    		```undefined
    		\mathbb E[I(X_i \leq x)] = P(X_i \leq x) = F(x) \\\text{Var}[I(X_i \leq x)] = F(x)(1-F(x))
    		```

    	- Now, use the properties of CLT to find limiting distribution of F_n(x) as n \to \infty

    		```undefined
    		\begin{aligned}\mathbb E[F_n(x)] &= \mathbb E\left[\frac{1}{n} \sum_{i=1}^{n} I(X_i \leq x)\right] \\&= \frac{1}{n} \sum_{i=1}^{n} \mathbb E[I(X_i \leq x)] \\&= \frac{1}{n} \sum_{i=1}^{n} F(x) = F(x)\end{aligned}
    		```

    		```undefined
    		\begin{aligned}Var[F_n(x)] &= Var\left[\frac{1}{n} \sum_{i=1}^{n} I(X_i \leq x)\right] \\&= \frac{1}{n^2} \sum_{i=1}^{n} Var[I(X_i \leq x)] \\&= \frac{1}{n^2} \sum_{i=1}^{n} F(x)(1-F(x))\\&= \frac{1}{n} F(x)(1-F(x))\end{aligned}
    		```

    ## Exercise 7.5

    	- Let x and y be two distinct points. Find \text{Cov}(\hat F_n(x), \hat F_n(y))

    		```undefined
    		\text{Cov}(\hat{F}_n(x), \hat{F}_n(y)) = \frac{1}{n-1} \sum_{i=1}^{n} (\hat{F}_n(x)_i - \bar{\hat{F}}_n(x))(\hat{F}_n(y)_i - \bar{\hat{F}}_n(y)).
    		```

    	- \bar{\hat{F}}_n(x) = \frac{1}{n} \sum_{i=1}^{n} \hat{F}_n(x)_i,\bar{\hat{F}}_n(y) = \frac{1}{n} \sum_{i=1}^{n} \hat{F}_n(y)_i. 대입하면

    		```undefined
    		\text{Cov}(\hat{F}_n(x), \hat{F}_n(y)) = \frac{1}{n(n-1)} \sum_{i=1}^{n} I(X_i \leq x) I(X_i \leq y) - \frac{1}{n^2},
    		```

    ## Exercise 7.6

    	- Let X_1,...,X_n \sim F and let \hat F be the empirical distribution function. Let a<b be fixed numbers and define θ = T(F) = F(b) − F(a). Let \hatθ= T(\hat F_n) =\hat F_n(b) −\hat F_n(a) . Find the estimated standard error of θ. Find an expression for an approximate 1 − α confidence interval for θ.

    	- \hat{F}n(x) = \frac{1}{n} \sum_{i=1}^{n} \mathbb{1}(X_i \leq x), SE(\hat{\theta}) = \sqrt{\text{Var}(\hat{\theta})}

    		```undefined
    		\begin{aligned}\text{Var}(\hat{\theta}) &= \text{Var}(\hat{F}_n(b) - \hat{F}_n(a))\\&= \text{Var}(\hat{F}_n(b)) + \text{Var}(\hat{F}_n(a)) - 2\text{Cov}(\hat{F}_n(b), \hat{F}_n(a)).\\&= \frac{F(b)(1 - F(b))}{n} + \frac{F(a)(1 - F(a))}{n}.\end{aligned}
    		```

    	- X_1,…,X_n independent, so covariance are 0

    		```undefined
    		SE(\hat{\theta}) = \sqrt{\frac{F(b)(1 - F(b))}{n} + \frac{F(a)(1 - F(a))}{n}}.
    		```

    	- Confidence Interval

    		```undefined
    		\text{CI}_{1-\alpha}(\theta) = \left(\hat{\theta} - z_{\alpha/2} \times \sqrt{\frac{F(b)(1 - F(b))}{n} + \frac{F(a)(1 - F(a))}{n}}, \, \hat{\theta} + z_{\alpha/2} \times \sqrt{\frac{F(b)(1 - F(b))}{n} + \frac{F(a)(1 - F(a))}{n}}\right).
    		```

    ## Exercise 7.7

    	- Data on the magnitudes of earthquakes near Fiji are available on the website for this book. Estimate the cdf F(x). Compute and plot a 95 percent confidence envelope for F (as described in the appendix). Find an approximate 95 percent confidence interval for F(4.9) − F(4.3).

    		```python
    		import numpy as np
    		import matplotlib.pyplot as plt
    		import pandas as pd
    		import requests
    		
    		url = 'https://www.stat.cmu.edu/~larry/all-of-statistics/=data/fijiquakes.dat'
    		
    		r = requests.get(url, verify=False)
    		
    		data = r.text.split('\n')
    		data = [x.split() for x in data if x != '']
    		df = pd.DataFrame(data[1:], columns=data[0])
    		r = np.array(df['mag'])
    		n = len(r)
    		alpha = 0.05
    		epsilon = np.sqrt(np.log(2 / alpha) / (2 * n))
    		
    		F_n = lambda x: np.sum(r < x)/n
    		L_n = lambda x: np.max([0, F_n(x) - epsilon])
    		U_n = lambda x: np.min([1, F_n(x) + epsilon])
    		xx = np.sort(r)
    		
    		d = pd.DataFrame({
    		        'x': xx,
    		        'F_n': [F_n(x) for x in xx],
    		        'L_n': [L_n(x) for x in xx],
    		        'U_n': [U_n(x) for x in xx]
    		    })
    		
    		plt.plot(d['x'], d['F_n'], label='F_n')
    		plt.plot(d['x'], d['L_n'], label='L_n')
    		plt.plot(d['x'], d['U_n'], label='U_n')
    		
    		plt.legend()
    		plt.show()
    		```

    	- Plot

    		![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/09097402-9adf-4c5b-bc97-29be8eff8976/fiji.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240204T004631Z&X-Amz-Expires=3600&X-Amz-Signature=4748833006e0ae81c39c1e8bd868979f9397d7890d2807e3c517fd06b57289d3&X-Amz-SignedHeaders=host&x-id=GetObject)

    ## Exercise 7.8

    	- Get the data on eruption times and waiting times between eruptions of the Old Faithful geyser from the website. Estimate the mean waiting time and give a standard error for the estimate. Also, give a 90 percent confidence interval for the mean waiting time. Now estimate the median waiting time. In the next chapter we will see how to get the standard
    	error for the median.

    		```python
    		url = 'https://www.stat.cmu.edu/~larry/all-of-statistics/=data/faithful.dat'
    		
    		re = requests.get(url, verify=False)
    		
    		data = re.text.split('\n')
    		data = [x.split() for x in data if x != '']
    		data = [x for x in data if len(x) == 3 and x[0].isdigit()]
    		columns = ['idx','eruptions', 'waiting']
    		
    		df = pd.DataFrame(data, columns=columns)[['eruptions', 'waiting']]
    		r = np.array(df['waiting'], dtype=float)
    		
    		# Mean waiting time
    		mean_waiting_time = r.mean()
    		se = r.std() / np.sqrt(len(r))
    		
    		print(f'Mean waiting time: {mean_waiting_time:.3f} +- {se:.3f}')
    		
    		# 90% confidence interval
    		import scipy.stats as stats
    		z_90 = stats.norm.ppf(0.95)
    		
    		ci = (mean_waiting_time - z_90 * se, mean_waiting_time + z_90 * se)
    		print(f'90% confidence interval: {ci}')
    		
    		# Median waiting time
    		median_waiting_time = np.median(r)
    		print(f'Median waiting time: {median_waiting_time:.3f}')
    		```

    ## Exercise 7.9

    	- 100 people are given a standard antibiotic to treat an infection and another 100 are given a new antibiotic. In the first group, 90 people recover; in the second group, 85 people recover. Let p_1 be the probability of recovery under the standard treatment and let p_2 be the probability of recovery under the new treatment. We are interested in estimating θ = p_1 − p_2. Provide an estimate, standard error, an 80 percent confidence interval, and a 95 percent confidence interval for θ.

    	- \hat{p}_1 = \frac{90}{100} = 0.9, \hat{p}_2 = \frac{85}{100} = 0.85, \hat{θ} = \hat{p}_1 - \hat{p}_2 = 0.9 - 0.85 = 0.05

    	- SE(\hat{p}_1 - \hat{p}_2) = \sqrt{\frac{0.9 \cdot (1 - 0.9)}{100} + \frac{0.85 \cdot (1 - 0.85)}{100}}

    	- 80% confidence interval

    		```undefined
    		\hat{θ} \pm 1.282 \cdot SE(\hat{p}_1 - \hat{p}_2) = 0.05 \pm 1.282 \cdot 0.1474 \approx (-0.1245, 0.2245)
    		```

    	- 95% confidence interval

    		```undefined
    		\hat{θ} \pm 1.96 \cdot SE(\hat{p}_1- \hat{p}_2) = 0.05 \pm 1.96 \cdot 0.1474 \approx (-0.2378, 0.3378)
    		```

    ## Exercise 7.10

    	- In 1975, an experiment was conducted to see if cloud seeding produced rainfall. 26 clouds were seeded with silver nitrate and 26 were not. The decision to seed or not was made at random. Get the data from [https://www.stat.cmu.edu/~larry/all-of-statistics/=data/clouds.dat](https://www.stat.cmu.edu/~larry/all-of-statistics/=data/clouds.dat) Let θ be the difference in the mean precipitation from the two groups. Estimate θ. Estimate the standard error of the estimate and produce a 95 percent confidence interval.

    		```python
    		url = 'https://www.stat.cmu.edu/~larry/all-of-statistics/=data/clouds.dat'
    		
    		re = requests.get(url, verify=False)
    		
    		data = re.text.split('\n')
    		data = [x.split() for x in data if x != '']
    		data = [x for x in data if len(x) == 2][3:]
    		columns = ['Unseeded', 'Seeded']
    		df = pd.DataFrame(data, columns=columns)
    		X = df['Seeded'].astype(float)
    		Y = df['Unseeded'].astype(float)
    		
    		# Difference in means
    		theta = X.mean() - Y.mean()
    		print(f'Difference in means: {theta:.3f}')
    		
    		# Standard error of the estimate
    		se = np.sqrt(X.var() / len(X) + Y.var() / len(Y))
    		print(f'Standard error of the estimate: {se:.3f}')
    		
    		# 95% confidence interval
    		import scipy.stats as stats
    		z_95 = stats.norm.ppf(0.975)
    		ci = (theta - z_95 * se, theta + z_95 * se)
    		print(f'95% confidence interval: {ci}')
    		```

# Week 6

    ## 8.1

    	- Consider the data in Example 8.6. Find the plug-in estimate of the correlation coefficient. Estimate the standard error using the bootstrap. Find a 95% percent confidence interval using the Normal, pivotal, and percentile method

    		`LSAT   576   635   558   578   666   580   555   661
    		       651   605   653   575   545   572   594`
    		
    		
    		`GPA    3.39  3.30  2.81  3.03  3.44  3.07  3.00  3.43
    		       3.36  3.13  3.12  2.74  2.76  2.88  3.96`

    	- Solution(Python Code)

    		```python
    		import numpy as np
    		LSAT = np.array([576, 635, 558, 578, 666, 580, 555, 661, 651, 605, 653, 575, 545, 572, 594])
    		GPA = np.array([3.39, 3.30, 2.81, 3.03, 3.44, 3.07, 3.00, 3.43, 3.36, 3.13, 3.12, 2.74, 2.76, 2.88, 3.96])
    		
    		# plug-in estimate of the correlation coefficient
    		coef = np.corrcoef(LSAT, GPA)[0, 1]
    		print("plug-in estimate of the correlation coefficient: ", coef)
    		
    		# bootstrap
    		import tqdm
    		import random
    		
    		B = 100000
    		r = np.zeros(B)
    		for i in tqdm.tqdm(range(B)):
    		    xx = np.random.choice(LSAT, size=len(LSAT), replace=True)
    		    yy = np.random.choice(GPA, size=len(GPA), replace=True)
    		    r[i] = np.corrcoef(xx, yy)[0, 1]
    		    
    		se = np.std(r)
    		# standard error
    		print("standard error: ", se)
    		
    		# 95% confidence interval
    		# Normal
    		print("95% confidence interval: ", coef + np.array([-1, 1]) * 1.96 * se)
    		# Pivotal
    		print("95% confidence pivotal interval: ", 2 * coef - np.percentile(r, [97.5, 2.5]))
    		# Percentile
    		print("95% confidence percentile interval: ", np.percentile(r, [2.5, 97.5]))
    		```

    	- Result

    		- plug-in estimate of the correlation coefficient: 0.5459189161795887

    		- standard error:  0.2662505722102419

    		- 95% confidence interval:  [0.02406779 1.06777004]

    		- 95% confidence pivotal interval:  [0.57269141 1.59023638]

    		- 95% confidence percentile interval:  [-0.49839855  0.51914643]

    ## 8.2

    	- Conduct a simulation to compare the various bootstrap confidence interval methods. Let n=50 and let T(F)=\int(x-\mu)^3 dF(x)/\sigma^3 be the skewness. Draw Y_1,…,Y_n\sim N(0,1) and set X_i=e^{Y_i},i=1,…,n. Construct the three types of bootstrap 95% intervals for T(F) from the data X_1,…,X_n. Repeat this whole thing many times and estimate the true coverage of the three intervals

    	- Code

    		```python
    		import numpy as np
    		import tqdm
    		
    		def create_data(n):
    		    y = np.random.normal(size=n)
    		    return np.exp(y)
    		
    		def skewness(x):
    		    return np.mean((x - np.mean(x)) ** 3) / np.std(x) ** 3
    		
    		def bootstrap(x, B):
    		    n = len(x)
    		    r = np.zeros(B)
    		    for i in tqdm.tqdm(range(B)):
    		        xx = np.random.choice(x, size=n, replace=True)
    		        r[i] = skewness(xx)
    		    return r
    		
    		X = create_data(50)
    		boot_data = bootstrap(X, 100000)
    		
    		# Normal
    		print("Normal: ", skewness(X) + np.array([-1, 1]) * 1.96 * np.std(boot_data))
    		# Pivotal
    		print("Pivotal: ", 2 * skewness(X) - np.percentile(boot_data, [97.5, 2.5]))
    		# Percentile
    		print("Percentile: ", np.percentile(boot_data, [2.5, 97.5]))
    		```

    	- Solution

    		- Normal:  [1.32239513 3.91373325]

    		- Pivotal:  [1.68593852 4.25208253]

    		- Percentile:  [0.98404584 3.55018986]

    ## 8.3

    	- Let

    		```undefined
    		X_1,...,X_n\sim t_3
    		```

    		where n=25. Let \theta=T(F)=(q_{.75}-q_{.25})/1.34 where q_p denotes the p^{th} quantile. Do a simulation to compare the coverage and length of following confidence intervals for \theta

    		- Normal interval with standard error from bootstrap

    		- Bootstrap percentile interval

    		- Pivotal bootstrap interval

    	- Code

    		```python
    		import numpy as np
    		from scipy.stats import t
    		from tqdm import tqdm
    		
    		def create_data(n):
    		    return t.rvs(3, size=n)
    		
    		def theta(x):
    		    return (np.percentile(x, 75) - np.percentile(x, 25)) / 1.34
    		
    		def bootstrap(x, B):
    		    n = len(x)
    		    r = np.zeros(B)
    		    for i in tqdm(range(B)):
    		        xx = np.random.choice(x, size=n, replace=True)
    		        r[i] = theta(xx)
    		    return r
    		
    		
    		X = create_data(25)
    		boot_data = bootstrap(X, 100000)
    		
    		# Normal
    		print("Normal: ", theta(X) + np.array([-1, 1]) * 1.96 * np.std(boot_data))
    		# Percentile
    		print("Percentile: ", np.percentile(boot_data, [2.5, 97.5]))
    		# Pivotal
    		print("Pivotal: ", 2 * theta(X) - np.percentile(boot_data, [97.5, 2.5]))
    		```

    	- Solution

    		- Normal:  [0.58025268 2.07088886]

    		- Percentile:  [0.52818864 2.00149402]

    		- Pivotal:  [0.64964751 2.1229529 ]

    ## 8.4

    	- Let X_1,…,X_n be distinct observations (no ties). Show that there are

    		```undefined
    		\binom{2n-1}{n}
    		```

    		distinct bootstrap samples

    		- Hint: Imagine putting n balls into n buckets

    	- n distinct balls and n distinct bucket

    	- 각각이 어떤 bucket으로 들어가느냐는 n개씩의 경우의 수가 있으나, 이렇게 되면 빈 bucket이 생길 수 있음

    	- 그러니까 n개의 공을 n개로 나눠서 넣으려면, n-1개의 divider이 존재하여 이게 추가됨

    	- n-1개의 divider은 위치가 고정되어 있으니까 n개만 위치를 고르면 되고 이를 조합으로 표현하면 위의 식이 됨

    ## 8.5

    	- Let X_1, . . . , X_n be distinct observations (no ties). Let X_1^∗, . . . , X_n^∗ denote
    	a bootstrap sample and let \bar X^∗_n =n^{-1} \sum^n_{i=1} X_i^∗. Find: \mathbb E(\bar X^∗_n|X_1, . . . , X_n), \mathbb V(\bar X^∗_n|X_1, . . . , X_n), \mathbb E(\bar X^∗_n) and \mathbb V(\bar X^∗_n).

    	- \mathbb E(\bar X^∗_n|X_1, . . . , X_n)

    		```undefined
    		\mathbb E\left(n^{-1}\sum_{i=1}^n X_i\right)=n^{-1}\sum_{i=1}^n\mathbb E(X_i)=\mathbb E(X)
    		```

    	- \mathbb V(\bar X^∗_n|X_1, . . . , X_n)

    		```undefined
    		\begin{aligned}
    		\mathbb{V}(\bar{X}_n^* | X_1, ..., X_n) & =
    		\mathbb{E}((\bar{X}_n^*)^2 | X_1, ..., X_n) - \mathbb{E}(\bar{X}_n^* | X_1, ..., X_n)^2 \\
    		&= \mathbb{E}\left(\left(n^{-1}\sum_{i=1}^nX_i\right)^2\right) - \mathbb{E}\left(n^{-1}\sum_{i=1}^nX_i\right)^2 \\
    		&= \frac 1{n^{2}} \mathbb{E}\left(\sum_{i=1}^nX_i^2 + \sum_{i=1}^n \sum_{j=1, j \neq i}^n X_i X_j\right) - \mathbb{E}(X)^2 \\
    		&= \frac 1{n^{2}} \sum_{i=1}^n \mathbb{E}(X_i^2) + \frac 1{n^{2}} \sum_{i=1}^n \sum_{j=1, j \neq i}^n \mathbb{E}(X_i X_j) - \mathbb{E}(X)^2  \\
    		&= \frac 1n (\mathbb{V}(X) + \mathbb{E}(X)^2) + \frac 1{n^{2}}\sum_{i=1}^n \sum_{j=1, j \neq i}^n \mathbb{E}(X_i) \mathbb{E}(X_j) - \mathbb{E}(X)^2 \\
    		&= \frac 1n(\mathbb{V}(X) + \mathbb{E}(X)^2) + \frac 1n (n - 1) \mathbb{E}(X)^2 - \mathbb{E}(X)^2 \\
    		&= \frac{1}{n}\mathbb{V}(X)
    		\end{aligned}
    		```

    	- \mathbb E(\bar X^∗_n)

    		```undefined
    		\mathbb E\left(n^{-1}\sum_{i=1}^n X^*_i\right)=n^{-1}\sum_{i=1}^n\mathbb E(X^*_i)=\mathbb E(X)
    		```

    	- \mathbb V(\bar X^∗_n) → differs from bootstrap method!

    		```undefined
    		\mathbb{V}(\bar X_n^*) \approx \frac{1}{n} \mathbb{V}(\bar X_n)
    		```

    ## 8.6

    	- Let X_1,…,X_n\sim\text{Normal}(\mu,1). Let \theta=e^\mu and let \hat\theta=e^{\bar X}. Create a data set using \mu=5 consisting of n=100 observations

    		- Use the bootstrap to get the se and 95% confidence interval for \theta

    		- Plot a histogram of bootstrap replications. This is an estimate of the distribution of \hat\theta. Compare this to the true sampling distribution of \hat\theta

    	- Code

    		```python
    		import numpy as np
    		from tqdm import tqdm
    		
    		def create_data(n, mu):
    		    return np.random.normal(loc=mu, size=n)
    		
    		def theta(x):
    		    return np.exp(np.mean(x))
    		
    		def bootstrap(x, B):
    		    n = len(x)
    		    r = np.zeros(B)
    		    for i in tqdm(range(B)):
    		        xx = np.random.choice(x, size=n, replace=True)
    		        r[i] = theta(xx)
    		    return r
    		
    		# get se and 95% confidence interval for theta
    		X = create_data(100, 5)
    		boot_data = bootstrap(X, 100000)
    		print("se: ", np.std(boot_data))
    		print("95% confidence interval: ", np.percentile(boot_data, [2.5, 97.5]))
    		
    		# plot histogram
    		import matplotlib.pyplot as plt
    		# subplot 1
    		plt.subplot(1, 2, 1)
    		plt.hist(boot_data, bins=100)
    		
    		# compare to true sampling distribution
    		# subplot 2
    		plt.subplot(1, 2, 2)
    		# get theta of the true sampling distribution
    		X = create_data(100, 5)
    		theta_data = np.zeros(100000)
    		for i in tqdm(range(100000)):
    		    xx = create_data(100, 5)
    		    theta_data[i] = theta(xx)
    		    
    		plt.hist(theta_data, bins=100)
    		
    		plt.show()
    		```

    	- Solution

    		- se:  20.207732471344304

    		- 95% confidence interval:  [164.78311377 243.89758345]

    			![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/ba312f41-dbff-4635-8df9-45b644fe7c06/histogram.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240204T004641Z&X-Amz-Expires=3600&X-Amz-Signature=992558c5033c486f61e9134d1fd3062b43440e4c1f2c27186d19f336481b4149&X-Amz-SignedHeaders=host&x-id=GetObject)

    ## 8.7

    	- Let X_1,…,X_n \sim \text{Uniform}(0,\theta). Let \hat\theta = X_{\max}=\max\{X_1,...,X_n\} Generate a data set of size 50 with \theta=1

    		- Find the distribution of \hat\theta. Compare the true distribution of \hat\theta to the histograms from the bootstrap

    		- This is a case where the bootstrap does very poorly. In fact, we can prove that this is a case. Show that P(\hat\theta=\hat\theta)=0 and yet P(\hat\theta^*=\hat\theta)\approx .632.

    	- Code

    		```python
    		import numpy as np
    		from tqdm import tqdm
    		
    		X = np.random.uniform(size=50, low=0, high=1)
    		theta_hat = np.max(X)
    		
    		B = 100000
    		boot_data = np.zeros(B)
    		n = len(X)
    		for i in tqdm(range(B)):
    		    xx = np.random.choice(X, size=n, replace=True)
    		    boot_data[i] = np.max(xx)
    		    
    		    
    		# get se and 95% confidence interval for theta
    		print("se: ", np.std(boot_data))
    		print("95% confidence interva(Normal): ", theta_hat + np.array([-1, 1]) * 1.96 * np.std(boot_data))
    		# plot histogram
    		import matplotlib.pyplot as plt
    		# subplot 1
    		plt.subplot(1, 2, 1)
    		plt.hist(boot_data, bins=100)
    		
    		# compare to true distribution of theta_hat
    		# subplot 2
    		plt.subplot(1, 2, 2)
    		theta_data = np.zeros(100000)
    		for i in tqdm(range(100000)):
    		    xx = np.random.uniform(size=50, low=0, high=1)
    		    theta_data[i] = np.max(xx)
    		    
    		plt.hist(theta_data, bins=100)
    		
    		plt.savefig("histogram.png")
    		```

    	- SE and confidence interval

    		- se:  0.007846291239349261

    		- 95% confidence interva(Normal):  [0.96689164 0.99764911]

    	- Histogram

    		![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/f7d5b3ec-f4a9-4771-a03b-60cef8e47b65/histogram.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240204T004643Z&X-Amz-Expires=3600&X-Amz-Signature=24f30344276a45c74014af4a6128dbff4f4bc0a6dfdb5dd5201205f75b6e255f&X-Amz-SignedHeaders=host&x-id=GetObject)

    	- Chance of not being selected in any of n draws from n samples with replacement is (1-1/n)^n. Then chance of being selected in any of n draws from n samples with replacemnet is 1-(1-1/n)^n and as n goes to \infty, it become 1-e^{-1}\approx .632

    ## 8.8

    	- Let T_n=\bar X_n^2,\mu=\mathbb E(X_1),\alpha_k=\int|x-\mu|^kdF(x) and \hat\alpha_k = n^{-1}\sum_{i=1}^n|X_i-\bar X_n|^k. Show that

    		```undefined
    		v_{boot} = \frac{4\bar X_n^2\hat\alpha_2}n+ \frac{4\bar X_n\hat\alpha_3}{n^2}+ \frac{\hat\alpha_4}{n^3}
    		```

    	- bootstrap variance v_{boot}=\mathbb V(\bar X_n^2)=\mathbb E(\bar X_n^4)-\mathbb E(\bar X_n^2)^2

    	- Let \bar{X}_n = S_n + \bar{X}n = \frac{1}{n} \sum{i=1}^n (X_i - \bar{X}_n) + \bar{X}_n

    	- Then

    		```undefined
    		\begin{aligned}\mathbb{E}\left(\bar{X}_n^4\right) &= \mathbb{E}\left( (S_n + \bar{X}_n)^4 \right) \\&= \mathbb{E}\left( S_n^4 + 4 S_n^3 \bar{X}_n + 6 S_n^2 \bar{X}_n^2 + 4 S_n \bar{X}_n^3 + \bar{X}_n^4 \right) \\&= \mathbb{E}(S_n^4) + 4 \bar{X}_n \mathbb{E}(S_n^3) + 6 \bar{X}_n^2 \mathbb{E}(S_n^2) + 4 \bar{X}_n^3 \mathbb{E}(S_n) + \bar{X}_n^4\end{aligned}
    		```

    		and

    		```undefined
    		\mathbb{E}\left(\overline{X}_n^2\right)^2 = \mathbb{E}\left(\overline{X}_n^2 + S_n\right)^2 = \overline{X}_n^4 + 2 \overline{X}_n^2 \frac{\hat{\alpha}_2}{n} + \frac{\hat{\alpha}_2^2}{n^2}
    		```

    	- \mathbb E(S_n)=0, \mathbb E(S_n^2)=\frac{\hat\alpha_2}n, \mathbb E(S_n^3)=\frac{\hat\alpha_3}{n^2}, \mathbb E(S_n^4)=\frac{\hat\alpha_4+\hat\alpha_2^2}{n^3}

    ## 9.1

    	- Let X_1,…,X_n \sim \text{Gamma}(\alpha,\beta). Find the method of moments estimator for \alpha and \beta

    	- \alpha_1=\mathbb E(X)=\frac\alpha\beta

    	- \alpha_2=\mathbb E(X^2)=\mathbb V(X)+\mathbb E(X^2)=\frac{\alpha}{\beta^2}+\frac{\alpha^2}{\beta^2}=\frac{\alpha^2+\alpha}{\beta^2}

    	- \hat\alpha_1=\frac{\hat\alpha_n}{\hat\beta_n}, \hat\alpha_2=\frac{\hat\alpha_n^2+\hat\alpha_n}{\hat\beta_n^2}

    		```undefined
    		\begin{aligned}\hat\alpha_n &= \frac{\hat\alpha_1^2}{\hat\alpha_2-\hat\alpha_1^2}& \hat\beta_n&=\frac{\hat\alpha_1}{\hat\alpha_2-\hat\alpha_1^2}\end{aligned}
    		```

    ## 9.2

    	- Let X_1,…,X_n \sim \text{Uniform}(a, b) where a and b are unknown parameters and a<b

    		- Find the method of moments estimator for a and b

    			- \alpha_1=\mathbb E(X)=\frac{a+b}2, \alpha_2 = \mathbb E(X^2)=\mathbb V(X)+\mathbb E(X)^2 = \frac{a^2+ab+b^2}{3}

    			- hat을 각각 씌워도 똑같게 작용

    			```undefined
    			\hat{a} = \hat{\alpha}_1 - \sqrt{3}(\hat{\alpha}_1^2 - \hat{\alpha}_2)\quad \quad\hat{b} = \hat{\alpha}_1 + \sqrt{3}(\hat{\alpha}_1^2 - \hat{\alpha}_2)
    			```

    		- Find the MLE \hat a and \hat b

    			```undefined
    			\begin{aligned}f(x;(a,b))&= \begin{cases}\frac1{b-a}&\text{if }a\le x \le b\\0&\text{otherwise}\end{cases}\\\mathcal L_n(a,b)=\prod_{i=1}^nf(X_i;(a,b))&=\begin{cases}\frac1{(b-a)^n}&\text{if }a\le X_i \le b ,\forall X_i\\0&\text{otherwise}\end{cases}\end{aligned}
    			```

    			- Likelihood를 maximize하기 위해서는, b-a를 최소화해야 하고 결국 b가 miminum of x_i, a가 maximum of x_i여야 한다.

    		- Let \tau = \int x dF(x). Find the MLE of \tau

    			```undefined
    			\hat{\tau} = \int x  d\hat{F}(x) = \frac{n}{n} \sum_{i=1}^n X_i = \frac{1}{n} \sum_{i=1}^n X_i = \frac{\hat a + \hat b}2
    			```

    		- Let \hat\tau be the MLE of \tau. Let \widetilde \tau be nonparametric plug-in estimator for \tau = \int xdF(x). Suppose that a=1, b=3, and n=10. Find the mse of \hat\tau by simulation. Find the mse of \widetilde\tau analytically. Compare.

    			- Code

    				```python
    				import numpy as np
    				from tqdm import tqdm
    				a, b, n = 1, 3, 10
    				X = np.random.uniform(size=n, low=a, high=b)
    				
    				tau_hat = (X.min() + X.max()) / 2
    				
    				B = 100000
    				boot_data = np.zeros(B)
    				for i in tqdm(range(B)):
    				    xx = np.random.choice(X, size=n, replace=True)
    				    boot_data[i] = (xx.min() + xx.max()) / 2
    				    
    				# get se and 95% confidence interval for theta
    				print("se: ", np.std(boot_data))
    				print("95% confidence interval(Normal): ", tau_hat + np.array([-1, 1]) * 1.96 * np.std(boot_data))
    				
    				se_tau_hat = np.sqrt(1/n * (b-a)**2 / 12)
    				mse_tau_hat = se_tau_hat**2 + tau_hat**2
    				print("mse_tau_hat: ", mse_tau_hat)
    				```

    			- Solution

    				- se:  0.12764131590484684

    				- 95% confidence interval(Normal):  [1.92403362 2.42438758]

    				- mse_tau_hat:  4.760525068343031

    ## 9.3

    	- Let X_1,…,X_n \sim N(\mu,\sigma^2). Let \tau be 95% percentile

    		- Find the MLE of \tau

    			- Z \sim N(0,1), so (X_i-\mu)/\sigma\sim Z

    			- \tau is .95 percentile, so \mathbb P(X<\tau)=0.95

    			- \mathbb P(Z<\frac{\tau-\mu}\sigma)=0.95, \tau=\mu+z_{5\%}\sigma

    			- MLE of \tau 역시 \hat\tau=\hat\mu+z_{5\%}\hat\sigma

    		- Find an expression for an approximate 1-\alpha confidence interval for \tau

    			- General formula for approximate 1-\alpha confidence interval for \theta is

    				```undefined
    				\left(\hat\theta-z_{\alpha/2}\cdot \text{SE}(\hat\theta),\hat\theta+z_{\alpha/2}\cdot\text{SE}(\hat\theta)\right)
    				```

    			- Standard error of \hat\tau\approx σ\cdot\frac{z_{α/2} + (z_{α/2} + z_α)^2}{ n \cdot f(τ)^2}^{1/2}

    		- Suppose the data are:

    			- `3.23 -2.50  1.88 -0.68  4.43  0.17 1.03 -0.07 -0.01  0.76  1.76  3.18 0.33 -0.31  0.30 -0.61  1.52  5.43 1.54  2.28  0.42  2.33 -1.03  4.00 0.39`

    			Find the MLE \hat\tau. Find the standard error using the delta method. Find the standard error using the parametric bootstrap.

    			- Code

    				```python
    				import numpy as np
    				from tqdm import tqdm
    				from scipy.stats import norm
    				
    				z_05 = norm.ppf(0.95)
    				z_025 = norm.ppf(0.975)
    				
    				X = np.array([3.23, -2.50, 1.88, -0.68, 4.43, 0.17, 1.03, -0.07, -0.01, 0.76, 1.76, 3.18, 0.33, -0.31, 0.30, -0.61, 1.52, 5.43, 1.54, 2.28, 0.42, 2.33, -1.03, 4.00, 0.39])
    				
    				# MLE of tau
    				n = len(X)
    				mu_hat = np.mean(X)
    				sigma_hat = np.std(X)
    				tau_hat = mu_hat + sigma_hat * z_05
    				
    				print("tau_hat: ", tau_hat)
    				
    				# standard error using delta method
    				se_tau_hat = sigma_hat * np.sqrt((1/n) * (1 + z_05 * z_05 / 2))
    				print("se_tau_hat: ", se_tau_hat)
    				confid_interval = tau_hat + np.array([-1, 1]) * z_025 * se_tau_hat
    				print("95% confidence interval: ", confid_interval)
    				
    				# standard error using parametric bootstrap
    				B = 100000
    				boot_data = np.zeros(B)
    				for i in tqdm(range(B)):
    				    xx = np.random.normal(size=n, loc=mu_hat, scale=sigma_hat)
    				    boot_data[i] = np.mean(xx) + np.std(xx) * z_05
    				    
    				# get se and 95% confidence interval for theta
    				print("se: ", np.std(boot_data))
    				print("95% confidence interval(Normal): ", tau_hat + np.array([-1, 1]) * z_025 * np.std(boot_data))
    				```

    			- Answer

    				- \hat\tau: 4.180410658803283

    				- Delta method

    					- se_tau_hat:  0.5575801038636548

    					- 95% confidence interval:  [3.08757374 5.27324758]

    				- Parametric bootstrap

    					- se:  0.5565842254707458

    					- 95% confidence interval(Normal):  [3.08952562 5.2712957 ]

    ## 9.4

    	- Let X_1,…,X_n \sim \text{Uniform}(0, \theta). Show that the MLE is consistent.

    	- Hint: Let Y = \max\{X_1,…,X_n\}. For any c, \mathbb P(Y<C)=\mathbb P(X_1 <c, X_2<c,...,X_n<c)=\mathbb P(X_1<c)\mathbb P(X_2<c)...\mathbb P(X_n<c)

    	- For \text{Uniform}(0,\theta), pdf is

    		```undefined
    		f(x,\theta)=\begin{cases}\frac1\theta&\text{if }0\le x\le\theta\\0&\text{otherwise}\end{cases}
    		```

    	- n개가 되면

    		```undefined
    		f(x,\theta)=\begin{cases}\frac1{\theta^n}&\text{if }0\le x\le\theta\\0&\text{otherwise}\end{cases}
    		```

    	- MLE for \theta = \hat{\theta}_n = \max(x_1, x_2, \ldots, x_n)

    	- Let \epsilon > 0 given, then

    		```undefined
    		\mathbb P(\hat\theta_n<\theta-\epsilon)=\prod_{i=1}^n\mathbb P(X_i<\theta-\epsilon)=\left(1-\frac{\epsilon}{\theta}\right)^n
    		```

    	- If n\to\infty, \lim_{n\to\infty}\hat\theta_n=\theta, It means MLE is consistent!

    ## 9.5

    	- Let X_1,…,X_n\sim\text{Poisson}(\lambda). Find the method of moments estimator, the maximum likelihood estimator and the fisher information I(\lambda)

    	- Method of moment estimator

    		```undefined
    		\hat\lambda = \hat\alpha_1=\frac1n\sum_{i=1}^nX_i
    		```

    	- Likelihood function

    		```undefined
    		\mathcal L_n(\lambda)=\prod_{i=1}^nf(X_i;\lambda)=\prod_{i=1}^n\frac{\lambda^{X_i}e^{-\lambda}}{(X_i)!}
    		```

    	- Log likelihood

    		```undefined
    		\sum_{i=1}^n(X_i\log\lambda-\lambda-\log(X_i)!)=-n\lambda+\log\lambda\sum_{i=1}^nX_i-\sum_{i=1}^n\log X_i!
    		```

    	- \lambda로 편미분하면 -n+\frac{1}{\hat\lambda}\sum_{i=1}^n X_n=-n+n=0인 lambda가 위에 있음

    	- Fisher information

    		```undefined
    		I_n(\theta)=\sum_{i=1}^n\mathbb V_\theta(s(X_i;\theta))
    		```

    		- Score function

    			```undefined
    			s(X;\theta)=\frac{\partial\log f(X;\theta)}{\partial\theta}=\frac{X}{\lambda}-1
    			```

    		- Fisher Information

    			```undefined
    			I_n(\lambda)=\sum_{i=1}^n\mathbb V\left(\frac{X_i}\lambda - 1\right)=\frac{1}{\lambda^2}\sum_{i=1}^n\mathbb V(X_i) = \frac n\lambda
    			```

    ## 9.6

    	- Let X_1,…,X_n \sim N(\theta, 1). Define

    		```undefined
    		Y_i=\begin{cases}1&\text{if }X_i>0\\0&\text{if }X_i\le 0\end{cases}
    		```

    		Let \psi=\mathbb P(Y_1 = 1)

    		- Find the maximum likelihood estimator \hat\psi of \psi

    			- Y_i를 이항분포로 표현할 수 있으니까 Y_1,…,Y_n\sim\text{Bernoulli}(\Phi(\theta))고 이 \Phi(\theta)=p라고 가정하자

    			- \psi=\mathbb P(Y_1 = 1)=p=\Phi(\theta)이므로 각각에 hat을 씌우면

    			- \hat\psi=\hat p=\Phi(\bar X)

    		- Find an approximate 95% percent confidence interval for \psi

    			- Delta method를 쓰면 |g'(\hat\theta)|\hat{se}(\hat\theta)=\frac{\phi(\bar X)}{\sqrt n}

    			- confidence interval

    				```undefined
    				\Phi(\bar X)\left(1\pm\frac{z_{2.5\%}}{\sqrt n}\right)
    				```

    		- Define \widetilde\psi = (1/n)\sum_iY_i. Show that \widetilde\psi is a consistent estimator of \psi

    			- \hat\psi=\hat p=\Phi(\bar X)이고 이것들의 평균임

    			- Law of Large Number을 적용하면, n이 충분히 클 때 consistetnt해질 것

    		- Compute the asymptotic relative efficiency of \widetilde\psi to \hat\psi

    			- Y_1이 Bernoulli distribution이니까, \mathbb V(Y_1)=\psi(1-\psi)일 것이며

    				```undefined
    				\begin{aligned}\mathbb V(\widetilde \psi)&=\mathbb V(Y_1)/n=\psi(1-\psi)/n\\\mathbb V(\hat\psi)&=\phi(\theta)/n\end{aligned}
    				```

    		- Suppose that the data not really normal. Show that \hat\psi is not consistent. What, if anything, does \hat\psi converge to? 

    			- Not normal해도 law of large number에 의해서 \bar X는 converge하게 된다. 그러면 \hat\psi도 결국 converge하게 되는데, 실제로는 X_1과 \bar X가 다르기 때문에 consistent하다고는 말할수 없다.

    ## 9.7

    	- n_1 people are given treatment 1 and n_2 people are given treatment 2. Let X_1 be the number of people on treatment 1 who respond favorably to the treatment and let X_2 be the number of people on treatment 2 who respond favorably. Assume that X_1\sim\text{Binomial}(n_1,p_1), X_2\sim\text{Binomial}(n_2,p_2). Let \psi=p_1-p_2

    		- Find the MLE \hat\psi for \psi

    			```undefined
    			\hat\psi=\hat p_1-\hat p_2 = \frac{X_1}{n_1}-\frac{X_2}{n_2}
    			```

    		- Find the Fisher information matrix I(p_1,p_2)

    			- f((x_1,x_2);\psi)=f_1(x_1;p_1)f_2(x_2;p_2)

    			- Log likelihood

    				```undefined
    				\log f((x_1,x_2);\psi)=\sum_{i=1}^2\left(\log\binom{n_i}{x_i}+x_i\log p_i+(n_i-x_i)\log(1-p_i)\right)
    				```

    			- H_{11}=-\frac{x_1}{p_1^2}-\frac{n_1-x_1}{(1-p_1)^2} → \mathbb E[H_{11}]=-\frac{n_1}{p_1}-\frac{n_1}{1-p_1}

    			- H_{12}=0

    			- H_{21} = 0

    			- H_{22}=-\frac{x_2}{p_2^2}-\frac{n_2-x_2}{(1-p_2)^2}→ \mathbb E[H_{22}]=-\frac{n_2}{p_2}-\frac{n_2}{1-p_2}

    				```undefined
    				I(p_1,p_2)=\begin{bmatrix}H_{11}&H_{12}\\H_{21}&H_{22}\end{bmatrix}
    				```

    		- Use the multiparameter delta method to find the asymptotic standard error of \hat\psi

    			- g(\psi)=p_1-p_2

    				```undefined
    				\nabla g=\begin{bmatrix}\partial g/\partial p_1\\\partial g/\partial p_2\end{bmatrix}=\begin{bmatrix}1\\-1\end{bmatrix}
    				```

    			- \hat{se}(\hat\psi)=\sqrt{(\hat\nabla g)^\top\hat{I(p_1, p_2)^{-1}}(\hat\nabla g)}=\sqrt{\frac{p_1(1-p_1)}{n_1}+\frac{p_2(1-p_2)}{n_2}}

    		- Suppose that n_1=n_2=200, X_1=160,X_2=148. Find \hat\psi. Find an approximate 90% confidence interval for \psi using the delta method and parametric bootstrap

    			- Code

    				```python
    				import numpy as np
    				from tqdm import tqdm
    				from scipy.stats import binom
    				
    				n1, n2 = 200, 200
    				X1, X2 = 160, 148
    				p1_hat, p2_hat = X1 / n1, X2 / n2
    				psi_hat = p1_hat - p2_hat
    				
    				print("psi_hat: ", psi_hat)
    				
    				# standard error using delta method
    				se_psi_hat = np.sqrt(p1_hat * (1 - p1_hat) / n1 + p2_hat * (1 - p2_hat) / n2)
    				print("se_psi_hat: ", se_psi_hat)
    				confid_interval = psi_hat + np.array([-1, 1]) * 1.96 * se_psi_hat
    				print("95% confidence interval: ", confid_interval)
    				
    				# standard error using parametric bootstrap
    				B = 100000
    				boot_data = np.zeros(B)
    				for i in tqdm(range(B)):
    				    xx1 = np.random.binomial(size=n1, n=n1, p=p1_hat)
    				    xx2 = np.random.binomial(size=n2, n=n2, p=p2_hat)
    				    boot_data[i] = np.mean(xx1) - np.mean(xx2)
    				    
    				# get se and 95% confidence interval for theta
    				print("se: ", np.std(boot_data))
    				print("95% confidence interval(Normal): ", psi_hat + np.array([-1, 1]) * 1.96 * np.std(boot_data))
    				```

    			- Solution

    				- psi_hat:  0.06

    				- Delta method

    					- se_psi_hat:  0.04197618372363071

    					- 95% confidence interval:  [-0.02227332  0.14227332]

    				- Bootstrap

    					- se:  0.592232818857143

    					- 95% confidence interval(Normal):  [-1.10077632  1.22077632]

    ## 9.8

    	- Find the fisher information matrix for

    		- Let X_1,…,X_n\sim N(\mu,\sigma^2). Let \tau=g(\mu,\sigma)=\sigma/\mu

    	- Fisher Information matrix

    		```undefined
    		I_n(\mu,\sigma)=\begin{bmatrix}\frac{n}{\sigma^2}&0\\0&\frac{2n}{\sigma^2}\end{bmatrix}
    		```

    	- L(\mu, \sigma^2 | x_1, \ldots, x_n) = \frac{1}{(2\pi\sigma^2)^{n/2}} \exp\left(-\frac{1}{2\sigma^2} \sum_{i=1}^{n} (x_i - \mu)^2\right)

    		```undefined
    		\begin{aligned}\frac{\partial}{\partial \mu} \log L(\mu, \sigma^2 | x_1, \ldots, x_n) &= \frac{1}{\sigma^2} \sum_{i=1}^{n} (x_i - \mu)\\\frac{\partial}{\partial \sigma^2} \log L(\mu, \sigma^2 | x_1, \ldots, x_n) &= -\frac{n}{2\sigma^2} + \frac{1}{2(\sigma^2)^2} \sum_{i=1}^{n} (x_i - \mu)^2\end{aligned}
    		```

    	- I_{11}(\mu, \sigma^2) = -\mathbb E\left[\frac{\partial^2}{\partial \mu^2} \log L(\mu, \sigma^2 | x_1, \ldots, x_n)\right] = -\mathbb E\left[-\frac{n}{\sigma^2}\right] = \frac{n}{\sigma^2}

    	- I_{12}(\mu, \sigma^2) = I_{21}(\mu, \sigma^2) = -\mathbb E\left[\frac{\partial^2}{\partial \mu \partial \sigma^2} \log L(\mu, \sigma^2 | x_1, \ldots, x_n)\right] = 0

    	```undefined
    	\begin{aligned}I_{22}(\mu, \sigma^2) &= -\mathbb E\left[\frac{\partial^2}{\partial (\sigma^2)^2} \log L(\mu, \sigma^2 | x_1, \ldots, x_n)\right] \\&= -\mathbb E\left[\frac{n}{2(\sigma^2)^2} - \frac{1}{(\sigma^2)^3} \sum_{i=1}^{n} (x_i - \mu)^2\right] \\&= \frac{2n}{\sigma^2}\end{aligned}
    	```

    	```undefined
    	I(\mu, \sigma^2) = \begin{bmatrix} \frac{n}{\sigma^2} & 0 \\ 0 & \frac{2n}{\sigma^2} \end{bmatrix}
    	```

    ## 9.9(Same with 8.6)

    	- Let X_1,...,X_n \sim \text{Normal}(μ,1). Let θ = e^μ and let \hat θ= e^{\bar X} be the MLE. Create a data set (using μ = 5) consisting of n=100 observations.

    		- Use the delta method to get \hat{se} and a 95 percent confidence interval for θ. Use the parametric bootstrap to get \hat{se} and 95 percent confidence interval for θ. Use the nonparametric bootstrap to get \hat{se} and 95 percent confidence interval for θ. Compare your answers.

    		- Plot a histogram of bootstrap replications for the parametric and nonparametric bootstraps. These are estimates of the distribution of \hat\theta. The delta method also gives an approximation to this distribution namely, Normal (\hat\theta,se^2). Compare these to the true sampling distribution of \hat\theta. Which approximation is closer to the true distribution?

    ## 9.10(Same with 8.7)

# Week 7

    ## 10.16

    	- Let \theta be a scalar parameter and suppose we test

    		```undefined
    		\begin{aligned}H_0:\theta=\theta_0&&\text{versus}&&H_1:\theta\neq\theta_0\end{aligned}
    		```

    		Let W be the Wald test statistic and let \lambda be the likelihood ratio test statistic. Show that these tests are equivalent in the sense that

    		```undefined
    		\frac{W^2}{\lambda}\xrightarrow P 1
    		```

    		as n\to\infty. Hint: use a Taylor expansion of the log-likelihood l(\theta) to show that

    		```undefined
    		\lambda \approx \left(\sqrt n (\hat \theta-\theta_0)\right)^2\left(-\frac 1nl''(\hat\theta)\right)
    		```

    	- Likelihood Ratio Test Statistic \lambda

    		```undefined
    		\lambda = -2\log\left(\frac{L(\theta_0)}{L(\hat\theta)}\right)
    		```

    		- 한편, log likelihood 에 taylor expansion을 적용하고 \theta_0, \theta를 집어넣으면

    			```undefined
    			l(\theta_0) \approx l(\hat{\theta}) + (\theta_0 - \hat{\theta}) \cdot l'(\hat{\theta}) + \frac{1}{2} (\theta_0 - \hat{\theta})^2 \cdot l''(\hat{\theta})
    			```

    		- l(\hat\theta) 이항 후 양변에 -2 곱하기

    			```undefined
    			\begin{aligned}-2\log \left(\frac{L(\theta_0)}{L(\hat{\theta})}\right) &\approx -2(l(\theta_0) - l(\hat{\theta})) \\&=-2((\theta_0 - \hat{\theta}) \cdot l'(\hat{\theta}) + \frac{1}{2} (\theta_0 - \hat{\theta})^2 \cdot l''(\hat{\theta}))\end{aligned}
    			```

    		- 정리하면

    			```undefined
    			\begin{aligned}\lambda&\approx 2(\hat\theta-\theta_0)l'(\theta)-(\hat\theta-\theta_0)^2l''(\hat\theta)\\&=(\hat\theta-\theta_0)^2\left(\frac 2{\hat\theta-\theta_0}l'(\hat\theta)-l''(\hat\theta)\right)\end{aligned}
    			```

    	- Wald Test statistic W

    		```undefined
    		W=\frac{(\hat\theta-\theta_0)^2}{\text{Var}(\hat\theta)}
    		```

    		- 여기서

    			```undefined
    			\text{Var}(\hat{\theta}) \approx -\frac{1}{n} \left[ l''(\hat{\theta}) \right]^{-1}
    			```

    		- 이걸 대입하면, 

    			```undefined
    			W = \frac{(\hat{\theta} - \theta_0)^2}{-\frac{1}{n} \left[ l''(\hat{\theta}) \right]^{-1}} = -\frac{n (\hat{\theta} - \theta_0)^2}{l''(\hat{\theta})^{-1}}
    			```

    	- 2개의 식이 n\to\infty일 때 equivalent해짐

    ## 11.1

    	- Verify (11.7)

    	- Let X_1,…,X_n \sim N(\theta,\sigma^2). For simplicity, let us assume that \sigma is known. Suppose we take as prior \theta \sim N(a,b^2). The posterior for \theta is 

    		```undefined
    		\theta|X^n\sim N(\bar\theta,\tau^2)
    		```

    		where

    		```undefined
    		\bar\theta=w\bar X+(1-w)a,\\w=\frac{1/se^2}{1/se^2+1/b^2},\frac1{\tau^2}=1/se^2+1/b^2
    		```

    		and se=\sigma/\sqrt n

    	- Likelihood Function of X_1,…,X_n given parameter \theta

    		```undefined
    		L(\theta | X^n) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi}\sigma} \exp\left(-\frac{(X_i - \theta)^2}{2\sigma^2}\right)
    		```

    	- Log likelihood

    		```undefined
    		\log L(\theta | X^n) = -\frac{n}{2}\log(2\pi\sigma^2) - \frac{1}{2\sigma^2}\sum_{i=1}^{n}(X_i - \theta)^2
    		```

    	- Prior distribution(문제에 정의된 대로)

    		```undefined
    		\pi(\theta) = \frac{1}{\sqrt{2\pi}b} \exp\left(-\frac{(\theta - a)^2}{2b^2}\right)
    		```

    	- Posterior Distribution

    		```undefined
    		\begin{aligned}\log \pi(\theta | X^n) &\propto \log L(\theta | X^n) + \log \pi(\theta)\\&\propto -\frac{n}{2}\log(2\pi\sigma^2) - \frac{1}{2\sigma^2}\sum_{i=1}^{n}(X_i - \theta)^2 - \frac{1}{2b^2}(\theta - a)^2\\&\propto -\frac{1}{2\tau^2}(\theta - \bar{\theta})^2 + \text{constant}\end{aligned}
    		```

    	- \frac{1}{\tau^2} = \frac{1}{\sigma^2/n} + \frac{1}{b^2} and \bar{\theta} is given by \bar{\theta} = w\bar{X} + (1 - w)a임을 대입한 결과임

    	- 그러므로 posterior distribution도 normal distribution임을 볼 수 있고,

    		```undefined
    		\theta | X^n \sim N(\bar{\theta}, \tau^2)
    		```

    ## 11.2

    	- Let X_1,…,X_n\sim \text{Normal}(\mu,1)

    		- Simulate a dataset(using \mu=5 consisting of n=100 observations.

    		- Take f(\mu)=1 and find the posterior density. Plot the density

    		- Simulate 1000 draws from the posterior. Plot a histogram of the simulated values and compare the histogram to the answer in (b)

    		- Let \theta=e^\mu. Find the posterior density for \theta analytically and by simulation

    		- Find a 95% posterior interval for \mu

    			- 95% posterior interval for mu:  (5.033280883931001, 5.425273680839011)

    		- Find a 95% confidence interval for \theta

    			- 95% confidence interval for theta:  (26.293277492102494, 1325.0974288506318)

    	- Code

    		```python
    		import numpy as np
    		import matplotlib.pyplot as plt
    		import scipy.stats as stats
    		
    		n= 100
    		mu= 5
    		Sigma = 1
    		# a
    		X = stats.norm.rvs(mu, Sigma, size=n)
    		
    		# b
    		mu_hat = np.mean(X)
    		mu_values = np.linspace(mu_hat-3, mu_hat+3, 1000)
    		L_i = stats.norm.pdf(mu_values, loc=mu_hat, scale=Sigma/np.sqrt(n))
    		plt.subplot(2,2,1)
    		plt.plot(mu_values, L_i/np.sum(L_i))
    		plt.title("B")
    		
    		# c
    		plt.subplot(2,2,2)
    		posterior =stats.norm.rvs(mu_hat, Sigma/np.sqrt(n), size=1000)
    		plt.hist(posterior, density=True, bins=mu_values)
    		plt.title("C")
    		
    		# d
    		plt.subplot(2,2,3)
    		def posterior_density(z):
    		    with np.errstate(divide='ignore'):
    		        return np.where(z > 0, stats.norm.pdf(np.log(z)-mu_hat)/z,0)
    		
    		z_values = np.linspace(0, 500, 100)
    		f_values = posterior_density(z_values)
    		plt.plot(z_values, f_values)
    		plt.title("D - Analytical")
    		
    		plt.subplot(2,2,4)
    		Y = np.exp(stats.norm.rvs(mu_hat, Sigma, size=1000))
    		z_values = np.linspace(0, max(Y), 100)
    		f_values = posterior_density(z_values)
    		plt.hist(Y, density=True, bins=z_values)
    		plt.title("D - Simulation")
    		
    		plt.savefig("11.2.png")
    		
    		# e - 95% posterior interval for mu
    		print("95% posterior interval for mu: ", stats.norm.interval(0.95, loc=mu_hat, scale=Sigma/np.sqrt(n)))
    		
    		# f - 95% confidence interval for theta
    		print("95% confidence interval for theta: ", stats.lognorm.interval(0.95, s=Sigma, scale=np.exp(mu_hat)))
    		```

    	- Plot for 2~4

    		![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/46929168-bd3b-4191-9bbb-c5616feb2317/11.2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240204T004720Z&X-Amz-Expires=3600&X-Amz-Signature=1e3b38d5073a2c8374f3b70749ff3718295c084a2e2c620130b573b2c3dd6cc9&X-Amz-SignedHeaders=host&x-id=GetObject)

    ## 11.3

    	- Let X_1,…,X_n\sim\text{Uniform}(0,\theta). Let f(\theta)\propto1/\theta. Find the posterior density

    		```undefined
    		1=\int_{-\infty}^\infty f(\theta)d\theta=\int_m^\infty c\theta^{-(n+1)}d\theta = c/m^nn
    		```

    	- c=m^nn, use this posterior density is

    		```undefined
    		f(\theta)=\begin{cases}\frac{m^nn}{\theta^{n+1}}&\text{if }\theta\ge m\\0&\text{otherwise}\end{cases}
    		```

    		where m=\max\{X_1,…,X_n\}

    ## 11.4

    	- Suppose that 50 people are given a placebo and 50 are given a new treatment. 30 placebo patients show improvement while 40 treated patients show improvement. Let τ = p_2 − p_1 where p_2 is the probability of improving under treatment and p_1 is the probability of improving under placebo.

    		- Find the MLE of \tau. Find the standard error and 90% confidence interval using delta method

    			```undefined
    			\hat\tau=\hat p_2-\hat p_1 - 0.2\\\text{se}(\hat\tau)=\sqrt{\left(\frac{\partial\tau}{\partial p_1}\right)^2se^2(p_1)+\left(\frac{\partial\tau}{\partial p_2}\right)^2se^2(p_2)}\approx\sqrt{\frac{(0.6\cdot0.4)^2+(0.8\cdot0.2)^2}{50}}\\CI(\tau)=\hat\tau\pm z_{0.9}(\hat\tau)
    			```

    		- Find the standard error and 90% confidence interval using the parametric bootstrap

    			- Code

    				```python
    				import numpy as np
    				import matplotlib.pyplot as plt
    				import scipy.stats as stats
    				from tqdm import tqdm
    				
    				B = 100000
    				n1 = 50
    				n2 = 50
    				x1 = 30
    				x2 = 40
    				
    				p1 = x1/n1
    				p2 = x2/n2
    				
    				xx1 = np.random.binomial(n1, p1, size=B)
    				xx2 = np.random.binomial(n2, p2, size=B)
    				tau_boot = xx2/50 - xx1/50
    				
    				tau_boot_hat= np.mean(tau_boot)
    				q_05 = np.quantile(tau_boot, 0.05)
    				q_95 = np.quantile(tau_boot, 0.95)
    				
    				print("Difference of means: ", tau_boot_hat)
    				print("90% confidence interval: ", (q_05, q_95))
    				```

    			- Difference of means:  0.20000200000000004

    			- 90% confidence interval:  (0.05999999999999994, 0.34)

    		- Use the prior f(p_1,p_2)=1. Use simulation to find the posterior mean and posterior 90% interval for \tau

    			- Code

    				```python
    				import numpy as np
    				from scipy.stats import beta
    				
    				p1_boot = beta.rvs(x1+1, n1-x1+1, size=B)
    				p2_boot = beta.rvs(x2+1, n2-x2+1, size=B)
    				tau_boot = p2_boot - p1_boot
    				
    				tau_boot_hat= np.mean(tau_boot)
    				q_05 = np.quantile(tau_boot, 0.05)
    				q_95 = np.quantile(tau_boot, 0.95)
    				
    				print("Difference of means: ", tau_boot_hat)
    				print("90% confidence interval: ", (q_05, q_95))
    				```

    			- Difference of means:  0.19223770568596596

    			- 90% confidence interval:  (0.04674099097232667, 0.3353915922363718)

    		- Let

    			```undefined
    			\psi=\log\left(\left(\frac{p_1}{1-p_1}\right)\div\left(\frac{p_2}{1-p_2}\right)\right)
    			```

    			be the log-odds ratio. Note that \psi=0 if p_1=p_2. Find the MLE of \psi. Use the delta method to find a 90% confidence interval for \psi

    			- \psi can be represented as

    				```undefined
    				\psi=\log\left(\frac{p_1(1-p_2)}{p_2(1-p_1)}\right)
    				```

    			- \hat\psi=\log(\frac{0.6\cdot0.2}{0.8\cdot0.4})

    			- Standard ErrorSE(\hat\psi)=\sqrt{\nabla g(\hat\psi)^\top\hat{\mathbb V}\nabla g(\hat\psi)}﻿

    		- Use simulation to find the posterior mean and posterior 90% interval for \psi

    			- Code

    				```python
    				import numpy as np
    				from scipy.stats import beta
    				
    				p1_boot = beta.rvs(x1+1, n1-x1+1, size=B)
    				p2_boot = beta.rvs(x2+1, n2-x2+1, size=B)
    				psi_boot = np.log((p1_boot/(1-p1_boot))/(p2_boot/(1-p2_boot)))
    				
    				psi_boot_hat= np.mean(psi_boot)
    				q_05 = np.quantile(psi_boot, 0.05)
    				q_95 = np.quantile(psi_boot, 0.95)
    				
    				print("Difference of means: ", psi_boot_hat)
    				print("90% confidence interval: ", (q_05, q_95))
    				```

    			- Difference of means:  -0.9526034782397551

    			- 90% confidence interval:  (-1.7038154009321569, -0.22331002668283817)

    ## 11.5

    	- Consider the \text{Bernoulli}(p) observations

    		0 1 0 1 0 0 0 0 0 0

    		Plot the posterior for p using these priors

    		- \text{Beta}(1/2,1/2)

    		- \text{Beta}(1,1)

    		- \text{Beta}(10,10)

    		- \text{Beta}(100,100)

    	- Code

    		```python
    		import numpy as np
    		from scipy.stats import beta
    		import matplotlib.pyplot as plt
    		
    		n = 10
    		k = 2
    		p = np.linspace(0, 1, 1000)
    		
    		plt.figure(figsize=(10, 10))
    		for a, b in [(0.5, 0.5), (1, 1), (10, 10), (100, 100)]:
    		    plt.plot(p, beta.pdf(p, k+a-1, n-k+b-1), label=f'Beta({a}, {b})')
    		    plt.legend()
    		    
    		plt.show()
    		```

    	- Plot

    		![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/01820b1e-bd77-4b41-82b7-be850f03fc38/11.5.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240204T004728Z&X-Amz-Expires=3600&X-Amz-Signature=92f68484c3fbc2e7f9078bb362e58cd5312168fd4dc5a1e94bbd5d520e4edb45&X-Amz-SignedHeaders=host&x-id=GetObject)

    ## 11.6

    	- Let X_1,…,X_n \sim\text{Poisson}(\lambda).

    		- Let \lambda\sim\text{Gamma}(\alpha,\beta) be the prior. Show that the posterior is also a Gamma and find the posterior mean

    		- Find the Jeffreys’ prior. Find the posterior

    ## 11.7

    	- In Example 11.9, verify 11.11

    	- Define

    		```undefined
    		\hat\psi=\frac1n\sum_{i=1}^n\frac{R_iY_i}{\xi x_i}
    		```

    		then

    		```undefined
    		\mathbb E(\hat\psi)=\psi\text{ and }\mathbb V(\hat\psi)\le\frac{1}{n\delta^2}
    		```

    ## 11.8

    	- Let X\sim N(\mu, 1). Consider testing

    		```undefined
    		\begin{aligned}H_0:\mu=0&&\text{versus}&&H_1:\mu\neq0\end{aligned}
    		```

    		Take \mathbb P(H_0) =\mathbb P(H_1)=1/2. Let the prior for \mu under H_1 be \mu \sim
    		N(0, b^2). Find an expression for \mathbb P(H_0|X = x). Compare \mathbb P(H_0|X = x) to the p-value of the Wald test. Do the comparison numerically for a variety of values of x and b. Now repeat the problem using a sample of size n. You will see that the posterior probability of H_0 can be large even when the p-value is small, especially when n is large. This disagreement between Bayesian and frequentist testing is called the Jeffreys-Lindley paradox.
