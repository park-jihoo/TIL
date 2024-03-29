---
id: bcab10cb-9cba-471e-bda4-771a583f9f1e
title: Machine Learning and Deep Learning
created_time: 2023-08-07T06:47:00.000Z
last_edited_time: 2023-08-30T13:49:00.000Z
하위 항목:
  - id: 3e9df96f-67fe-46ce-9ea1-126fdb9a9fc7
subclass: 2023_QE
class: Coursework
작성일시: 2023-08-07T06:47:00.000Z
상위 항목: []

---

# Linear Regression

    ## Simple Linear Regression with single predictor

    	- Assume a model

    		```undefined
    		Y = \beta_0 + \beta_1 X + \epsilon
    		```

    		where \beta_0 and \beta_1 are two unknown constants that represent the intercept and slope.

    	- Given some estimates \hat\beta_0 and \hat\beta_1 for the model coefficients, we predict

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
    		H_0 : \beta_1 = 0 \text{ vs. } H_A: \beta_1\not=0
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

# Classification: Logistic Regression

    > 📖 Logistic regression or Discriminant analysis is more appropriate than linear regression

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

# Classification: Generative Models for Classification

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

# Resampling Methods: Cross-Validation, Bootstrap

    ## Cross-Validation

    	### Validation-set approach

    		- We randomly divide the available set of samples into two parts: training and validation(hold-out)

    		- The learning method is fit on the training set, and its performance is evaluated on the validation set

    		- However, validation set error may tend to overestimate the test error for the model fit on the entire data set

    	### K-fold CV

    		- A set of n observations is randomly split into K non-overlapping groups of observations

    		- Each of these K groups acts as a validation set, and the remainder as a training set.

    		- LOOCV(Leave-one out CV): A training set contains all except one, and validation set is only one observation.

    			```undefined
    			CV_{(n)} = \frac1n\sum_{i=1}^n\left(\frac{y_i-\hat y_i}{1-h_i}\right)^2
    			```

    	### CV for classification

    		- Compute

    			```undefined
    			CV_k = \sum_{k=1}^K\frac{n_k}n\text{Err}_k
    			```

    		- The estimated standard deviation of CV_K is

    			```undefined
    			\hat{SE}(CV_k) = \sqrt{\frac1k\sum_{k=1}^K\frac{(\text{Err}_k-CV_k)^2}{K-1}}
    			```

    		- This is useful estimate but not quite valid

    ## Bootstrap

    	- The bootstrap is a flexible and powerful statistical tool that resamples a single dataset to create many simulated samples and can be used to quantify the uncertainty associated with a given estimator or ML method

    	- For example, we want to minimize \text{Var}(\alpha X+(1-\alpha)Y), and one saw

    		```undefined
    		\alpha=\frac{\sigma_Y^2-\sigma_{XY}}{\sigma_X^2+\sigma_Y^2-2\sigma_{XY}}
    		```

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

# Model Selection: Subset Selection

    ## Considerations

    	- Prediction accuracy: especially when p>n

    	- Model interpretability: by removing irrelevant features

    ## Best subset selection

    	- Let M_0 denote the null model, which contains no predictors. This model simply predicts the sample mean for each observations

    	- For k=1,2,…,p

    		- Fit all \begin{pmatrix}p\\k\end{pmatrix}=\frac{p!}{k!(p-k!)} models that contain exactly k predictors

    		- Pick the best among these models and call it M_k Here k best is defined as having the smallest RSS(or largest R-squared)

    	- Select a single best model among M_0,…,M_p using cross validated prediction error, C_p, AIC, BIC or adjusted R^2

    ## Stepwise selection

    	- There are a lot of kinds that can happen if p goes very large. It can also leads to overfitting, so suggest stepwise selection

    	### Forward stepwise selection

    	- Let M_0 denote the null model, with no predictors

    	- For k=0,…,p-1

    		- Consider all p-k models that augment the predictors in M_k with one additional predictor

    		- Choose the best among this p-k models, and call it M_{k+1}.

    	- Select a single best model from among M_0,…,M_p using cross validated prediction error, C_p, AIC, BIC, or adjusted R^2

    	### Backward stepwise selection

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

