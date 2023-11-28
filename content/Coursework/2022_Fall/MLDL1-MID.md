---
id: d8913c3a-829d-42bf-8f77-fc465794b330
title: MLDL1 MID
created_time: 2023-07-25T05:02:00.000Z
last_edited_time: 2023-10-07T08:35:00.000Z
icon_emoji: 💨
하위 항목: []
subclass: 2022_Fall
class: Coursework
작성일시: 2023-07-25T05:02:00.000Z
상위 항목: []

---

# Statistical Learning

    ## Is there an ideal f(X)?

    	- \mathbb{E}(Y|X=4) means expected value of Y given X = 4

    	- The good choice of f(x) = \mathbb{E}(Y|X=x) is called the regression function

    ## Regression function f(x)

    	- Is the ideal or optimal predictor of Y with regard to mean-squared prediction error: f(x) = \mathbb{E}(Y|X=x) is the function that minimizes \mathbb{E}[(Y-g(X))^2|X=x] over all functions g at all points X =x

    	- \epsilon = Y-f(x) is the irreducible error. Even if we knew f(x) we would still make erros in prediction ,since at each X=x there is typically a distribution of possible 

    	- For any estimate of \hat f(x) of f(x), we have

    		```undefined
    		\begin{aligned}\mathbb{E}\left[(Y-\hat f(X))^2 | X= x \right]&=\mathbb E\left[(f(X)+\epsilon - \hat f(X))^2|X=x \right]\\&=[f(x)-\hat f(x)]^2 + \text{Var}(\epsilon)\end{aligned}
    		```

    ## How to estimate f

    	- We will always assume that we have observed a set of n different data points, which are called training data

    	- Our goal is to apply learning method to the training data in order to estimate the unknown function f

    	- Most statistical learning method for this task can be characterized as either **parametric** or **non-parametric**

    	### Parametric(Structured) Models
    	
    	- A linear model is an important example of a parametric model, which is specified in terms of p+1 parameters
    	
    	- Another examples: Logistic model, or etc.
    	
    	- There exist a risk that the functional form used to estimate f can be different from true f
    	
    	
    	
    	### Non-parametric models
    	
    	- Non parametric methods do not make explicit assumptions about the functional form of f.
    	
    	- They seek in estimate of f that gets close to data points as possible without being too rough or wiggly
    	
    	- Non-parametric model require a very large number of observations to obtain an accurate estimate for f

    ## Trade-offs

    	- Prediction accuracy vs. interpretability

    	- Goot fit vs overfit(or underfit)

    	- Parsimony vs black-box

    	### Model accuracy

    	```undefined
    	\text{MSE}_\text{te} = \text{Ave}_{i\in\text{te}}\left[y_i - \hat f(x_i)  \right] ^2 = \frac 1M \sum_{i\in\text{te}}\left[y_i - \hat f(x_i)  \right] ^2 
    	```

    	- Compute model accuracy using fresh test data different from training data

    	### Bias-Variance Tradeoff

    	```undefined
    	\mathbb{E}\left[y_0 - \hat f(x_0) \right]^2 = \text{Var}(\hat f(x_0)) + \left[\text{Bias}(\hat f(x_0)) \right]^2 + \text{Var}(\epsilon)
    	```

    	- Typically as the flexibility of \hat f increases, its variance increases and its bias decreases. So choosing the flexibility based on average test error amounts to bias-variance tradeoff

    ## Classification Problem

    	- If Y is qualitive, build a classifier C(X) that assigns a class label from C to future unlabeled observation X

    	- Bayes optimal classifier at x is

    		```undefined
    		C_{\text{Bayes}}(x)=j^* \text{ where  }j^* = \arg\max_{j\in C}\mathbb P(Y=j|X=x)
    		```

    		and this classifier has smallest error