# Model Selection: Shrinkage Methods

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

# Tree Based Methods, Decision Trees, Bagging, Random forests, Boosting

    ## Decision Trees

    	### Tree-based methods

    		- The set of splitting rules used to segment the predictor space can be sumamrized in a tree, these types of approaches are known as decision tree methods

    		- Simple and useful for interpretation

    		- Are not competitive with the best supervised learning approaches in terms of prediction accuracy

    	### Tree-Building process

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

    	### Choosing the best tree

    		- Pruning

    			- A small tree with fewer splits might lead to lower variance, and larger tree an lead to overfit

    			- Cost complexity pruning → introduce tuning parameter \alpha

    				```undefined
    				\sum_{m=1}^{|T|}\sum_{x_i\in R_m}(y_i-\hat y_{R_m})^2 + \alpha|T|
    				```

    			- Similar to LASSO, and select an optimal value \hat\alpha with cross-validation

    	### Classification trees

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

    ## Bagging

    	- Bootstrap aggregation, or bagging is a general purpose procedure for reducing the variance of a machine learning method. Averaging a set of observations reduce variance

    		```undefined
    		\hat f_{bag}(x) = \frac 1B\sum_{b=1}^B\hat f^{*^b}(x)
    		```

    	- In classification tree, take majority vote

    	- Remaining one-third of the observations not used to fit given bagged trees are referred to as the out of bag(OOB) distribution

    ## Random Forests

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

# SVM

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

# Unsupervised Learning: PCA & Clustering

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

# Nearest Neighbor Classifiers

    - For the query(test) data point, find the (K) closest training data point and predict using its label

    - Memorize all data and labels → Output the label of the most similar training example

    - Problem with NN

    	- We need some similarity metric between two images

    	- Training takes O(1) and prediction takes O(N)

    	- k nearest neighbors with pixel distance are never used

    	- Curse of dimensionality

# Linear & Softmax Classifiers

    - Think of a function f that maps to the input(image x) to the label scores(class y)

    - Linear function: weighted sum of input pixels: W_{11}x_{11}+W_{12}x_{12}+\cdots+W_{mn}x_{mn}

    	```undefined
    	Wx+b = f(x,W)
    	```

    - Bias b: affecting the output without interacting with the data x

    	```undefined
    	f(x,W)=Wx+b=\begin{bmatrix}W&b\end{bmatrix}\begin{bmatrix}X\\1\end{bmatrix}
    	```

    - Advantage of parametric models

    	- Once trained, what we need is the weights W only. We don’t need to store the huge training set

    	- At test time, an example can be evaluated by a single matrix-vector multiplication

    - What linear classifier does

    	- At training: learning the template from training data

    	- At testing: performing the template matching with a new example

    ## Softmax Classifier

    - Limitations of Linear Classifier

    	- Unbounded: it can be arbitrarily large

    	- Hard to interpret: What is the meaning of score and how good is it?

    - Sigmoid function \sigma(s)=\frac1{1+e^{-s}}

    - Generalize sigmoid to n>2 classes

    	```undefined
    	p(y=c_i|x)=\frac{e^{s_i}}{\sum_j e^{s_j}}
    	```

    ## Loss Functions

    - A loss function quantifies how good our current machine learning

    - A function of our prediction \hat y and ground truth label y: \mathcal L(\hat y,y)

    - 0-1 Loss, Log loss, Exponential loss, Hinge Loss

    - Cross Entropy: sum of -log(”our predicted probability for true class”)

    	```undefined
    	\mathcal L = -\frac 1N\sum_{i=1}^N\sum_{k=1}^Ky_{ik}\log(\hat y_{ik})
    	```

    - KL Divergence

    	```undefined
    	\begin{aligned}D_{KL}(P\|Q)&=\sum_iP(i)\log\frac{P(i)}{Q(i)}\\D_{KL}(P\|Q)&=\int P(x)\log\frac{P(x)}{Q(x)}dx\end{aligned}
    	```

    ## Optimization

    - Update the parameters(W) based on loss function

    - We have cost function J(\theta) to minimize, so calculate gradient

    - Update equation

    	```undefined
    	\theta_i^{new}=\theta_i^{old}-\alpha\frac{\partial}{\partial\theta^{old}}J(\Theta)
    	```

    - Potential problems of GD

    	- The surface may not be convex

    	- It works only if the cost function is differentiable

    	- Converging to a local minimum can be quite slow

    - Stochastic Gradient Descent: do GD only on a randomly sampled subset