# Linear Regression

    ## Simple Linear Regression with single predictor

    	- Assume a model

    		```undefined
    		Y = \beta_0 + \beta_1 X + \epsilon
    		```

    		where \beta_0 and \beta_1 are two unknown constants that represent the intercept and slope.

    	- Given some estimates \hat\beta_0 and \hat\beta_1 for the model coefficients, we predict ]

    		```undefined
    		\hat y = \hat\beta_0 + \hat\beta_1x
    		```

    	- The residual sum of square RSS = e_1^2 + e_2^2 + \cdots+e_n^2

    	- The least squares approach to choose \hat\beta_0 and \hat\beta_1 to minimize RSS

    		```undefined
    		\hat\beta_1 = \frac{\sum_{i=1}^n(x_i-\bar x)(y_i - \bar y)}{\sum_{i=1}^n(x_i-\bar x)^2}\\ \hat\beta_0 = \bar y - \hat\beta_1x
    		```

    	- Standard error of estimator reflects how it varies under repeated sampling

    		```undefined
    		SE(\hat\beta_1)^2 = \frac{\sigma^2}{\sum_{i=1}^n(x_i-\bar x)^2}, SE(\hat\beta_0)^2=\sigma^2\left[ \frac1n + \frac{\bar x^2}{\sum_{i=1}^n(x_i-\bar x)^2}\right]
    		```

    	- This standard error can be used to compute confidence intervals!

    ## Hypothesis Testing

    	- Null hypothesis H_0 means there is no relationship between X and Y

    	- Alternative hypothesis H_A means there is some relationship between X and Y

    	- In linear regression,

    		```undefined
    		H_0 : \beta_1 = 0 \text{ versus } H_A: \beta_1\not=0
    		```

    	- To test null hypothesis, we compute t-statistics with n-2 degrees of freedom

    		```undefined
    		t = \frac{\hat\beta_1 - 0}{SE(\hat\beta_1)}
    		```

    	- Residual standard error RSE = \sqrt{\frac{RSS}{n-2}}

    	- R-squared R^2 = 1-\frac{RSS}{TSS}

    	- Correlation r = \frac{\sum_{i=1}^n(x_i-\bar x)(y_i - \bar y)}{\sqrt{\sum_{i=1}^n(x_i-\bar x)^2}\sqrt{\sum_{i=1}^n(y_i-\bar y)^2}}

    ## Multiple Linear Regression

    	- Model is

    		```undefined
    		Y = \beta_0 + \beta_1 X_1 + \beta_2X_2 +\cdots+\beta_pX_p+\epsilon
    		```

    	- The ideal scenario is when the predictors are uncorrelated because correlations amongst predictors cause problems

    	- We calculate RSS and \hat\beta like this

    		```undefined
    		\begin{aligned}RSS &= (y-X\hat\beta)^\top(y-X\hat\beta)\\\frac{\partial RSS}{\partial\hat\beta}&=-2X^\top y + 2X^\top X\hat\beta = 0\\\hat\beta &= (X^\top X)^{-1}X^\top y\end{aligned}
    		```

    	- If X^\top X is not invertible, that means columns are not independent, and it’s not full rank. This means xs are correlated.

    	- Is at least 1 predictor useful? We use F-statistic to check this

    		```undefined
    		F = \frac{(TSS-RSS)/p}{RSS/(n-p-1)}\sim F_{p,n-p-1}
    		```

    ## Deciding on the important variables

    	- Forward selection: begin with null model and fit p simple linear regression, then add to model with lowest RSS

    	- Backward selection: begin with full model, and remove the variable with largest p value

    	- How to choose optimal member? AIC, BIC, adjusted R-square, CV