# Neural Networks & Backpropagation

    - Issues with linear classifiers

    	- Visually: Linear Classifiers learn one template per class

    	- Geometrically: Linear Classifiers can only draw linear decision boundaries

    - Features

    	- Instead of directly mapping input-output relationship with a linear classifier, we may extract some features

    	- Color histogram, Histogram of oriented gradients, bag of words can be example

    ## Neural Networks

    - A perceptron y=f(w_1x_1+w_2x_2)

    	![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/03999249-4602-4130-bff6-69bf9b7b07d3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240305T004218Z&X-Amz-Expires=3600&X-Amz-Signature=c76d485032fcfb705d9330fcdc618ea6cecc6f8b444a6216d3ebdd7c10bf8ecf&X-Amz-SignedHeaders=host&x-id=GetObject)

    - Neural network with a single layer: x \in\R^d,W\in\R^{c\times d},s\in\R^c

    - Multilayer perceptron: x \in\R^d,W_1\in\R^{h\times d},W_2\in\R^{c\times h},s\in\R^c and use activation function to add non linearity

    	```undefined
    	f(x) = a_2(W_2a_1(W_1x))
    	```

    - Activation function: sigmoid, tanh(\tanh(x)), ReLU(\max(0,x))

    - Gradient of the classification loss w.r.t each parameter \frac{\partial\cal L}{\partial W_1},\frac{\partial\cal L}{\partial W_2}

    	```python
    	import numpy as np
    	from numpy.random import randn
    	n, d, h, c = 64, 1000, 100, 10
    	x, y = randn(n, d), randn(n, c)
    	w1, w2 = randn(d, h), randn(h, c)
    	learning_rate = 1e-4
    	for t in range(1000):
    	  h = 1 / (1 + np.exp(-x.dot(w1)))
    	  y_pred = h.dot(w2)
    	  loss = np.square(y_pred - y).sum()
    	  print(t, loss)
    	  grad_y_pred = 2.0 * (y_pred - y)
    	  grad_w2 = h.T.dot(grad_y_pred)
    	  grad_h = grad_y_pred.dot(w2.T)
    	  grad_w1 = x.T.dot(grad_h * h * (1 - h))
    	  w1 -= learning_rate * grad_w1
    	  w2 -= learning_rate * grad_w
    	```

    ## Backpropagation: Computing Gradients

    - We need partial derivative of f w.r.t each variable (x,y,z) to backpropagate f(x,y,z)

    - Chain Rule

    	```undefined
    	\frac{\partial\cal L}{\partial x}=\frac{\partial\cal L}{\partial z}\frac{\partial z}{\partial x}, \frac{\partial\cal L}{\partial y}=\frac{\partial\cal L}{\partial z}\frac{\partial z}{\partial y} 
    	```

    ### Backpropagation with vector

    - Scalar to scalar

    	```undefined
    	\begin{aligned}x\in\R,&&y\in\R,&&\frac{\partial y}{\partial x}\in\R\end{aligned}
    	```

    - Vector to scalar: Gradient vector

    	```undefined
    	\begin{aligned}x\in\R^n,&&y\in\R,&&\frac{\partial y}{\partial x}\in\R^n &&\left(\frac{\partial y}{\partial x}\right)_i=\frac{\partial y_j}{\partial x_i}\end{aligned}
    	```

    - Vector to vector: Jacobian

    	```undefined
    	\begin{aligned}x\in\R^n,&&y\in\R^m,&&\frac{\partial y}{\partial x}\in\R^{n\times m} &&\left(\frac{\partial y}{\partial x}\right)_{ij}=\frac{\partial y_j}{\partial x_i}\end{aligned}
    	```

    - Gradients of variable with respect to loss have same dimensionality as the original variable.