# Classification

    - Logistic regression or discriminant analysis is more appropriate than linear regression!

    ## Logistic Regression

    	- Logistic regression uses the form

    		```undefined
    		p(X;\beta) = \frac{e^{\beta_0+\beta_1 X}}{1+e^{\beta_0+\beta_1 X}}
    		```

    	- If we rearrange this, then

    		```undefined
    		\log\left(\frac{p(X;\beta)}{1-p(X;\beta)} \right) = \beta_0 + \beta_1 X
    		```

    		and this monotone transformation is called the log odds

    ## Maximum Likelihood Estimation

    	- We use maximum likelihood to estimate the parameters

    		```undefined
    		\mathcal{L}(\beta) = \mathcal{L}(\beta_0, \beta_1) = \prod_{i:y_i=1}p(x_i;\beta)\prod_{j:y_j=0}(1-p(x_j;\beta))
    		```

    	- This likelihood gives the probability of the observed zeros and ones in the data, and we pick \beta to maximize the likelihood of the observed data.

    	- Log make products to sums

    		```undefined
    		\log\mathcal{L}(\beta) = \sum_{i:y_i=1}\log p(x_i;\beta)+\sum_{j:y_j=0}\log(1-p(x_j;\beta))
    		```

    	- To maximize log likelihood, set its derivatives to zero, but this doesn’t have closed form

    ## Multiple Logistic Regression

    	- Confounding: Outcome에 영향을 미치는 것을 포함시키지 않으면 결과가 달라질 수 있는 것을 언급함 → 해결하기 위해서 Multiple Logistic Regression 이용

    	- For class k \in \{1,...,K\}

    		```undefined
    		\mathbb{P}(Y=k|X,\beta) = \frac{e^{\beta_{0k}+\beta_{1k}X_1+\cdots+\beta_{pk}X_p}}{\sum_{l=1}^Ke^{\beta_{0l}+\beta_{1l}X_1+\cdots+\beta_{pl}X_p}}
    		```

    ## Linear Discriminant Analysis

    	- Use Bayes theorem slightly differently

    		```undefined
    		\mathbb{P}(Y=k|X=x) = \frac{\pi_kf_k(x)}{\sum_{l=1}^K\pi_lf_l(x)}
    		```

    	- When the classes are well separated, the parameter estimates for the logistic regression model are surprisingly unstable.

    	### LDA when p=1

    	- p_k(x) = \mathbb P(Y=k|X=x), and \delta_k(x) = \log p_k(x)

    	- k^* = \argmax_k p_k(x) = \argmax_k\delta_k(x) = x\frac{\mu_k}{\sigma^2}-\frac{\mu_k^2}{2\sigma^2}+\log(\pi_k)

    	- Then, \hat\mu_k = \frac 1{n_k} \sum_{i:y_i=k}x_i, \hat\sigma^2 = \sum_{k=1}^K\frac{n_k-1}{n-K}\hat\sigma_k^2, \hat\pi_k =\frac{n_k}n

    	### LDA when p>1

    	- Density

    		```undefined
    		f(x) = \frac1{(2\pi)^{p/2}|\Sigma|^{1/2}}e^{-\frac12(x-\mu)^\top\Sigma^{-1}(x-\mu)}
    		```

    	- Discriminant funciton \delta_k(x) = x^\top\Sigma^{-1}\mu_k - \frac 12 \mu_k^\top\Sigma^{-1}\mu_k + \log\pi_k

    	- Once we have estimated \hat\delta_k(x), then we can turn theses into estimates for class probabilities

    		```undefined
    		\mathbb{\hat P}(Y=k|X=x) = \frac{e^{\hat\delta_k(x)}}{\sum_{l=1}^K e^{\hat\delta_l(x)}}
    		```

    ## Types of errors

    	- False positive rate: The fraction of negative examples that are classified as positive

    	- False negative rate: The fraction of positive examples that are classified as negative

    	- In order to reduce the false negative rate, we may want to reduce threshold but it may increase the overall error rate

    ## Quadratic Discriminant Analysis

    	- With Gaussians but different \Sigma_k in each class, we get quadratic discriminant analysis

    	- \delta_k(x) = -\frac12(x-\mu_k)^\top \Sigma_k^{-1}(x-\mu_k)+\log\pi_k-\frac12\log|\Sigma_k|

    ## Naive Bayes

    	- Assume features are independent in each class

    	- Gaussian naive bayes assumes each \Sigma_k is diagonal

    		```undefined
    		\begin{aligned}\delta_k(x) &\propto\log\left[\pi_k\prod_{j=1}^pf_{kj}(x_j)\right]\\&=-\frac12\sum_{j=1}^p\left[ \frac{(x_j-\mu_{kj})^2}{\sigma_{kj}^2}+\log\sigma^2_{kj}\right]+\log\pi_k\end{aligned}
    		```

# Cross-Validation

    ## Validation-set approach

    	- We randomly divide the available set of samples into two parts: training and validation(hold-out)

    	- The learning method is fit on the training set, and its performance is evaluated on the validation set

    	- However, validation set error may tend to overestimate the test error for the model fit on the entire data set

    ## K-fold CV

    	- A set of n observations is randomly split into K non-overlapping groups of observations

    	- Each of these K groups acts as a validation set, and the remainder as a training set.

    	- LOOCV(Leave-one out CV): A training set contains all except one, and validation set is only one observation.

    		```undefined
    		CV_{(n)} = \frac1n\sum_{i=1}^n\left(\frac{y_i-\hat y_i}{1-h_i}\right)^2
    		```

    ## CV for classification

    	- Compute

    		```undefined
    		CV_k = \sum_{k=1}^K\frac{n_k}n\text{Err}_k
    		```

    	- The estimated standard deviation of CV_K is

    		```undefined
    		\hat{SE}(CV_k) = \sqrt{\frac1k\sum_{k=1}^K\frac{(\text{Err}_k-CV_k)^2}{K-1}}
    		```

    	- This is useful estimate but not quite valid

# Bootstrap

    - The bootstrap is a flexible and powerful statistical tool that resamples a single dataset to create many simulated samples and can be used to quantify the uncertainty associated with a given estimator or ML method

    - For example, we want to minimize \text{Var}(\alpha X+(1-\alpha)Y), and one saw \alpha=\frac{\sigma_Y^2-\sigma_{XY}}{\sigma_X^2+\sigma_Y^2-2\sigma_{XY}}

    	- To estimate standard deviation of \hat\alpha, repeat process of simulating 100 paired observations of X and Y and estimate \alpha 1000 times, then we will get \hat\alpha_1,...\hat\alpha_{1000}

    	- The mean over all 1000 estimates for \alpha is

    		```undefined
    		\bar\alpha=\frac 1{1000}\sum_{r=1}^{1000}\hat\alpha_r
    		```

    	- The standard deviation of the estimate is

    		```undefined
    		\sqrt{\frac1{1000-1}\sum_{r=1}^{1000}(\hat\sigma_r-\bar\sigma)^2}
    		```

    - Each of the bootstrap data sets is created by sampling with replacement, and same size as original dataset.

    - We estimate the standard error of these bootstrap estimates using the formula

    	```undefined
    	SE_B(\hat\alpha) = \sqrt{\frac{1}{B-1}\sum_{r=1}^B(\hat\alpha^{*r}-\bar{\hat\alpha}^*)^2}
    	```

    - Bootstrap can be used to approximate confidence interval

    - However, each bootstrap sample has significant overlap with the original data. About 2/3 of the original data points appear in each bootstrap sample

# Model Selection

    ## Considerations

    	- Prediction accuracy: especially when p>n

    	- Model interpretability: by removing irrelevant features

    ## Subset Selection

    	- Best subset selection

    		- Let M_0 denote the null model, which contains no predictors. This model simply predicts the sample mean for each observations

    		- For k=1,2,…,p

    			- Fit all \begin{pmatrix}p\\k\end{pmatrix}=\frac{p!}{k!(p-k!)} models that contain exactly k predictors

    			- Pick the best among these models and call it M_k Here k best is defined as having the smallest RSS(or largest R-squared)

    		- Select a single best model among M_0,…,M_p using cross validated prediction error, C_p, AIC, BIC or adjusted R^2

    	- Stepwise selection

    		- There are a lot of kinds that can happen if p goes very large. It can also leads to overfitting, so suggest stepwise selection

    		- Forward stepwise selection

    			- Let M_0 denote the null model, with no predictors

    			- For k=0,…,p-1

    				- Consider all p-k models that augment the predictors in M_k with one additional predictor

    				- Choose the best among this p-k models, and call it M_{k+1}.

    			- Select a single best model from among M_0,…,M_p using cross validated predictoin error, C_p, AIC, BIC, or adjusted R^2

    		- Backward stepwise selection

    			- Let M_p denote the full model, with all predictors

    			- For k=p,p-1,…,1

    				- Consider all k models that contain all but one of the predictors in M_k

    				- Choose the best among this k models and call it M_{k-1}

    			- Select a single best model from among M_0,…,M_p using cross-validated prediction error, C_p, AIC, BIC or adjusted R^2

    ## Estimating test error

    	- Directly estimate the test error with using either a validation set or cross validation approach

    	- Mallow’s C_p = \frac1n(RSS+2d\hat\sigma^2)

    	- The AIC = -2\log L + 2d

    	- BIC = \frac1n(RSS+\log(n)d\hat\sigma^2)

    	- Adjusted R^2 = 1-\frac{RSS/(n-d-1)}{TSS/(n-1)} → large value indicates a model with low test error 

    ## Ridge Regression

    	- Ridge regression coefficient estimates \hat\beta^R that minimizes

    		```undefined
    		\sum_{i=1}^n\left(y_i-\beta_0-x_i^\top\beta\right)^2 + \lambda\|\beta\|_2^2
    		```

    		with x_i = [x_{i1},...x_{ip}]^\top\in\R^p and \beta=[\beta_1,...,\beta_p]^\top\in\R^p

    	- Selecting a good value for \lambda is critical, and it’s found with CV

    	- It is best to apply ridge regression after standardizing the predictors, using the formula

    		```undefined
    		\tilde x_{ij} = \frac{x_{ij}}{\sqrt{\frac1n\sum_{i=1}^n(x_{ij}-\bar x_i)^2}}
    		```

    ## LASSO

    	```undefined
    	\text{minimize}_\beta\left\{\sum_{i=1}^n\left(y_i-\beta_0-x_i^\top\beta \right)^2+\lambda\|\beta\|_1\right\}
    	```

    	where \lambda\ge0 is tuning paramter and \|\beta\|_1 = \sum_{j=1}^p|\beta_j|

    	- Lasso’s l_1 penalty has the effect of forcing some of the coefficient estimates to be exactly equal to zero when the tuning parameter \lambda is sufficiently large

    	- Like best subset selection, lasso performs variable selection

    	```undefined
    	\text{minimize}_\beta\sum_{i=1}^n\left(y_i-x_i^\top\beta\right)^2\text{ subject to } \|\beta\|_1\le s
    	```

    	- Lasso prefers sparse model because \|\beta\|_1=|\beta_1|+|\beta_2|\le s(lasso, square) and \|\beta\|_2^2 = \beta_1^2+\beta_2^2\le s(ridge, circle)