# Convolution Neural Networks

    - Fully Connected Layer’s problem

    	- It is assumed that any output value can be affected by any input value

    - Convolution neural networks assume

    	- Spatial locality: each filter looks at nearby pixels only

    	- Positional invariance: same filters are applied to all locations in the image

    ## Convolution Layer

    - In RGB image, 32*32 image and 3 channels with 3*3*3 filter → slide over the image spatially with computing dot products

    - In total, 27(3*3*3 filter)+1(bias) are added

    - Given a fixed capacity

    	- high level features learn a set of features that are most useful to distinguish different classes in the dataset

    	- mid level features learn a set of features that are most useful to distinguish high level features

    	- low level features learn a set of features that are most useful to distinguish mid level features

    - Stride: How much pixels to slide

    - Padding: It’s common to zero pad the border

    - Given an input volume of W\times H\times C and Number of filters K, filter size F, stride S, and zero padding P

    	- This will produce an output size of W' \times H' \times K where

    	- W'=(W-F+2P)/S+1

    	- H'=(H-F+2P)/S+1

    	- Number of parameters K(F^2 C+1)

    - Convolutional layer is a special case of fully connected layers

    - Each value in the output is defined by all input values, and values with small region

    ## Pooling Layer

    - With downsampling, makes the representations smaller and more manageable

    - Some level of denoising to control overfitting

    - Max pooling and Average pooling can be used

    - Given an input volume of W\times H\times C and and spatial extent F, stride S

    	- This will produce an output size of W' \times H' \times C where

    	- W'=(W-F)/S+1

    	- H'=(H-F)/S+1

    	- Number of parameters 0

# Activation functions, data augmentation, weight initialization, learning rate

    ## Activation function

    - Sigmoid: killing gradient, not zero centered, computationally expensive

    - Tanh: killing gradient

    - ReLU: not zero-centered, not differentiable, dead ReLU problem if initial output is negative

    - Leaky ReLU: needs an additional parameter

    - Usually use ReLU and don’t use sigmoid or tanh in middle

    ## Data Preprocessing & Augmentation

    ### Normalization

    - It may help to zero-centering the data by subtracting global mean

    - It is also common to normalize the data by dividing by standard deviation

    ### Augmentation

    - There are a lot of ways to slightly modifying each datum without affecting its semantics

    - Flips, Crops, Scaling, Color Jitter, etc.

    ## Weight Initialization

    - Small Gaussian Random: standard normal distribution multiplied by small constant → Activations shrink

    - Large Gaussian Random: Activation Saturate

    - Xavier initialization: Just right scale, for convolution d_in = F^2C

    	- This works because \text{Var}(w_{ij})=1/d_{\text{in}}

    - Weight initialization for ReLU: W = np.random.randn(d_in, d_out) * np.sqrt(2/d_in)

    ## Learning Rate Scheduling

    - Learning Rate Decay: as it gets closer to the local optimum, smaller learning rates are necessary to correctly reflect the gradient direction

    	- Step: reduce learning rate at a few fixed points

    	- Cosine, linear, inverse sqrt

    	- Initial warmup