# Decision Trees

    ## Tree-based methods

    	- The set of splitting rules used to segment the predictor space can be sumamrized in a tree, these types of approaches are known as decision tree methods

    	- Simple and useful for interpretation

    	- Are not competitive with the best supervised learning approaches in terms of prediction accuracy

    ## Tree-Building process

    	- Divide the predictor space - set of possible values for X_1,X_2,…,X_p into J distinct and non-overlapping region R_1,R_2,…,R_J

    	- For every observation that falls into the region R_j, we make the same predictioni, which is simply the mean of the response values for the training observations in R_j

    	- The goal is to find R_1,R_2,…R_J that minimizes the RSS

    		```undefined
    		\sum_{j=1}^J\sum_{i\in R_j}(y_i-\hat y_{R_j})^2
    		```

    	- This approach is top down greedy approach that is known as recursive binary splitting

    	- In greater detail, we define the pair of half planes

    		```undefined
    		R_1(j,s) = \{X|X_j<s\}\text{ and } R_2(j,s)=\{X|X_j\ge s\}
    		```

    		and minimize

    		```undefined
    		\sum_{i:x_i\in R_1(j,s)}(y_i-\hat y_{R_1})^2 + \sum_{i:x_i\in R_2(j,s)}(y_i-\hat y_{R_2})^2
    		```

    ## Choosing the best tree

    	### Pruning

    	- A small tree with fewer splits might lead to lower variance, and larger tree an lead to overfit

    	- Cost complexity pruning → introduce tuning parameter \alpha

    		```undefined
    		\sum_{m=1}^{|T|}\sum_{x_i\in R_m}(y_i-\hat y_{R_m})^2 + \alpha|T|
    		```

    	- Similar to LASSO, and select an optimal value \hat\alpha with cross-validation

    ## Classification trees

    	- For a classification tree, we predict that each observation belongs to the most commonly occuring class of training observations in the region to which it belongs

    	- The Gini index is defined by

    		```undefined
    		G = \sum_{k=1}^K\hat p_{mk}(1-\hat p_{mk})
    		```

    		is a measure of total variance across the K classes

    	- An alternative to the gini index is cross-entropy, given by

    		```undefined
    		D = -\sum_{k=1}^K\hat p_{mk}\log\hat p_{mk}
    		```

# Another Tree-based methods

    ## Bagging

    	- Bootstrap aggregation, or bagging is a general purpose procedure for reducing the variance of a machine learning method. Averaging a set of observations reduce variance

    		```undefined
    		\hat f_{bag}(x) = \frac 1B\sum_{b=1}^B\hat f^{*^b}(x)
    		```

    	- In classification tree, take majority vote

    	- Remaining one-third of the observations not used to fit given bagged trees are referred to as the out of bag(OOB) distribution

    ## Random Forest

    	- Random forests provide an improvement over bagged trees by way of a small tweak that decorrelates the trees

    	- When building decision trees, each time a split in a tree is considered, a random selection of m predictors is chosen as split candidates from the full set of p predictors. The split is allowed to use only one of those m predictors

    ## Boosting

    	- Boosting works in similar way with bagging, except that the trees are grown sequentially: each tree is grown using information from previously grown trees

    	- Set \hat f(x_i)=0 and r_i=y_i for all i=1,…,n in the training set

    	- For b=1,2,…,B, repeat

    		- Fit a tree \hat f_b with d splits to surrogate training data \{x_i, r_i\}_{i=1}^n

    		- Update \hat f by adding in a shrunken version of the new tree

    			```undefined
    			\hat f(x)\leftarrow\hat f(x)+\lambda \hat f_b(x)
    			```

    		- Update the residual

    			```undefined
    			r_i \leftarrow r_i-\lambda\hat f_b(x_i)
    			```

    	- Output the boosted model

    		```undefined
    		\hat f(x) = \sum_{b=1}^B \lambda\hat f_b(x)
    		```

    	- The boosting approach learns slowly

    	- By fitting small trees to the residuals we slowly improve \hat f in areas where it doesn’t perform well. The shrinkage parameter \lambda slows the process down even further

    	- Parameter: number of tree B, shrinkage parameter \lambda, number of splits d in each tree