# Regularization, advanced optimization, batch norm

    ## Regularization

    - Adding an additional penalty term in the objective function

    - Ridge Regression

    	```undefined
    	\min_\theta(Y-X\theta)^\top(Y-X\theta)+\lambda\|\theta\|_2
    	```

    - LASSO

    	```undefined
    	\min_\theta(Y-X\theta)^\top(Y-X\theta)+\lambda\|\theta\|_1
    	```

    - Early stopping: stop when validation set is starting to overfit

    - Dropout: randomly set some neurons to zero

    - Cutout: Set zero to some randomly chosen sub-area

    ## Advanced Optimization

    - SGD’s problem

    	- SGD progresses very slowly

    	- On a local minimum or at a saddle point, gradient becomes 0 and it gets stuck

    	- Gradient is computed from mini-batches, so its estimation may not be accurate

    - SGD+Momentum: build up velocity as a running mean of gradients

    	```undefined
    	\begin{aligned}v_{t+1}&=\rho v_t-\alpha\nabla f(x_t)\\x_{t+1}&=x_t+v_{t+1}\end{aligned}
    	```

    - Adagrad: element-wise scaling of the gradient based on the historical sum of squares in each dimension

    - RMSProp: Leaky Adagrad: Adagrad can lead to quickly shrinking learning rate, so add convex combination

    - Adam: RMSProp + SGD with momentum

    ## Batch Normalization

    - In intermediate layers, we want to make data zero-centered and normalized

    - Consider a batch activations at some layer. To make each dimension zero-mean and unit-variance

    	```undefined
    	\hat x^{(k)}=\frac{x^{(k)}-\mathbb E[x^{(k)}]}{\sqrt{\text{Var}[x^{(k)}]}}
    	```

    - Simply normalizing each input of a layer may change what the layer represent, so we need to make sure that transform inserted