# Support Vector Machine

    > 💡 We try and find a plane that separates the classes in feature space

    ## Hyperplane

    	- Hyperplane

    		```undefined
    		\beta_0+\beta_1X_1+\beta_2X_2+\cdots+\beta_pX_p = 0
    		```

    	- In this hyperplane, \beta = (\beta_1, \beta_2,...,\beta_p) is called the normal vector

    	- If Y_i\cdot f(X_i) > 0 for all i, f(X)=0 defines a separating hyperplane

    ## Classifier

    	- Maximal margin classifier

    		```undefined
    		\begin{aligned}\text{maximize}_{\beta_0,...,\beta_p}\text{ } & M \\\text{subject to} &\sum_{j=1}^p\beta_j^2 = 1,\\&y_i(\beta_0+\beta_1x_{i1}+...+\beta_px_{ip})\ge M\\&\forall i = 1,...,n\end{aligned}
    		```

    	- Support vector classifier(maximizes a soft margin)

    		```undefined
    		\begin{aligned}\text{maximize}_{\beta_0,...,\beta_p}\text{ } & M \\\text{subject to} &\sum_{j=1}^p\beta_j^2 = 1,\\&y_i(\beta_0+\beta_1x_{i1}+...+\beta_px_{ip})\ge M(1-\xi_i),\xi_i\ge0&\forall i = 1,...,n\\&\sum_{i=1}^n\xi_i\le C\end{aligned}
    		```

    	- If C becomes larger then margin becomes wider

    ## Kernels

    	- Inner product \lang x_i, x_{i'} \rang = \sum_{i=1}^px_{ij}x_{i'j}

    	- The linear support vector classifier can be represented as

    		```undefined
    		f(x) = \beta_0 + \sum_{i=1}^n \alpha_i\lang x,x_i\rang
    		```

    	- Kernel: a generalization of the inner product of the form K(x_i, x_{i'}) for vectors x_i,x_{i'}\le\R^p

    		```undefined
    		f(x) = \beta_0 +\sum_{i\in\mathcal S}\hat\alpha_i K(x, x_i)
    		```

    ## Multi Class

    	- OVA(one vs all): fit K different 2-class SVM classifiers \hat f_k(x)

    	- OVO(one vs one): fit all \begin{pmatrix}K\\2\end{pmatrix} pairwise classifiers \hat f_{kl}(x)

# Unsupervised Learning

    ## PCA

    	- PCA produces a low-dimensional representation of a dataset. Finds a sequence of linear combinations of the variables that have maximal variance

    	- First principal component of the set is

    		```undefined
    		Z_1 = \phi_{11}X_1+\phi_{21}X_2+...+\phi_{p1}X_p
    		```

    	- We refers to the elements \phi_{k1} as the loadings of first principal component.

    	- Score: z_{i1}=\phi_{11}\phi_{i1}+\phi_{21}\phi_{i2}+...+\phi_{p1}\phi_{ip}

    	- We want to maximize \frac 1n \sum_{i=1}^n z_{i1}^2 → solve by SVD

    	- Strength of each component is about proportion of variance explained by each one

    		```undefined
    		\frac{\sum_{i=1}^n z_{im}^2}{\sum_{j=1}^p\sum_{i=1}^nx_{ij}^2}
    		```

    ## Clustering

    	- Refers to a very broad set of techniques for finding subgroups, or clusters in a data set

    	- K-means clustering: seek to partition the observations into a pre-specifed number of clusters

    	- Hierarchical clustering: we do not know in advance how many clusters we want.