# Recurrent Neural Networks

    - Sequential Data: what if input x is a sequence of multiple instances?

    - Problem types

    	- One-to-one: Vanilla Neural-net

    	- Many-to-one: Action recognization

    	- Many-to-many: Frame classification

    	- One-to-many: Image captioning

    	- Many-to-many: video captioning

    ## Word Embeddings

    - We usually represent an object as a vector.

    - Word2vec(frequently co-occurring neighboring words)

    - GloVe: ratios of co-occurrence probabilities can encode meaning components

    ## Recurrence Neural Networks for Many to one

    - To control variable length, introduce encoder which embeds the entire sequence preserving 

    - RNNs maintain an internal state, representing the semantics of input sequence processed so far

    	```mermaid
    	graph BT
    	  A[RNN] --> A
    		x --> A
    	```

    - The RNN cell starts with its initial state and takes an input x_i, updates its hidden state h_i from h_{i-1}

    	```undefined
    	h_t = f_W(h_{t-1},x_t)
    	```

    - It’s important to note that same function and the same set of parameters are used at every time step

    	```undefined
    	h_t = \tanh(W_{hh}h_{t-1}+W_{xh}x_t)
    	```

    - Forward pass: all parameters W_{hh},W_{xh},W_{hy} are fixed and they are used to compute \hat y

    - Backpropagation: from the loss(diff(\hat y,y), parameters are updated 

    ## RNN for Sequential Prediction

    - Use many-to-many rnn with multi layers

    - However, it has vanishing gradient problem, and fails to model long-range dependence in a sequence

    ### Exploding & Vanishing Gradient problem

    - For RNN, input sequence length acts like depth, so W is large then gradient explodes → clipping can be solution but it can’t maintain gradient direction

    - If W is small then shrink layer by layer

    ## LSTM

    - To avoid vanishing gradient problem, we make new set of hidden state c_t with a highway detouring FC layer

    - Even if the cell state is for long term memory, we still need some mechanism to control it(forget gate)

    - At the input side, add the input gate to control the flow from the input

    - Lastly, we add output gate to control the value updated to the hidden state h_t

    ```undefined
    \begin{aligned}f_t&=\sigma(W_fx_t+U_fh_{t-1}+b_f)\\i_t&=\sigma(W_ix_t+U_ih_{t-1}+b_i)\\o_t&=\sigma(W_ox_t+U_oh_{t-1}+b_o)\\c_t&=f_t\circ c_{t-1}+i_t\circ\tanh(W_cx_t+U_ch_{t-1}+b_c)\\h_t&=o_t\circ\tanh(c_t)\end{aligned}
    ```

    - LSTM doesn’t guarantee that there is no vanishing/exploding gradient, but it does provide an easier way for the model to learn long-distance dependencies

    ## GRU

    - No additional cell states as in LSTM

    - Fewer parameters compared to LSTM

    - Provide a gradient highway similar to LSTM, using convex combination of previous hidden state and new one computed from the input

    ```undefined
    \begin{aligned}r_t&=\sigma(W_rx_t+U_rh_{t-1}+b_r)\\z_t&=\sigma(W_zx_t+U_zh_{t-1}+b_z)\\h_t&=(1-z_t)\circ h_{t-1}+z_t\circ\tanh(W_hx_t+U_h(r_t\circ h_{t-1})+b_h)\end{aligned}
    ```

    ## Seq2Seq Models

    - RNN assumes 1:1 relationship, so input length and output length must be same

    - Encoder-decoder structure

    	- Passing encoder, we have an embedding containing semantics of the entire input sequence

    	- Then we build a decoder, generating outputs one by one starting from this embedding

    - At training, we only use ground truth y_{t-1} as input, because the model needs to learn what to output from the correct inputs

    - At inference, we don’t have to access ground truth so use previous output

# Attentions & Basics of Transformer

    - Limitations of RNN-based model

    	- Information loss is unavoidable for long sequence, even though model is LSTM or GRU

    ## Attention is all you need

    - Attention Function: Attention(Q,K,V) = Attention value

    - Q and K must be comparable, V and attention value are in the same dimensionality

    - In seq2seq, Q is decoder hidden state, K is encoder hidden state and V is the encoder hidden state

    ### Dot-product Attention

    - Start with encoder hidden states h_1,...,h_T\in\R^h

    - The decoder state at time step t is s_t\in\R^h

    - We compute attention scores for time step t

    	```undefined
    	e_t = \begin{bmatrix}s_t^\top h_1&...&s_t^\top h_T\end{bmatrix}\in \R^T
    	```

    - Then, we take softmax to get attention coefficients for this time step t

    	```undefined
    	\alpha_t = \text{softmax}(e_t)=\frac{\exp\{e_t\}}{\sum_i\exp\{[e_t]_i\}}\in\R^T
    	```

    - We take weighted sum of the encoder hidden states according to the attention coefficients, to get the attention value

    	```undefined
    	a_t=\sum_{i=1}^T[a_t]_ih_i\in\R^h
    	```

    - Finally, we concentrate the attention value with the decoder hidden state and proceed as in the vanilla seq2seq model: [a_t;s_t]\in\R^{2h}

    ## Transformer

    ![](https://prod-files-secure.s3.us-west-2.amazonaws.com/0d54cb71-779e-4bdf-883b-5ad3380d7d11/a2ef8825-114b-465a-8355-6b2ba82488fb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45HZZMZUHI%2F20240305%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20240305T004231Z&X-Amz-Expires=3600&X-Amz-Signature=2a752f562d39c2d9f31d48f8e7b25133b0bb3b033926dd743725264fd92dd35a&X-Amz-SignedHeaders=host&x-id=GetObject)

    - Input Embedding

    	- Input is a sequence of tokens

    	- Each of them is represented as a pre-trained embedding

    - Positional Encoding: to inject the order information

    - Contextualizing the word embedding with self-attention

    	- Multi-head self-attention: having multiple projection to Q,K,V is beneficial

    - Feed-forward layer

    	- Contextualized word embedding goes through an additional FC layer. Output is still a same size contextualized token embedding

    - Stacked self-attention blocks

    - Decoder input: generates an output sequence auto-regressively

    - Masked Multi-head self attention: the input sequence is fed into multi-head self-attention layer as in the encoder

    - Encoder-Decoder attention: input attends the encoder output, no masking

    - Feed-forward layer

    - Linear layer

    - Softmax Layer to make probability

    ## BERT

    - Bidirectional Encoder Representations from Transformers

    - Input sequence consists of 2 sentences, with sum of token embedding, segment embedding and position embedding

    - Training task: masked language model, next sentence prediction

    ## ViT

    - Image split into patches and the sequence of linear embeddings of these patches are fed into Transformer
